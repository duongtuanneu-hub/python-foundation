# LÝ THUYẾT BÀI 5 +6 - OOP nâng cao
# Câu 1: Phân biệt giữa Class và Object
# Class = Bản thiết kế. Object = Thứ đc tạo ra từ bản thiết kế đó.
# VD mình là chủ một xưởng may. Trước khi may áo cần có một tờ rập mẫu ghi rõ: áo này có cổ, có tay, có size, có màu. Tờ rập mẫu này kp là cái áo, k mặc đc, nhưng từ 1 tờ rập mẫu có thể may ra hàng nghìn cái áo khác nhau.

# Trong lập trình:
# - Class  = tờ rập mẫu  → định nghĩa cấu trúc và hành vi
# - Object = cái áo thực → thực thể cụ thể đc tạo ra từ class

# VD trong hệ thống thương mại điện tử:
# Class Product là bản thiết kế sản phẩm:
# - Có các thuộc tính: tên, giá, tồn kho, danh mục
# - Làm đc: giảm giá, kiểm tra còn hàng

# Object p1 = Product(1, "Áo thun",   120000, 10, "Thời trang")
# Object p2 = Product(2, "Quần jean", 350000,  0, "Thời trang")
# Object p3 = Product(3, "Tất",        25000,  5, "Phụ kiện")

# Ba object khác nhau, nhưng đều đc tạo từ cùng 1 class. Mỗi object có giá trị riêng, nhưng dùng chung cấu trúc và hành vi.

# Khác biệt:
# - Class là khuôn mẫu, chỉ đc định nghĩa 1 lần, k ngốn RAM
# - Object là thực thể cụ thể, có thể tạo ra vô số, ngốn RAM

# Trong project thực tế, một hệ thống TMĐT có thể có hàng triệu sản phẩm, nhưng chỉ cần 1 class Product duy nhất để mô tả tất cả. Nếu cần thêm
# tính năng mới (ví dụ: thêm trường rating), chỉ cần sửa class một chỗ thì toàn bộ object sẽ có tính năng đó ngay lập tức. Tóm lại OOP là viết ít dùng đc nhiều.

# Câu 2: Tác dụng của hàm __init__() và tham số self
# __init__() = Hàm chạy tự động ngay khi tạo object. self = tôi - object đang tự nói về chính nó.

# VD: __init__() giống như tờ khai nhập học. Khi một học sinh mới vào trường, nhà trường tự động điền tên, ngày sinh, lớp vào hồ sơ ngay lúc đó - k cần ai gọi thủ công. __init__() hoạt động y vậy: tự động chạy và điền thông tin ban đầu cho object mỗi khi đc tạo ra.

# Còn self thì giống như đại từ "tôi" trong câu. Khi object Product nói self.name = "Áo thun" thì có nghĩa là "tên của TÔI là Áo thun". Nếu k có self, Python k biết đang nói đến thuộc tính của object nào.

# VD với class Product:
# class Product:
# def __init__(self, product_id, name, price):
# self.product_id = product_id  # gán cho chính object này
# self.name       = name
# self.price      = price
# p1 = Product(1, "Áo thun", 120000)   # __init__ tự chạy ở đây
# p2 = Product(2, "Quần jean", 350000) # __init__ tự chạy ở đây

# Khi viết p1 = Product(...), Python tự gọi __init__ và truyền p1 vào tham số self. Tức là self chính là p1 lúc đó. Còn khi tạo p2, self lại là p2.
# Self luôn phải là tham số đầu tiên để Python biết đang làm việc với object nào trong số hàng triệu object có thể tồn tại.

# Câu 3: Các loại phương thức trong Class
# 3 loại method = 3 vai trong một nhà hàng.
# Instance method = nhân viên phục vụ. Cần biết đang phục vụ bàn nào (self) mới làm việc đc. Phổ biến nhất, dùng để xử lý dữ liệu của
# từng object cụ thể.
# Class method = quản lý. Không cần biết bàn cụ thể, chỉ cần biết mình đang quản lý nhà hàng nào (cls). Dùng @classmethod, tham số đầu là cls.
# Static method = cái máy tính treo tường. Không quan tâm bàn nào hay nhà hàng nào, chỉ làm đúng 1 việc cụ thể khi đc gọi. Dùng @staticmethod, k có self hay cls.

# VD với class Order:

#     class Order:
#         total_orders = 0  # class attribute

#         def __init__(self, order_id, total):
#             self.order_id = order_id
#             self.total    = total
#             Order.total_orders += 1

