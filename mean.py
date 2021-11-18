import csv
with open ('SOCR-HeightWeight.csv',newline='')as f:
    reader=csv.reader(f)
    filedata=list(reader)

filedata.pop(0)
newdata=[]
for i in range(len(filedata)):
    m=filedata[i][1]
    newdata.append(float(m))

n=len(newdata)
total=0
for x in newdata:
    total+=x

mean=total/n
print('mean of height data is :'+str(mean))