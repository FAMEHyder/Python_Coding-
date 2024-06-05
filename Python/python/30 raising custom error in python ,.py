a = int (input("Enter any value between 1 and 5 :"))

if (a<1 or a>5):
    raise ValueError("The value of a should be between 1 and 5")