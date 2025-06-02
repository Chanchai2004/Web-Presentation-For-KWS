from moviepy import *
from PIL import Image
import os
import tkinter as tk
from tkinter import filedialog

# ฟังก์ชันสำหรับเลือกโฟลเดอร์จาก GUI
def select_folder():
    root = tk.Tk()
    root.withdraw()  # ซ่อนหน้าต่างหลักของ Tkinter
    folder_selected = filedialog.askdirectory()  # เปิด dialog box ให้เลือกโฟลเดอร์
    return folder_selected

# ฟังก์ชันสำหรับสร้างวิดีโอจากภาพที่อัปโหลด
def create_video_from_images(image_folder, output_filename="output_video.mp4", frame_duration=5, resolution=(1920, 1080)):
    images = []

    # โหลดภาพทั้งหมดจากโฟลเดอร์ที่กำหนด และจัดเรียงตามชื่อไฟล์จากน้อยไปมาก
    image_files = sorted(os.listdir(image_folder), key=lambda x: int(x.split('.')[0]))  # จัดเรียงตามหมายเลขในชื่อไฟล์
    for filename in image_files:
        if filename.endswith(".jpg") or filename.endswith(".png"):  # ตรวจสอบนามสกุลไฟล์
            image_path = os.path.join(image_folder, filename)
            img = Image.open(image_path)

            # ปรับขนาดภาพให้ตรงกับ resolution ที่กำหนด
            img = img.resize(resolution)
            images.append(img)

    # สร้างคลิปจากภาพที่โหลดมา
    clips = []
    for img in images:
        # สร้างแอนิเมชันให้ภาพเลื่อน
        img_clip = ImageClip(img).set_duration(frame_duration)
        clips.append(img_clip)

    # รวมคลิปภาพทั้งหมด
    final_clip = concatenate_videoclips(clips, method="compose")
    final_clip.write_videofile(output_filename, fps=24)  # สร้างวิดีโอใน 24 fps

# เลือกโฟลเดอร์
image_folder = select_folder()

# ตรวจสอบว่าโฟลเดอร์ถูกเลือกหรือไม่
if image_folder:
    create_video_from_images(image_folder)
else:
    print("ไม่ได้เลือกโฟลเดอร์")
