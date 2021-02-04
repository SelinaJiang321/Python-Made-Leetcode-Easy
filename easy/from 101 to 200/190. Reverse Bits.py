"""
Reverse bits of a given 32 bits unsigned integer.

Example 1:

Input: n = 00000010100101000001111010011100
Output:    964176192 (00111001011110000010100101000000)
Explanation: The input binary string 00000010100101000001111010011100 represents the unsigned integer 43261596, so return 964176192 which its binary representation is 00111001011110000010100101000000.
Example 2:

Input: n = 11111111111111111111111111111101
Output:   3221225471 (10111111111111111111111111111111)
Explanation: The input binary string 11111111111111111111111111111101 represents the unsigned integer 4294967293, so return 3221225471 which its binary representation is 10111111111111111111111111111111.

"""

class Solution:
    # @param n, an integer
    # @return an integer
    # the target of this function is to reverse the whole number in bits
    def reverseBits(self, n):
        rev, power = 0, 31
        # while n is not 0 , which means that the bit manipulation hasn't finished yet
        while n:
        # n & 0000 0000 0000 0000 0000 0000 0000 0001
        # the least significant bit( the right most bit) << power then becomes the most significant bit in the return value
        # power -= 1 then the second most sig bit
        # n >> 1 then the second last least least sig bit
            rev += (n & 1) << power
            power -= 1
            n = n >> 1
            
        return rev
