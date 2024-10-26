import tkinter as tk

# ساخت پنجره اصلی
root = tk.Tk()
root.title("")  # عنوان پنجره
root.geometry("200x160")  # تنظیم اندازه پنجره

# ایجاد یک لیبل برای نمایش پیام
label = tk.Label(root, text="commission...", font=('Arial', 20), fg="black")
label.pack(pady=50)  # تنظیم فاصله از بالا

# اجرای برنامه
root.mainloop()
