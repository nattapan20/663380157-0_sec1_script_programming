# activity4_2.py - Interactive To-Do List Manager
# โปรแกรมจัดการรายการสิ่งที่ต้องทำ (To-Do List) โดยใช้โครงสร้างข้อมูลแบบ List

print("--- Activity 4.2: Interactive To-Do List ---")

# 1) สร้าง List ว่างเริ่มต้นไว้ตัวหนึ่งชื่อว่า todo_list
todo_list = []

# 2) ใช้การวนลูป while เพื่อแสดงเมนูคำสั่งให้ผู้ใช้เลือกตลอดการทำงาน
while True:
    print("\n==============================")
    print("      My To-Do List Manager   ")
    print("==============================")
    print("1. Add a task (เพิ่มงาน)")
    print("2. View tasks (ดูงานทั้งหมด)")
    print("3. Mark task as complete (ทำเสร็จสิ้น/ลบงาน)")
    print("4. Exit (ออกจากโปรแกรม)")
    print("==============================")
    
    # 3) ใช้คำสั่ง input() เพื่อรับค่าเมนูที่ผู้ใช้เลือก
    choice = input("Enter your choice (1-4): ")
    
    # 2.1) เพิ่มรายการงาน (Add a task)
    if choice == '1':
        print("\n[1] Add a Task")
        new_task = input("Enter the task you want to do: ").strip()
        
        if new_task != "":
            # 4) ใช้คำสั่ง append() เพื่อเพิ่มข้อมูลลงไปในท้าย List
            todo_list.append(new_task)
            print(f"Added: '{new_task}' successfully!")
        else:
            print("Task cannot be empty!")
            
    # 2.2) ดูรายการงานทั้งหมด (View tasks)
    elif choice == '2':
        print("\n[2] View Tasks")
        # 4) ใช้ len() ตรวจสอบก่อนว่ามีงานในลิสหรือไม่
        if len(todo_list) == 0:
            print("Your To-Do List is currently empty. Enjoy your day! 😊")
        else:
            print("--- Your Current Tasks ---")
            # วนลูปเพื่อดึงงานพร้อมตำแหน่ง index ออกมาแสดงผลอย่างสวยงาม
            for i in range(len(todo_list)):
                print(f"{i + 1}. {todo_list[i]}")
                
    # 2.3) ทำเครื่องหมายว่างานเสร็จสิ้นแล้ว (ลบงานออก)
    elif choice == '3':
        print("\n[3] Mark Task as Complete")
        if len(todo_list) == 0:
            print("No tasks to complete!")
            continue
            
        # ออกแบบให้ผู้ใช้เลือกได้ 2 วิธีเพื่อเอาคะแนนพิเศษเพิ่มเติม (ลบด้วยชื่อ หรือลบด้วยเลขลำดับ)
        print("Choose complete method:")
        print("A: Remove by Name (ลบด้วยชื่อชิ้นงาน)")
        print("B: Remove by Number (ลบด้วยตัวเลขลำดับ)")
        sub_choice = input("Choose (A or B): ").strip().upper()
        
        # ลบด้วยชื่อชิ้นงาน (Remove by Name)
        if sub_choice == 'A':
            task_name = input("Enter the task name to complete: ").strip()
            # ตรวจสอบก่อนว่าชิ้นงานนั้นอยู่ใน list หรือไม่ เพื่อไม่ให้โปรแกรม Error
            if task_name in todo_list:
                # 4) ใช้ remove() เพื่อลบตามข้อมูลชื่อตรงๆ
                todo_list.remove(task_name)
                print(f"Task '{task_name}' has been marked as complete and removed!")
            else:
                print(f"'{task_name}' not found in your list.")
                
        # ลบด้วยตัวเลขลำดับ (Remove by Index)
        elif sub_choice == 'B':
            try:
                # รับเลขลำดับ (1, 2, 3...) แล้วแปลงเป็น Index ในระบบ Python (0, 1, 2...)
                task_num = int(input("Enter task number to complete: "))
                index_to_remove = task_num - 1
                
                # ตรวจสอบว่าผู้ใช้กรอกตัวเลขที่อยู่ในช่วงดัชนีของ list หรือไม่
                if 0 <= index_to_remove < len(todo_list):
                    # 4) ใช้ pop() เพื่อลบข้อมูลที่ระบุตำแหน่ง index
                    completed_task = todo_list.pop(index_to_remove)
                    print(f"Task {task_num} '{completed_task}' is completed and removed!")
                else:
                    print("Invalid task number!")
            except ValueError:
                print("Please enter a valid integer number!")
        else:
            print("Invalid selection! Please choose A or B.")
            
    # 2.4) ออกจากโปรแกรม (Exit)
    elif choice == '4':
        print("\nThank you for using To-Do List Manager. Have a productive day! Bye!")
        break
        
    else:
        print("Invalid choice! Please select 1-4.")