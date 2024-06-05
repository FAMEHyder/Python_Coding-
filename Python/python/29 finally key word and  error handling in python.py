a = input("Enter your number:" )
print(f"multiplication table of {a}")
try:
    for i in range(1,11):
        print (f"{a}X{i} = {int(a)*int (i)}")

except Exception as e:
    print (e)

# print ("In this case the rest code will run without any problem")



finally:
    print ("This line of code will always run")

    #finally code will always run even if it is in function and the function returns any value before finally