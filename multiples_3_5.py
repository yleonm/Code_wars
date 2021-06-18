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