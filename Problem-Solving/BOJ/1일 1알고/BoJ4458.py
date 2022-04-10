num = int(input())
str_lst = []

for i in range(num):
    string = input()
    string[0].upper()
    string_first = string[0].upper()
    string_second = string[1:]
    string = string_first + string_second
    str_lst.append(string)

print(*str_lst, sep = "\n")
