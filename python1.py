a = int(input(" Enter the first number : "))
b =int(input(" Enter the second number :"))
c =int(input(" Enter the third number :"))

if a < b + c  and b < a + c  and c < b + a :
    print(" it is possible to from a tringle with these side.")
else: 
    print(" it is not possile to from a tringle with these side.")
