# 1. Print all integers from 0 to 150
for numAllInt in range(0,151):
    print(numAllInt)

# 2. Print all the multiples of 5 from 5 to 1,000
for numMultFive in range(5,1001,5):
    print(numMultFive)

# 3. Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo"
for numIntDivide in range(1,101):
    if numIntDivide % 10 == 0:
        print("Coding Dojo")
    elif numIntDivide % 5 == 0:
        print("Coding")
    else:
        print(numIntDivide)

# 4. Add odd integers from 0 to 500,000 and print the final sum
finalSum = 0
for oddInt in range(0,500001):
    if oddInt % 2 != 0:
        finalSum = finalSum + oddInt
print(finalSum)

# 5. Print positive numbers starting at 2018, counting down by fours
for posInt in range(2018,0,-4):
    print(posInt)

# 6. Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult
lowNum = 1
highNum = 50
mult = 3
for int in range(lowNum,highNum):
    if int % mult == 0:
        print(int)