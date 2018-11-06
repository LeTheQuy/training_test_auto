# Bài tập sẽ là: Viết chương trình nhập vào một số từ bàn phím và in ra số đó là số âm hay số dương.
# how to input from keyboard in python

user_input = input("Input a number: ")

try:
    val = int(user_input)
    if val == 0:
        print(str(val) + " is equal to 0")
    elif val > 0:
        print(str(val) + " is greater than 0")
    else:
        print(str(val) + " is smaller than 0")
except ValueError:
    print("That's not an int!")
