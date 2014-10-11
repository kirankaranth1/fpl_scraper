# -*- coding: utf-8 -*-
from __future__ import print_function
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import time
import string
import re



success = True
wd = WebDriver()
wd.implicitly_wait(60)

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False
        
def get_score(id) :
    url="http://fantasy.premierleague.com/entry/"+str(id)+"/event-history/"+str(gw)+"/"
    wd.get(url)
    t_points=str(wd.find_element_by_xpath(".//*[@id='ism']/section[1]/div[3]/div[1]/div[2]/div[1]/div[1]/div/div[1]/div/div").text) 
    t_points=int(re.findall('\d+', t_points)[0])
    #print t_points
    transfers=str(wd.find_element_by_xpath(".//*[@id='ism']/section[1]/div[3]/div[1]/div[2]/div[1]/div[2]/div/div[2]/dl/dd[2]").text)
    name=str(wd.find_element_by_xpath(".//*[@id='ism']/section[2]/h1").text)
    try:
        transfers=int(re.findall('\d+', transfers)[1])
    except IndexError,e :
        transfers=0;
    #print transfers
    t_score=t_points-transfers
    #print t_score
    
    return (t_score,name)
    
def get_team(team,gw):
    scores=[0,0,0,0,0]
    names=["","","","",""]
    print("",file=f)
    print(team[5]+" Gameweek "+str(gw),file=f)
    for i in range(0,5):
        scores[i],names[i]=get_score(team[i])
    #print(team[5]+" Gameweek "+str(gw))
    print("1. "+names[1]+" "+str(scores[1])+", "+names[2]+" "+str(scores[2])+", "+names[3]+" "+str(scores[3])+", "+names[4]+" "+str(scores[4])+" = "+str(scores[1]+scores[2]+scores[3]+scores[4]),file=f)
    print("2. "+names[0]+" "+str(scores[0])+"*2 = "+str(scores[0]*2),file=f)
    ha=0
    if team[gw]=='h':
        
        ha=max(scores)*0.2
        print("3. Home advantage= "+"0.2*"+str(max(scores))+"="+str(ha),file=f)
    else:
        print("3. No home advantage",file=f)
        
    print("Total="+str(scores[1]+scores[2]+scores[3]+scores[4]+scores[0]*2+ha)+" ~"+str(round(scores[1]+scores[2]+scores[3]+scores[4]+scores[0]*2+ha)),file=f)
    print("",file=f)
    

    
try:
    #game=raw_input("Home or Away(h/a): ")
    
    gw=7
    fn="Gameweek_"+str(gw)+".txt"
    f = open(fn,'a')
    #gw=input("Game week number: ")
    hull=[192687,1677986,1149861,282609,235293,"Hull City","h","h","a"]
    arsenal=[454989,1187227,379286,59139,1874374,"Arsenal FC","h","a","h"]
    villa=[1511244,1793894,1245460,286331,870575,"Aston Villa","a","h","a"]
    burnley=[108067,325056,684282,333912,136183,"Burnley","a","a","h"]
    chelsea=[79759,1657614,2365314,320451,386880,"Chelsea","h","h","a"]
    palace=[297679,344694,192858,72711,1594177,"Crystal Palace","h","a","h"]
    everton=[1251421,1375942,995844,193410,451136,"Everton","a","a","h"]
    leicester=[286373,2093448,257328,41975,1318470,"Leicester City","a","h","a"]
    liverpool=[541519,833373,400106,468192,194237,"Liverpool FC","h","h","a"]
    city=[721763,384500,540855,1620596,68930,"Manchester City","a","a","h"]
    scums=[2326261,262415,51092,81179,1461413,"Manchester United","h","h","a"]
    newcastle=[407205,342876,52355,56998,1144868,"Newcastle United","a","a","h"]
    qpr=[277719,264939,1880769,1697834,1599192,"Queens Park Rangers","a","a","h"]
    saints=[258535,383212,278413,2317698,1173922,"Southampton","h","a","h"]
    stoke=[376009,2062491,779871,366861,451272,"Stoke City","h","a","h"]
    ham=[1031829,319332,1485675,2639408,654398,"West Ham United","a","h","a"]
    sunderland=[15003,129763,86905,385980,1203445,"Sunderland","h","h","a"]
    swans=[1721201,1340663,82318,1276345,506284,"Swansea","a","h","a"]
    spurs=[1046402,103596,901455,232054,1628118,"Tottenham","a","h","a"]
    westbrom=[166582,310730,68335,276748,1392297,"West Brom","h","a","h"]    
    
    
    
    get_team(arsenal,gw)
    get_team(villa,gw)
    get_team(burnley,gw)
    get_team(chelsea,gw)
    get_team(palace,gw)
    get_team(everton,gw)
    get_team(hull,gw)
    get_team(leicester,gw)
    get_team(liverpool,gw)
    get_team(city,gw)
    get_team(scums,gw)
    get_team(newcastle,gw)
    get_team(qpr,gw)
    get_team(saints,gw)
    get_team(stoke,gw)
    get_team(sunderland,gw)
    get_team(swans,gw)
    get_team(spurs,gw)
    get_team(westbrom,gw)
    get_team(ham,gw)
    
  
    
finally:
    wd.quit()
    if not success:
        raise Exception("Test failed.")
