def main():
    numbers = input("Give me 2 seperate numbers (x,y): ")
    symbol = input("Would you like to +,-,/,* ")

    x,y = map(int, numbers.split(","))


    total2 = calc(symbol, x,y)

    print(total2)

    


def calc(symbol, x,y):

    if symbol == "+":
        total = x + y
    elif symbol == "-":
        total = x - y
    elif symbol == "/":
        total = x / y
    elif symbol == "*":
        total = x * y
    return(total)




if __name__ == "__main__":
    main()



