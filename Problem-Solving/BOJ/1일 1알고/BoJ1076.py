# 1. 딕셔너리 사용
# 72ms

resistance = {"black" : ["0", 10**0], "brown" : ["1", 10**1], "red" : ["2", 10**2], "orange" : ["3", 10**3], "yellow" : ["4", 10**4],
             "green" : ["5", 10**5], "blue" : ["6", 10**6], "violet" : ["7", 10**7], "grey" : ["8", 10**8], "white" : ["9", 10**9]}


first = input()
second = input()
third = input()

ans_fir = resistance[first][0]
ans_sec = resistance[second][0]
ans_fir_sec = ans_fir + ans_sec
ans_thir = resistance[third][1]

answer = int(ans_fir_sec) *resistance[third][1]
print(answer)

# ---------------------------------------------------------------------------------------------------

# 2. 리스트 사용
# 72ms

resistance_color = ["black", "brown", "red", "orange", "yellow", 
              "green", "blue", "violet", "grey", "white"]

color1 = input()
color2 = input()
color3 = input()

color1_idx = str(resistance_color.index(color1))
color2_idx = str(resistance_color.index(color2))
sum_color = color1_idx + color2_idx
color3_idx = 10**resistance_color.index(color3)


answer = int(sum_color) * color3_idx

print(answer)