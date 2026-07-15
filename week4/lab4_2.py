# lab4_2.py - Geometric Calculations (Tuples & Immutability)
# ฉบับปรับปรุงสมบูรณ์ + รวมฟีเจอร์ Challenge (รับค่าพิกัดจากผู้ใช้) เพื่อคะแนนพิเศษ!

import math

print("--- Lab 4.2: Geometric Calculations ---")

# 1) กำหนดจุดสองจุดด้วย tuple: point1 และ point2
# เติมพิกัด (3, 4) และ (6, 8) ตามโจทย์กำหนด
point1 = (3, 4) 
point2 = (6, 8) 

# 2) เข้าถึงค่าพิกัด x, y ของแต่ละจุด
print("\n[1] Access Coordinates")
# ใช้ Index 0 สำหรับแกน x และ Index 1 สำหรับแกน y 
print(f"Point 1: x = {point1[0]}, y = {point1[1]}") 
print(f"Point 2: x = {point2[0]}, y = {point2[1]}") 

# 3) ทดลองแก้ไขค่าใน tuple เพื่อแสดงให้เห็นว่า tuple เปลี่ยนแปลงไม่ได้ (immutable)
print("\n[2] Attempt Modification (Immutability Demonstration)")
try:
    point1[0] = 5  # บรรทัดนี้จะทำให้เกิด TypeError เพราะ tuple แก้ไขไม่ได้ [cite: 80]
except TypeError as e:
    print(f"Error trying to modify tuple: {e}") 

# 4) คำนวณระยะห่างระหว่างจุดสองจุดด้วยสูตรระยะทาง [cite: 84]
#    distance = sqrt( (x2 - x1)^2 + (y2 - y1)^2 )
print("\n[3] Calculate Distance")
# ดึงค่า x ของจุดที่สอง point2[0] ลบด้วย x ของจุดแรก point1[0] และทำแบบเดียวกันกับแกน y (Index 1) 
distance = math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2) 
print(f"Distance between point1 {point1} and point2 {point2}: {distance:.2f}")

# ====================================================================
# 🌟 ส่วน Challenge (สำหรับคะแนนพิเศษเพิ่มเติม): 
# เขียนโค้ดรับพิกัดของจุดใหม่ 2 จุดจากผู้ใช้ และนำมาคำนวณหาระยะทางอย่างถูกต้อง [cite: 87]
# ====================================================================
print("\n==============================")
print("     CHALLENGE COMPLETED      ")
print("==============================")
print("Let's calculate the distance between your custom points!")

try:
    # รับค่าพิกัดจุดที่ 1 จากผู้ใช้และแปลงค่าเป็น float (เพื่อรองรับทศนิยม) 
    user_x1 = float(input("Enter Point 1 (x1): "))
    user_y1 = float(input("Enter Point 1 (y1): "))
    user_point1 = (user_x1, user_y1) # รวมเป็น Tuple ของจุดที่ 1 

    # รับค่าพิกัดจุดที่ 2 จากผู้ใช้และแปลงค่าเป็น float 
    user_x2 = float(input("Enter Point 2 (x2): "))
    user_y2 = float(input("Enter Point 2 (y2): "))
    user_point2 = (user_x2, user_y2) # รวมเป็น Tuple ของจุดที่ 2 

    # คำนวณระยะห่างระหว่างจุดทั้งสองที่ผู้ใช้กรอกเข้ามา [cite: 84, 85, 87]
    user_distance = math.sqrt((user_point2[0] - user_point1[0]) ** 2 + (user_point2[1] - user_point1[1]) ** 2) 
    
    print(f"\nUser Point 1: {user_point1}")
    print(f"User Point 2: {user_point2}")
    print(f"Calculated distance between your points: {user_distance:.4f}")

except ValueError:
    print("\nError: Please enter valid numbers for the coordinates!") 