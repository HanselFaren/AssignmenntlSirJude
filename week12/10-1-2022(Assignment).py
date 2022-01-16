import csv
import statistics as st
import pandas as pd
import pygal

dictionaryWeekday = {}
dictionaryWeekend = {}
filename = 'activity.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header = next(reader)

    wr = open("WeekendActivity.csv", "w")
    wr.write(str(header[0]) + "," + str(header[1]) + "," + str(header[2]))
    wr.write("\n")

    n = 0
    for row in reader:
        interval = int(row[2])
        if (row[0] == "NA"):
            row[0] = 0
            n += 1
        steps = row[0]
        temp = pd.Timestamp(row[1])
        if temp.dayofweek < 5:
            row.append("weekday")
            dictionaryWeekday.setdefault(interval, [])
            dictionaryWeekday[interval].append(int(steps))
        else:
            row.append("weekend")
            dictionaryWeekend.setdefault(interval, [])
            dictionaryWeekend[interval].append(int(steps))
        wr.write(str(row[0]))
        wr.write(str(row[0]) + "," + str(row[1]) + "," + str(row[2]) + "," + str(row[3]))
        wr.write("\n")

    wr.close

AvgperIntervalWeekend = []
AvgperIntervalWeekday = []

for i in dictionaryWeekday.keys():
    AvgperIntervalWeekday.append(st.mean(dictionaryWeekday.get(i)))

for i in dictionaryWeekend.keys():
    AvgperIntervalWeekend.append(st.mean(dictionaryWeekend.get(i)))

hist = pygal.Bar()
hist.title = "Average per interval on the Weekdays"
hist.x_title = "The interval"
hist.y_title = "Average per interval"
hist.x_labels = dictionaryWeekday.keys()
hist.add("Average steps", AvgperIntervalWeekday)
hist.render_to_file('stepsversion2.svg')

hist = pygal.Bar()
hist.title = "Average per interval on the Weekends"
hist.x_title = "The interval"
hist.y_title = "Average per interval"
hist.x_labels = dictionaryWeekend.keys()
hist.add("Average steps", AvgperIntervalWeekend)
hist.render_to_file('stepsversion3.svg')

print("The total number of missing values is ", n)
print("New dataset created")