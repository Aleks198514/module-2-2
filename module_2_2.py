a=int(input('ведите 1 число: '))
b=int(input('ведите 2 число: '))
c=int(input('ведите 3 число: '))
if a==b==c:
    print(3)
elif a==b or b==c or a==c:
    print(2)
else:
    print(0)