#         # Instance method - cần self, làm việc với order cụ thể
#         def apply_discount(self, percent):
#             return self.total * (1 - percent / 100)

#         # Class method - đếm tổng số đơn hàng toàn hệ thống
#         @classmethod
#         def get_total_orders(cls):
#             return cls.total_orders

#         # Static method - validate dữ liệu, k cần biết order nào
#         @staticmethod
#         def is_valid_amount(amount):
#             return amount > 0

#     o1 = Order("ORD-001", 500000)
#     o2 = Order("ORD-002", 300000)
#     print(o1.apply_discount(10))     # Instance: giảm giá đơn o1
#     print(Order.get_total_orders())  # Class: tổng = 2 đơn
#     print(Order.is_valid_amount(-1)) # Static: False

# ---

# Câu 4: Tính đóng gói (Encapsulation) và access modifiers

# Encapsulation = giấu dữ liệu nhạy cảm bên trong, chỉ cho truy cập qua cửa chính thức.

# VD như căn nhà:
# - Phòng khách (public): ai cũng vào đc
# - Phòng ngủ (protected _): chỉ người nhà mới vào đc
# - Két sắt (private __): chỉ chủ nhà mới mở đc

# Python k có từ khóa public/private như Java, thay vào đó dùng dấu
# gạch dưới theo convention:
# - name      → public: ai cũng truy cập đc
# - _email    → protected: nên chỉ dùng trong class và class con
# - __password → private: chỉ dùng trong chính class đó

# VD class User với __password:

#     class User:
#         def __init__(self, name, password):
#             self.name       = name        # public
#             self.__password = password    # private

#         def check_password(self, input_pw):
#             return self.__password == input_pw  # chỉ class mới đọc đc

#     u = User("An", "secret123")
#     print(u.name)              # OK - public
#     print(u.__password)        # LỖI - AttributeError
#     print(u.check_password("secret123"))  # OK - qua cửa chính thức

# Getter/setter dùng để làm gì? Vì nếu để __credit_balance truy cập
# trực tiếp, ai đó có thể set thành -999999. Setter cho phép thêm
# validation trước khi ghi giá trị:

#     @credit_balance.setter
#     def credit_balance(self, value):
#         if value < 0:
#             raise ValueError("Số dư k đc âm")
#         self.__credit_balance = value

# Tóm lại: Encapsulation giúp bảo vệ dữ liệu khỏi bị sửa linh tinh
# từ bên ngoài. Getter/setter là cái cổng bảo vệ đó.

# ---

# Câu 5: Kế thừa (Inheritance) và ghi đè phương thức

# Kế thừa = con thừa hưởng mọi thứ từ cha, nhưng có thể có cá tính riêng.

# VD như gia đình: con cái thừa hưởng họ tên, đặc điểm từ cha mẹ. Nhưng
# con có thể có nghề nghiệp, tính cách riêng mà cha mẹ không có.

# Trong OOP: class con kế thừa toàn bộ thuộc tính và method của class
# cha. Muốn thêm hoặc thay đổi hành vi → override (ghi đè) method.

# VD lớp cha Person → lớp con Customer:

#     class Person:
#         def __init__(self, name, age):
#             self.name = name
#             self.age  = age

#         def introduce(self):
#             return f"Tôi là {self.name}, {self.age} tuổi"

#     class Customer(Person):
#         def __init__(self, name, age, customer_id):
#             super().__init__(name, age)   # gọi __init__ của Person trước
#             self.customer_id = customer_id

#         def introduce(self):             # override - khác với Person
#             return f"Tôi là KH [{self.customer_id}] {self.name}"

#     p  = Person("An", 25)
#     c  = Customer("Bình", 30, "C001")
#     print(p.introduce())   # Tôi là An, 25 tuổi
#     print(c.introduce())   # Tôi là KH [C001] Bình

# super() quan trọng vì nếu k gọi, class con sẽ k khởi tạo phần của
# class cha → thiếu các thuộc tính thừa hưởng → bug.

# Tóm lại: kế thừa giúp tái sử dụng code, tránh viết lại từ đầu. Override
# giúp lớp con có hành vi riêng mà không phá vỡ lớp cha.

# ---

# Câu 6: Scope (Phạm vi hoạt động) của biến trong class

# Scope = biến sống ở đâu thì chỉ đọc đc ở đó.

# VD như chìa khóa: chìa khóa nhà chung cư (global) ai cũng dùng đc,
# chìa khóa phòng (local) chỉ dùng trong phòng đó, chìa khóa tủ riêng
# (instance) mỗi người một cái khác nhau.

