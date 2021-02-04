"""
Count the number of prime numbers less than a non-negative number, n.

Example 1:

Input: n = 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
Example 2:

Input: n = 0
Output: 0
Example 3:

Input: n = 1
Output: 0
 

Constraints:

0 <= n <= 5 * 106


"""
# Here is a pretty classical programming question which has its origin back to ancient Greece
# The clasic solution is Sieve of Eratosthenes, which you can check upon the website:\
# https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
     # when n is smaller/ equal to 2, 1 and 2 don't count for primes   
     if n <= 2:
         return 0
     # create a text-based table in python
     # mark each number is True
     table = [True] * n
     # the index starts from 0 and since the first two items are not prime numbers, assign the values to false
     table[0], table[1] = False, False
     
     i = 2
     
     # Here is the logic: to calculate the i^2 first, and then goes forward with i each time->which are also the multiples of i
     # assign the multiples of i as False, so they are not prime numbers 
     # For example, assumes n = 100
     # when i = 3, 3 * 3 = 9, then j will be iterated from [9,100), each time j += 3
     # so 9,12,15,18... will be marked as False
     # then what about 6? 6 is already marked when i == 2
     # This is the process which can help avoid the repetition and reduce the computation time
     while i * i < n:
          if table[i]:
              for j in range(i * i, n, i) :
                  table[j] = False
           i += 1
     # sum() function returns the sum of all the True statement in the loop ,since True is regarded as 1     
     return sum(table)
