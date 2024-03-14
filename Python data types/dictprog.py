# dictionary inro and print
employee = {"name": "agniswar", "ID" : 200, "salary" : 2000.69}
print("name of the employee" , employee['name'])
employee["dept"] = "Computer Sc"
print("Dept of the employee" , employee['dept'])
print("The whole dict" , employee)


# printing the key valey 

employee = {"name": "agniswar", "ID" : 200, "salary" : 2000.69}

# printing the keys of the dictionary
print("Dictionary keys" , employee.keys())

print("Dictionary values" , employee.values())

print("Dictionary items" , employee.items())


# nested dictionary

employee = {"emplote_code": {"name": "Agniswar" , "other_key" : 563.29}, "ID" : 200, "salary" : 2000.69}

print(employee)

from collections import OrderedDict

d = OrderedDict();

d["abc1"] = {"name": "agniswar", "ID" : 200, "salary" : 2000.69}
d["xvb2"] =  {"name": "agniswar2", "ID" : 300, "salary" : 4000.69}
d["opp3"] =  {"name": "agniswar3", "ID" : 400, "salary" : 6000.69}


for i,j in d.items():
    print(i, j, sep="\t")


d = {"1" : 1, "2" : 6, "1" :9}

print(d)
#delete the id
employee = {"name": "agniswar", "ID" : 200, "salary" : 2000.69}
del employee['ID']

print(employee)
# get fuction also can access value from the key
print(employee.get("name"))