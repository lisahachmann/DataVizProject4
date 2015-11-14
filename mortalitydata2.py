# write a Python web server in Bottle that can access the mortality database using the sqlite3 module
# Data Viz project 4 part one

import bottle
import sqlite3

conn = sqlite3.connect("mortality.db")
cur = conn.cursor()
#cur.execute("SELECT cause_Recode_39 FROM mortality WHERE sex = 'F'")
#cur.execute("SELECT * FROM sqlite_master WHERE name='mortality'")
#cur.execute("SELECT 'Age_Value text' FROM 'mortality' WHERE sex = 'M' OR sex = 'F'")
cur.execute("SELECT * FROM mortality WHERE sex = 'F'")
#print cur.fetchone()


causeDict = {}
for i in range(10):
    data = cur.fetchone()
    if int(data[25]) not in causeDict:
        causeDict[int(data[25])] = [int(data[5])]
    else:
        causeDict[int(data[25])].append(int(data[5]))
    
#print causeDict

causeAvgDict = {}
for key,value in causeDict.iteritems():
    if key not in causeAvgDict:
        causeAvgDict[key] = sum(value)/len(value)

print causeAvgDict
        



    
