# preamble: a series of n numbers, after which each following number is the sum
# of any two of the previous n numbers
PREAMBLE_LENGTH = 25
INPUT = [int(line) for line in open('input.txt', 'r').readlines()]

def check(i, set):
    
    # nested for loop iterates one number in the set against every other
    for num1 in set:
        for num2 in set:
            
            # skip this comparison if they're the same number
            if num1 != num2:

                # test 
                if (num1 + num2) == i:
                    return False
    
    # didn't pass test
    return True

def findOddOne(input):

    # the series against which to check each number
    preamble = input[:PREAMBLE_LENGTH]

    # first digit after preamble
    i = input[len(preamble)]

    # check this number
    if not check(i, preamble):
        # move everything forward one digit by removing the 1st number
        input.pop(0)
        # try again
        findOddOne(input)
    else:
        print(i)


findOddOne(INPUT)