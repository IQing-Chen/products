#重复输入商品名称和价格
#清单中还有清单 = 二维度
products = []
while True:
	name = input('请输入商品名称：')
	if name == "q":
		break
	price = input('请输入商品价格：')
	p = []
	p.append(name)
	p.append(price)
	products.append(p)
print(products)