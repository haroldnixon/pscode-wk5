# Even or Odd Number detection
# Took out the == 0 and switched the Odd/Even
# Changed code a bit after learning any number above 0 was true

numAsk = input("Enter a number: ")
if int(numAsk) % 2:
  print('Odd')
else:
  print('Even')