# Bài 1 - BrowserHistory [STACK]
class BrowserHistory:
    def __init__(self, homepage):
        self.back_stack = [homepage]
        self.forward_stack = []

    def visit(self, url):
        self.back_stack.append(url)
        self.forward_stack = []

    def back(self, steps):
        for _ in range(steps):
            if len(self.back_stack) > 1:
                self.forward_stack.append(self.back_stack.pop())
        return self.back_stack[-1]

    def forward(self, steps):
        for _ in range(steps):
            if self.forward_stack:
                self.back_stack.append(self.forward_stack.pop())
        return self.back_stack[-1]

h = BrowserHistory("trang-chu")
h.visit("san-pham/ao-thun")
h.visit("san-pham/quan-jean")
h.visit("gio-hang")
print(h.back(1))
print(h.back(1))
print(h.forward(1))
print(h.back(3))

# Bài 2 - Kiểm tra ngoặc hợp lệ [STACK]
def is_valid_brackets(s):
    stack = []
    mapping = {')': '(', ']': '[', '}': '{'}
    for char in s:
        if char in '({[':
            stack.append(char)
        elif char in ')}]':
            if not stack or stack[-1] != mapping[char]:
                return False
            stack.pop()
    return len(stack) == 0

print(is_valid_brackets('{"name": "An", "items": [1, 2]}'))
print(is_valid_brackets('{"data": [{"id": 1}'))
print(is_valid_brackets('(())'))
print(is_valid_brackets('{"data": [{"id": 1]}'))

# Bài 3 - Validate transaction order [STACK]
def validate_transaction_order(events):
    states = {}
    errors = []
    completed_count = 0

    VALID_TRANSITIONS = {
        None:          "INIT",
        "INIT":        "PROCESSING",
        "PROCESSING":  ["COMPLETED", "FAILED"]
    }

    for e in events:
        txn     = e["txn_id"]
        event   = e["event"]
        current = states.get(txn)
        expected = VALID_TRANSITIONS.get(current)

        if isinstance(expected, list):
            valid = event in expected
        else:
            valid = event == expected

        if not valid:
            errors.append(f"{txn}: thieu buoc PROCESSING")
        else:
            states[txn] = event
            if event in ("COMPLETED", "FAILED"):
                completed_count += 1

    return {"valid": len(errors) == 0, "completed": completed_count, "errors": errors}

events1 = [
    {"txn_id": "T1", "event": "INIT"},
    {"txn_id": "T2", "event": "INIT"},
    {"txn_id": "T2", "event": "PROCESSING"},
    {"txn_id": "T2", "event": "COMPLETED"},
    {"txn_id": "T1", "event": "PROCESSING"},
    {"txn_id": "T1", "event": "FAILED"},
]
events2 = [
    {"txn_id": "T3", "event": "INIT"},
    {"txn_id": "T3", "event": "COMPLETED"},
]
print(validate_transaction_order(events1))
print(validate_transaction_order(events2))

# Bài 4 - Hàng đợi ưu tiên giao hàng [QUEUE]
import heapq

class PriorityShippingQueue:
    PRIORITY = {"express": 1, "vip": 2, "normal": 3}

    def __init__(self):
        self.heap    = []
        self.counter = 0

    def enqueue(self, order):
        priority = self.PRIORITY[order["type"]]
        heapq.heappush(self.heap, (priority, self.counter, order))
        self.counter += 1

    def dequeue(self):
        if self.heap:
            _, _, order = heapq.heappop(self.heap)
            return order

psq = PriorityShippingQueue()
psq.enqueue({"id": "S1", "type": "normal",  "dest": "HN"})
psq.enqueue({"id": "S2", "type": "express", "dest": "HCM"})
psq.enqueue({"id": "S3", "type": "vip",     "dest": "DN"})
psq.enqueue({"id": "S4", "type": "express", "dest": "HN"})
print(psq.dequeue())
print(psq.dequeue())
print(psq.dequeue())

