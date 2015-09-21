import math

a = input('a = ')
b = input('b = ')
c = input('c = ')

try:
    a = int(a)
    b = int(b)
    c = int(c)

except:
    print('error: some values are not integers')
    exit(1)

if a == 0:
    print('error: `a` mustn\'t be a zero')
    exit(1)

D = b * b - 4 * a * c
print('D = %.2f' % D)

if D > 0:
    x1 = (-b + math.sqrt(D)) / (2 * a)
    x2 = (b + math.sqrt(D)) / (2 * a)
    print('x1 = %.2f, x2 = %.2f' % (x1, x2))

elif D == 0:
    x = -b / float(2 * a)
    print('x = %.2f' % x)
else:
    print('no result')
