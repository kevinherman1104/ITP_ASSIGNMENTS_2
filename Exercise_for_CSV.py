#1
#import all libraries
import matplotlib.pyplot as plt
import csv
import numpy as np 
import statistics

csv_open = open("activity.csv","r")
csv_reader = csv.reader(csv_open, delimiter = ",")

#1 calculate total steps per day
line = 0
days ={}
days_list = []
intervals = {}
days_of_NA = {}
counter_NA = 0
weekly_counter = 0
weekend = {}
weekend_list =[]
weekdays = {}
weekdays_list = []
for row in csv_reader :
    if line == 0:
        line += 1
#A 1
    else:
        steps = row[0]
        day = row[1]
        interval = row[2]
        if day in days:
            if steps == "NA": 
                counter_NA += 1      
            else:
                days[day].append(int(steps))
        else:
            if steps == "NA":
                counter_NA += 1
                days[day] = [0]
            else:
                days[day] = [int(steps)]
#B 1
        if interval in intervals:
            if steps == "NA":
                pass
            else:
                intervals[interval] += int(steps)
        else:
            if steps == "NA":
                intervals[interval] = 0
            else:
                intervals[interval] = int(steps)
        if day not in days_list:
            days_list.append(day)
#C 3
        if day in days_of_NA:
            if steps == "NA":
                counter_NA += 1
                days_of_NA[day].append(0)
            else:
                days_of_NA[day].append(int(steps))
        else:
            if steps == "NA":
                #C 1
                counter_NA += 1
                #C 2
                days_of_NA[day] = [0]
            else:
                days_of_NA[day] = [int(steps)]
        #D 1
        if weekly_counter <= 5:
            if interval in weekdays:
                if steps == "NA":
                    pass
                else:
                    weekdays[interval] += int(steps)
            else:
                if steps == "NA":
                    weekdays[interval] = 0
                else:
                    weekdays[interval] = int(steps)
            if day not in weekdays_list:
                weekdays_list.append(day)
        elif weekly_counter <= 7:
            if interval in weekend:
                if steps == "NA":
                    pass
                else:
                    weekend[interval] += int(steps)
            else:
                if steps == "NA":
                    weekend[interval] = 0
                else:
                    weekend[interval] = int(steps)
            if day not in weekend_list:
                weekend_list.append(day)
        weekly_counter += 1
        if weekly_counter == 7:
            weekly_counter = 1

            
        
            
#A1
print(days)
total_steps_per_day = {}
for day in days:
    total = 0
    for steps in days[day]:
        total += steps
    total_steps_per_day[day] = total
print(total_steps_per_day)



# A 2 : Histogram of total steps per day
plt.bar(total_steps_per_day.keys(), total_steps_per_day.values(), 1.0)
plt.show()

# A 3 : Mean and median of each day
for day in days:
    print(day, ":")
    print(statistics.mean(days[day]))
    print(statistics.median(days[day]))

#B 1 2
print(intervals)
print(days_list)
average_intervals = {}
for interval in intervals:
    average_intervals[interval]= intervals[interval] / len(days_list)
print(average_intervals)

#b 1 graph
intervals = []
average_steps = []
for interval in average_intervals:
    intervals.append(interval)
for step in average_intervals.values():
    average_steps.append(step)
plt.plot(intervals,average_steps)
plt.show()


#C1 

print(counter_NA)

#C  3
print(days_of_NA)
total_steps_per_day_no_NA = {}
for day in days_of_NA:
    total = 0
    for steps in days_of_NA[day]:
        total += steps
        total_steps_per_day_no_NA[day] = total
print(total_steps_per_day_no_NA)

#C4
plt.bar(total_steps_per_day_no_NA.keys(),total_steps_per_day_no_NA.values(),1.0)
plt.show()
for day in days_of_NA:
    print(day, ":")
    print(statistics.mean(days_of_NA[day]))
    print(statistics.median(days_of_NA[day]))

#D 2
average_intervals_weekdays = {}
for interval in weekdays:
    average_intervals_weekdays[interval]= weekdays[interval] / len(weekdays_list)
print(average_intervals_weekdays)
average_intervals_weekend = {}
for interval in weekend:
    average_intervals_weekend[interval] = weekend[interval] / len(weekend_list)
print(average_intervals_weekend)

#graph
weekdays_intervals = []
weekend_intervals = []
average_steps_weekdays = []
average_steps_weekend = []
for interval in average_intervals_weekdays:
    weekdays_intervals.append(interval)
for step in average_intervals_weekdays.values():
    average_steps_weekdays.append(step)
for interval in average_intervals_weekend:
    weekend_intervals.append(interval)
for step in average_intervals_weekend.values():
    average_steps_weekend.append(step)
plt.plot(weekdays_intervals,average_steps_weekdays)
plt.show()
plt.plot(weekend_intervals,average_intervals_weekend)
plt.show()

