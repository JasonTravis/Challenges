
from tqdm import tqdm

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

for i in tqdm(range(1, 10000)):

    for j in range(1, 10000):

        p_t = i/j
        
        flag = 0 

        p_r = tester(p_t, flag)

        if p_r == 2:
            if i == j:
                numlist1.append(i)

print(numlist1)
        

        
