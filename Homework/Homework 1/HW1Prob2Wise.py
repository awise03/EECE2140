x = number2 = number = int(input("Input the a number: "))
count = reverse = 0
while x > 0:
    count += 1
    x = x // 10
    print(x)
for i in range(count):
    y = number2 % 10 #* 10**((count-1) - i)
    print(y)
    reverse += y * 10**((count-1) - i)

    number2 = number2 // 10
if reverse == number: print("This is a palindrone!")
else: print("This is not a palindrone!")