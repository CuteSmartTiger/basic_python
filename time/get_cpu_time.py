import time
start = time.clock()
for i in range(100000):
    pass
end = time.clock()
print(end-start)

time.sleep(3)