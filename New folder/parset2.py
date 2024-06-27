print('enter your marks:')
marks = input()

if int(marks)<= 25:
    print('f')
elif int(marks)<= 45:
    print('e')
elif int(marks)<= 50:
    print('d')
elif int(marks)<= 60:
    print('c')
elif int(marks)<= 80:
    print('b')
elif int(marks)<= 100:
    print('a')
else:
    print('marks are wrong!')
