a = int(input("a:"))
b = int(input("b:"))
count = 0
sum = 0
if a > b:
    a, b = b, a
for i in range(a+1,b):
    print(i, end=' ')
    sum += i
    count += 1
print(f"Total sum is {sum}")
print(f"Average is {sum/count}")
