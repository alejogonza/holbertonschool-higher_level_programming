#!/usr/bin/python3
def roman_to_int(roman_string):
    if isinstance(roman_string, str) is False or roman_string is None:
        return (0)
    res = 0
    rom_str = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for i in range(len(roman_string), 0, -1):
        if roman_string[i-1] in rom_str:
            res += rom_str[roman_string[i-1]]
            if i != 0 and (i-2) >= 0:
                if rom_str[roman_string[i - 2]] < rom_str[roman_string[i - 1]]:
                    res -= (2 * rom_str[roman_string[i - 2]])
        else:
            return (0)
    return (res)
