import math
# BEGIN (write your solution here)

x = input('x = ')
figure = input('figure is: ')

try:
    x = float(x)
    figure = str(figure)

except:
    print('error: invalid types')
    exit(1)

if x <= 0:
    print('error: x must be positive')
    exit(1)

if figure == 'square':
    print('area is %.2f' % (x * x))

elif figure == 'circle':
    print('area is %.2f' % (math.pi * x * x))

else:
    print('error: unknown figure')
    exit(1)