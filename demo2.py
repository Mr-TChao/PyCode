import tkinter as tk
from tkinter import messagebox

class SimpleGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("简单的 GUI 示例")
        self.root.geometry("400x300")

        # 创建标签
        self.label = tk.Label(root, text="欢迎使用！", font=("Arial", 14))
        self.label.pack(pady=20)

        # 创建输入框
        self.entry = tk.Entry(root)
        self.entry.pack(pady=10)

        # 创建按钮
        self.button = tk.Button(root, text="点击我", command=self.show_message)
        self.button.pack(pady=10)

        # 创建文本框
        self.text_area = tk.Text(root, height=5, width=30)
        self.text_area.pack(pady=10)

    def show_message(self):
        user_input = self.entry.get()
        if user_input:
            messagebox.showinfo("消息", f"你输入了: {user_input}")
            self.text_area.insert(tk.END, user_input + "\n")
        else:
            messagebox.showwarning("警告", "请输入一些内容！")

if __name__ == "__main__":
    root = tk.Tk()
    app = SimpleGUI(root)
    root.mainloop()