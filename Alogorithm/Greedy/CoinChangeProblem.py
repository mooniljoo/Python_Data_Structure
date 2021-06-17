# O(n)
n = int(input("거슬러 주어야 할 금액 입력 : "))
cnt = 0

# 큰 단위의 화페부터 차례대로 확인하기
arr = [500, 100, 50, 10]

for coin in arr:
    cnt += n // coin  # 해당 화폐로 거슬러 줄 수 있는 동전의 갯수 세기
    n %= coin

print(f"거슬러 주어야 하는 동전의 최소 갯수 : {cnt}개")
