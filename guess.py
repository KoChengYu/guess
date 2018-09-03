# 產生一個隨機整數1~100(不要印出來)
# 讓使用者重複輸入數字去猜
# 猜對的話 則印出 "猜對了"
# 猜錯的話 則印出 "比答案大or小"


import random
r = random.randint(1, 100)

while True:
	num = input('請猜猜數字: ')
	num = int(num)
	if num == r:
		print('你猜對囉!')
		break
	elif num > r:
		print('太大囉!')
	elif num < r:
		print('太小囉!')