# 4 loại scope, VD với class ShoppingCart:

#     cart_count = 0   # GLOBAL - tồn tại suốt chương trình, ai cũng đọc đc

#     class ShoppingCart:
#         store_name = "ShinShop"  # CLASS attribute - chung cho mọi object

#         def __init__(self, owner):
#             self.owner = owner   # INSTANCE attribute - riêng từng object
#             self.items = []

#         def add_item(self, item):
#             tax_rate = 0.1       # LOCAL - chỉ sống trong hàm này
#             price    = item["price"] * (1 + tax_rate)
#             self.items.append(item)

#     c1 = ShoppingCart("An")
#     c2 = ShoppingCart("Bình")

#     # c1.owner và c2.owner khác nhau (instance)
#     # c1.store_name và c2.store_name đều là "ShinShop" (class)
#     # tax_rate k truy cập đc từ bên ngoài hàm add_item (local)

# Vấn đề hay gặp: dùng biến global trong class rất nguy hiểm vì bất kỳ
# hàm nào cũng có thể thay đổi nó → bug khó tìm. Rule là: function chỉ
# dùng dữ liệu đc truyền vào (input) hoặc tự tạo bên trong (local).

# Tóm lại: instance attribute cho dữ liệu riêng của từng object, class
# attribute cho dữ liệu chung, local cho biến tạm thời, global thì hạn
# chế tối đa.

# ---

# Câu 7: Polymorphism và Abstraction

# POLYMORPHISM = cùng 1 cái tên, nhiều cách thực hiện khác nhau.

# VD như nút Play: bấm Play trên Spotify thì phát nhạc, bấm Play trên
# YouTube thì phát video, bấm Play trên game thì bắt đầu chơi. Cùng 1
# hành động "play" nhưng mỗi thứ phản ứng khác nhau.

#     class Animal:
#         def speak(self): pass

#     class Dog(Animal):
#         def speak(self): return "Gâu gâu"

#     class Cat(Animal):
#         def speak(self): return "Meo meo"

#     class Bird(Animal):
#         def speak(self): return "Chip chip"

#     animals = [Dog(), Cat(), Bird()]
#     for a in animals:
#         print(a.speak())   # cùng gọi speak() nhưng kết quả khác nhau

# Ưu điểm: viết code tổng quát, k cần if/else cho từng loại. Thêm loài
# mới chỉ cần tạo class mới, k cần sửa code cũ.

# ---

# ABSTRACTION = ẩn đi bên trong phức tạp, chỉ lộ ra cái cần dùng.

# VD như lái xe: mình chỉ cần biết vô lăng, ga, phanh. K cần biết động
# cơ hoạt động ra sao. Abstract class giống như bản cam kết: "bất kỳ
# class nào kế thừa tao đều phải có những method này."

#     from abc import ABC, abstractmethod

#     class Shape(ABC):
#         @abstractmethod
#         def area(self): pass   # bắt buộc class con phải override

#     class Circle(Shape):
#         def __init__(self, r): self.r = r
#         def area(self): return 3.14 * self.r ** 2

#     class Square(Shape):
#         def __init__(self, s): self.s = s
#         def area(self): return self.s ** 2

# Abstraction khác Encapsulation ở chỗ:
# - Encapsulation: giấu DỮ LIỆU (ví dụ: __password)
# - Abstraction: giấu CÁCH THỰC HIỆN (ví dụ: k cần biết area() tính
#   thế nào, chỉ cần biết gọi là có kết quả)

# Tóm lại: Polymorphism giúp cùng 1 interface xử lý nhiều loại object
# khác nhau. Abstraction giúp thiết kế hệ thống rõ ràng, ép các class
# con phải tuân theo "hợp đồng" đã định.

# ---

# Câu 8: Schema - Cách lập kế hoạch xây dựng class

# Schema = bản vẽ thiết kế trước khi đổ bê tông. Làm xong bản vẽ mới
# đc cầm búa.

# Trong OOP, schema giúp trả lời 3 câu hỏi trước khi code:
# 1. Class này có những dữ liệu gì? (attributes)
# 2. Class này làm đc gì? (methods)
# 3. Class này quan hệ thế nào với class khác? (kế thừa, composition)

# VD schema cho PaymentProcessor:

