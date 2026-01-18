"""
Problem: Chessboard Cell Color
Platform: Unstop
Day: 001

Description:
Given a chessboard coordinate (e.g., a1, b2), determine whether the cell
is Black or White.

Approach:
- Convert column letter to number (a=1, b=2, ...)
- Add column number and row number
- Even sum → Black, Odd sum → White
"""

def determine_color(position: str) -> str:
    col = ord(position[0]) - ord('a') + 1
    row = int(position[1])
    return "Black" if (col + row) % 2 == 0 else "White"


def main():
    import sys
    position = sys.stdin.read().strip()
    print(determine_color(position))


if __name__ == "__main__":
    main()
