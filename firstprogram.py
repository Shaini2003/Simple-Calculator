firstNumber=float(input("Enter your first number : "))
Function=(input("Enter the sum(+,/,*,-) : "))
secondNumber=float(input("Enter your second number : "))

if Function=='+':
    output=firstNumber+secondNumber
elif Function=='/':
    output=firstNumber/secondNumber
elif Function=='*':
    output=firstNumber*secondNumber
elif Function=='-':
    output=firstNumber-secondNumber

print(firstNumber+Function+secondNumber+"="+output)