#     PaymentProcessor (abstract class - lớp cha)
#     ├── Attributes : payment_id, amount, status
#     ├── Methods    : process() [abstract], validate() [abstract]
#     └── Con        :
#         ├── CreditCardPayment
#         │   ├── Thêm: card_number, cvv, expiry_date
#         │   └── Override: process() → gọi API ngân hàng, validate() → kiểm tra cvv
#         ├── BankTransferPayment
#         │   ├── Thêm: bank_account, bank_code
#         │   └── Override: process() → chuyển khoản, validate() → kiểm tra số TK
#         └── EWalletPayment
#             ├── Thêm: wallet_id, provider (Momo/ZaloPay/VNPay)
#             └── Override: process() → gọi API ví, validate() → kiểm tra số dư

# Tại sao cần abstract class ở đây? Vì k bao giờ tạo object
# PaymentProcessor chung chung - luôn phải là 1 trong 3 loại cụ thể.
# Abstract class chỉ định ra "hợp đồng": bất kỳ phương thức thanh toán
# nào cũng phải có process() và validate(), còn làm thế nào thì tự lo.

# Tóm lại: schema giúp nhìn toàn cảnh hệ thống trước khi code, tránh
# viết xong rồi mới phát hiện thiếu method hay thiết kế sai quan hệ giữa
# các class.

# ---

# Câu 9: Vẽ sơ đồ tư duy (Mind Map) để thiết kế class

# Mind map trước khi code = vẽ bản đồ trước khi đi vào rừng. Không vẽ
# thì đi lạc, mất thời gian sửa lại nhiều lần.

# Lợi ích:
# - Nhìn toàn cảnh hệ thống trước khi bị cuốn vào từng dòng code
# - Phát hiện sớm class nào bị "ôm đồm" quá nhiều việc
# - Dễ trình bày với team, với khách hàng
# - Giảm bug vì đã nghĩ rõ quan hệ giữa các class từ đầu

# Cấu trúc mind map gồm 3 nhánh chính:
# - Thuộc tính: tên, kiểu dữ liệu, mức truy cập
# - Phương thức: tên, input, output, mức truy cập
# - Quan hệ: kế thừa từ ai, composition với class nào

# VD mind map cho class InventoryManager:

#     InventoryManager
#     ├── Thuộc tính
#     │   ├── __products (private, dict)       → kho lưu toàn bộ sản phẩm
#     │   ├── __low_stock_threshold (private, int) → ngưỡng cảnh báo hết hàng
#     │   └── warehouse_name (public, str)     → tên kho
#     │
#     ├── Phương thức
#     │   ├── add_product(product)             → thêm sản phẩm vào kho
#     │   ├── remove_product(product_id)       → xóa sản phẩm
#     │   ├── update_quantity(product_id, qty) → cập nhật tồn kho
#     │   ├── get_low_stock_items()            → trả về list sản phẩm sắp hết
#     │   └── generate_report()               → xuất báo cáo tồn kho
#     │
#     └── Quan hệ
#         ├── Composition với Product          → quản lý list các Product object
#         └── Dùng bởi OrderService           → OrderService gọi update_quantity
#                                                sau khi đơn hàng đc xác nhận

# Tóm lại: vẽ mind map tốn 15 phút nhưng tiết kiệm đc hàng giờ debug
# sau này. Đây là thói quen phân biệt dev mới và dev có kinh nghiệm.


# THỰC HÀNH BÀI 5 + 6 - Cấu trúc dữ liệu Queue và Stack
from datetime import date

# Bài 1 - Xây dựng class Product
class Product:
    """Đại diện cho một sản phẩm trong hệ thống thương mại điện tử."""

    def __init__(self, product_id, name, price, quantity, category):
        if price <= 0:
            raise ValueError("Giá sản phẩm phải lớn hơn 0")
        if quantity < 0:
            raise ValueError("Số lượng không được âm")
        self.product_id = product_id
        self.name       = name
        self.price      = price
        self.quantity   = quantity
        self.category   = category

    def apply_discount(self, discount_percent):
        """Trả về giá sau khi giảm discount_percent%."""
        return self.price * (1 - discount_percent / 100)

    def is_in_stock(self):
        """Kiểm tra sản phẩm còn hàng không."""
        return self.quantity > 0

    def __str__(self):
        return (f"[{self.product_id}] {self.name} - {self.price:,}đ"
                f" | Tồn kho: {self.quantity} | Danh mục: {self.category}")


p1 = Product(1, "Áo thun",   120000, 10, "Thời trang")
p2 = Product(2, "Quần jean", 350000,  0, "Thời trang")
p3 = Product(3, "Tất",        25000,  5, "Phụ kiện")

