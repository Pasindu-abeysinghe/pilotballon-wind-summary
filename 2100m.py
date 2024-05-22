from pathlib import Path
import csv

pilot_time = input("Enter Pilot Time : ")


def myround(x,base=5):
    return str(base * round(x/base) )

Path_dir = Path.cwd()/"pilotdata.csv"
with open(Path_dir, 'r') as csv__file:
    for row in csv__file:
        data = row.split(",")
        date_time = data[6]
        
        try:
            
            if date_time[11:13] == pilot_time:
                knots = float(data[23]) * 1.944
                #print(f"Date and Time : {data[6]} | 300m Wind Speed : {data[15]} | 300m Wind Direction : {data[16]} | Round up : {myround(float(data[16])).rjust(3,'0')} | Round up : {str(round(float(data[15]))).rjust(2,'0')}")
                #Wind Speed and Directon With Date
                print(f"Date and Time : {data[6]} | 2100m Layer | Code : {myround(float(data[24])).rjust(3,'0')}{str(round(float(knots))).rjust(2,'0')}")

        except ValueError:
            print("Empty Cell Found")
            
        
    
