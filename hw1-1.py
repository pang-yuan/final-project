XL = int(input())
XI = int(input())
y = float(input())

if XL+XI >= 10 and XI > 1 and y >= 3.5:
    print(min(15000+4000*XI, 150000))
else:
    print(0)