print(p1)
print(f"  → Giá sau giảm 10% : {p1.apply_discount(10):>10,.0f}đ | Còn hàng: {p1.is_in_stock()}")
print(p2)
print(f"  → Còn hàng         : {p2.is_in_stock()}")
print(p3)
print(f"  → Giá sau giảm 20% : {p3.apply_discount(20):>10,.0f}đ | Còn hàng: {p3.is_in_stock()}")

# Bài 2 - Xây dựng class Customer với Encapsulation
class Customer:
    """Quản lý thông tin khách hàng với các mức độ truy cập khác nhau."""

    def __init__(self, customer_id, name, email, password, credit_balance=0):
        self.customer_id      = customer_id   # public
        self.name             = name           # public
        self._email           = email          # protected  (_email)
        self.__password       = password       # private    (__password)
        self.__credit_balance = credit_balance # private    (__credit_balance)

    @property
    def credit_balance(self):
        """Getter: đọc số dư tài khoản."""
        return self.__credit_balance

    @credit_balance.setter
    def credit_balance(self, value):
        """Setter: chỉ cho phép giá trị >= 0."""
        if value < 0:
            raise ValueError("Số dư không được âm")
        self.__credit_balance = value

    def add_credit(self, amount):
        """Nạp tiền vào tài khoản."""
        if amount <= 0:
            raise ValueError("Số tiền nạp phải lớn hơn 0")
        self.__credit_balance += amount
        print(f"  Nạp {amount:,}đ thành công → Số dư: {self.__credit_balance:,}đ")

    def use_credit(self, amount):
        """Thanh toán bằng số dư tài khoản, kiểm tra đủ số dư."""
        if amount > self.__credit_balance:
            print(f"  Không đủ số dư! Cần: {amount:,}đ | Hiện có: {self.__credit_balance:,}đ")
            return False
        self.__credit_balance -= amount
        print(f"  Thanh toán {amount:,}đ → Số dư còn: {self.__credit_balance:,}đ")
        return True

    def __str__(self):
        return (f"Customer [{self.customer_id}] {self.name}"
                f" | Email: {self._email} | Số dư: {self.__credit_balance:,}đ")


c1 = Customer(1, "Nguyễn An",  "an@email.com",   "pass123", 500000)
c2 = Customer(2, "Trần Bình",  "binh@email.com", "pass456")

print(c1)
c1.add_credit(200000)
c1.use_credit(100000)
c1.use_credit(700000)   # không đủ số dư - hiển thị thông báo lỗi

try:
    print(c1.__password)
except AttributeError:
    print("  ✗ Không thể truy cập __password từ bên ngoài class (Encapsulation hoạt động)")

# Bài 3 - Xây dựng class Order và tính tổng tiền
class Order:
    """Đại diện cho một đơn hàng trong hệ thống."""

    def __init__(self, order_id, customer):
        self.order_id   = order_id
        self.customer   = customer
        self.order_date = date.today()
        self.items      = []    # list of Product
        self.quantities = []    # list of int

    def add_item(self, product, quantity):
        """Thêm sản phẩm vào đơn hàng."""
        if quantity <= 0:
            raise ValueError("Số lượng phải lớn hơn 0")
        if not product.is_in_stock():
            print(f"  ✗ '{product.name}' hết hàng, không thể thêm vào đơn!")
            return
        self.items.append(product)
        self.quantities.append(quantity)

    def calculate_total(self):
        """Tính tổng tiền đơn hàng."""
        return sum(p.price * q for p, q in zip(self.items, self.quantities))

    def apply_discount(self, discount_percent):
        """Áp dụng giảm giá toàn bộ đơn hàng."""
        return self.calculate_total() * (1 - discount_percent / 100)

    def __str__(self):
        lines = [f"Đơn [{self.order_id}] KH: {self.customer.name} | Ngày: {self.order_date}"]
        for p, q in zip(self.items, self.quantities):
            lines.append(f"  + {p.name:<15} x{q} = {p.price * q:>10,}đ")
        lines.append(f"  {'Tổng cộng':>20}   {self.calculate_total():>10,}đ")
        return "\n".join(lines)


o1 = Order("ORD-001", c1)
o1.add_item(p1, 2)
o1.add_item(p3, 3)
print(o1)
print(f"  → Sau giảm 10%: {o1.apply_discount(10):,.0f}đ")

o2 = Order("ORD-002", c2)
o2.add_item(p2, 1)   # hết hàng
o2.add_item(p1, 1)
o2.add_item(p3, 5)
print(o2)

