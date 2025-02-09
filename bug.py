def function_with_uncommon_bug(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        return a / b

result = function_with_uncommon_bug(0, 0)
print(result) # This will raise ZeroDivisionError

result2 = function_with_uncommon_bug(5, 0) 
print(result2) # This will also raise ZeroDivisionError, but the previous should have returned 0.