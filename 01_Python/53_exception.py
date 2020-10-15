list=[1,2,3]
try:
    list[8]
except Exception as e: 
    print("out of range")
    print(e)
