# ex17.py 更多文件操作

from os.path import exists

from_file = input("File to copy from:")
to_file = input("File to copy to:")

print(f"Copying frome {from_file} to {to_file}")

# we could do these two on one line, how?
in_file = open(from_file,'r')
indata = in_file.read()

print(f"The input file is {len(indata)} bytes long")

print(f"Does the output file exise? {exists(to_file)}")
print("Ready , hit RETURN to continue, CTRL-C to abort.")
input()

out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright , all done.")

out_file.close()
in_file.close()