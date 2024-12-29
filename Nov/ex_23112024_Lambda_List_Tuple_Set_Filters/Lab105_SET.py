# find the non-repeating charcter in a string using sets.

#swiss > s -Not w _yes

def non_repeating_char(string):
    for char in string:
        if string.count(char) == 1:
            return char

    return
print(non_repeating_char("swiss"))
print(non_repeating_char("pepper"))
print(non_repeating_char("python"))
print(non_repeating_char("vivi"))
print(non_repeating_char("s"))
print(non_repeating_char("_yesyes"))