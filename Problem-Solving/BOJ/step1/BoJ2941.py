croa_lan = list(input())

croa_list = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']   # 크로아티아 언어 리스트

count = 0       # 크로아티어 언어 적용 단어 숫자 count용도
count_1 = 0     # 2개로 조합된 단어 count하기 위한 용도
count_2 = 0     # 3개로 조합된 단어 count하기 위한 용도

for i in range(len(croa_lan) - 1):      # 2개로 조합된 단어 찾기
    if croa_lan[i] + croa_lan[i+1] in croa_list:    # 두개 단어 합친것이 크로아티아 언어 리스트에 있으면 count_1에 +1
        count_1 += 1
        continue
for j in range(len(croa_lan) - 2):      # 3개로 조합된 단어 찾기
    if croa_lan[j] + croa_lan[j+1] + croa_lan[j+2] in croa_list:      # 세개 단어 합친것이 크로아티아 언어 리스트에 있으면 count_2에 +1
        count_2 += 1
        continue

count  = len(croa_lan) - count_1 - count_2  # 총 단어 길이에서 크로아티아 언어로 적용된것을 빼면 됨

print(count)