# Bài 5 - Mô phỏng hàng chờ thanh toán [QUEUE]
def simulate_checkout(customers, n_counters):
    counters = [(0, i, [], 0) for i in range(n_counters)]
    heapq.heapify(counters)

    for customer in customers:
        total, idx, cust_list, total_items = heapq.heappop(counters)
        cust_list.append(customer["id"])
        total_items += customer["items"]
        heapq.heappush(counters, (total + 1, idx, cust_list, total_items))

    result = {}
    for total, idx, cust_list, total_items in sorted(counters, key=lambda x: x[1]):
        result[f"counter_{idx + 1}"] = {
            "customers":   cust_list,
            "total_items": total_items
        }
    return result

customers = [
    {"id": "C1", "items": 5},
    {"id": "C2", "items": 12},
    {"id": "C3", "items": 3},
    {"id": "C4", "items": 8},
    {"id": "C5", "items": 1},
]
print(simulate_checkout(customers, n_counters=2))


# LÝ THUYẾT BÀI 4
# Câu 6: Graph và Tree khác nhau như thế nào?
# Tree = Graph đặc biệt có kỷ luật. Graph = tự do, k ràng buộc.

# VD Tree như sơ đồ tổ chức công ty: có 1 CEO (gốc), mỗi người chỉ có
# đúng 1 sếp trực tiếp, k có chuyện 2 người cùng báo cáo lẫn nhau, k
# có vòng lặp. Quan hệ 1 chiều từ trên xuống.

# VD Graph như bản đồ giao thông: từ điểm A có thể đến B bằng nhiều
# đường, có thể quay vòng, k cần có điểm xuất phát cố định.

# Khác biệt chính:
# - Tree: có gốc (root), k có chu trình, mỗi node chỉ có 1 cha
# - Graph: k cần gốc, có thể có chu trình, node có thể kết nối tùy ý

# Khi nào dùng Tree:
# - Dữ liệu có quan hệ phân cấp rõ ràng
# - VD: cây danh mục sản phẩm (Thời trang → Áo → Áo thun),
#   cấu trúc thư mục file, cây quyết định trong AI

# Khi nào dùng Graph:
# - Quan hệ phức tạp, nhiều chiều, có thể có chu trình
# - VD: gợi ý sản phẩm (sản phẩm A liên quan B liên quan C),
#   bản đồ kho vận, mạng xã hội người dùng

# ---

# Câu 7: So sánh DFS và BFS

# DFS = đi sâu hết 1 nhánh rồi mới quay lại. BFS = khám phá hết tầng
# gần rồi mới đi xa hơn.

# VD DFS như người tìm chìa khóa trong nhà: vào phòng ngủ, lục hết ngăn
# kéo 1, ngăn kéo 2, tủ, gầm giường... xong mới sang phòng khách. Đi
# sâu đến cùng trước khi chuyển chỗ.

# VD BFS như vết dầu loang: lan từ tâm ra ngoài theo từng vòng tròn đều
# nhau. Hết vòng gần mới đến vòng xa hơn.

# So sánh:
# - DFS dùng Stack (LIFO), BFS dùng Queue (FIFO)
# - DFS tốn ít RAM hơn, BFS tốn nhiều RAM hơn (phải lưu cả tầng)
# - BFS luôn tìm được đường đi ngắn nhất, DFS thì k đảm bảo

# VD trong hệ thống TMĐT:

# Dùng DFS: duyệt cây danh mục sản phẩm để lấy toàn bộ sản phẩm con
# của 1 danh mục. VD: "Thời trang" → "Áo" → "Áo thun" → "Áo polo"...
# cần đi hết 1 nhánh danh mục trước khi sang nhánh khác.

# Dùng BFS: tìm sản phẩm gợi ý gần nhất với sản phẩm đang xem. VD:
# đang xem iPhone → tầng 1 gợi ý ốp lưng/cáp sạc (liên quan trực
# tiếp) → tầng 2 mới gợi ý tai nghe/pin dự phòng. Ưu tiên thứ liên
# quan gần trước.

# ---

# Câu 8: Binary Search Tree (BST) - Tìm kiếm và Insert

# BST = cây nhị phân có quy tắc: trái luôn nhỏ hơn, phải luôn lớn hơn
# node hiện tại.

