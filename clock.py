import tkinter as tk
from time import strftime

# ساخت پنجره اصلی
root = tk.Tk()

# تنظیم فونت و رنگ برای ساعت
clock_label = tk.Label(root, font=('calibri', 40, 'bold'), background='black', foreground='orange')
clock_label.pack(anchor='center')

# تابع به روز رسانی زمان
def update_time():
    current_time = strftime('%H:%M:%S')  # دریافت زمان فعلی به فرمت ساعت:دقیقه:ثانیه
    clock_label.config(text=current_time)
    clock_label.after(1000, update_time)  # هر ۱۰۰۰ میلی‌ثانیه (۱ ثانیه) ساعت به‌روز شود

# شروع به روز رسانی ساعت
update_time()

# اجرای برنامه
root.mainloop()
