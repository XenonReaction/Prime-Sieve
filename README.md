# Prime Sieve Experiments (bitarray)

This mini-project is a set of **experiments around optimizing the Sieve of Eratosthenes** using Python’s `bitarray` for compact, fast prime flags.

## Files

### `MakePrimeBitArray.py`
Implements multiple sieve variants (`simpleSieve1` … `simpleSieve9`) that progressively add optimizations:

- Baseline sieve that marks multiples starting at `2n` and checks all `n` values. fileciteturn1file4L6-L28  
- Stop sieving once `n*n >= N` (only primes up to √N are needed). fileciteturn1file4L31-L55  
- Start crossing off at `n*n` to avoid re-marking composites already handled by smaller primes. fileciteturn1file4L57-L78  
- Skip even numbers after handling `2`, and later add additional “skip patterns” to avoid checking values that are known composites from smaller primes. fileciteturn1file4L81-L108 fileciteturn1file7L34-L64 fileciteturn1file3L20-L81  

Utility helpers included:

- `simpleSieve(sieveNumber, size)`: dispatches to `simpleSieve{N}` by number. fileciteturn1file3L84-L92  
- `checkAllSievesMatch(size)`: sanity-check that all sieve variants produce identical prime flags. fileciteturn1file2L25-L38  
- Timing helpers:
  - `timeSieve(...)`, `timeAllSieves(size)` to benchmark each variant. fileciteturn1file2L40-L60  
  - `printAllSieveTimes(size)` for a quick console dump. fileciteturn1file2L62-L67  
- Debug printing:
  - `printPrimes(...)` and `printPrimes10(...)` print the bitarray prime flags in fixed-width rows. fileciteturn1file2L70-L90  

**Output:** Each `simpleSieveX` returns a `bitarray` of length `size` where `primes[i] == True` means `i` is prime.

---

### `MakePrimeSkipsFiles.py`
Explores **“gap patterns”** that appear when you look only at numbers not already eliminated by earlier primes (useful for designing skip-step sequences like wheel factorization).

Key pieces:

- `uncheckedNumbersPatterns(size, numberOfPatterns)`:
  - Runs a classic sieve loop and, for the first `numberOfPatterns` primes encountered, records the spacing (“gaps”) between remaining `True` entries. fileciteturn1file1L18-L46  
- `findUncheckedNumberPattern(primesBitArray, currentPrime)`:
  - Given the current sieve state and a prime, returns a list like `["Pattern for 7", 4, 2, 4, 2, 4, 6, ...]` describing distances to the next still-`True` value. fileciteturn1file1L49-L64  
- `distanceToNewCompositeNumber(size)`:
  - For each prime `n` (up to √N), walks its multiples and records distances between *newly discovered composites* (multiples that were still marked `True` before being crossed off). fileciteturn1file5L46-L78  
- `compressList(list)`:
  - Attempts to detect and compress repeated patterns by finding an initial repeating block. fileciteturn1file5L81-L106  
- `write_list_to_file(lst, filename)`:
  - Writes a Python list (including nested lists) line-by-line to a `.txt` file inside a local `./data/` folder. fileciteturn1file1L67-L77  

**Output:** Pattern lists and `.txt` files intended for later inspection / analysis.

---

### `MakeStatistics.py`
Runs automated **timing experiments** for the sieve variants in `MakePrimeBitArray.py`, then exports the results as text files (via `write_list_to_file` from `MakePrimeSkipsFiles.py`). fileciteturn1file0L1-L2

What it does:

- `testTimes(numTests, size)`: collects `numTests` runs of `timeAllSieves(size)` (one timing list per run). fileciteturn1file0L6-L13  
- `averageResult(tests)`: averages each sieve’s time over repeated runs. fileciteturn1file0L15-L28  
- `generateStatistics(maxTest)`:
  - Normalizes `maxTest` to a power of 10, then measures increasing `testSize` values starting at 1000, with a default of 10 tests per size. fileciteturn1file0L30-L56  
- `convertStatsToFunctions(stats)`:
  - Repackages stats into “functions” like `["Sieve 1", [[size, avgTime], ...]]` so each sieve has its own ordered-pair dataset. fileciteturn1file0L58-L76  
- Script section:
  - Sets `size = 10000000`, generates stats, then writes:
    - `Statistics_up_to_10000000.txt`
    - `Functions_up_to_10000000.txt` fileciteturn1file0L78-L84  

## How to run

### 1) Install dependencies
These scripts require the `bitarray` package:

```bash
pip install bitarray
```

### 2) Run the benchmark script
From the directory containing these files:

```bash
python MakeStatistics.py
```

This will generate `.txt` output files using `write_list_to_file(...)` into a `data/` folder (relative to `MakePrimeSkipsFiles.py`). fileciteturn1file1L67-L77

## Notes / gotchas

- Very large sizes (like `10,000,000`) can take time and memory—`bitarray` is compact, but crossing off multiples is still CPU-heavy. (This is exactly what the benchmarks are exploring.)
- The sieve variants are experimental; `checkAllSievesMatch(size)` is there to guard against a “fast but wrong” optimization. fileciteturn1file2L25-L38

