def emphasise(string):
  string=string.split(" ")
  for i in range(len(string)):
    if string[i].isalpha():
      string[i]=string[i].replace(string[i][0],string[i][0].upper())
      string[i]=string[i].replace(string[i][1:],string[i][1:].lower())
  new_string=""
  for i in string:
    if i ==string[-1]:
      new_string+=i
    else:
      new_string+=i+" "
  return new_string

emphasise("11 HELLO WORLD")


