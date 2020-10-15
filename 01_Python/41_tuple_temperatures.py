# 절대온도를 입력받아 섭씨온도와 화씨온도 리턴
def calculate_temperatures(kelvin):
    celsius = kelvin - 273
    fahrenheit = celsius * 9 / 5 + 32
    return celsius, fahrenheit

c,f = calculate_temperatures(340)
print(c)
print(f)
