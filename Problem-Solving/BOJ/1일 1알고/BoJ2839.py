sugar = int(input())

pack_num = 0

while sugar > 0:
    if sugar % 5 == 0:
        pack_num += (sugar // 5)
        break
    sugar -= 3
    pack_num += 1

if sugar < 0:
    print(-1)
else:
    print(pack_num)