string = input("Исходное слово: ")
anything_left = True

# A&a -> a& (1)
# B&b -> b& (2)
# Ax -> xA  (3)
# Bx -> xB  (4)
# %a -> a%A (5)
# %b -> b%B (6)
# ?# -> # 7
# # ->! 8
# &? -> ? 9
# %^ ->! $ 10
# & -> # 11
# $ -> ^&   (8) 12
# L -> %L   (9) 13
# ^ ->!     (10) 14

print("Шаги: ", end="")
while True:
    # 1
    if "A&a" in string:
        print("1.1", end=' ')
        string = string.replace("A&a", "a&", 1)
        continue
    # 2
    if "B&b" in string:
        print("2.1", end=' ')
        string = string.replace("B&b", "b&", 1)
        continue
    # 3
    if "Aa" in string:
        print("3.1", end=' ')
        string = string.replace("Aa", "aA", 1)
        continue
    if "Ab" in string:
        print("3.2", end=' ')
        string = string.replace("Ab", "bA", 1)
        continue
    if "A^" in string:
        print("3.3", end=' ')
        string = string.replace("A^", "^A", 1)
        continue
    # 4
    if "Ba" in string:
        print("4.1", end=' ')
        string = string.replace("Ba", "aB", 1)
        continue
    if "Bb" in string:
        print("4.2", end=' ')
        string = string.replace("Bb", "bB", 1)
        continue
    if "B^" in string:
        print("4.3", end=' ')
        string = string.replace("B^", "^B", 1)
        continue
    # 5
    if "%a" in string:
        print("5.1", end=' ')
        string = string.replace("%a", "a%A", 1)
        continue
    # 6
    if "%b" in string:
        print("6.1", end=' ')
        string = string.replace("%b", "b%B", 1)
        continue
    # 7
    if "a#" in string:
        print("7.1", end=' ')
        string = string.replace("a#", "#", 1)
        continue
    if "b#" in string:
        print("7.2", end=' ')
        string = string.replace("b#", "#", 1)
        continue
    if "^#" in string:
        print("7.3", end=' ')
        string = string.replace("^#", "#", 1)
        continue
    if "A#" in string:
        print("7.4", end=' ')
        string = string.replace("A#", "#", 1)
        continue
    if "B#" in string:
        print("7.5", end=' ')
        string = string.replace("B#", "#", 1)
        continue
    if "%#" in string:
        print("7.6", end=' ')
        string = string.replace("%#", "#", 1)
        continue
    # 8
    if "#" in string:
        print("8.1", end=' ')
        string = string.replace("#", "", 1)
        break
    # 9
    if "&a" in string:
        print("9.1", end=' ')
        string = string.replace("&a", "&", 1)
        continue
    if "&b" in string:
        print("9.2", end=' ')
        string = string.replace("&b", "&", 1)
        continue
    if "&^" in string:
        print("9.3", end=' ')
        string = string.replace("&^", "&", 1)
        continue
    if "&A" in string:
        print("9.4", end=' ')
        string = string.replace("&A", "&", 1)
        continue
    if "&B" in string:
        print("9.5", end=' ')
        string = string.replace("&B", "&", 1)
        continue
    if "&%" in string:
        print("9.6", end=' ')
        string = string.replace("&%", "&", 1)
        continue
    # 10
    if "%^" in string:
        print("10.1", end=' ')
        string = string.replace("%^", "", 1)
        break
    # 12
    if "$" in string:
        print("12.1", end=' ')
        string = string.replace("$", "^&", 1)
        continue
    # 13
    if "a" in string:
        print("13.1", end=' ')
        string = string.replace("a", "%a", 1)
        continue
    if "b" in string:
        print("13.2", end=' ')
        string = string.replace("b", "%b", 1)
        continue
    # 11 
    if "&" in string:
        print("11.1", end=' ')
        string = string.replace("&", "#", 1)
        continue
    # 14
    if "^" in string:
        print("14.1", end=' ')
        string = string.replace("^", "", 1)
        break
print("\nРезультат:", string)
     