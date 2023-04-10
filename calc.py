# get two integer parameters
# return sum
def plus(x, y):
    return x+y
def minus(x,y):
    return x-y
def multi(x,y):
    return x*y
def divi(x,y):
    return x/y
# main function
def main():
    check = 1
    print("Welcome to calcuator")
    while check >= 1:        
        print("0: exit, 1: plus, 2: minus, 3: multiplication, 4:division")
        check = int(input())
        if check == 1:
            print("First Number")
            x = int(input())
            print("Second Number")
            y = int(input())
            print("answer : ", plus(x,y))
          
        elif check == 2:
            print("First Number")
            x = int(input())
            print("Second Number")
            y = int(input())
            print("answer : ", minus(x,y))
        
        elif check == 3:
            print("First Number")
            x = int(input())
            print("Second Number")
            y = int(input())
            print("answer : ", multi(x,y))

        elif check == 4:
            print("First Number")
            x = int(input())
            print("Second Number")
            y = int(input())
            print("answer : ", divi(x,y))
        
        elif check > 4 :
            print("Unsupported")
        else:
            print("Thank you")

if __name__ == "__main__":
    main()
