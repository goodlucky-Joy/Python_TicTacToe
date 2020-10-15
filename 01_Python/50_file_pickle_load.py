import pickle
f = open('mylistpickle', 'r+b')
other_array = pickle.load(f)
f.close()
print(other_array)
