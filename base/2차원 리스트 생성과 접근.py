'''2차원 리스트 생성과 접근'''

#1차원 리스트 생성
a=[0]*3
print(a)

#2차원 리스트 생성
# for _ in 이렇게 하면 변수 없이 반복문만 돈다.
a=[[0]*3 for _ in range(3)]
print(a)

