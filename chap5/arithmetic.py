result = {
    "+": "x+y",
    "-": "x-y",
    "*": "x*y",
    "/": '''x/y if y!=0   \
        else "divided by zero"'''
}
x = int(input())
z = input().strip()
y = int(input())
r = eval(result.get(z))
if type(r) != str:
    print(format(r, '.2f'))
else:
    print(r)
