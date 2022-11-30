import locale
import chardet

print(locale.getpreferredencoding())

with open('test_file.txt', 'rb') as fl:
    s = fl.read()
    print(s)
    print(chardet.detect(s))

with open('test_file.txt', encoding='utf-8', errors='replace') as fl:
    print(fl.read())