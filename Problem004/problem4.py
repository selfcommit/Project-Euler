
def is_palindrom(num):
    palindrome = str(num)[::-1]
    if str(num) == palindrome:
        # print num, "is a palindrome:", str(num), palindrome
        return True
    else:
        # print num, "is not a palindrome:", str(num), palindrome
        return False

x = 100
xarray = []
while x < 1000:
    xarray.append(x)
    x = x+1
# print xarray
y = 100
yarray = []
while y < 1000:
    yarray.append(y)
    y = y + 1
# print yarray


