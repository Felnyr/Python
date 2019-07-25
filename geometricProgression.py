# Geometric progression

def checkGeometric():
    print("input the first number")
    num1 = int(input())
    print("input the secound number")
    num2 = int(input())  
    print("input the third number")  
    num3 = int(input())

    arr = [num1,num2,num3]
    arr.sort()

    # Geometric progression property check
    if arr[1]*arr[1] == arr[0]*arr[2]:
        print('Geometric progression found')
    else:
        print('Geometric progression not found')

checkGeometric()

# http://matematyka.pisz.pl/strona/279.html

x = 1.5