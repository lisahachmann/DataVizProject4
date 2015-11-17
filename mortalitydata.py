# write a Python web server in Bottle that can access the mortality database using the sqlite3 module
# Data Viz project 4 part one
import bottle
import sqlite3
import json
from bottle import route, run, template

@route('/mortality')
def death_list():
    conn = sqlite3.connect('mortality.db')
    c = conn.cursor()
    c.execute("SELECT * FROM mortality WHERE sex = 'F'")
    causeDict = {}
    for i in range(100):
        data = c.fetchone()
        if int(data[25]) not in causeDict:
            causeDict[int(data[25])] = [int(data[5])]
        else:
            causeDict[int(data[25])].append(int(data[5]))
    #print causeDict
    causeAvgDict = {}
    for key,value in causeDict.iteritems():
        if key not in causeAvgDict:
            causeAvgDict[key] = sum(value)/len(value)
    with open('/home/li/GitRepos/DataVizProject4/averageage.json', 'w') as outfile:
        json.dump(causeAvgDict, outfile, indent = 4)
    return causeAvgDict
run(host='localhost', port=8081, debug=True)
