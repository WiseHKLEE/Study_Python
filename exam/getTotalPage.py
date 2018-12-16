#게시물 총 페이지 구하기

def getTotalPage(m,n):  # 게시물의 총 건수(m), 페이지별 보여줄 게시물 수 (n)
    if m%n == 0:
        return m//n
    else:
        return (m//n)+1

print(getTotalPage(5,10))
print(getTotalPage(15,10))
print(getTotalPage(25,10))
print(getTotalPage(30,10))