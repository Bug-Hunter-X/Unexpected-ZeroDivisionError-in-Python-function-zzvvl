def function_with_uncommon_bug_fixed(a, b):
    if a == 0 and b == 0:
        return 0  # Handle the case where both are zero
    elif a == 0:
        return b
    elif b == 0:
        return a
    else:
        return a / b

result = function_with_uncommon_bug_fixed(0, 0)
print(result)  # Output: 0

result2 = function_with_uncommon_bug_fixed(5, 0) 
print(result2)  # Output: 5

result3 = function_with_uncommon_bug_fixed(5, 2)
print(result3) #Output: 2.5