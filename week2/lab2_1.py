#แก้ไขโค้ดนี้ให้ถูกต้อง

num = int(input("Enter a number: "))

if num < 0:
    text = "negative"
elif num > 0:
    text = "positive"
else:
    text = "zero"

if num % 2 == 0:
    even_odd = "even"
else:
    even_odd = "odd"

print(f"{num} The number is {text} and {even_odd}.")