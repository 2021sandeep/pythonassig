def reverse(s):
    if len(s) == 0:
      return s
    else:
      return reverse(s[1:])+s[0].upper()
       
  
s = input()
reverse(s)
