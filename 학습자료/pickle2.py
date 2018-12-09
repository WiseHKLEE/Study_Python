import pickle

f = open('text.txt','rb')
data = pickle.load(f)
print(data)