# VD như trò chơi đoán số: "Nghĩ số từ 1-100, mỗi lần đoán mình nói
# cao hơn hay thấp hơn." Mỗi lần đoán loại đi được một nửa → rất nhanh.
# BST hoạt động y vậy.

# Với cây trong đề bài (root = 1, trái = 2, phải = 3...):

# INSERT giá trị 12:
# - So với node 1: 12 > 1 → đi phải đến node 3
# - So với node 3: 12 > 3 → đi phải đến node 7
# - Node 7 chưa có con phải → chèn 12 vào đây

# SEARCH giá trị 10:
# - So với node 1: 10 > 1 → đi phải đến node 3
# - So với node 3: 10 > 3 → đi phải đến node 7
# - So với node 7: 10 > 7 → đi phải → k có node nào → return None

# Tại sao BST nhanh? Vì mỗi bước loại được một nửa số node còn lại.
# 1000 node chỉ cần tối đa ~10 bước (log2(1000) ≈ 10). So với list
# thông thường phải duyệt từng phần tử một, BST nhanh hơn rất nhiều.

# ---

# Câu 9: Adjacency List vs Adjacency Matrix

# Matrix = bảng ô vuông. List = mỗi node chỉ lưu những ai kết nối với nó.

# VD Matrix như bảng điểm danh cả lớp 40 người: dù chỉ có 5 cặp bạn
# thân, vẫn phải kẻ bảng 40x40 = 1600 ô, phần lớn là số 0 vô dụng.

# VD Adjacency List như danh bạ điện thoại: mỗi người chỉ lưu số của
# những người họ quen. Không quen thì k lưu, k tốn chỗ.

# Bài toán 10,000 kho, mỗi kho kết nối trung bình 5 kho khác:

# Matrix cần: 10,000 x 10,000 = 100,000,000 ô nhớ
# List cần  : 10,000 x 5      =      50,000 kết nối thực tế

# Đây là sparse graph (đồ thị thưa) vì số cạnh thực tế (50,000) rất
# nhỏ so với số cạnh tối đa có thể (100 triệu). Dùng Matrix là lãng
# phí RAM kinh khủng, 99.95% ô đều là số 0.

# → Chọn Adjacency List.

# Khi nào dùng Matrix? Khi graph dày - gần như mọi node đều kết nối
# với nhau. VD: bảng so sánh giá vận chuyển giữa 10 kho lớn (10x10=100
# ô, tất cả đều có nghĩa).

# ---

# Câu 10: Kiểm tra chu trình trong Graph (Cycle Detection)

# Chu trình = đường đi khép kín, đi mãi lại quay về điểm xuất phát.

# VD như mê cung: nếu đi theo 1 lối mà quay lại chỗ cũ khi chưa ra
# được → có chu trình. Nếu k có chu trình thì cứ đi thẳng sẽ đến đích
# hoặc ngõ cụt.

# Dùng DFS để phát hiện, nhưng cần lưu thêm 2 tập hợp:
# - visited    : tất cả các node đã thăm (dù xong hay chưa)
# - rec_stack  : các node đang trên đường đi HIỆN TẠI (chưa backtrack)

# Logic: nếu DFS đang đi và gặp lại 1 node đang có trong rec_stack
# → có chu trình. Vì mình đang đi tới mà gặp lại chỗ mình chưa rời
# khỏi = đang đi vòng.

#     def has_cycle(graph):
#         visited   = set()
#         rec_stack = set()

#         def dfs(node):
#             visited.add(node)
#             rec_stack.add(node)
#             for neighbor in graph.get(node, []):
#                 if neighbor not in visited:
#                     if dfs(neighbor): return True
#                 elif neighbor in rec_stack:  # gặp lại node đang đi → cycle
#                     return True
#             rec_stack.remove(node)           # xong node này, bỏ khỏi stack
#             return False

#         for node in graph:
#             if node not in visited:
#                 if dfs(node): return True
#         return False

# Tại sao cần 2 tập thay vì 1? Vì visited một mình k đủ: node có thể
# đã được thăm ở nhánh khác (k phải chu trình), chỉ khi node đang nằm
# trong đường đi hiện tại (rec_stack) mà gặp lại thì mới là chu trình.