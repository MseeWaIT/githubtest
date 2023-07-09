# Python code to add 3 numbers, , if two values are equal sum will be zero

x = int(input("Enter first no: "));
y = int(input("Enter second no: "));
z = int(input("Enter third no: "));

if x == y or y == z or x==z:
    sum = 0
else:
    sum = x + y + z

print(sum);
