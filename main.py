from textwrap import indent
import json

header=[]
parsed_data=[]

with open("sample.txt" ,'r',) as f1:
    lines = f1.readlines()

line_no=1
temp =""
temp2=""
temp3=[] 

for line in lines:
    if(line_no <= 5):
        temp = temp + line.strip()
    else:
        for row in line.split("\n"):
            for item in row.split(" "):
                if(item != "" and not(item.isnumeric()) and not(item.isupper())):
                    temp2 = temp2 +" "+item
                elif(item != "" and not(item.isnumeric()) and (item.isupper())):
                    temp3.append(temp2)
                    temp3.append(item)
                    temp2=""
                elif (item != "" and (item.isnumeric()) and not(item.isupper())):
                    temp3.append(item)
    line_no+=1

for col in  temp.split(' '):
    if(col != "" and col not in header):
        header.append(col)


parsed_data=[]
j=0
while(j<len(temp3)-1):
    d={}
    for i in range(0, len(header)):
        d[header[i]]=temp3[i+j]
    parsed_data.append(d)
    j+=3

print(json.dumps(parsed_data, indent=2))




