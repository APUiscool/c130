import csv
import pandas as pd

final = []
srt = []

with open("final.csv", "r") as f:
    csv_reader=csv.reader(f)
    for i in csv_reader:
        srt.append(i)
        
with open("data_srtd.csv", "r") as f:
    csv_reader=csv.reader(f)
    for i in csv_reader:
        final.append(i)

hd1=final[0]
hd2=srt[0]
pl_dt1=final[1:]
pl_dt2=srt[1:]

hd=hd1+hd2
pl_dt =[]
for index,data_row in enumerate(pl_dt1):
    pl_dt.append(pl_dt1[index])

for index,data_row in enumerate(pl_dt2):
    pl_dt.append(pl_dt1[index]+pl_dt2[index])
with open("table.csv","a+") as f:
    csvwriter=csv.writer(f)
    csvwriter.writerow(hd)
    csvwriter.writerows(pl_dt)
