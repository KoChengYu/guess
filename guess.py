# 產生一個隨機整數1~100(不要印出來)
# 讓使用者重複輸入數字去猜
# 猜對的話 則印出 "猜對了"
# 猜錯的話 則印出 "比答案大or小"


import random
start = input('請輸入隨機數字範圍初始值: ')
end = input('請輸入隨機數字範圍結束值: ')
start = int(start)
end = int(end)
r = random.randint(start, end)
count = 0
while True:
	count = count + 1  #count += 1
	num = input('請猜猜數字: ')
	num = int(num)
	if num == r:
		print('你猜對囉!')
		print('這是你猜的第', count, '次')
		break
	elif num > r:
		print('太大囉!')
	elif num < r:
		print('太小囉!')
	print('這是你猜的第', count, '次')