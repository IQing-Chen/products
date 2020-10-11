#讀取檔案
products = []
with open('products.csv', 'r', encoding = 'utf-8') as f:
	for line in f:
		#跳過欄位
		if '商品，價格' in line:
			continue #繼續
		#split切割完的結果就是清單
		#strip()除掉換行符號
		name , price= line.strip().split(',')
		products.append([name, price])

print(products)

#重复输入商品名称和价格
#清单中还有清单 = 二维度
while True:
	name = input('请输入商品名称：')
	if name == "q":
		break
	price = int(input('请输入商品价格：'))
	 #大清單中的小清單
	products.append([name, price]) #小清單裝入大清單
print(products)

for p in products:
	print(p[0], '的價格是', p[1])

#若沒有檔案會自動創建一個新的檔案
#csv 是excel的格式檔案縮寫
with open('products.csv', 'w', encoding = 'utf-8') as f:
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n')	
		#f.write才是寫入檔案
		#csv檔案是用逗號做區隔