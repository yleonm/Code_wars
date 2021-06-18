"""If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
The sum of these multiples is 23.

Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number
 passed in.

Note: If the number is a multiple of both 3 and 5, only count it once. Also, if a number is 
negative, return 0(for languages that do have them)
"""

def solution(number):
    if number < 0:
        return 0
    elif number >=0:
         lista = [x for x in range(1,number)]
         contador = 0
         for x in lista:
             if x%5 == 0 and x%3 == 0:
                 contador += x
             elif x%5 ==0 or x %3 == 0:
                 contador+=x
    return contador

print(solution(10))

def solution_2(number):
    return sum(x for x in range(number) if x % 3 == 0 or x % 5 == 0)

print(solution_2(-6))

from itertools import chain

def solution_4(number):
    return sum(set(chain(range(3,number,3), range(5,number,5))))

print(solution_4(10))



"""def solution_3(number):
    threes = range(3, number, 3)
    fives = range(5, number, 5)
    return sum(list(set(threes + fives)))

print(solution_3(10))"""