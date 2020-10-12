import os #作業系統模組 operating system

#讀取檔案
def read_file(filename):
	products = [] #不管有没有找当档案都要有这个空清单
	if os.path.isfile(filename): #檢查檔案是否存在
		print('档案有存在')
		with open(filename, 'r', encoding = 'utf-8') as f:
			for line in f:
				#跳過欄位
				if '商品，價格' in line:
					continue #繼續
				#split切割完的結果就是清單
				#strip()除掉換行符號
				name , price= line.strip().split(',')
				products.append([name, price])
	else:
		print("没有档案")
	return products

#重复输入商品名称和价格
#清单中还有清单 = 二维度
def user_input(products):
	while True:
		name = input('请输入商品名称：')
		if name == "q":
			break
		price = int(input('请输入商品价格：'))
		#大清單中的小清單
		products.append([name, price]) #小清單裝入大清單
	print(products)
	return products


#商品的購買記錄
def print_products(products):
	for p in products:
		print(p[0], '的價格是', p[1])

#若沒有檔案會自動創建一個新的檔案
#csv 是excel的格式檔案縮寫
def write_file(filename, products):
	with open(filename, 'w', encoding = 'utf-8') as f:
		f.write('商品,價格\n')
		for p in products:
			f.write(p[0] + ',' + str(p[1]) + '\n')	
			#f.write才是寫入檔案
			#csv檔案是用逗號做區隔


#使用function
products = read_file('products.csv')
products = user_input(products)
print_products(products)
write_file('products.csv', products)