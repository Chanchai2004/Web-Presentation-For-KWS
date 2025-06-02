from PIL import Image, ImageEnhance
import os
from tkinter import Tk
from tkinter.filedialog import askdirectory

# สร้างหน้าต่าง Tkinter (ไม่แสดงหน้าต่างหลัก)
Tk().withdraw()

# เปิดหน้าต่างให้เลือกโฟลเดอร์
folder_path = askdirectory(title="เลือกโฟลเดอร์ที่มีภาพ")

# ตรวจสอบว่าเลือกโฟลเดอร์หรือไม่
if folder_path:
    # สร้างโฟลเดอร์ใหม่สำหรับเก็บภาพที่ปรับขนาดแล้ว
    output_folder = os.path.join(folder_path, 'images')
    os.makedirs(output_folder, exist_ok=True)

    # วนลูปตรวจสอบไฟล์ทั้งหมดในโฟลเดอร์
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # ตรวจสอบว่าไฟล์เป็นภาพหรือไม่
        if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
            try:
                # เปิดภาพ
                with Image.open(file_path) as img:
                    # เปลี่ยนขนาดภาพเป็น 1920x1080
                    resized_img = img.resize((1920, 1080))

                    # ทำให้ภาพชัดขึ้น
                    enhancer = ImageEnhance.Sharpness(resized_img)
                    sharpened_img = enhancer.enhance(2.0)  # ค่า 1.0 คือไม่มีการเปลี่ยนแปลง, ค่า 2.0 คือเพิ่มความชัด

                    # บันทึกภาพที่ปรับขนาดและทำให้ชัดขึ้นแล้วลงในโฟลเดอร์ใหม่
                    output_path = os.path.join(output_folder, filename)
                    sharpened_img.save(output_path)

                    print(f"Image {filename} resized, sharpened, and saved to {output_folder}")
            except Exception as e:
                print(f"Error processing {filename}: {e}")

    print("Image resizing and sharpening complete.")
else:
    print("No folder selected.")
