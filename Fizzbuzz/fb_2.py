numlist = ()
numlist1 = list(numlist)

def tester(number, flag):

    while number != 0 and flag == 0:

     if number < 0:
         flag = 1 
         return 1

     if number > 0:
         number = number - 1 

    return 2

unum = input("Enter size of list: ")

for i in range(1, int(unum)):

    num_d_three = (i/3 - 1)
    num_d_five = (i/5 - 1)
    flag = 0 

    d_three = tester(num_d_three, flag)

    d_five = tester(num_d_five, flag)

    if d_three == 2 and d_five == 2:
        numlist1.append("Fizz Buzz")
    elif d_three == 2:
        numlist1.append("Fizz")
    elif d_five == 2:
        numlist1.append("Buzz")
    else:
        numlist1.append(i)

print(numlist1)




