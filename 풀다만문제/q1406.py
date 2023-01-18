import sys
input = sys.stdin.readline

def editor(string, cursor, key, stroke):
    if not cursor:
        if key == "L":
            cursor -= 1
        if key == "B":
            cursor -= 1
            string.pop(cursor)
    if cursor != len(string) and key == "D":
        cursor += 1
    if cursor == "P":
        string.insert(cursor, stroke)

string = list(input().rstrip())
cursor = len(string)

N = int(input())
for n in range(N):
    key = list(map(str, input().rstrip().split(" ")))
    stroke = None
    if key[0] == "P":
        stroke = key[1]
    editor(string, cursor, key[0], stroke)

print(str(string))