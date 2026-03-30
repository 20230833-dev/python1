_a = int(input("do dai canh a:"))
_b = int(input("do dai canh b:"))
_c = int(input("do dai canh c:"))

if (_a + _b > _c) and ( _a+_c > _b) and (_b+_c >_a):
    print("Day la 1 tam giac")
else:
    print("Day deo phai la tam giac")

