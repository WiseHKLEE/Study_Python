import os


def search(dirname):
    try:
        filenames = os.listdir(dirname)
        for filename in filenames:
            full_filename = os.path.join(dirname, filename) #여기서 구해지는 파일List는 파일명만 포함되어 있으므로, 입력받은 dirname을 앞에 덧붙여주었음.
            if os.path.isdir(full_filename):  #full_filename이 directory인지 file인지 구분. directory일 경우 해당 경로를 입력으로 다시 받아, Search함수를 재 호출.
                search(full_filename)
            else:
                ext = os.path.splitext(full_filename)[-1]  #full_filename이 file일 경우, file확장자명만 분류
                if ext == '.py':
                    print(full_filename)
    except PermissionError:
        pass

search("c:/")