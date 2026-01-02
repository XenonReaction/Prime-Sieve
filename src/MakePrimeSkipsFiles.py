# Make a program that can take the gaps between unchecked values in the sieve before each prime
# 2 would result in 1 1 1 1 1 1 1 1 ... since no numbers have been removed
# 3 results in 2 2 2 2 2 2 2 2 ... since every even number was removed
# 5 results in 2 4 2 4 2 4 2 4 ... every sixth number in between evens was removed
# 7 results in 4 2 4 2 4 6 2 6 4 ...
# Try and use these patterns to detemine the pattern of numbers to check for each prime
# looking to optimize the sieve by finding a formula that can be used to determine the patern of
# numbers to check based on previous primes
# The way this can work is when you get to 3 in the sieve, instead of checking every third number
# Just check every sixth number since that skips the even numbers that were already crossed of by 2
# At 5, you can check the number 20 larger then 10 larger alternating since 2 and 3 already eliminated the others
# the patern for 7 is wild, but can be found in the unchecked numbers gap pattern in line 5 above
# Can 11 reveal a useful patern? Is ther a patern for every prime? If yes, does it speed up the algorithm?

from bitarray import bitarray
import os

def uncheckedNumbersPatterns(size, numberOfPatterns):
    N = size
    primes = bitarray(N)
    primes.setall(True)

    patterns = []
    patterns.append(f"Patterns of unchecked numbers in sieve form a starting number up to {size-1}")
    patternsCount = 0

    # Mark 0 and 1 as not prime
    primes[0] = False
    primes[1] = False

    # Sieve of Eratosthenes
    n = 2
    while n < N:
        if primes[n] == True:
            if patternsCount < numberOfPatterns:
                uncheckedNumberPattern = findUncheckedNumberPattern(primes,n)
                patterns.append(uncheckedNumberPattern)
                patternsCount += 1

            m = n+n
            while m < N:
                primes[m] = False
                m += n
        n += 1

    return patterns


def findUncheckedNumberPattern(primesBitArray, currentPrime):
    patternDescription = f"Pattern for {currentPrime}"
    pattern = []
    pattern.append(patternDescription)

    n = currentPrime+1

    distanceToNextPrime = 1
    while n < len(primesBitArray):
        if primesBitArray[n] == True:
            pattern.append(distanceToNextPrime)
            distanceToNextPrime = 0
        distanceToNextPrime += 1
        n += 1

    return pattern


# make a .txt file from a list
def write_list_to_file(lst, filename):
    if not filename.endswith(".txt"):
        filename = filename + ".txt"
    # Go up one directory from src and into the data folder
    filepath = os.path.join(os.path.dirname(__file__), '..', 'data', filename)
    filepath = os.path.abspath(filepath)  # Convert to absolute path

    with open(filepath, 'w') as f:
        for item in lst:
            f.write(f"{item}\n")



# make list of distance to numbers that will be checked off by a new prime
def distanceToNewCompositeNumber(size):
    N = size
    primes = bitarray(N)
    primes.setall(True)
    primes[0] = False
    primes[1] = False

    compositeDistancesList = []

    compositeDistancesList.append(f"This is a list of patterns for the distances to the next composite number in"
                                  f" multiples of the current prime up to {size}")

    n = 2

    while n*n < N:
        if primes[n] == True:
            compositeDistances = []
            compositeDistances.append(f"Pattern for {n}")
            m = n+n
            lastPrime = n
            while m < N:
                if primes[m] == True:
                    distance = (m-lastPrime)//n
                    compositeDistances.append(distance)
                    lastPrime = m
                    primes[m] = False
                m += n
            compositeDistances = compressList(compositeDistances)
            compositeDistancesList.append(compositeDistances)
        n += 1

    return compositeDistancesList


# compress list of distances
def compressList(list):
    compressedList = []
    compressedList.append(list[0])

    found = False
    end = 1
    while not found and end<(len(list)-1)//2:
        for n in range(1,end+1):
            if list[n] != list[end+n]:
                end += 1
                break
            elif n == end:
                found = True

    if found:
        compressedList.append("Found")
        for n in range(1,end+1):
            compressedList.append(list[n])
        compressedList.insert(2, f"Length: {len(compressedList)-2}")
    else:
        list.insert(1,"Not Found")
        list.insert(2,"Length: NA")
        return list

    return compressedList

