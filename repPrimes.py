import random


# Pseudocode in comments from https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test
# The Miller-Rabin test (implemented here) is based on the Fermat Primality test
def main(n, k):
    r = 0                                       # Write n − 1 as 2^r·d with d odd by
    d = n - 1                                   # factoring powers of 2 from n − 1
    while True:
        quotient, remainder = divmod(d, 2)
        if remainder == 1:
            break
        r += 1
        d = quotient

    for cur in range(0, k):                     # repeat k times:
        a = random.randrange(2, n - 2)          #   Pick a random integer a in the range [2, n − 2]
        x = pow(a,d,n)                          #   x ← a^d mod n
        if x == 1 or x == n - 1:
            continue                            #   if x = 1 or x = n − 1 then continue WitnessLoop
        for cur2 in range (0, r - 1):           #   repeat r − 1 times:
            x = pow(x,2,n)                      #       x ← x2 mod n
            if x == 1:                          #       if x = 1 then return composite
                return False
            elif x == n - 1:                    #       if x = n − 1 then continue WitnessLoop
                continue
        return False                            #   return composite
    return True                                 # return probably prime

if __name__ == '__main__':
    strNum = '11'
    length = 2
    while True:                                 # Loops infinitely by default
            num = int(strNum)
            res = main(num, 4)
            if res:
                print(strNum + ' | ' + str(length))
            elif length % 10 == 0:              # Every 10 for the sake of console speed
                print(str(length))
            strNum += '1'
            length += 1