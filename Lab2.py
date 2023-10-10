goots = []
CoffeShop = ["OnePrice", "Baggins", "КофеБон"]
posts = []
isTrue = True
while isTrue:
    goot = input(f'Введите название товара \n')
    if goot != '':
        goots.append(goot)
    else:
        isTrue = False


for goos in goots:
    goots_posts = []
    for shop in CoffeShop:
        price = int(input(f"Введите цену на товар {goos} в магазине {shop}\n"))
        goots_posts.append(price)
    posts.append(goots_posts)
bascet = []
for count, value in enumerate(CoffeShop): 
    total = 0
    for idx, product in enumerate(goots):
        total+= posts[idx][count]
    print(f'Общая стоимость товаров в магазине {value}: {total}')
    bascet.append(total)
min_dx = 0
min_value = 0
for idx, value in enumerate(bascet):
    if min_value == None  or value < min_value:
        min_dx = idx
        min_value = value
print(f'Самая выгодная цена в магазине {CoffeShop[min_dx]}')