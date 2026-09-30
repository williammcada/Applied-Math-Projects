#!/usr/bin/env python3
"""Verify dossier v1.0.0 reference mathematics. No application/UI is tested.
Usage: python verify_reference_fixtures.py [reference_fixtures.json]
Standard library only; writes nothing unless --report PATH is supplied.
"""
from __future__ import annotations
import argparse, json
from decimal import Decimal as D
from fractions import Fraction as F
from pathlib import Path
from collections import deque


def verify(data: dict) -> dict:
    checks: list[dict] = []
    def check(name: str, actual, expected) -> None:
        ok = actual == expected
        checks.append({'id': name, 'passed': ok, 'actual': str(actual), 'expected': str(expected)})
    rt=data['road_trip']; party=rt['party']; distance=D(rt['distance_km']); eff=D(rt['km_per_liter']); fuel=distance/eff*D(rt['fuel_price'])
    check('RT.fuel_liters', distance/eff, D('75')); check('RT.fuel_cost',fuel,D('120'))
    def road(h: str, f: str):
        m=D(rt['rental_per_day'])+D(h)+party*D(f)+D(rt['activity_per_group_day'])
        b=D(rt['one_off'])+fuel-D(h)
        return m,b,m*rt['days']+b
    check('RT.base_model',road('90','20'),(D('220'),D('230'),D('1770')))
    check('RT.hotel_event',road('110','20'),(D('240'),D('210'),D('1890')))
    check('RT.food_revision',road('110','15'),(D('225'),D('210'),D('1785')))
    check('RT.original_table',[D('220')*x+D('230') for x in (1,3,5,7)],list(map(D,['450','890','1330','1770'])))
    check('RT.max_whole_days',int((D(rt['budget'])-D('230'))//D('220')),7)
    check('RT.next_day_over_budget',D('220')*8+D('230')>D(rt['budget']),True)
    check('RT.hotel_event_counts_six_nights',road('110','20')[2]-road('90','20')[2],D('120'))
    check('RT.affordable_choice_count',sum(road(h,f)[2] <= D(rt['budget']) for h in ('60','90','130') for f in ('10','15','20'))>=3,True)
    ft=data['food_truck']; batch=sum(D(r['quantity'])*D(r['unit_price']) for r in ft['ingredients']); variable=batch/D(ft['batch_portions']); fixed=D(ft['fixed_cost'])
    check('FT.batch_cost',batch,D('90'));check('FT.portion_cost',variable,D('4.5'))
    check('FT.break_even',fixed/(D('12')-variable),D('60'));check('FT.first_profitable',D('7.5')*61-fixed,D('7.5'))
    check('FT.service_capacity',ft['service_rate']*ft['hours'],96)
    def launch(price: int,q: int):
        demand=ft['demand'][str(price)];sales=min(demand,q,ft['service_rate']*ft['hours']);revenue=D(price)*sales;cost=fixed+variable*q
        return sales,revenue,cost,revenue-cost,q-sales
    check('FT.base_launch',launch(12,100),(90,D('1080'),D('900'),D('180'),10))
    check('FT.low_waste',launch(12,80),(80,D('960'),D('810'),D('150'),0))
    check('FT.premium',launch(15,60),(60,D('900'),D('720'),D('180'),0))
    check('FT.loss_fixture',launch(9,120),(96,D('864'),D('990'),D('-126'),24))
    check('FT.viable_not_distinction',launch(12,120),(90,D('1080'),D('990'),D('90'),30))
    check('FT.unsold_cost_error',D('7.5')*90-fixed-launch(12,100)[3],D('45'))
    tp=data['theme_park'];step=tp['grid_m'];site=set((x,y) for x in range(0,60,step) for y in range(0,40,step))
    def cells(r):
        x,y,w,h=r
        if any(v%step for v in r):raise ValueError(f'Off-grid rectangle: {r}')
        return set((a,b) for a in range(x,x+w,step) for b in range(y,y+h,step))
    buildings=set();overlap=False
    for obj in tp['facilities']:
        c=cells(obj['rect']);overlap |= bool(buildings&c);buildings|=c
    paths=set().union(*(cells(r) for r in tp['paths']));greens=set().union(*(cells(r) for r in tp['green']))
    check('TP.no_building_overlap',overlap,False);check('TP.all_allocations_in_bounds',(buildings|paths|greens)<=site,True)
    check('TP.no_building_path_overlap',bool(buildings&paths),False);check('TP.no_green_overlap',bool(greens&(buildings|paths)),False)
    check('TP.facility_area',len(buildings)*4,704);check('TP.path_area',len(paths)*4,432);check('TP.green_area',len(greens)*4,480)
    check('TP.undeveloped',len(site-(buildings|paths|greens))*4,784)
    zone=cells(tp['expansion_rect']);check('TP.expansion_area',len(zone)*4,140);check('TP.expansion_is_unoccupied',bool(zone&(buildings|paths|greens)),False)
    # Check the path network is connected using 4-neighbor cells.
    seen=set();todo=deque([next(iter(paths))])
    while todo:
        c=todo.popleft()
        if c in seen:continue
        seen.add(c);x,y=c
        todo.extend((x+dx,y+dy) for dx,dy in ((2,0),(-2,0),(0,2),(0,-2)) if (x+dx,y+dy) in paths and (x+dx,y+dy) not in seen)
    check('TP.paths_connected',seen==paths,True)
    for item in tp['facilities']:
        x,y=item['door']
        touch=any(cx<=x<=cx+2 and cy<=y<=cy+2 for cx,cy in paths)
        check('TP.door.'+item['id'],touch,True)
    check('TP.carousel_area',D('3.14')*D(5)**2,D('78.5'));check('TP.triangle_area',D(8)*D(6)/2,D('24'))
    cost=sum(o['cost'] for o in tp['facilities'])+len(paths)*4*25+len(greens)*4*10+200*20
    check('TP.cost',cost,79600);check('TP.budget_reserve',90000-cost,10400)
    mc=data['mars_colony'];n=D(mc['population']);water=n*D('3');oxygen=n*D('.8');food=n*D('.6')
    check('MC.daily_demands',(water,oxygen,food),(D('72'),D('19.2'),D('14.4')))
    load=D('24')+3*D('12')+3*D('8')+3*D('10');check('MC.daily_load',load,D('114'))
    check('MC.normal_solar',D(4)*36,D('144'));check('MC.storm_solar',D(4)*36*D('.75'),D('108'))
    battery=D(36);history=[battery]
    for day in range(1,11):
        generated=D(4)*36*(D('.75') if 4<=day<=6 else D(1));battery=min(D(36),battery+generated-load);history.append(battery)
    check('MC.battery_after_storm',history[6],D('18'));check('MC.battery_never_negative',min(history)>=0,True);check('MC.battery_cap',max(history),D('36'))
    check('MC.water_end',D('144')+(3*D(30)-water)*10,D('324'));check('MC.oxygen_end',D('38.4')+(3*D(8)-oxygen)*10,D('86.4'));check('MC.food_end',D('172.8')-food*10,D('28.8'))
    basecost=3*2000+3*1500+3*3000+4*1000+800+1000
    mass=3*D(200)+3*D(150)+3*D(400)+4*D(100)+D(80)+D(144)+D('38.4')+D('172.8')+D(100)
    check('MC.base_cost',basecost,25300);check('MC.base_mass',mass,D('3185.2'))
    check('MC.extra_solar_cost',basecost+1000-800,25500);check('MC.extra_solar_mass',mass+100-80,D('3205.2'));check('MC.extra_solar_storm',5*D(36)*D('.75'),D('135'))
    check('MC.lean_cost',basecost-200,25100);check('MC.lean_mass',mass-D('14.4'),D('3170.8'));check('MC.lean_food_end',D('158.4')-food*10,D('14.4'))
    sn=data['powers_of_ten']
    operations=[D('8e-6')*D('2.5e1'),D('3e8')*D('1.28'),D('6.4e-5')/D('8e-6'),D('1.5e11')/D('3e8'),D('2.4e-5')+D('7.5e-6'),D('3.84e8')+D('6e7'),D('8e-6')-D('2e-6'),D('1.4e9')-D('1.28e7')]
    for i,(a,e) in enumerate(zip(operations,sn['operation_answers']),1):check(f'SN.operation.{i}',a,D(e))
    k=D('.16')/D('8e-6');check('SN.micro_scale',k,D('20000'));check('SN.person_comparison_m',k*D('1.7'),D('34000'));check('SN.dna_model_mm',k*D('2e-9')*1000,D('.04'))
    cosmic=F(1,640000000);check('SN.cosmic_scale',F(D('.02'))/F(D('1.28e7')),cosmic)
    check('SN.moon_model_mm',F(D('3.5e6'))*cosmic*1000,F(D('5.46875')))
    check('SN.moon_distance_mm',F(D('3.84e8'))*cosmic*1000,F(600))
    check('SN.sun_model_m',F(D('1.4e9'))*cosmic,F(D('2.1875')))
    check('SN.sun_distance_m',F(D('1.5e11'))*cosmic,F(D('234.375')))
    check('SN.earth_to_cell_ratio',D('1.28e7')/D('8e-6'),D('1.6e12'))
    return {'scope':'Reference mathematics and geometry only; no HTML application or physical device tested.', 'passed':all(c['passed'] for c in checks),'count':len(checks),'checks':checks}

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('file',nargs='?',default=str(Path(__file__).with_name('reference_fixtures.json')));parser.add_argument('--report')
    args=parser.parse_args()
    try:
        result=verify(json.loads(Path(args.file).read_text(encoding='utf-8')))
    except (OSError,ValueError,KeyError,TypeError,ArithmeticError) as exc:
        parser.exit(2,f'Reference verification failed to run: {exc}\n')
    if args.report:Path(args.report).write_text(json.dumps(result,indent=2,ensure_ascii=False),encoding='utf-8')
    print(f"{sum(c['passed'] for c in result['checks'])}/{result['count']} reference checks passed.")
    for check in result['checks']:
        if not check['passed']:print('FAIL',check)
    print(result['scope']);raise SystemExit(0 if result['passed'] else 1)
