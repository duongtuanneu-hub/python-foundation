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