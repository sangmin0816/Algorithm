import sys
input = sys.stdin.readline

for a in range(2, 101):
    cube = a**3
    for b in range(2, a):
        for c in range(b, a):
            for d in range(c, a):
                triple = b**3 + c**3 + d**3
                if(cube == triple):
                    print('Cube = %d, Triple = (%d,%d,%d)' %(a, b, c, d))