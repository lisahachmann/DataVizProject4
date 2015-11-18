# write a Python web server in Bottle that can access the mortality database using the sqlite3 module
# Data Viz project 4 part one

import bottle
import sqlite3
import json
from bottle import route, run, template
@route('/mortality')
conn = sqlite3.connect("/home/li/GitRepos/DataVizProject4/mortality.db")
cur = conn.cursor()
#cur.execute("SELECT cause_Recode_39 FROM mortality WHERE sex = 'F'")
#cur.execute("SELECT * FROM sqlite_master WHERE name='mortality'")
#cur.execute("SELECT 'Age_Value text' FROM 'mortality' WHERE sex = 'M' OR sex = 'F'")
#cur.execute("SELECT * FROM mortality WHERE sex = 'F'")
#print cur.fetchone()


#For each cause of death in the Cause_Recode_39 column, the average age of the persons that died from that cause, for each year.
#age = data[5], cause = data[25]
def p1():
    causeDict = {}
    for i in range(10):
        data = cur.fetchone()
        if int(data[25]) not in causeDict:
            causeDict[int(data[25])] = [int(data[5])]
        else:
            causeDict[int(data[25])].append(int(data[5]))

    print causeDict

    causeAvgDict = {}
    for key,value in causeDict.iteritems():
        if key not in causeAvgDict:
            causeAvgDict[key] = sum(value)/len(value)
        #with open('/averageage.json', 'w') as outfile: #Julian's file path
        with open('/home/li/GitRepos/DataVizProject4/averageage.json', 'w') as outfile: #Lisa's file path
            json.dump(causeAvgDict, outfile, indent = 4)
    return causeAvgDict

#p1()


#For each age, the top cause of death (as per the Cause_Record_39) for deaths at that age, for each year.

from collections import Counter

def Most_Common(lst):
    data = Counter(lst)
    return data.most_common(1)[0][0]


topDeathYear = {}

def p2(year):
    cur.execute("SELECT * FROM mortality WHERE year = " + year)
    death = {}
    topDeath = {}

    for i in range(100):
        data = cur.fetchone()
        if int(data[5]) not in death:
            death[int(data[5])] = [int(data[25])]
        else:
            death[int(data[5])].append(int(data[25]))

    for key,value in death.iteritems():
        if key not in topDeath:
            topDeath[key] = Most_Common(value)
    #with open('/averageage.json', 'w') as outfile: #Julian's file path
    with open('/home/li/GitRepos/DataVizProject4/topcause.json', 'w') as outfile: #Lisa's file path
        json.dump(topDeath, outfile, indent = 4)
    return topDeath

topDeathYear['2003'] = p2('2003')
topDeathYear['2008'] = p2('2008')
topDeathYear['2013'] = p2('2013')

print topDeathYear

run(host='localhost', port=8081, debug=True)



"""
Sex text: 3             (String)
Age: 5                  (int)
Marital_Status text: 12 (String)


Marital Status
S ... Never married, single
M ... Married
W ... Widowed
D ... Divorced
U ... Marital Status unknown
"""

SMA = {}
def p3():
    cur.execute("SELECT * FROM mortality")
    for i in range(100000):
        data = cur.fetchone()
        
        if str(data[3]) not in SMA:
            SMA[str(data[3])] = [{str(data[12]): int(data[5])}]
        else:
            SMA[str(data[3])].append({str(data[12]): int(data[5])})
        
    with open('C:\Users\jmorris\Documents\Fall_2015\Data Visualization\HW4/SexMarriageAge.json', 'w') as outfile: #Julian's file path
        json.dump(SMA, outfile, indent = 4)
    return SMA

#p3()
   
YSMA = {}
def p4():
    cur.execute("SELECT year, Sex, Marital_Status, Age_Value FROM mortality")
    i = 0
    while True:
        try:
            data = cur.fetchone()
            i+=1
            
            if i%500000 == 0:
                print i
            
            if int(data[0]) not in YSMA.keys():
                YSMA[int(data[0])] = {str(data[1]): {str(data[2]): [int(data[3])]}}
                
            
            elif str(data[1]) not in YSMA[int(data[0])]:
                YSMA[int(data[0])][str(data[1])] = {str(data[2]): [int(data[3])]}
            
            
            elif str(data[2]) not in YSMA[int(data[0])][str(data[1])]:
                YSMA[int(data[0])][str(data[1])][str(data[2])] = [int(data[3])]
            
            else:
                YSMA[int(data[0])][str(data[1])][str(data[2])].append(int(data[3]))
            
                
                
        except:
            break
    with open('C:\Users\jmorris\Documents\Fall_2015\Data Visualization\HW4/YearSexMarriageAge.json', 'w') as outfile: #Julian's file path
        json.dump(YSMA, outfile, indent = 4)
    
    return YSMA

p4()

