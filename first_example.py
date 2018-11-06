if __name__ == '__main__':
    num = input("please input an integer: ")
    num = int(num)
    if num == 0:
        print(num)
    elif num > 0:
        print(num, "is greater than 0")
    else:
        print(num, "is lower than 0")