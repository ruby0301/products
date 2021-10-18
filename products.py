products = []
while True:
	name = input('請輸入商品名稱：')
	if name == 'q':
		break
	price = input('請輸入商品價格：')
	price = int(price) 
	products.append([name, price])
print(products)

#增加 for loop：
for p in products:
	print(p[0], '的價格是：', p[1])

#寫入檔案：
with open('products.csv', 'w', encoding='utf-8') as f: #編碼
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n')


