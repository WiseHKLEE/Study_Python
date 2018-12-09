import pickle  #pickle은 객체의 형태를 그대로 유지하면서 파일에 저장하고 불러올수 있게 하는 기능
f = open('text.txt', 'wb')
data = {1:'python', 2:'you need'}
pickle.dump(data,f)
f.close()
