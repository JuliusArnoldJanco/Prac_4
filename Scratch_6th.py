# Lottery Numbers - www.101computing.net/lottery-numbers

import random


def main():

    qp = input("How many quick picks?")
    qp = int(qp)


    '''Quick Pick Function: Returns: a row of random numbers 1-45'''

    def Quick_Picks():

        lucky_nums = []

        for i in range(0, 6):

            '''Generates random number'''

            num = random.randint(1, 45)

            '''Same number error check'''

            while num in lucky_nums:

                '''Picks new number'''

                num = random.randint(1, 45)


            '''Apends new number'''

            lucky_nums.append(num)

        '''Ascending order'''

        lucky_nums.sort()

        '''Returns line of lottery numbers'''

        return lucky_nums

    '''Arranges format of the output numbers to a column width of 2'''

    for i in range(qp):
        print(' '.join(('%*s' % (2, i) for i in Quick_Picks())))

main()
