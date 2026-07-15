# lab4_1.py - Student Management System (List Operations)
# ฉบับปรับปรุงสมบูรณ์ + รวมฟีเจอร์ Challenge (ระบบเมนูด้วย while loop) เพื่อคะแนนพิเศษ! [cite: 58, 72]

print("--- Lab 4.1: Student Management System ---") 

# 1) เริ่มต้นด้วย list ว่างสำหรับเก็บชื่อนักศึกษา
student_names = [] 

# ใช้ระบบเมนูในการควบคุมโปรแกรม (ส่วน Challenge สำหรับคะแนนพิเศษ) 
while True:
    print("\n==============================")
    print("      STUDENT SYSTEM MENU     ")
    print("==============================")
    print("1. Add Students (เพิ่มรายชื่อ)")
    print("2. Find a Student (ค้นหารายชื่อ)")
    print("3. Remove a Student (ลบรายชื่อ)")
    print("4. Sort Students (เรียงลำดับรายชื่อ)")
    print("5. Count Students (นับจำนวนนักเรียน)")
    print("6. Exit (ออกจากโปรแกรม)")
    print("==============================")
    
    choice = input("Enter your choice (1-6): ") 
    
    # 2) เพิ่มนักศึกษา [cite: 63]
    if choice == '1':
        print("\n[1] Add Students") 
        try:
            num = int(input("How many students do you want to add? (3-5): "))
        except ValueError:
            print("Please enter a valid number.")
            continue
            
        # เติมคำสั่งลูปด้วยการใช้ตัวแปร i และรัน range(num) ตามจำนวนที่ผู้ใช้ต้องการ
        for i in range(num): 
            name = input(f"Enter student name #{i + 1}: ") 
            student_names.append(name) 
            
        print(f"Current list: {student_names}") 
        
    # 3) ค้นหานักศึกษา [cite: 65]
    elif choice == '2':
        print("\n[2] Find a Student") 
        search_name = input("Enter a name to search for: ") 

        # เติมเงื่อนไขเช็คว่ามีชื่อในลิสหรือไม่
        if search_name in student_names: 
            position = student_names.index(search_name) 
            print(f"Found '{search_name}' at index {position}") 
        else:
            print(f"'{search_name}' not found in the list")

    # 4) ลบนักศึกษา [cite: 67]
    elif choice == '3':
        print("\n[3] Remove a Student") 
        remove_name = input("Enter a name to remove: ") 

        # เช็คก่อนว่ามีชื่อในลิสหรือไม่ เพื่อป้องกัน Error
        if remove_name in student_names: 
            student_names.remove(remove_name) # เติมฟังก์ชัน remove(remove_name) 
            print(f"'{remove_name}' has been removed") 
        else:
            print(f"'{remove_name}' not found, nothing removed") 

        print(f"Updated list: {student_names}") 

    # 5) เรียงลำดับรายชื่อตามตัวอักษรด้วย sort() [cite: 70]
    elif choice == '4':
        print("\n[4] Sort Students") 
        student_names.sort() # เติมฟังก์ชัน sort() ในการเรียงลำดับในที่ (in-place) 
        print(f"Sorted list: {student_names}") 

    # 6) นับจำนวนนักศึกษาทั้งหมดด้วย len() [cite: 71]
    elif choice == '5':
        print("\n[5] Count Students") 
        # ใช้คำสั่ง len(student_names) เพื่อหาขนาดหรือจำนวนข้อมูลภายใน List 
        print(f"Total students: {len(student_names)}") 

    # ออกจากโปรแกรม
    elif choice == '6':
        print("\nThank you for using Student Management System. Goodbye!")
        break
        
    else:
        print("Invalid choice! Please select 1-6.")