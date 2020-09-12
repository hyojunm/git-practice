print("Change #2")

import time

date = time.strftime("%A, %B %d, %Y")
message = f"Today is {date}"


print(message)


clock = time.localtime()
current_time = time.strftime("%H:%M:%S", clock)
print(current_time)