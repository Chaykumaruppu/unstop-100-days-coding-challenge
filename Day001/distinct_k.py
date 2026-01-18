"""
Problem: Distinct K
Platform: Unstop
Day: 001

Description:
Find the k-th distinct string (appearing exactly once) while preserving
the order of appearance.

Approach:
- Count frequency of each string
- Traverse again to locate the k-th string with frequency = 1
"""

def main():
    import sys
    data = sys.stdin.read().strip().split()

    n = int(data[0])
    strings = data[1:1 + n]
    k = int(data[1 + n])

    freq = {}
    for s in strings:
        freq[s] = freq.get(s, 0) + 1

    distinct_count = 0
    for s in strings:
        if freq[s] == 1:
            distinct_count += 1
            if distinct_count == k:
                print(s)
                return

    print(-1)


if __name__ == "__main__":
    main()
