try:
    f = open('foo.txt', 'r')
except FileNotFoundError as e:  #foo.txt가 없다면 FileNotFoundError로 인해 Except문이 수행
    print(str(e))
else:
    data = f.read() #foo.txt가 있다면 else문이 수행
    print(data)
    f.close()