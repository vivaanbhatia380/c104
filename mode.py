from collections import Counter
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
data=Counter(newdata)
modedata_forrange={
    '50-60':0,
    '60-70':0,
    '70-80':0
}
for height,occurance in data.items():
    if 50<float(height)<60:
        modedata_forrange['50-60']+=occurance
    elif 60<float(height)<70:
        modedata_forrange['60-70']+=occurance
    elif 70<float(height)<80:
        modedata_forrange['70-80']+=occurance

moderange,modeoccurance=0,0
for range,occurance in modedata_forrange.items():
    if occurance>modeoccurance:
        moderange,modeoccurance=[int(range.split('-')[0]),int(range.split('-')[1])],occurance

mode=float((moderange[0]+moderange[1])/2)
print(mode)

