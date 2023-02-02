physics = int(input("physics: "))
chemistry = int(input("chemistry: "))
maths = int(input("maths: "))
avg = 0

if maths < 35 or physics < 35 or chemistry < 35:
    print("You have failed")
elif maths > 35 and physics > 35 and chemistry >35:
    print("passed")
    avg = (maths + physics + chemistry) / 3

if avg > 35 and avg < 59:
    print("C")
elif avg > 59 and avg < 69:
    print("B")
elif avg > 69 and avg < 100:
    print("A")