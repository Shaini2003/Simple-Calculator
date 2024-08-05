def add(a,b):
    return a+b
def substract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    try:
        return a/b
    except Exception as e:
        print(e)
def power(a,b):
    return a**b
def remainder(a,b):
    return a%b

def select_op(choice):
    if(choice == '#'):
        return -1
    elif(choice=='$'):
        return 0
    elif(choice in('+','-','*','/','^','%')):
        while(True):
            num1=str(input("Enter first number: "))
            print(num1)
            if num1.endswith('$'):
                return 0
            if num1.endswith('#'):
                return -1
            
            try:
                num1=float(num1)
                break
            except:
                print("Not a valid number,please enter again")
                continue
        while(True):
            num2=str(input("Enter second number: "))
            print(num2)
            if num2.endswith('$'):
                return 0
            if num2.endswith('#'):
                return -1
            try:
                num2=float(num2)
                break
            except:
                print("Not a valid number,please enter again")
                continue
            
        if choice=='+':
            print(num1, "+", num2, "=",add(num1,num2))
        elif choice=='-':
            print(num1, "+", num2, "=",substract(num1,num2))
        elif choice=='*':
            print(num1, "*", num2, "=",multiply(num1,num2))
        elif choice=='/':
            print(num1, "/",num2, "=",divide(num1,num2))
        elif choice=='^':
            print(num1, "^",num2, "=",power(num1,num2))
        elif choice=='%':
            print(num1, "%",num2, "=",remainder(num1,num2))
        else:
            print("Something Went Wrong")
    else:
        print("Unrecognized operation")



while True:
  print("Select operation.")
  print("1.Add      : + ")
  print("2.Subtract : - ")
  print("3.Multiply : * ")
  print("4.Divide   : / ")
  print("5.Power    : ^ ")
  print("6.Remainder: % ")
  print("7.Terminate: # ")
  print("8.Reset    : $ ")
  

  # take input from the user
  choice = input("Enter choice(+,-,*,/,^,%,#,$): ")
  print(choice)
  if(select_op(choice) == -1):
    #program ends here
    print("Done. Terminating")
    exit()