print("Welcome to Bill Tip Splitter!")
total_bill=float(input("What is your total bill? rs.\n"))
percent =float(input("How much tip would you like to give? 10 , 12 , 15?\n"))
n=float(input("How many people are splitting the bill\n"))
if percent==10:
    print("Each person should pay:",round(((10/100)*total_bill)/n,3),"Rs.")
elif percent==12:
    print("Each person should pay:",round(((12/100)*total_bill)/n,2),"Rs.")
elif percent==15:
    print("Each person should pay:", round(((15/100)*total_bill)/n,2),"Rs.")
else:
    print("Invalid input")


