num = []
for i in range(5):
 number = int(input("Number: "))
 num.append(number)
print("The first number is:", num[0])
print("The last number is:", num[-1])
print("The smallest number is:", min(num))
print("The largest number is:", max(num))
print("The avg of the numbers is:", sum(num) / len(num))