import pickle
mylist = ['some text' , 123, [4,5,True]]
f = open('mylistpickle', 'w+b')
pickle.dump(mylist,f)
f.close()
