print ("welcome to my dictionary")

dic = {
    "Hyder" : "angry lion",

    "abbas" : "hunting lion ",

    "ali": "attacking lion"




}

print(dic["abbas"],dic["Hyder"],dic["ali"],sep='    ~    ')


print ("employee details of my company")
dic1 = {

        "ali" : "1122h",
        "ahmad": "1122g",
        "aslam": "1122j",
        "dilawer": "1122y"



}

print (dic1["ali"])

dic2 = {"name":"zeeshan hyder","age" : 22, "code name":"sattara","mission": "love"}

print (dic2)

print (dic2.keys())

print (dic2.values())


for key in dic2.keys():
    print (f"{key} is {dic2[key]}")



print (dic2.items())

for key,value in dic2.items():
    print (f"{key} is {value}")