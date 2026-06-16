# age = int(input("Enter your age: "))
# if age >= 18:
#     print("You Can Vote!")
# else:
#     print("You Cannot Vote!")


# num1 = input("Enter the first number: ")
# num2 = input("Enter the second number: ")
# sum = float(num1) + float(num2)
# print("The sum of", num1, "and", num2, "is", sum)

# function
# def sum(num1,num2):
#     print("The sum of", num1, "and", num2, "is", num1 + num2);
# sum(10,40)

# List
# item = ["ankit", 10, 20,"Kumar"]
# print(item)
# for i in range(len(item)):
#     print(item[i])

# Find negative and positive numbers in a list

numbers = [10, -5, 20, -3, 15, -8]
positive_numbers = []
negative_numbers = []

for num in numbers:
    if num >= 0:
        positive_numbers.append(num)
    else:
        negative_numbers.append(num)
print("Positive numbers:", positive_numbers)
print("Negative numbers:", negative_numbers)