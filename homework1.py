# Bài 1
price = 1200000
quantity = 3
# Yêu cầu:
# Tính và print tổng tiền đơn hàng
# Note: In ra kết quả theo định dạng: "Tổng tiền: xxx VND"
# Dùng toán tử *
total = price * quantity
print("Tổng tiền:", total, "VND")

# Bài 2
price = 500000
discount_percent = 10 # so tien duoc giam
# Tính và print số tiền được giảm
# Tính và print giá cuối cùng sau khi giảm
total = price * discount_percent / 100
final_price = price - total
print("số tiền đc giảm:", total, "VND")
print("giá cuối cùng sau khi giảm:", final_price, "VND")

#Bài 3
salary_per_day = 300000
working_days = 22
# Tính tổng lương tháng (Sẽ bằng lương của mỗi ngày nhân với số ngày làm việc)
total_monthly_salary = salary_per_day * working_days
print("Tổng lương tháng:", total_monthly_salary, "VND")

# Bài 4
distance_km = 12
cost_per_km = 5000
# Tính tổng phí vận chuyển (Bằng khoảng cách * giá vận chuyển mỗi km)
total_shipping_cost = distance_km * cost_per_km
print("Tổng chi phí vận chuyển:", total_shipping_cost, "VND")

# Bài 5
total_storage = 256
used_storage = 180
# Tính dung lượng còn lại (Bằng tổng trừ đi lượng đã dùng)
remaining_storage = total_storage - used_storage
print("Tổng dung lượng còn lại:", remaining_storage, "GB")

# Bài 6
# balance = 200000 # so tien dang co trong tk
# item_price = 150000 # tien hang
# # Kiểm tra người dùng có đủ tiền để thanh toán không, nếu có thì in ra “Thanh toán thành công”. 
# # Ngược lại, in ra “Bạn không đủ tiền trong tài khoản”
# if balance >= item_price:
#     print("Thanh toán thành công")
# else:
#     print("Bạn không đủ tiền trong tài khoản")

balance = 100000
item_price = 150000
if balance >= item_price:
    print("Thanh toán thành công")
else:
    print("Bạn không đủ tiền trong tài khoản")

# Bài 7
order_value = 250000
if order_value >= 200000:
    print("Đơn hàng được miễn phí vận chuyển")
else:
    print("Đơn hàng không được miễn phí vận chuyển")

# Bài 8
is_logged_in = True
is_admin = False
if is_logged_in and is_admin:
    print("Người dùng có quyền admin")
else:
    print("Người dùng không có quyền admin")

# Bài 9
hour = 14
if hour >= 9 and hour <= 18:
    print("Trong giờ làm việc")
else:
    print("Ngoài giờ làm việc")

# Bài 10
email = "user@gmail.com"
if "@" in email and "." in email:
    print("Email hợp lệ")
else:
    print("Email không hợp lệ")

# Bài 11
order_value = 180000
total = order_value
if order_value >= 200000:
    print("Miễn phí vận chuyển")
else:
    total = order_value + 30000

print("Tổng tiền phải trả:", total, "VND")

# Bài 12
performance_score = 8.2
if performance_score >= 9:
    bonus = 5000000
elif performance_score >= 7:
    bonus = 2000000
else:
    bonus = 0

print("Thưởng:", bonus, "VND")

# Bài 13
status_code = 2

if status_code == 1:
    print("Pending")
elif status_code == 2:
    print("Shipping")
elif status_code == 3:
    print("Delivered")
else:
    print("Unknown")

# Bài 14
age = 15

if age < 12:
    ticket_price = 50000
elif age <= 17:
    ticket_price = 70000
else:
    ticket_price = 100000

print("Giá vé:", ticket_price, "VND")

# Bài 15
total_spent = 1200000

if total_spent >= 1000000:
    print("VIP")
elif total_spent >= 500000:
    print("Gold")
else:
    print("Normal")

# Bài 16
kwh = 135

if kwh <= 50:
    total = kwh * 1678
elif kwh <= 100:
    total = (50 * 1678) + ((kwh - 50) * 1734)
else:
    total = (50 * 1678) + (50 * 1734) + ((kwh - 100) * 2014)

print("Tiền điện:", total, "VND")

# Bài 17
base_salary = 10000000
kpi = 0.85

if kpi >= 0.9:
    total_salary = base_salary * 1.3
elif kpi >= 0.8:
    total_salary = base_salary * 1.1
else:
    total_salary = base_salary

print("Tổng lương:", total_salary, "VND")

# Bài 18
distance = 12

if distance <= 1:
    fare = 15000
elif distance <= 10:
    fare = 15000 + (distance - 1) * 12000
else:
    fare = 15000 + (9 * 12000) + ((distance - 10) * 10000)

print("Tiền taxi:", fare, "VND")

# Bài 19
income = 15000000
debt = 3000000

if income >= 10000000 and debt <= income * 0.5:
    print("Đủ điều kiện vay")
else:
    print("Không đủ điều kiện vay")

# Bài 20
price = 1000000
is_member = True
voucher = 100000

if is_member:
    price = price * 0.9

price = price - voucher

if price < 0:
    price = 0

print("Giá cuối cùng:", price, "VND")