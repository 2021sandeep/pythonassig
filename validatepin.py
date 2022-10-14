def valid(num):
    if num.isdigit() and (len(num)==4 or len(num)==6):
        return True
    else:
        return False
print(valid("123456"))
