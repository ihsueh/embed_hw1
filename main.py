# Part. 1
#=======================================
# Import module
#  csv -- fileIO operation
import csv
#=======================================
# Part. 2
#=======================================
# Read cwb weather data
cwb_filename = '106062225.csv'
data = []
header = []
with open(cwb_filename) as csvfile:
    mycsv = csv.DictReader(csvfile)
    header = mycsv.fieldnames
    for row in mycsv:
        data.append(row)
k=[]
for i in data:
    if i['PRES']=='-99.000':
        k.append(data.index(i))
k.reverse()
#print(k)
for i in k:
    del data[i]
name =['C0A880', 'C0F9A0', 'C0G640', 'C0R190', 'C0X260']
w = {}
try1 = []
for n in name:
    w[n]=[]
    for i in data:
        if (i['station_id']==n) :
            w[i['station_id']].append(i['PRES'])
            #w[i['station_id']] = [i['PRESS']]
            #w[i['station_id']].append(4)
            #w['C0A880'][0]='3'
            #print(len(w[i['station_id']]))

            #w[n][1]='3'
            #w[n][len.w[n]+1]=i['PRESS']
for i in w.items():
    a = i[1]
    sum = 0
    if(len(a)):
        for k in a:
            sum += float(k)
        sum = sum/len(a)
        t1 = [i[0], round(sum, 2)]
    else:
        t1 = [i[0], 'None']
    try1.insert(len(try1), t1)
print(try1)
def targetid(x):
    de = False
    for i in name:
        if(x['station_id']==i):
            de = True
    return de
#target_data = list(filter(targetid, data))

#target_data = data[:1]

#print(target_data)
