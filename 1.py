Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # گرفتن عدد از کاربر
... n = int(input("یک عدد وارد کن: "))
... 
... # حلقه برای چاپ مثلث عددی
... for i in range(1, n + 1):
...     for j in range(1, i + 1):
...         print(j, end=' ')
