from pathlib import Path
import csv

pilot_time = input("Enter Pilot Time : ")

direction = 20 #900m level
Speed = 19 #900m level

total_count = 0

Calm_900m = 0
Level_1_N = 0
Level_1_NE = 0
Level_1_E = 0
Level_1_SE = 0
Level_1_S = 0
Level_1_SW = 0
Level_1_W = 0
Level_1_NW =0

Level_2_N = 0
Level_2_NE = 0
Level_2_E = 0
Level_2_SE = 0
Level_2_S = 0
Level_2_SW = 0
Level_2_W = 0
Level_2_NW =0

Level_3_N = 0
Level_3_NE = 0
Level_3_E = 0
Level_3_SE = 0
Level_3_S = 0
Level_3_SW = 0
Level_3_W = 0
Level_3_NW =0

Level_4_N = 0
Level_4_NE = 0
Level_4_E = 0
Level_4_SE = 0
Level_4_S = 0
Level_4_SW = 0
Level_4_W = 0
Level_4_NW =0

def myround(x,base=5):
    return str(base * round(x/base) )

Path_dir = Path.cwd()/"pilotdata.csv"
with open(Path_dir, 'r') as csv__file:
    for row in csv__file:
        data = row.split(",")
        date_time = data[6]
        try:
            if date_time[11:13] == pilot_time:
                if float(data[Speed]) <= 1.4 :
                    Calm_900m += 1
                    total_count += 1
                elif float(data[Speed]) >= 1.5 and float(data[Speed]) <= 7.4:
                    if float(data[direction]) >= 338 or float(data[direction]) <= 22:
                        Level_1_N += 1
                        total_count += 1
                    elif float(data[direction]) >= 23 and float(data[direction]) <= 67:
                        Level_1_NE += 1
                        total_count += 1
                    elif float(data[direction]) >= 68 and float(data[direction]) <= 112:
                        Level_1_E += 1
                        total_count += 1
                    elif float(data[direction]) >= 113 and float(data[direction]) <= 157:
                        Level_1_SE += 1
                        total_count += 1
                    elif float(data[direction]) >= 158 and float(data[direction]) <= 202:
                        Level_1_S += 1
                        total_count += 1
                    elif float(data[direction]) >= 203 and float(data[direction]) <= 247:
                        Level_1_SW += 1
                        total_count += 1
                    elif float(data[direction]) >= 248 and float(data[direction]) <= 292:
                        Level_1_W += 1
                        total_count += 1
                    else:
                        Level_1_NW += 1 
                        total_count += 1    
                elif float(data[Speed]) >= 7.5 and float(data[Speed]) <= 14.5:
                    if float(data[direction]) >= 338 or float(data[direction]) <= 22:
                        Level_2_N += 1
                        total_count += 1
                    elif float(data[direction]) >= 23 and float(data[direction]) <= 67:
                        Level_2_NE += 1
                        total_count += 1
                    elif float(data[direction]) >= 68 and float(data[direction]) <= 112:
                        Level_2_E += 1
                        total_count += 1
                    elif float(data[direction]) >= 113 and float(data[direction]) <= 157:
                        Level_2_SE += 1
                        total_count += 1
                    elif float(data[direction]) >= 158 and float(data[direction]) <= 202:
                        Level_2_S += 1
                        total_count += 1
                    elif float(data[direction]) >= 203 and float(data[direction]) <= 247:
                        Level_2_SW += 1
                        total_count += 1
                    elif float(data[direction]) >= 248 and float(data[direction]) <= 292:
                        Level_2_W += 1
                        total_count += 1
                    else:
                        Level_2_NW += 1
                        total_count += 1
                elif float(data[Speed]) >= 14.6 and float(data[Speed]) <= 20.5:
                    if float(data[direction]) >= 338 or float(data[direction]) <= 22:
                        Level_3_N += 1
                        total_count += 1
                    elif float(data[direction]) >= 23 and float(data[direction]) <= 67:
                        Level_3_NE += 1
                        total_count += 1
                    elif float(data[direction]) >= 68 and float(data[direction]) <= 112:
                        Level_3_E += 1
                        total_count += 1
                    elif float(data[direction]) >= 113 and float(data[direction]) <= 157:
                        Level_3_SE += 1
                        total_count += 1
                    elif float(data[direction]) >= 158 and float(data[direction]) <= 202:
                        Level_3_S += 1
                        total_count += 1
                    elif float(data[direction]) >= 203 and float(data[direction]) <= 247:
                        Level_3_SW += 1
                        total_count += 1
                    elif float(data[direction]) >= 248 and float(data[direction]) <= 292:
                        Level_3_W += 1
                        total_count += 1
                    else:
                        Level_3_NW += 1
                        total_count += 1
                else:
                    if float(data[direction]) >= 338 or float(data[direction]) <= 22:
                        Level_4_N += 1
                        total_count += 1
                    elif float(data[direction]) >= 23 and float(data[direction]) <= 67:
                        Level_4_NE += 1
                        total_count += 1
                    elif float(data[direction]) >= 68 and float(data[direction]) <= 112:
                        Level_4_E += 1
                        total_count += 1
                    elif float(data[direction]) >= 113 and float(data[direction]) <= 157:
                        Level_4_SE += 1
                        total_count += 1
                    elif float(data[direction]) >= 158 and float(data[direction]) <= 202:
                        Level_4_S += 1
                        total_count += 1
                    elif float(data[direction]) >= 203 and float(data[direction]) <= 247:
                        Level_4_SW += 1
                        total_count += 1
                    elif float(data[direction]) >= 248 and float(data[direction]) <= 292:
                        Level_4_W += 1
                        total_count += 1
                    else:
                        Level_4_NW += 1
                        total_count += 1
            
        except ValueError:
            print("Empty Cell Found")