# Bài 4 - Kế thừa - class SpecialCustomer từ Customer
class SpecialCustomer(Customer):
    """Khách hàng thành viên VIP với điểm tích lũy và ưu đãi giảm giá."""

    DISCOUNT_RATE = {"Bronze": 5, "Silver": 10, "Gold": 15}

    def __init__(self, customer_id, name, email, password, credit_balance=0):
        super().__init__(customer_id, name, email, password, credit_balance)
        self.loyalty_points = 0
        self.loyalty_level  = "Bronze"

    def add_loyalty_points(self, points):
        """Tích lũy điểm và tự động cập nhật hạng thành viên."""
        self.loyalty_points += points
        if self.loyalty_points >= 1000:
            self.loyalty_level = "Gold"
        elif self.loyalty_points >= 500:
            self.loyalty_level = "Silver"
        print(f"  +{points} điểm → Tổng: {self.loyalty_points} | Hạng: {self.loyalty_level}")

    def get_discount(self):
        """Trả về % giảm giá theo hạng thành viên."""
        return self.DISCOUNT_RATE[self.loyalty_level]

    def __str__(self):
        return (f"SpecialCustomer [{self.customer_id}] {self.name}"
                f" | Hạng: {self.loyalty_level}"
                f" | Điểm: {self.loyalty_points}"
                f" | Ưu đãi: {self.get_discount()}%")


sc1 = SpecialCustomer(3, "Lê Văn C", "c@email.com", "vip789", 1000000)
print(sc1)
sc1.add_loyalty_points(300)   # còn Bronze
sc1.add_loyalty_points(250)   # lên Silver (550 điểm)
sc1.add_loyalty_points(500)   # lên Gold  (1050 điểm)
print(f"  → Mức giảm giá hiện tại: {sc1.get_discount()}%")
sc1.add_credit(300000)
sc1.use_credit(150000)
print(sc1)

# Bài 5 - Polymorphism - Các loại sản phẩm khác nhau
class PhysicalProduct(Product):
    """Sản phẩm vật lý - có phí vận chuyển."""

    def __init__(self, product_id, name, price, quantity, category, weight, shipping_fee):
        super().__init__(product_id, name, price, quantity, category)
        self.weight       = weight        # kg
        self.shipping_fee = shipping_fee  # đồng

    def calculate_final_price(self):
        """Giá cuối = giá gốc + phí vận chuyển."""
        return self.price + self.shipping_fee


class DigitalProduct(Product):
    """Sản phẩm số - phần mềm, khóa học..."""

    def __init__(self, product_id, name, price, quantity, category, file_size, license_type):
        super().__init__(product_id, name, price, quantity, category)
        self.file_size    = file_size     # MB
        self.license_type = license_type  # 'one-time' hoặc 'lifetime'

    def calculate_final_price(self):
        """one-time: giảm 20% | lifetime: giá gốc."""
        if self.license_type == "one-time":
            return self.price * 0.8
        return self.price


class ServiceProduct(Product):
    """Sản phẩm dịch vụ tính theo ngày."""

    def __init__(self, product_id, name, price, quantity, category, duration_days, renewal_fee):
        super().__init__(product_id, name, price, quantity, category)
        self.duration_days = duration_days  # số ngày sử dụng
        self.renewal_fee   = renewal_fee    # phí gia hạn

    def calculate_final_price(self):
        """Tổng giá = (giá/ngày × số ngày) + phí gia hạn."""
        return self.price * self.duration_days + self.renewal_fee


catalog = [
    PhysicalProduct(10, "Laptop Dell",      15000000, 5, "Điện tử",   2.1,  50000),
    PhysicalProduct(11, "Tai nghe Sony",     2000000, 8, "Điện tử",   0.3,  30000),
    DigitalProduct( 12, "Adobe Photoshop",   3000000, 99, "Phần mềm", 2048, "one-time"),
    DigitalProduct( 13, "Microsoft Office",  2500000, 99, "Phần mềm",  512, "lifetime"),
    ServiceProduct( 14, "Bảo hành 1 năm",     5000, 99, "Dịch vụ",   365, 100000),
    ServiceProduct( 15, "Cloud Storage",      3000, 99, "Dịch vụ",    30,   20000),
]

print("=== Giá cuối cùng danh mục sản phẩm ===")
for p in catalog:
    print(f"  {p.name:<22} → {p.calculate_final_price():>12,.0f}đ  ({type(p).__name__})")