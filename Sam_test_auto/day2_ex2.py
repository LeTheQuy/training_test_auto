# ex2: Count the number of even and odd numbers from a series of numbers
series_numbers = [5, 3, 7, 4, 2, 45, 68, 43, 22, 21, 1]
print(series_numbers)
number_of_even_numbers = 0
number_of_odd_numbers = 0

for number in series_numbers:
    if number % 2 == 0:
        number_of_even_numbers = number_of_even_numbers + 1
    elif number % 2 == 1:
        number_of_odd_numbers = number_of_odd_numbers + 1
    else:
        print(str(number) + "is not an integer")

print("number of odd numbers: " + str(number_of_odd_numbers))
print("number of even numbers: " + str(number_of_even_numbers))
