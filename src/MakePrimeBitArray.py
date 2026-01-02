from bitarray import bitarray
import time

numberOfSieves = 0

# This sieve follows the classic definition where each prime is used from start to finish
# For example 2 will change every even number greater than 2 to False
# But 3 doesn't account for already marked composites such as 6
def simpleSieve1(size):
    N = size
    primes = bitarray(N)
    primes.setall(True)

    # Mark 0 and 1 as not prime
    primes[0] = False
    primes[1] = False

    # Sieve of Eratosthenes
    n = 2
    while n < N:
        if primes[n] == True:
            m = n+n
            while m < N:
                primes[m] = False
                m += n
        n += 1

    return primes


# This version only checks up until we have reached the square root of the max value
# For example if size is 100, we only need to sieve through 2, 3, 5, and 7 since
# all other composite numbers less than the square root of 100 will already be
# accounted for
def simpleSieve2(size):
    N = size
    primes = bitarray(N)
    primes.setall(True)

    # Mark 0 and 1 as not prime
    primes[0] = False
    primes[1] = False

    # Sieve of Eratosthenes
    n = 2
    while n * n < N:
        if primes[n] == True:
            m = n + n
            while m < N:
                primes[m] = False
                m += n
        n += 1

    return primes


# This version includes the previous improvement, but also starts the next prime numbers checks at its square.
# This reduces double checks of composites such as 2 finding 6 and then 3 finding 6 in the next itteration.
def simpleSieve3(size):
    N = size
    primes = bitarray(N)
    primes.setall(True)

    # Mark 0 and 1 as not prime
    primes[0] = False
    primes[1] = False

    # Sieve of Eratosthenes
    n = 2
    while n * n < N:
        if primes[n] == True:
            m = n*n
            while m < N:
                primes[m] = False
                m += n
        n += 1

    return primes


# This version takes into account that every second check will have already been done by 2, so
# it skips every other check for primes greater than 2
def simpleSieve4(size):
    N = size
    primes = bitarray(N)
    primes.setall(True)

    # Mark 0 and 1 as not prime
    primes[0] = False
    primes[1] = False

    # Sieve for just 2
    n = 4
    while n < N:
        primes[n] = False
        n += 2

    # Sieve of Eratosthenes with skips
    n = 3
    while n * n < N:
        if primes[n] == True:
            m = n*n
            while m < N:
                primes[m] = False
                m += 2*n
        n += 1

    return primes


# Change the increment of m so it refereences a static variable
def simpleSieve5(size):
    N = size
    primes = bitarray(N)
    primes.setall(True)

    # Mark 0 and 1 as not prime
    primes[0] = False
    primes[1] = False

    # Sieve for just 2
    n = 4
    while n < N:
        primes[n] = False
        n += 2

    # Sieve of Eratosthenes
    n = 3
    while n * n < N:
        if primes[n] == True:
            m = n*n
            jump = 2*n
            while m < N:
                primes[m] = False
                m += jump
        n += 1

    return primes


# Increment the skips based on 2 and 3
def simpleSieve6(size):
    N = size
    primes = bitarray(N)
    primes.setall(True)

    # Mark 0 and 1 as not prime
    primes[0] = False
    primes[1] = False

    # Sieve for just 2
    n = 4
    while n < N:
        primes[n] = False
        n += 2

    # Sieve for just 3
    n = 9
    while n < N:
        primes[n] = False
        n += 6

    # Sieve of Eratosthenes
    n = 5
    while n * n < N:
        if primes[n] == True:
            bigJump = 4*n
            littleJump = 2*n
            m = n + bigJump
            jump = littleJump
            while m < N:
                primes[m] = False
                m += jump
                if jump == bigJump:
                    jump = littleJump
                else:
                    jump = bigJump
        n += 1

    return primes


# Increment the position to be checked by 2 instead of 1
def simpleSieve7(size):
    N = size
    primes = bitarray(N)
    primes.setall(True)

    # Mark 0 and 1 as not prime
    primes[0] = False
    primes[1] = False

    # Sieve for just 2
    n = 4
    while n < N:
        primes[n] = False
        n += 2

    # Sieve for just 3
    n = 9
    while n < N:
        primes[n] = False
        n += 6

    # Sieve of Eratosthenes
    n = 5
    while n * n < N:
        if primes[n] == True:
            bigJump = 4*n
            littleJump = 2*n
            m = n + bigJump
            jump = littleJump
            while m < N:
                primes[m] = False
                m += jump
                if jump == bigJump:
                    jump = littleJump
                else:
                    jump = bigJump
        n += 2

    return primes


