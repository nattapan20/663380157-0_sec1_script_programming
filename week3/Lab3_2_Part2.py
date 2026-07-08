# --- Lab 3.2 Part 2: Simple Guessing Game (Challenge) ---
secret_number = 42
attempts = 0       # ตัวนับจำนวนครั้งที่ทายไป
max_attempts = 5   # จำกัดจำนวนสิทธิ์การทาย

# เปลี่ยนจาก while True เป็นการตรวจสอบสิทธิ์การทาย
while attempts < max_attempts:
    guess = int(input(f"Guess the number (Attempt {attempts + 1}/{max_attempts}): "))
    attempts += 1  # ทายแล้ว 1 ครั้ง เพิ่มจำนวนนับขึ้นทีละ 1
    
    if guess < secret_number:
        print(f"{guess} is too low! Try again.")
    elif guess > secret_number:
        print(f"{guess} is too high! Try again.")
    else:
        print("Congratulations! You guessed it!")
        break  # ทายถูก ออกจากลูปทันที
else:
    # บล็อกนี้จะทำงานก็ต่อเมื่อเงื่อนไข while เป็นเท็จ (ทายครบ 5 ครั้งแล้วแต่ยังไม่เจอ break)
    print(f"\nSorry, you ran out of attempts! The secret number was {secret_number}.")