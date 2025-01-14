'''
Created on 10/18/17
@author:   bpatton rkim4
Pledge:    I pledge my honor that I have abided by the Stevens Honor System.

Brandon Patton
Ronald Kim

CS115 - Hw 6
'''
# Number of bits for data in the run-length encoding format.
# The assignment refers to this as k.
COMPRESSED_BLOCK_SIZE = 5

# Number of bits for data in the original format.
MAX_RUN_LENGTH = 2 ** COMPRESSED_BLOCK_SIZE - 1

# Do not change the variables above.
# Write your functions here. You may use those variables in your code.

'''Comment Question Answers:'''
#The largest number of bits would be 325
#I used the tests given in the assignment. The rations I found were the following:
#Penguin: 1.484375
#Smile: 1.328125
#Five: 1.015625
#In the worst case input, the program must alternate between 0's and 1's at every bit
#and has to start with 1, making the output longer than the original string no matter what.
#The length of the compressed string will always be the compressed block size multiplied
#by 65.


def countRun(s, c, maxRun, count):
    """
    Param s: is a string
    Param c: is what we're counting
    Param maxRun: maximum length of run
    Takes a string returns the number of times
    that string occurs in that block
    """
    if s == '':
        return count
    if count == maxRun:
        return count
    if c == '0':
        if s[0] == '0':
            return countRun(s[1:], c, maxRun, count + 1) 
        if s[0] == '1':
            return count
    if c == '1':
        if s[0] == '1':
            return countRun(s[1:], c, maxRun, count + 1)
        if s[0] == '0':
            return count
        

def fiveBits(s):
    '''Makes sure every block is 5 bits by adding necessary 0's'''
    if len(s) >= 5:
        return s
    else:
        return fiveBits('0' + s)
    

def numToBinary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the binary representation of non-negative integer n.
    If n is 0, the empty string is returned.'''
    if n == 0:
        return ''
    if n % 2 == 1:
        return numToBinary(n//2) + '1'
    return numToBinary(n//2) + '0'    


def compress(s):
    """
    Return compressed string
    count the runs in s switching
    from counting runs of zeroes to counting runs ones
    return compressed string 
    """
    def compress_helper(s,c):
        '''Helps the compress function by using c and next c to switch between
        0's and 1's'''
        if s == '':
            return ''
        runlen = countRun(s,c,MAX_RUN_LENGTH, 0)
        runlenBinary = fiveBits(numToBinary(runlen))
        nextC = '0'
        if c =='0':
            nextC = '1' 
        return runlenBinary + compress_helper(s[runlen:], nextC)
    return compress_helper(s,'0')



def binaryToNum(s):
    '''Precondition: s is a string of 0s and 1s.
    Returns the integer corresponding to the binary representation in s.
    Note: the empty string represents 0.'''
    def bToN_helper(s, accum):
        if s == '':
            return 0
        if int(s[-1]) == 1:
            return accum + bToN_helper(s[:-1], accum * 2)
        return bToN_helper(s[:-1], accum * 2)
    return bToN_helper(s, 1)


def uncompress(s):
    """
    param s:
    in chunks of COMPRESSED_BLOCK_SIZE,
    convert the binary represenation of a number
    in that block into that many zeros or ones,
    switching from decompressing zeros to decompressing
    ones alternatively
    return decompressed string
    """
    def uncompress_helper(s,c):
        '''Helps uncompress function by using c to expand each compressed block to original size'''
        if s == '':
            return ''
        first5 = s[:COMPRESSED_BLOCK_SIZE]
        first5Num = binaryToNum(first5)
        uncompressed_bit = c * first5Num
        nextC = '0'
        if c =='0':
            nextC = '1' 
        return uncompressed_bit + uncompress_helper(s[COMPRESSED_BLOCK_SIZE:], nextC)
    return uncompress_helper(s, '0')


def compression(s):
    """
    Returns ratio of compressed string length and string length
    """
    compressed_string_length = len(compress(s))
    string_length = len(s)
    return compressed_string_length/string_length
    
