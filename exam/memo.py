import sys

option = sys.argv[1]  #python memo.py -a "Life is too short"
                      #python memo.py -v 는 출력

if option == '-a':
    memo = sys.argv[2]   #"Life is too short"
    f = open('memo.txt', 'a') #append 모드로 파일 open
    f.write(memo)
    f.write('\n')
    f.close()
elif option == '-v':
    f = open('memo.txt', 'r')
    memo = f.read()
    f.close()
    print(memo)