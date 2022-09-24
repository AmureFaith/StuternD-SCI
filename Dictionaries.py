#squaresOfNumber = {5: 25, 6: 36, 7: 49, 8: 64,9: 81, 10: 100, 11: 121, 12: 144, 13: 169,
 #14: 196, 15:225}
#print ('These are the squares of numbers:', squaresOfNumber)


names = ['jenny', 'alex', 'samuel', 'late']
heights = [61,23,45,70]

students = {names:heights for names, heights in zip(names,heights)}
print (students) 