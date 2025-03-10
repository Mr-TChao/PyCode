import tkinter as tk
from tkinter import ttk, messagebox
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class WebModifierGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("网页内容修改器")
        self.root.geometry("600x400")
        self.driver = None
        
        # 创建主框架
        self.main_frame = ttk.Frame(self.root, padding="10")
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # URL输入
        ttk.Label(self.main_frame, text="网址:").grid(row=0, column=0, sticky=tk.W)
        self.url_entry = ttk.Entry(self.main_frame, width=50)
        self.url_entry.grid(row=0, column=1, columnspan=2, padx=5, pady=5)
        
        # 元素选择器
        ttk.Label(self.main_frame, text="选择器:").grid(row=1, column=0, sticky=tk.W)
        self.selector_type = ttk.Combobox(self.main_frame, 
                                        values=["ID", "Class", "CSS", "XPath"])
        self.selector_type.grid(row=1, column=1, padx=5, pady=5)
        self.selector_type.set("ID")
        
        self.selector_entry = ttk.Entry(self.main_frame, width=30)
        self.selector_entry.grid(row=1, column=2, padx=5, pady=5)
        
        # 新内容输入
        ttk.Label(self.main_frame, text="新内容:").grid(row=2, column=0, sticky=tk.W)
        self.content_text = tk.Text(self.main_frame, height=5, width=50)
        self.content_text.grid(row=2, column=1, columnspan=2, padx=5, pady=5)
        
        # 按钮
        self.button_frame = ttk.Frame(self.main_frame)
        self.button_frame.grid(row=3, column=0, columnspan=3, pady=10)
        
        ttk.Button(self.button_frame, text="打开浏览器", 
                  command=self.open_browser).pack(side=tk.LEFT, padx=5)
        ttk.Button(self.button_frame, text="修改内容", 
                  command=self.modify_content).pack(side=tk.LEFT, padx=5)
        ttk.Button(self.button_frame, text="关闭浏览器", 
                  command=self.close_browser).pack(side=tk.LEFT, padx=5)
    
    def open_browser(self):
        try:
            self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
            url = self.url_entry.get()
            if url:
                self.driver.get(url)
            messagebox.showinfo("成功", "浏览器已打开")
        except Exception as e:
            messagebox.showerror("错误", f"打开浏览器失败: {str(e)}")
    
    def modify_content(self):
        if not self.driver:
            messagebox.showerror("错误", "请先打开浏览器")
            return
        
        try:
            selector_type = self.selector_type.get()
            selector = self.selector_entry.get()
            new_content = self.content_text.get("1.0", tk.END).strip()
            
            # 选择定位方式
            if selector_type == "ID":
                by = By.ID
            elif selector_type == "Class":
                by = By.CLASS_NAME
            elif selector_type == "CSS":
                by = By.CSS_SELECTOR
            else:
                by = By.XPATH
            
            # 等待元素加载并修改
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((by, selector))
            )
            
            # 使用JavaScript修改内容
            self.driver.execute_script(
                "arguments[0].innerHTML = arguments[1]",
                element,
                new_content
            )
            
            messagebox.showinfo("成功", "内容已修改")
        except Exception as e:
            messagebox.showerror("错误", f"修改内容失败: {str(e)}")
    
    def close_browser(self):
        if self.driver:
            self.driver.quit()
            self.driver = None
            messagebox.showinfo("成功", "浏览器已关闭")

if __name__ == "__main__":
    root = tk.Tk()
    app = WebModifierGUI(root)
    root.mainloop()