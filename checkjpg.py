import os
import tkinter as tk
from tkinter import filedialog

# ฟังก์ชันเลือกโฟลเดอร์
def select_folder():
    root = tk.Tk()
    root.withdraw()  # ซ่อนหน้าต่างหลักของ Tkinter
    folder_path = filedialog.askdirectory(title="เลือกโฟลเดอร์")
    return folder_path

# ฟังก์ชันตรวจสอบไฟล์ว่าเป็นไฟล์ .jpg หรือไม่
def check_files_in_folder(folder_path):
    found_files = False  # ตัวแปรเพื่อตรวจสอบว่าเจอไฟล์ที่ต้องการหรือไม่
    # สร้าง list ของไฟล์ที่ต้องการเช็ค
    for i in range(100, 131):  # 100-130
        file_name = f"{i}.jpg"  # ตั้งชื่อไฟล์
        file_path = os.path.join(folder_path, file_name)  # เช็คที่อยู่ของไฟล์

        # ตรวจสอบว่าไฟล์มีอยู่ในโฟลเดอร์หรือไม่
        if os.path.exists(file_path):
            found_files = True  # เจอไฟล์แล้ว
            # เช็คว่าไฟล์นั้นเป็นไฟล์ .jpg หรือไม่
            if not file_name.lower().endswith(".jpg"):
                print(f"ไฟล์ {file_name} ไม่ใช่ไฟล์ .jpg")
        else:
            print(f"ไม่พบไฟล์ {file_name} ในโฟลเดอร์")

    # หากไม่พบไฟล์เลย
    if not found_files:
        print("ไม่พบไฟล์จาก 100.jpg ถึง 130.jpg ในโฟลเดอร์นี้")

# เรียกใช้งานโปรแกรม
folder = select_folder()  # เลือกโฟลเดอร์
if folder:  # ถ้าเลือกโฟลเดอร์สำเร็จ
    check_files_in_folder(folder)  # ตรวจสอบไฟล์ในโฟลเดอร์
else:
    print("ไม่ได้เลือกโฟลเดอร์")
