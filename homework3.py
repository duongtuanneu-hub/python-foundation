# Bài 1
def filter_available(products):
    result = []
    for p in products:
        if p["stock"] > 0 and p["is_active"] == True:
            result.append(p)
    return result

products = [
    {"id": 1, "name": "Áo thun",     "stock": 10, "is_active": True},
    {"id": 2, "name": "Quần jean",   "stock": 0,  "is_active": True},
    {"id": 3, "name": "Giày sneaker","stock": 5,  "is_active": False},
    {"id": 4, "name": "Nón baseball","stock": 3,  "is_active": True},
]
print(filter_available(products))

# Bài 2
def cart_total(cart, discount=10):
    total = 0
    for item in cart:
        total = total + item["price"] * item["quantity"]
    total = total * (1 - discount / 100)
    return total

cart = [
    {"name": "Áo thun", "price": 120000, "quantity": 2},
    {"name": "Quần dài", "price": 350000, "quantity": 1},
    {"name": "Tất",      "price": 25000,  "quantity": 3},
]
print(cart_total(cart, discount=10))

# Bài 3
def related_products(product_id, products, limit=3):
    # Tìm category của sản phẩm hiện tại
    current_category = None
    for p in products:
        if p["id"] == product_id:
            current_category = p["category"]
            break

    # Lọc sản phẩm cùng category, bỏ sản phẩm hiện tại
    related = []
    for p in products:
        if p["category"] == current_category and p["id"] != product_id:
            related.append(p)

    # Sắp xếp theo rating giảm dần
    related.sort(key=lambda x: x["rating"], reverse=True)

    return related[:limit]

products = [
    {"id": 1, "name": "Áo polo",  "category": "ao", "rating": 4.5},
    {"id": 2, "name": "Áo thun",  "category": "ao", "rating": 4.8},
    {"id": 3, "name": "Áo khoác", "category": "ao", "rating": 4.2},
    {"id": 4, "name": "Quần jeans","category": "quan","rating": 4.7},
    {"id": 5, "name": "Áo sơ mi", "category": "ao", "rating": 4.6},
]
print(related_products(product_id=1, products=products, limit=3))

# Bài 4
def detect_anomalies(orders, threshold=2.5):
    # Tính trung bình
    total = 0
    for order in orders:
        total = total + order["total"]
    avg = total / len(orders)

    # Lọc đơn vượt ngưỡng
    result = []
    for order in orders:
        if order["total"] > threshold * avg:
            result.append(order)
    return result

orders = [
    {"id": 101, "total": 250000},
    {"id": 102, "total": 180000},
    {"id": 103, "total": 920000},
    {"id": 104, "total": 210000},
    {"id": 105, "total": 195000},
]
print(detect_anomalies(orders, threshold=2.5))

# Bài 5
def top_selling(items, top_n=2):
    summary = {}  # dict tạm để gom dữ liệu

    for item in items:
        pid = item["product_id"]
        if pid not in summary:
            summary[pid] = {
                "product_id": pid,
                "name": item["name"],
                "total_qty": 0,
                "revenue": 0
            }
        summary[pid]["total_qty"] += item["qty"]
        summary[pid]["revenue"] += item["qty"] * item["price"]

    # Chuyển dict thành list để sort
    result = list(summary.values())
    result.sort(key=lambda x: x["total_qty"], reverse=True)
    return result[:top_n]

items = [
    {"product_id": 1, "name": "Áo thun",   "qty": 5, "price": 120000},
    {"product_id": 2, "name": "Quần jean",  "qty": 3, "price": 350000},
    {"product_id": 1, "name": "Áo thun",   "qty": 8, "price": 120000},
    {"product_id": 3, "name": "Giày",       "qty": 2, "price": 450000},
    {"product_id": 2, "name": "Quần jean",  "qty": 4, "price": 350000},
]
print(top_selling(items, top_n=2))

# Bài 6
def build_catalog(products):
    catalog = {}
    for p in products:
        catalog[p["id"]] = p
    return catalog

products = [
    {"id": "SP001", "name": "Áo thun basic", "price": 120000, "category": "ao"},
    {"id": "SP002", "name": "Quần jogger",   "price": 280000, "category": "quan"},
    {"id": "SP003", "name": "Nón bucket",    "price": 95000,  "category": "phu_kien"},
]
print(build_catalog(products))

