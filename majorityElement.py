#UTF-8

#!/usr/bin/env python3

#User function template for Python 3

class Solution:
    def majorityElement(self, A: list, N: int) -> int:
        """Given an array 'A' of size 'N' return the majority element in the array.
        If there is no majority element return -1.

        Args:
            A (list): list of unsorted integers
            N (int): integer == len(A), N >= 1, N <= 10000000

        Returns:
            int: value of majority element in list(A)
        """
        
        # quick check to ensure not wasting time
        if N == 1:
            return A[0]
        elif N == 0:
            return -1         
        elif ( N != len(A) ) or ( N > 10**7 ):
            return -1
        
        # parameters
        majorityThreshold = N // 2  # number to beat to be majority
        #print("majorityThreshold: ", majorityThreshold)
        count = 0   # counter variable
        candidate = None    # will equal value of current suspected majority element during search
        arrIndex = 0    # will hold current arrIndex to make sure we have looped out of bounds
        #prevCandidate = None    # former heavyweight (may not need this)
        
        # sort array
        # necessary for accuracy and space / constant operations efficiency
        # O(N log N)
        A.sort()
                
        # loop search for majority element
        while count <= majorityThreshold and arrIndex < N :
            # candidate capture
            if candidate != A[arrIndex]:
                # if previously set
                # if candidate:
                #     # record candidate change
                #     prevCandidate = candidate
                    
                # save current contender
                candidate = A[arrIndex]
                
                # reset counter after candidate change
                # start at 1 given that your candidate
                # is the first instance of the new number
                # being evaluated
                count = 0
                arrIndex += 1
                continue
                
            # increment array index to continue the loop
            arrIndex += 1
            count += 1
            
        if count > majorityThreshold:
            return candidate
        else:
            return -1
                
        
#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math

from sys import stdin


def main():
        # T=int(input())
        # while(T>0):
            
        #     N=int(input())

        #     A=[int(x) for x in input().strip().split()]
            
            
        #     obj = Solution()
        #     print(obj.majorityElement(A,N))
            
        #     T-=1

        N = 1
        # print("n//2 == ", N//2)
        A=[int(x) for x in [15]]
            
        obj = Solution()
        print(obj.majorityElement(A,N))


if __name__ == "__main__":
    main()

# END of code