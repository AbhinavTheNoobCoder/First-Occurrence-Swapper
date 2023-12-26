s = input("Enter a string: ")
print('''
*Ensure that swap characters 1 and 2 are in the same order as they occur in the string
 For example, if your string is:
 "I am from a country" - then the swap characters 1 & 2 cannot be "country" & "I" respectively
 but can be "I" & "country"
''')
swap1 = input("Enter swap character 1: ")
swap2 = input("Enter swap character 2: ")
replaced_s = ""
try:
    sub1 = s[:s.index(swap1) + len(swap1)]
    sub2 = s[s.index(swap2): ]
    sub_1 = sub1.replace(swap1, swap2, 1)
    sub_2 = sub2.replace(swap2, swap1, 1)
    replaced_s = sub_1 + s[len(sub1): len(s) - len(sub2) ] + sub_2
    print(replaced_s)
except:
    print("Invalid swap characters.")