# Increment the position to be checked by 2 instead of 1
def simpleSieve8(size):
    N = size
    primes = bitarray(N)
    primes.setall(True)

    # Mark 0 and 1 as not prime
    primes[0] = False
    primes[1] = False

    # Sieve for just 2
    n = 4
    while n < N:
        primes[n] = False
        n += 2

    # Sieve for just 3
    n = 9
    while n < N:
        primes[n] = False
        n += 6

    # Sieve of just 5
    patternFor5 = [4,2]
    patternIndex = 0
    n = 5
    m = n
    m += n*patternFor5[patternIndex]
    while m < N:
        primes[m] = False
        patternIndex += 1
        if patternIndex == 2:
            patternIndex = 0
        m += n*patternFor5[patternIndex]

    # Sieve for 7+
    patternFor7AndUp = [6,4,2,4,2,4,6,2]
    patternIndex = 0
    n = 7
    while n * n < N:
        if primes[n] == True:
            patternIndex = 0
            m = n
            m += n*patternFor7AndUp[patternIndex]
            while m < N:
                primes[m] = False
                patternIndex += 1
                if patternIndex == 8:
                    patternIndex = 0
                m += n*patternFor7AndUp[patternIndex]
        n += 2

    return primes


# Use the sevens pattern but start at n*n
def simpleSieve9(size):
    N = size
    primes = bitarray(N)
    primes.setall(True)

    # Mark 0 and 1 as not prime
    primes[0] = False
    primes[1] = False

    # Sieve for just 2
    n = 4
    while n < N:
        primes[n] = False
        n += 2

    # Sieve for just 3
    n = 9
    while n < N:
        primes[n] = False
        n += 6

    # Sieve of just 5
    patternFor5 = [4,2]
    patternIndex = 0
    n = 5
    m = n
    m += n*patternFor5[patternIndex]
    while m < N:
        primes[m] = False
        patternIndex += 1
        if patternIndex == 2:
            patternIndex = 0
        m += n*patternFor5[patternIndex]

    # Sieve for 7+
    patternFor7AndUp = [6,4,2,4,2,4,6,2]
    patternIndex = 0
    startingIndex = 0
    firstSkip = 6
    n = 7
    while n * n < N:
        if primes[n] == True:
            while firstSkip != n-1:
                startingIndex += 1
                if startingIndex == 8:
                    startingIndex = 0
                firstSkip += patternFor7AndUp[startingIndex]

            m = n
            m += n*firstSkip
            patternIndex = startingIndex

            while m < N:
                primes[m] = False
                patternIndex += 1
                if patternIndex == 8:
                    patternIndex = 0
                m += n*patternFor7AndUp[patternIndex]
        n += 2

    return primes


# Calls specific sieve based on number
def simpleSieve(sieveNumber, size):
    func_name = f"simpleSieve{sieveNumber}"
    func = globals().get(func_name)
    if func:
        return func(size)
    else:
        raise ValueError(f"Function {func_name} not found.")


# Comapre two given bitarrays and return true if all values match
def comparePrimesList(primes1, primes2):
    if len(primes1) != len(primes2):
        print("Compared primes list are not the same size.")
        return False

    n = 0
    while n < len(primes1):
        if primes1[n] != primes2[n]:
            return False
        n += 1

    return True


# Test to make sure all sieves come to the same conclusion
def checkAllSievesMatch(size):
    numberOfSieves = countSieves()

    primes1 = simpleSieve1(size)

    for n in range(2, numberOfSieves+1):
        primesN = simpleSieve(n, size)
        if not comparePrimesList(primes1, primesN):
            print(f"{n}: ", end="")
            return False

    return True


# Time a single sieve
def timeSieve(sieveNumber, size):
    elapsed_time = 0

    start_time = time.time()
    primes = simpleSieve(sieveNumber, size)
    end_time = time.time()
    elapsed_time = end_time-start_time

    return elapsed_time

# Times each sieve's speed
def timeAllSieves(size):
    numberOfSieves = countSieves()
    sieveTimes = []

    for n in range(1, numberOfSieves+1):
        sieveTimes.append(timeSieve(n, size))

    return sieveTimes


# Prints all Sieve times
def printAllSieveTimes(size):
    numberOfSieves = countSieves()
    sieveTimes = timeAllSieves(size)
    for n in range(0, numberOfSieves):
        print(f"Sieve {n+1} Time:\t{sieveTimes[n]}")


# This prints the primes in a bitarray "primes" up until a given integer "number"
# This always prints the given primes in rows of 10 bits
def printPrimes(primes, number, rowLength):
    # limit number to size of primes
    if number >= len(primes):
        number = len(primes)-1
        
    currentRow = 0
    while currentRow*rowLength < number:
        currentColumn = 1
        while currentColumn <= rowLength and currentRow*rowLength+currentColumn <= number:
            index = currentRow * rowLength + currentColumn
            print(primes[index], end="")
            currentColumn += 1
        print()
        currentRow += 1


# Prints primes in rows of 10
def printPrimes10(primes, number):
    printPrimes(primes, number, 10)


# Counts the current number of sieves and returns
def countSieves():
    sieveNumber = 1
    sieveCount = 0
    func_name = f"simpleSieve{sieveNumber}"
    func = globals().get(func_name)
    while func:
        sieveCount += 1
        sieveNumber += 1
        func_name = f"simpleSieve{sieveNumber}"
        func = globals().get(func_name)

    return sieveCount