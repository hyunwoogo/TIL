import sys

string = sys.stdin.readline()
new_string = []
sub_string = []

# 출력 초과 나중에 다시 풀어보기
if "<" in string:
    
    while len(string) > 1:
        a = string.index("<")
        b = string.index(">")
        new_voc = string[:a].split()
        for i in new_voc:
            sub_string.append(i[::-1])
        new_string.append(" ".join(sub_string))
        new_string.append(string[a:b+1])
        string = string[b+1:]
    print("".join(new_string))
  
else:
    try:
        string_sub = string.split()
        for i in string_sub:
            new_voc = i[::-1]
            new_string.append(new_voc)
        print(" ".join(new_string))

    except:
        print(string[::-1])