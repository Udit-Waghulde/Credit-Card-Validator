def check_validity(num):
    validlist = []
    for i in num:
        validlist.append(int(i))
    for i in range(0,len(num), 2):
        validlist[i] = validlist[i]*2
        if validlist[i] >= 10:
            validlist[i] = (validlist[i]//10 + validlist[i]%10)

    if sum(validlist)%10 == 0:
        print("This card is VALID")
    else:
        print("This card is INVALID")

def cardnumber():
    n = ''
    while True:
        try:
            n = input("Enter your credit card number : ")
            if not (len(n) == 16) or not type(int(n)== int):
                raise Exception
        except Exception:
            print("Please enter a valid number! \nMake sure you are entering all 16 digits , not characters!")
            continue
        else:
            break
    return n

def goagain():
    return input("Do you want to check again? (yes/no) : ").lower()[0] == 'y'

def main():
    while True:
        num = cardnumber()
        check_validity(num)

        if not goagain():
            break

if __name__ == '__main__':
    main()
