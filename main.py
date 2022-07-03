from textwrap import indent
import json

header=[]
parsed_data = []
temp =""
temp2 = ""
temp3 = [] 

with open("sample.txt" ,'r',) as f1:
    line = f1.read().splitlines()
    for i in range(0,5):
        temp = temp + line[i].strip()
    
    for i in  range(0, len(temp.split(' '))):
        if(temp.split(' ')[i] != "" and temp.split(' ')[i] not in temp3):
            header.append(temp.split(' ')[i])

    for j in range(5, len(line)):
        for item in line[j].split(" "):
            if(item != "" and not(item.isnumeric()) and not(item.isupper())):
                temp2 = temp2 +" "+item
            elif(item != "" and not(item.isnumeric()) and (item.isupper())):
                temp3.append(temp2)
                temp3.append(item)
                temp2=""
            elif (item != "" and (item.isnumeric()) and not(item.isupper())):
                temp3.append(item)


k = 0
while(k<len(temp3)):
    dict={}
    dict[header[k%3]] = temp3[k]
    dict[header[k%3 +1]] = temp3[k +1]
    dict[header[k%3 +2]] = temp3[k +2]
    parsed_data.append(dict)
    k+=3

with open("output.json", "w") as file:
    json.dump(parsed_data, file ,indent=2)