prices = {
    "iphone" : 500,
    "ipad"   : 400,
}
new_price = {
    'iphone': 600,
    'imac'  : 1500,
}

prices.update(new_price)
print(prices) # {'iphone': 600, 'ipad': 400, 'imac': 1500}

prices.pop('ipad')
print(prices) # {'iphone': 600, 'imac': 1500}