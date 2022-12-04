import csv
data=[]
with open("data.csv","r") as f:
    csvreader=csv.reader(f)
    for row in csvreader:
        data.append(row)
hd=data[0]
pl_dt=data[1:]

for data_point in pl_dt:
    data_point[2] = data_point[2].lower()

pl_dt.sort(key=lambda pl_dt:pl_dt[2])
with open("data_srtd.csv","a+") as f:
    csvwriter=csv.writer(f)
    csvwriter.writerow(hd)
    csvwriter.writerow(pl_dt)

with open("data_srtd.csv") as input,open('data_srtd1.csv', 'w', newline='') as output:
    writer=csv.writer(output)
    for row in csv.reader(input):
        if any(field.strip() for field in row):
            writer.writerow(row)
