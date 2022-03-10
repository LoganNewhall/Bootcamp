# Basics
for i in range(150):
    print(i)
# Multiples of 5
for i in range(5,1000,5):
    print(i)
# Counting, the Dojo Way
for i in range(1,100):
    if i % 10 == 0:
        print("Coding Dojo")
    elif i % 5 == 0:
        print("Coding")
    else:
        print(i)
# Whoa. That Sucker's Huge
sum = 0
for i in range(500000):
    sum = sum + i
print(sum)
# Countdown by Fours
for i in range(2018,0,-4):
    print(i)
# Flexible Counter
lowNum = 4
highNum = 22
mult = 2
for i in range(lowNum,highNum):
    if i % mult == 0:
        print(i)