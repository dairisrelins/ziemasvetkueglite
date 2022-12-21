width = int(input("Enter Christmas Tree Width   = "))
height = int(input("Enter Christmas Tree Height = "))
alphabeth = 64
space = width * height
n = 1

print("====The Christmas Tree Star Pattern====")

x = 1

while(x <= height):
    i = n
    while(i <= width):
        j = space
        while(j >= i):
            print(end = ' ')
            j = j - 1
        k = 1
        while(k <= i):
            print('', end = ' ')
            k = k + 1
        print()
        i = i + 1
    n = n + 2
    width = width + 2
    x = x + 1

i = 1
while(i < height):
    j = space - 3
    while(j >= 0):
        print(end = ' ')
        j = j - 1
    k = 1
    while(k < height):
        print('', end = ' ')
        k = k + 1
    print()
    i = i + 1