# ex16.py  读写文件
filename = input("请输入文件名: ")

print(f"We're going to erase {filename}")
print("If you don't want that, hit CTRL-C(^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, 'w')

print("Truncating the file, Goodbye!")
target.truncate()                   # 清空文件内容

print("Now i'm going to ask you for three lines.")

line1 = input("line1:")
line2 = input("line2:")
line3 = input("line3:")

print("I'm going to write these to the file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally , we close it.")
target.close()