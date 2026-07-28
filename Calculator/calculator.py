def add(i,j):
    return i+j
def sub(i,j):
    return i-j
def mul(i,j):
    return i*j
def div(i,j):
    return i/j
to_continue="yes"
while to_continue:
 a=int(input("whats the first number?:"))
 b=int(input("whats the second number?:"))
 op=input("what do you want to do?:\n + ,-,* or /")
 if op == "+":
    print(f"{a} {op} {b} =",add(a,b))
 elif op == "-":
     print(f"{a} {op} {b} =",sub(a,b))
 elif op == "*":
    print(f"{a} {op} {b} =",mul(a,b))
 elif op == "/":
    print(f"{a} {op} {b} =",div(a,b))
 else:
    print("invalid input")
 to_continue=input("Do you want to continue?type y for yes and n for no:").lower()
 if to_continue == "n":
     print("Good Bye!")
     to_continue=False