# Bài 7
def count_by_status(statuses):
    result = {}
    for status in statuses:
        if status not in result:
            result[status] = 0
        result[status] += 1
    return result

statuses = ["confirmed","pending","shipped","confirmed","delivered",
            "pending","cancelled","confirmed","shipped","delivered"]
print(count_by_status(statuses))

# Bài 8
def apply_coupon(cart_total, code, coupon_db):
    if code not in coupon_db:
        return {"valid": False, "message": "Mã không tồn tại"}

    coupon = coupon_db[code]

    if cart_total < coupon["min_order"]:
        return {"valid": False, "message": "Đơn hàng chưa đủ điều kiện"}

    if coupon["type"] == "percent":
        discount_amount = cart_total * coupon["value"] / 100
    else:  # fixed
        discount_amount = coupon["value"]

    final_price = cart_total - discount_amount

    return {
        "valid": True,
        "discount_amount": discount_amount,
        "final_price": final_price,
        "message": f"Áp dụng thành công {code} (-{coupon['value']}%)"
    }

coupon_db = {
    "SALE20": {"type": "percent", "value": 20, "min_order": 200000},
    "SHIP50K": {"type": "fixed",  "value": 50000, "min_order": 150000},
    "VIP30":  {"type": "percent", "value": 30, "min_order": 500000},
}
print(apply_coupon(350000, "SALE20", coupon_db))

# Bài 9
def daily_report(transactions):
    report = {}
    for t in transactions:
        date = t["date"]
        if date not in report:
            report[date] = {"total": 0, "count": 0}
        report[date]["total"] += t["amount"]
        report[date]["count"] += 1

    # Tính avg
    for date in report:
        report[date]["avg"] = report[date]["total"] / report[date]["count"]

    return report

transactions = [
    {"date": "2024-01-15", "amount": 320000},
    {"date": "2024-01-15", "amount": 185000},
    {"date": "2024-01-16", "amount": 450000},
    {"date": "2024-01-15", "amount": 270000},
    {"date": "2024-01-16", "amount": 390000},
]
print(daily_report(transactions))

# Bài 10
import time  # thư viện lấy thời gian hiện tại

class SessionStore:
    def __init__(self, timeout=1800):
        self.timeout = timeout
        self.sessions = {}

    def create(self, user_id, data):
        now = int(time.time())
        self.sessions[user_id] = {
            "user_id": user_id,
            "data": data,
            "created_at": now,
            "expires_at": now + self.timeout
        }

    def get(self, user_id):
        if user_id not in self.sessions:
            return None
        session = self.sessions[user_id]
        if int(time.time()) > session["expires_at"]:
            return None  # hết hạn
        return session

    def delete(self, user_id):
        if user_id in self.sessions:
            del self.sessions[user_id]

store = SessionStore(timeout=1800)
store.create("user_123", {"name": "An", "role": "customer"})
print(store.get("user_123"))
store.delete("user_123")
print(store.get("user_123"))

# Bài 11
def can_access(role, resource, action, rbac):
    if role not in rbac:
        return False
    if resource not in rbac[role]:
        return False
    return action in rbac[role][resource]

rbac = {
    "admin":    {"products": ["read","create","update","delete"], "orders": ["read","update","delete"]},
    "seller":   {"products": ["read","create","update"], "orders": ["read"]},
    "customer": {"orders": ["read","create"]},
}
print(can_access("seller",   "products", "delete", rbac))  # False
print(can_access("admin",    "orders",   "delete", rbac))  # True
print(can_access("customer", "products", "read",   rbac))  # False

# Bài 12
def calc_shipping(city, weight_kg, order_total, zones):
    zone = zones.get(city, zones["other"])

    if order_total >= zone["free_threshold"]:
        return {"fee": 0, "free_shipping": True, "message": f"Miễn phí ship đến {city}"}

    fee = zone["zone_rate"] * weight_kg
    fee = max(fee, zone["min_fee"])  # không thấp hơn phí tối thiểu

    return {
        "fee": fee,
        "free_shipping": False,
        "message": f"Phí ship đến {city}: {int(fee):,}đ"
    }

