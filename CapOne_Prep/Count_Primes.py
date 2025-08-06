#Practice Problem URL =https://leetcode.com/problems/count-primes/

class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n<2: 
            return 0
        primes=[True] *n 

        primes[0]= False
        primes[1]=False

        i=2
        while i*i < n: 
            if primes[i]: 
                for j in range(i*i,n,i): 
                    primes[j]=False
            i+=1
        return sum(primes)
        