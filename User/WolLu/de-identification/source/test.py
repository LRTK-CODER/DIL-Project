def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a * b
def div(a,b):
    return a/b

a = int(input())
c = input()
b = int(input())

if c=='+':
    print(add(a,b))
elif c=='-':
    print(sub(a,b))
elif c=='':
    print(mul(a,b))
elif c=='/':
    print(div(a,b))