print("!-----900m UPPER WIND FREQUENCY-----!") 
print("-------------------------------------")            
print(f"CALM 900M : {Calm_900m}")
print(f"01.5-07.4 N : {Level_1_N} | 01.5-07.4 NE : {Level_1_NE} | 01.5-07.4 E : {Level_1_E} | 01.5-07.4 SE : {Level_1_SE} | 01.5-07.4 S : {Level_1_S} | 01.5-07.4 SW : {Level_1_SW} | 01.5-07.4 W : {Level_1_W} | 01.5-07.4 NW : {Level_1_NW} ")
print(f"07.5-14.5 N : {Level_2_N} | 07.5-14.5 NE : {Level_2_NE} | 07.5-14.5 E : {Level_2_E} | 07.5-14.5 SE : {Level_2_SE} | 07.5-14.5 S : {Level_2_S} | 07.5-14.5 SW : {Level_2_SW} | 07.5-14.5 W : {Level_2_W} | 07.5-14.5 NW : {Level_2_NW} ")
print(f"14.6-20.5 N : {Level_3_N} | 14.6-20.5 NE : {Level_3_NE} | 14.6-20.5 E : {Level_3_E} | 14.6-20.5 SE : {Level_3_SE} | 14.6-20.5 S : {Level_3_S} | 14.6-20.5 SW : {Level_3_SW} | 14.6-20.5 W : {Level_3_W} | 14.6-20.5 NW : {Level_3_NW} ")
print(f"  >  20.5 N : {Level_4_N} |   >  20.5 NE : {Level_4_NE} |   >  20.5 E : {Level_4_E} |   >  20.5 SE : {Level_4_SE} |   >  20.5 S : {Level_4_S} |   >  20.5 SW : {Level_4_SW} |   >  20.5 W : {Level_4_W} |   >  20.5 NW : {Level_4_NW} ")  
print("-------------------------------------")
print(f"Total Data Count : {total_count}")        
