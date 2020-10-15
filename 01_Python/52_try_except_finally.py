list=[1,2,3]

try:
    list[8]
except:     # 예외 발생시 except문 실행
    print("out of range")
else:       # 예외가 없을 경우 else문 실행
    print("in range")
finally:    # 예외 발생 여부와 상관없이 finally문 실행
    print("always do this")

