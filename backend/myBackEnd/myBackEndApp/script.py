import csv
import sqlite3

conn=sqlite3.connect("db.sqlite3")
c = conn.cursor()

i=0

list = []

with open('Centre-Stats1.csv') as csvfile:
    data = csv.reader(csvfile)
    for d in data:
    	if d[1]=="" and i>3:
    		break
    	else:
    		gender = d[4]
    		if (gender=="Male" or gender=="Female"):
    			age = "Over 18"
    		elif gender[:4] == "Male":
    			age = "Under 18"
    			gender = "Male"
    		else:
    			age = "Under 18"
    			gender = "Female"
    		list.append({"seenBy":d[1],
    					 "person": d[2],
    					 "visitType": d[3],
    					 "cancerSite":d[5],
    					 "journeySite":d[6],
    					 "natureOfVisit":d[7],
    					 "gender": gender,
    					 "age":age})


print list