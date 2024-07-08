print('Garding System.\n')

name = str(input('Enter the Student name: '))

marks = int(input('Enter score: '))

if marks>=80 and marks<=100:
    print('Distinction 1')

elif marks>=70 and marks<=80:
    print('Distinction 2')

elif marks >= 60 and marks<=70:
    print('Credit')

elif marks>=40 and marks<=60:
    print('Pass'),

elif marks<40:
    print('Fail'),
