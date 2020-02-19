import numpy as np
n = int(input('enter the number of elements :'))

a1 = np.zeros((2,n))
a2 = np.zeros((2,n))
r = np.zeros((2,n))

print('enter the elements of first set :')
for i in range(0,n):
    a1[0][i] = i+1
    r[0][i] = i+1
    a1[1][i] = float(input())

print('enter the elements of second set :')
for i in range(0,n):
    a2[0][i] = i+1
    a2[1][i] = float(input())

print()
for i in range(0,n):
    print('(',int(a1[0][i]),',',a1[1][i],')',end='')
print()
for i in range(0,n):
    print('(',int(a2[0][i]),',',a2[1][i],')',end='')

print('\n\n-----------SELECT CHOICE------------')
print(' 1. UNION\n 2. INTERSECTION\n 3. DIFFERENCE\n 4. COMPLEMENT\n')
ch = int(input(':'))

if(ch == 1):
    for i in range (0,n):
        if(a1[1][i] > a2[1][i]):
            r[1][i] = a1[1][i]
        else:
            r[1][i] = a2[1][i]
elif(ch == 2):
    for i in range (0,n):
        if(a1[1][i] < a2[1][i]):
            r[1][i] = a1[1][i]
        else:
            r[1][i] = a2[1][i]
elif(ch == 3):
    for i in range (0,n):
        a2[1][i] = 1 - a2[1][i]
    for i in range (0,n):
        if(a1[1][i] < a2[1][i]):
            r[1][i] = a1[1][i]
        else:
            r[1][i] = a2[1][i]
elif(ch == 4):
    for i in range (0,n):
        a1[1][i] = 1 - a1[1][i]
    for i in range (0,n):
        a2[1][i] = 1 - a2[1][i]
else:
    print('invalid')
    exit(0)

if(ch == 4):
    print('complement of 1st set :')
    for i in range(0,n):
        print('(',int(a1[0][i]),',',a1[1][i],')',end='')
    print()
    print('complement of 2nd set :')
    for i in range(0,n):
        print('(',int(a2[0][i]),',',a2[1][i],')',end='')
    print()
else:
    print('result :')
    for i in range(0,n):
        print('(',int(r[0][i]),',',r[1][i],')',end='')
    print()