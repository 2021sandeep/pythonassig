#camel case to snak case
def change_case(str):
    res = [str[0].lower()]
    for c in str[1:]:
        if c in ('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
            res.append('_')
            res.append(c.lower())
        else:
            res.append(c)

    return ''.join(res)

str = "hello_Edabit"
print(change_case(str))


# snake case to camel case
def snake_to_camel(word):
    import re
    return ''.join(x.capitalize() or '_' for x in word.split('_'))


print(snake_to_camel('hello_Edabit'))

