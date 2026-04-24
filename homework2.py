# Bài 1
products = ["Áo", "Quần", "Giày", "Mũ"]
for i in range(len(products)):
    print(i + 1, ".", products[i])

# Bài 2
prices = [100000, 200000, 150000]
total = 0
for price in prices:
    total = total + price

print("Total:", total, "VND")

# Bài 3
prices = [100000, 500000, 700000, 200000]
count = 0

for price in prices:
    if price > 300000:
        count = count + 1

print("Total products with high price:", count)

# Bài 4
prices = [100000, 500000, 700000, 200000]
max_price = prices[0]  # giả sử phần tử đầu là lớn nhất

for price in prices:
    if price > max_price:
        max_price = price

print("Highest price:", max_price)

# Bài 5
numbers = [1, 2, 3, 4, 5, 6]
total = 0

for n in numbers:
    if n % 2 == 0:  # % là chia lấy dư, chẵn thì dư = 0
        total = total + n

print("Total even numbers:", total)

# Bài 6
for i in range(1, 6):       # i chạy từ 1 đến 5
    for j in range(1, 11):  # j chạy từ 1 đến 10
        print(i, "x", j, "=", i * j)

# Bài 7
n = 17
is_prime = True
for i in range(2, n):
    if n % i == 0:
        is_prime = False
        break
if is_prime:
    print(n, "là số nguyên tố")
else:
    print(n, "không phải số nguyên tố")

# Bài 8
orders = ["A", "B", "A", "C", "A"]
count = 0

for order in orders:
    if order == "A":
        count = count + 1

print("A xuất hiện:", count, "lần")

# Bài 9
def calculate_total(price, quantity):
    return price * quantity

result = calculate_total(50000, 3)
print("Tổng tiền:", result)

# Bài 10
def check_login(is_logged_in):
    if is_logged_in:
        return "Đã đăng nhập"
    else:
        return "Chưa đăng nhập"

print(check_login(True))

# Bài 11
def apply_discount(price, percent):
    discount = price * percent / 100
    return price - discount

print(apply_discount(500000, 10))

# Bài 12
def is_free_shipping(order_value):
    if order_value >= 200000:
        return True
    else:
        return False

result = is_free_shipping(250000)
print("Free ship:", result)

# Bài 13
def classify_customer(total_spent):
    if total_spent >= 1000000:
        return "VIP"
    elif total_spent >= 500000:
        return "Gold"
    else:
        return "Normal"

print(classify_customer(1200000))

# Bài 14
def is_valid_email(email):
    if "@" in email and "." in email:
        return True
    else:
        return False

email = "user@gmail.com"
if is_valid_email(email):
    print("Email hợp lệ")
else:
    print("Email không hợp lệ")

# Bài 15
def total_revenue(orders):
    total = 0
    for order in orders:
        total = total + order
    return total

orders = [100000, 200000, 300000]
print("Tổng doanh thu:", total_revenue(orders))

# Bài 16
def filter_prices(prices):
    result = []
    for price in prices:
        if price > 300000:
            result.append(price)
    return result

prices = [100000, 500000, 700000, 200000]
print(filter_prices(prices))

# Bài 17
def check_orders(orders):
    count = 0
    for order in orders:
        if order > 0:
            count = count + 1
    return count

orders = [100000, 0, 200000, -50000]
print("Đơn hợp lệ:", check_orders(orders))

# Bài 18
def apply_discount(price):
    return price * 0.9

prices = [100000, 200000, 300000]
total = 0

for price in prices:
    total = total + apply_discount(price)

print("Tổng sau giảm:", total)

# Bài 19
def vip_checker(cart):
    total = 0
    for item in cart:
        total = total + item
    if total >= 3000000:
        return True
    else:
        return False

cart = [200000, 1500000, 800000]
print(vip_checker(cart))

# Bài 20
def checkout(cart, balance):
    total = 0
    for item in cart:
        total = total + item

    if balance >= total:
        return {"status": "Thanh toán thành công", "Số dư còn lại": balance - total}
    else:
        return {"status": "Không đủ tiền", "Số dư còn lại": balance}

cart = [100000, 200000, 150000]
balance = 500000
print(checkout(cart, balance))

