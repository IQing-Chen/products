#重复输入商品名称和价格
#清单中还有清单 = 二维度
products = []
while True:
	name = input('请输入商品名称：')
	if name == "q":
		break
	price = input('请输入商品价格：')
	 #大清單中的小清單
	products.append([name, price]) #小清單裝入大清單
print(products)

for p in products:
	print(p[0], '的價格是', p[1])

#若沒有檔案會自動創建一個新的檔案
#csv 是excel的格式檔案縮寫
with open('products.csv', 'w') as f:
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')	
		#f.write才是寫入檔案
		#csv檔案是用逗號做區隔