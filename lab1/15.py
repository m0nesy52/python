sales_data = [
    {"name": "Ноутбук", "price": 50000, "quantity": 3},
    {"name": "Смартфон", "price": 30000, "quantity": 5},
    {"name": "Наушники", "price": 5000, "quantity": 12},
    {"name": "Смартфон", "price": 30000, "quantity": 2},
    {"name": "Монитор", "price": 15000, "quantity": 4}
]
revenue_by_product = {}
for item in sales_data:
    name = item["name"]
    revenue = item["price"] * item["quantity"]
    if name in revenue_by_product:
        revenue_by_product[name] += revenue
    else:
        revenue_by_product[name] = revenue
print("Выручка по каждому товару:")
for product, total in revenue_by_product.items():
    print(f"- {product}: {total} руб.")
most_profitable_product = max(revenue_by_product, key=revenue_by_product.get)
print(f"\nСамый прибыльный товар: **{most_profitable_product}** ({revenue_by_product[most_profitable_product]} руб.)")
unique_count = len(revenue_by_product)
print(f"Количество уникальных наименований: **{unique_count}**")
