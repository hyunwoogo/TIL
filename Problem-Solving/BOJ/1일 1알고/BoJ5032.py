e, f, c = map(int, input().split())

bottle_num = e + f  # 현재 가지고 있는 빈병 
soda_num = 0        # 빈병을 가지고 먹을 수 있는 탄산음료 개수 
soda = 0 

while bottle_num >= c:
    soda = bottle_num // c
    soda_num += soda
    bottle_num += soda - (soda * c)
    
print(soda_num)