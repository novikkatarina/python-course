import time

seconds = time.time()
sec_str = str(seconds)
last_two_str = sec_str[-2:]
l = int(last_two_str)
print(l)