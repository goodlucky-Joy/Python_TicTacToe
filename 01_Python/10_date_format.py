from datetime import datetime
d = datetime.now()

print(d)
print("{:%Y-%m-%d %H:%M:%S}".format(d))
