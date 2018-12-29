import sys

src = sys.argv[1]   #python tabto4.py a.txt(tab으로 띄어쓰기되어있는 임의의 파일) b.txt (tab으로 띄어쓰기되어있는 파일이 공란*4 으로 변경되어 저장되는 파일)
dst = sys.argv[2]

f = open(src)
tab_content = f.read()
f.close()

space_content = tab_content.replace('\t',' '*4)
f = open(dst,'w')
f.write(space_content)
f.close()