shipping_zones = {
    "HN":    {"zone_rate": 15000, "free_threshold": 300000, "min_fee": 15000},
    "HCM":   {"zone_rate": 15000, "free_threshold": 300000, "min_fee": 15000},
    "DN":    {"zone_rate": 20000, "free_threshold": 350000, "min_fee": 20000},
    "other": {"zone_rate": 30000, "free_threshold": 500000, "min_fee": 30000},
}
print(calc_shipping("DN", 1.5, 200000, shipping_zones))

# Bài 13
def is_wishlisted(product_id, wishlist):
    return product_id in wishlist

wishlist = {"SP001", "SP005", "SP012", "SP018", "SP024"}
print(is_wishlisted("SP005", wishlist))  # True
print(is_wishlisted("SP999", wishlist))  # False

# Bài 14
def get_unviewed(all_products, viewed_products):
    return all_products - viewed_products

all_products = {"SP001","SP002","SP003","SP004","SP005","SP006"}
viewed_products = {"SP001","SP003","SP005"}
print(get_unviewed(all_products, viewed_products))

# Bài 15
def unique_categories(products):
    categories = set()
    for p in products:
        categories.add(p["category"])
    return categories

products = [
    {"name": "Áo thun",  "category": "ao"},
    {"name": "Quần jean","category": "quan"},
    {"name": "Áo khoác", "category": "ao"},
    {"name": "Giày",     "category": "giay"},
    {"name": "Áo polo",  "category": "ao"},
]
print(unique_categories(products))

# Bài 16
def cross_sell(product_id, order_history, current_cart):
    co_purchased = set()
    for order in order_history:
        if product_id in order["items"]:
            for item in order["items"]:
                if item != product_id:
                    co_purchased.add(item)
    return co_purchased - current_cart

order_history = [
    {"items": ["SP001","SP002","SP005"]},
    {"items": ["SP001","SP003"]},
    {"items": ["SP001","SP002","SP004"]},
    {"items": ["SP006","SP002"]},
]
current_cart = {"SP001", "SP003"}
print(cross_sell("SP001", order_history, current_cart))

# Bài 17
def sale_diff(old_sale, new_sale):
    return {
        "removed": old_sale - new_sale,
        "added":   new_sale - old_sale,
        "kept":    old_sale & new_sale
    }

old_sale = {"SP001","SP002","SP003","SP004","SP005"}
new_sale = {"SP002","SP004","SP005","SP006","SP007"}
print(sale_diff(old_sale, new_sale))

# Bài 18
def filter_verified_reviews(reviews, verified_buyers):
    result = []
    for review in reviews:
        if review["user_id"] in verified_buyers:
            result.append(review)
    return result

verified_buyers = {"U001", "U003", "U005", "U007"}
reviews = [
    {"user_id": "U001", "rating": 5, "comment": "Rất tốt!"},
    {"user_id": "U002", "rating": 1, "comment": "Kém chất lượng"},
    {"user_id": "U003", "rating": 4, "comment": "Ưng ý"},
    {"user_id": "U004", "rating": 5, "comment": "Tuyệt vời"},
]
print(filter_verified_reviews(reviews, verified_buyers))

# Bài 19
def segment_users(order_counts):
    result = {"one_time": set(), "repeat": set(), "vip": set()}
    for user_id, count in order_counts.items():
        if count == 1:
            result["one_time"].add(user_id)
        elif count <= 4:
            result["repeat"].add(user_id)
        else:
            result["vip"].add(user_id)
    return result

order_counts = {
    "U001": 1, "U002": 7, "U003": 3, "U004": 1,
    "U005": 5, "U006": 2, "U007": 9, "U008": 4,
}
print(segment_users(order_counts))

# Bài 20
def check_conflicts(flash_sale_items, active_campaigns):
    conflicts = {}
    for campaign_name, items in active_campaigns.items():
        overlap = flash_sale_items & items  # giao nhau
        for item in overlap:
            if item not in conflicts:
                conflicts[item] = []
            conflicts[item].append(campaign_name)

    safe_items = flash_sale_items - set(conflicts.keys())

    return {
        "has_conflict": len(conflicts) > 0,
        "conflicts": conflicts,
        "safe_items": safe_items
    }

active_campaigns = {
    "clearance":  {"SP001","SP005","SP009"},
    "bundle_deal":{"SP003","SP007","SP011"},
    "new_arrival":{"SP013","SP015"},
}
flash_sale_items = {"SP001","SP003","SP007","SP020","SP025"}
print(check_conflicts(flash_sale_items, active_campaigns))