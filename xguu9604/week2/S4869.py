import sys

sys.stdin = open('input_S4869.txt')

T = int(input()) # 시행횟수를 받아줌
cnt = 1          # 문제의 현재 횟수를 알려줌

while T > 0:     # 반복을 전체를 돌릴 반복문
    N = int(input())  # 문제에서 주어지는 가로 길이
    lst = [0] * ((N // 10) + 1)  # index값을 만들어 주기 위해 가로 길이의 몫으로 계산하고 
                                 # 내가 얻을 리스트 생성
    lst[0] = 0                   # 가로 = 0 일때는 종이 붙이기 불가능
    lst[1] = 1                   # 가로 = 10 일때는 경우의 수 = 1
    lst[2] = 3                   # 가로 = 20 일때는 경우의 수 = 3
    for i in range(3, (N//10) + 1):  # 가로 = 30 일때 부터 반복문을 돌려 계산하자
                                     # 우리가 구하고자 하는 가로는 N일때이므로 range끝값에 1을 더해줌
        lst[i] = lst[i-1] + lst[i-2] * 3 - lst[i-2] # 종이 붙이기의 경우의 수는 다음과 같은 규칙을 가짐
    result = lst[-1]  # 마지막 결과값에 리스트의 맨 끝값(top)을 할당해준다

    print(f'#{cnt} {result}')   # 원하는 답 도출
    T -= 1
    cnt += 1