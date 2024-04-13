#!/usr/bin/env python3
"""
"""
def is_additive(my_str: str) -> bool:
    """
    """
    for first_index in range(1, len(my_str) - 1):
        first = my_str[0:first_index]

        for second_index in range(first_index + 1, len(my_str)):
            second = my_str[first_index:second_index]

            combined = str(int(first) + int(second))

            if combined ==my_str[second_index:second_index + len(combined)]:
                if second_index + len(combined) == len(my_str):
                    return True
                return is_additive(my_str[first_index:])
            return False


print(is_additive("347"))
print(is_additive("347111829"))
print(is_additive("15051101152"))
print(is_additive("15141161152"))
