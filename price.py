def format_price(price):
	res_price=int(price)
	return ('Цена: '+ str(res_price) + ' руб.')
display_price=format_price(56.24)
print(display_price)