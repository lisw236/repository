import time

result = 0
start = time.time()

for i in range(1, 20000001):
    result += i
print(result)

end = time.time()
print(end - start)
