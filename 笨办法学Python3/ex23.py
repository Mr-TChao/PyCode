# ex23.py  字符串, 字节串和字符编码
from pyexpat import errors
import sys
script, encoding, error = sys.argv

def main(language_file, encoding, errors):
    line = language_file.readline()

    if line :
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)

def print_line(line, encoding, errors):
    next_lang = line.strip()
    raw_bytes = next_lange.encoding(encoding, errors = errors)
    cooked_string = raw_bytes.decode(encoding, errors = errors)

    print(raw_bytes, "<==>", cooked_string)

languages = open("languages.txt", encoding="utf-8")

main(languages, encoding, error)