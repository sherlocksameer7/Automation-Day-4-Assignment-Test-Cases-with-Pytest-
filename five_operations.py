def Armstrong_Num_or_Not(Num):

    Sum = 0
    Temp = Num
    while Temp > 0:
        Digit = Temp % 10
        Sum += Digit ** 3
        Temp //= 10
        if Num == Sum:

            return True

        else:

            return False



def Divisible_by_8_Not(Num):

    if Num % 8 == 0:
        return True
    else:
        return False



def Smallest_among_3(x, y, z):

    if x < y and x < z:
        return x

    elif y < x and y < z:
        return y

    else:
        return z



def Even_or_Odd(Num):

    if Num % 2 == 0:
        return True

    else:
        return False



def String_is_Palindrome_or_Not(string):

    if string == string[::-1]:
        return True

    else:
        return False



if __name__ == "__main__":

    Num = int(input("Enter any Number ot Check Armstrong & Divisible & Even_or_Odd"))

    x = int(input("Enter 1st Number: "))
    y = int(input("Enter 2nd Number: "))
    z = int(input("Enter 3rd Number: "))

    string = int(input("Enter any Word: "))

    Arm_or_Not = Armstrong_Num_or_Not(Num)
    print(Arm_or_Not)

    Div_By_8 = Divisible_by_8_Not(Num)
    print(Div_By_8)

    Small_Num = Smallest_among_3(x, y, z)
    print(Small_Num)

    Even_Odd = Even_or_Odd(Num)
    print(Even_Odd)

    String_Palindrome = String_is_Palindrome_or_Not(string)
    print(String_Palindrome)