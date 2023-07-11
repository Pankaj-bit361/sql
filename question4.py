

str = input("Enter you Input: ")
str2 = str[::-1]

print(str2)




employee=[
    {"name":"john", "salary":3000, "designation": "developer"},
    {"name":"Emma", "salary":4000, "designation": "manager"},
    {"name":"Kelly", "salary":3500, "designation": "tester"}
]

def find_max(employees):
    maxs = 0
    arr=[]
    for i in employees:
        # print(i)
        if i["salary"] > maxs:
            maxs = i["salary"]

    print(maxs)

    for i in employees:
        if i["salary"] == maxs:
            return i
value = find_max(employee)

print(value)
            







