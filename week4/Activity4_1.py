# activity4_1.py - Scenario Matching (List vs Tuple Demonstration)
import math

print("=== Activity 4.1: List vs. Tuple: Scenario Matching ===")

# -------------------------------------------------------------------------
# สถานการณ์ที่ 1: ข้อมูลอุณหภูมิประจำวันที่มีการบันทึกไว้ตลอดหนึ่งสัปดาห์
# เลือกใช้: List (เพื่อให้สามารถอัปเดตหรือแก้ไขข้อมูลย้อนหลังได้สะดวก)
# -------------------------------------------------------------------------
print("\n[Scenario 1] Weekly Temperatures (List)")
# เริ่มต้นบันทึกอุณหภูมิ 7 วัน
daily_temps = [32.5, 33.0, 31.8, 30.5, 34.2, 35.0, 33.8] 
print(f"Original Temperatures: {daily_temps}")

# สมมติว่าต้องการแก้ไขอุณหภูมิของวันที่ 4 (Index 3) เนื่องจากเครื่องมือวัดคลาดเคลื่อน
daily_temps[3] = 31.2 
print(f"Updated Temperatures:  {daily_temps} (Index 3 updated successfully)")


# -------------------------------------------------------------------------
# สถานการณ์ที่ 2: ค่าสี RGB ของเฉดสีเฉพาะเฉดหนึ่ง 
# เลือกใช้: Tuple (เนื่องจากสีเฉพาะเฉดหนึ่งต้องมีโครงสร้าง 3 ค่าที่คงที่ ห้ามแก้ไข)
# -------------------------------------------------------------------------
print("\n[Scenario 2] RGB Color Value (Tuple)")
# กำหนดค่าสีแดง (Red, Green, Blue) [cite: 96]
red_color = (255, 0, 0) 
print(f"RGB Red Color Tuple: {red_color}")

# ทดลองจำลองว่ามีส่วนของโค้ดพยายามจะเปลี่ยนค่าสีแดงให้เป็นสีอื่น
try:
    red_color[1] = 50 # จะเกิด Error เพราะ Tuple แก้ไขไม่ได้ (Immutable) [cite: 41, 49]
except TypeError as e:
    print(f"Demonstration: Cannot modify RGB Tuple: {e} (Data is protected!)")


# -------------------------------------------------------------------------
# สถานการณ์ที่ 3: รายการสินค้าในรถเข็นชอปปิงที่สามารถกดเพิ่มหรือลบออกได้
# เลือกใช้: List (เนื่องจากต้องเพิ่มหรือลบข้อมูลได้ตลอดเวลาตามการชอปปิง)
# -------------------------------------------------------------------------
print("\n[Scenario 3] Shopping Cart (List)")
# เริ่มต้นด้วยการหยิบสินค้าเข้าตะกร้า [cite: 97]
shopping_cart = ["Notebook", "Pen"] 
print(f"Initial Cart: {shopping_cart}")

# เพิ่มสินค้าเข้าตะกร้าด้วย .append() 
shopping_cart.append("Eraser")
print(f"After Adding 'Eraser': {shopping_cart}")

# ลบสินค้าออกด้วย .remove() 
shopping_cart.remove("Pen")
print(f"After Removing 'Pen':  {shopping_cart}")


# -------------------------------------------------------------------------
# สถานการณ์ที่ 4: รายชื่อวันในหนึ่งสัปดาห์เรียงตามลำดับ (จันทร์ - อาทิตย์)
# เลือกใช้: Tuple (เนื่องจากจำนวนวันและชื่อของวันมีค่าคงที่ตายตัวเสมอ)
# -------------------------------------------------------------------------
print("\n[Scenario 4] Days of the Week (Tuple)")
# กำหนดวันในสัปดาห์ [cite: 98]
days_of_week = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday") 
print(f"Days of the week: {days_of_week}")

# แสดงการเข้าถึงข้อมูลด้วย Index [cite: 48]
print(f"First day of work: {days_of_week[0]}")
print(f"Weekend starts on: {days_of_week[5]}")

# ป้องกันความผิดพลาดจากการเขียนโค้ดลบวันทิ้ง
try:
    del days_of_week[0] # จะเกิด Error เพราะห้ามลบสมาชิกใน Tuple [cite: 135]
except TypeError as e:
    print(f"Demonstration: Cannot delete from days Tuple: {e} (Structure remains safe!)")


# -------------------------------------------------------------------------
# สถานการณ์ที่ 5: คะแนนเก็บของนักเรียนซึ่งอาจมีการอัปเดตหรือแก้ไขภายหลังได้
# เลือกใช้: List (เพื่อให้สามารถเข้าถึงและแก้ไขคะแนนของนักเรียนแต่ละคนได้)
# -------------------------------------------------------------------------
print("\n[Scenario 5] Student Assignment Scores (List)")
# รายการคะแนนเก็บของนักเรียน [cite: 99]
student_scores = [85, 90, 78, 92] 
print(f"Original Scores: {student_scores}")

# คุณครูทำการตรวจประเมินคะแนนของนักเรียนคนแรก (Index 0) ใหม่และเพิ่มคะแนนให้
student_scores[0] = 88 
print(f"Updated Scores:  {student_scores} (Index 0 score increased!)")


# -------------------------------------------------------------------------
# สถานการณ์ที่ 6: พิกัด GPS ของสถานที่สำคัญหรือจุดแลนด์มาร์กที่ตั้งอยู่กับที่
# เลือกใช้: Tuple (เนื่องจากเป็นพิกัดทางภูมิศาสตร์ที่คงที่ ไม่เคลื่อนย้ายหรือเปลี่ยนแปลง)
# -------------------------------------------------------------------------
print("\n[Scenario 6] GPS Coordinates of a Landmark (Tuple)")
# พิกัด GPS ของสถานที่สำคัญ (Latitude, Longitude) [cite: 100]
landmark_gps = (16.4322, 102.8231) 
print(f"GPS Coordinates: {landmark_gps}")

# การกระจายค่าออกจาก Tuple (Tuple Unpacking) เพื่อนำไปใช้งาน 
lat, lon = landmark_gps 
print(f"Unpacked Coordinates -> Latitude: {lat}, Longitude: {lon}")

# ป้องกันการเปลี่ยนแปลงพิกัดโดยไม่ตั้งใจ
try:
    landmark_gps[0] = 13.7563 # จะเกิด Error 
except TypeError as e:
    print(f"Demonstration: Cannot change GPS Tuple: {e} (Coordinates are locked!)")