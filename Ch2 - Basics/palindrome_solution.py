# Python code​​​​​​‌​‌‌​​​​​‌‌​‌‌‌​​‌‌​​‌​​​ below
# Use print("messages...") to debug your solution.

def is_palindrome(teststr):
    temp_str = teststr.lower()

    new_str = ""
    for i in temp_str:
        if i.isalnum(): # checks if the character is alphanumeric
            new_str += i
    
    total = 0
    rev_str = new_str[::-1]
    if rev_str == new_str:
        total += 1
        return True
    else:
        return False

print("String is", is_palindrome("Hello World"))