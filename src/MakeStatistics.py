from MakePrimeBitArray import timeAllSieves
from MakePrimeSkipsFiles import write_list_to_file

def testTimes(numTests, size):
    results = []
    results.append(size)

    for n in range(0,numTests):
        results.append(timeAllSieves(size))

    return results

def averageResult(tests):
    results = []
    averages = []
    results.append(tests[0])

    for n in range(0,len(tests[1])):
        average = 0
        for m in range(1, len(tests)):
            average += tests[m][n]
        average /= (len(tests)-1)
        averages.append(average)

    results.append(averages)
    return results

def generateStatistics(maxTest):
    # set maxTest to be a power of 10
    n = 1000
    while n<=maxTest:
        n *= 10
    maxTest = n//10

    testSize = 1000
    testsPerSize = 10

    stats = []
    testInfo = [["Smallest Test Size", "Largest Test Size", "Number of Tests per Sieve per Size"],
                [testSize, maxTest, testsPerSize]]
    stats.append(testInfo)

    while testSize <= maxTest:
        currentJump = testSize
        rangeLimit = testsPerSize-1
        if testSize == maxTest:
            rangeLimit = 1
        for n in range(0,rangeLimit):
            times = testTimes(testsPerSize,testSize)
            averages = averageResult(times)
            stats.append(averages)
            testSize += currentJump

    return stats

def convertStatsToFunctions(stats):
    functions = []

    numFunctions = len(stats[1][1])

    for n in range(0, numFunctions):
        functionName = f"Sieve {n+1}"
        function = []
        function.append(functionName)
        orderedPairs = []
        for m in range(1,len(stats)):
            orderedPair = []
            orderedPair.append(stats[m][0])
            orderedPair.append(stats[m][1][n])
            orderedPairs.append(orderedPair)
        function.append(orderedPairs)
        functions.append(function)

    return functions

size = 10000000

stats = generateStatistics(size)
write_list_to_file(stats, f"Statistics_up_to_{size}")

functions = convertStatsToFunctions(stats)
write_list_to_file(functions, f"Functions_up_to_{size}")