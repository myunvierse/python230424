#DemoDict.py
color = {"apple":"red","banana":"yello"}
color["kiwi"] = "green"
print(color)
print(color["apple"])

print("--- 형식변경---")
a=set((1,2,3))
print(a)
b=list(a)
b.append(4)
print(b)

device = {"아이폰":5, "아잉패드":10, "윈도우":20}
device["맥북"] =15
for item in device.items():
    print(item) #튜플

for k,v in device.items():
    print(k,v)  


phone = {"kim":"111","lee":"222","park":"333"}
print("park" in phone)
print("kang" not in phone)
p = phone
print(phone)
print(p)
print(id(phone),id(p))