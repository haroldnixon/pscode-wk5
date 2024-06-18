
numA = input("Enter First Number: ")
numB = input("Enter Second Number: ")
numC = input("Enter Third Number: ")
numD = input("Enter Fourth Number: ")
numE = input("Enter Fifth Number: ")
#print(numA, numB, numC, numD, numE)
numTotal = (int(numA) + int(numB) + int(numC) + int(numD) + int(numE))
#print("The total is: ", numTotal)
numAverage = (numTotal / 5)
#print(numAverage)
# Had to make sure vars were ints to do math!!!
numArray = [int(numA),int(numB),int(numC),int(numD),int(numE)]
#print(numArray)

numMax = 0
for i in numArray:
  if i > numMax:
    numMax = i
#print("The largest number is: ", numMax)

numMin = numMax
for i in numArray:
  if i < numMin:
    numMin = i
#print("The lowest number is: ", numMin)

print(numAverage, 'is the average of the 5 numbers entered a moment ago.')
print(numMax, 'is the largest of the numbers while', numMin, 'is the lowest.') 