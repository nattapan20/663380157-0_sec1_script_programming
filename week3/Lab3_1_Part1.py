# --- Lab 3.1 Part 1: Single Number Multiplication Table ---
n = int(input("Enter a number for its multiplication table (e.g., 7): "))

# ใช้ range(1, 13) เพื่อให้ลูปทำงานตั้งแต่ i = 1 จนถึง i = 12
for i in range(1, 13):
    # ใช้ f-string เพื่อจัดรูปแบบการแสดงผลตามคำใบ้
    print(f"{n} x {i} = {n * i}")

print() # spacer