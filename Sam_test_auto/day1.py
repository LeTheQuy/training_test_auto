# Bài tập sẽ là: Viết chương trình nhập vào một số từ bàn phím và in ra số đó là số âm hay số dương.
# how to input from keyboard in python

number = int(input("Input a number: "))
if number == 0:
    print("So 0")
elif number > 0:
    print("So duong")
else:
    print("So am")