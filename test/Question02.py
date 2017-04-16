# Jump to Python 문제 A 씨는 게시판 프로그램을 작성하고 있다. 그런데 게시물의 총 건수와 한 페이지에 보여줄 게시물 수를 입력으로 주었을 때 총 페이지수를 출력하는 프로그램이 필요하다고 한다.
def getTotalPage(totalCount, pagePerCount):
    result = totalCount // pagePerCount
    return result if totalCount % pagePerCount == 0 else result + 1

print(getTotalPage(25, 10))