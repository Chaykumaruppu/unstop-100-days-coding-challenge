"""
Problem: Exchanging Gifts
Platform: Unstop
Day: 001

Description:
Identify the youngest family member who receives gifts from all others
but does not give any gifts.

Approach:
- Track gifts given and received using two arrays
- Youngest member has:
  - Given = 0
  - Received = n - 1
"""

def find_youngest_member(n, m, gifts):
    given = [0] * (n + 1)
    received = [0] * (n + 1)

    for a, b in gifts:
        given[a] += 1
        received[b] += 1

    for i in range(1, n + 1):
        if given[i] == 0 and received[i] == n - 1:
            return i

    return -1


def main():
    import sys
    data = sys.stdin.read().strip().split()

    n = int(data[0])
    m = int(data[1])

    gifts = []
    idx = 2
    for _ in range(m):
        gifts.append((int(data[idx]), int(data[idx + 1])))
        idx += 2

    print(find_youngest_member(n, m, gifts))


if __name__ == "__main__":
    main()
