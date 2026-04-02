import numpy as np

print("=" * 70)
print("BÀI 3: PHÂN TÍCH DOANH THU BẰNG PHÉP TOÁN MA TRẬN")
print("=" * 70)

# Dữ liệu đầu vào
quantity = np.array([
    [10, 12, 9, 14],
    [5, 7, 8, 6],
    [20, 18, 25, 22]
])

price = np.array([15000, 25000, 10000])

print("\n" + "-" * 70)
print("DỮ LIỆU ĐẦU VÀO")
print("-" * 70)

print("\nSố lượng bán theo sản phẩm và ngày (3 sản phẩm x 4 ngày):")
print(quantity)

print("\nGiá của từng sản phẩm (VNĐ):")
print(price)

# 1. Tính doanh thu của từng sản phẩm theo từng ngày
print("\n" + "-" * 70)
print("1. DOANH THU CỦA TỪNG SẢN PHẨM THEO TỪNG NGÀY")
print("-" * 70)

# Reshape price để phù hợp với broadcasting: (3, 1)
revenue = quantity * price.reshape(3, 1)
print("\nDoanh thu (VNĐ):")
print(revenue)
print("\nGiải thích:")
print("  - Dòng 1 (SP1): Số lượng × 15.000")
print("  - Dòng 2 (SP2): Số lượng × 25.000")
print("  - Dòng 3 (SP3): Số lượng × 10.000")

# 2. Tính tổng doanh thu của từng sản phẩm
print("\n" + "-" * 70)
print("2. TỔNG DOANH THU CỦA TỪNG SẢN PHẨM")
print("-" * 70)

sum_product = np.sum(revenue, axis=1)
print("\nTổng doanh thu từng sản phẩm (VNĐ):")
for i, revenue_total in enumerate(sum_product, 1):
    print(f"  Sản phẩm {i}: {revenue_total:,.0f}")

# 3. Tính tổng doanh thu của từng ngày
print("\n" + "-" * 70)
print("3. TỔNG DOANH THU CỦA TỪNG NGÀY")
print("-" * 70)

sum_day = np.sum(revenue, axis=0)
print("\nTổng doanh thu từng ngày (VNĐ):")
for i, revenue_daily in enumerate(sum_day, 1):
    print(f"  Ngày {i}: {revenue_daily:,.0f}")

# 4. Tìm ngày có doanh thu cao nhất
print("\n" + "-" * 70)
print("4. NGÀY CÓ DOANH THU CAO NHẤT")
print("-" * 70)

best_day = np.argmax(sum_day) + 1
max_revenue_day = np.max(sum_day)
print(f"\nNgày {best_day} có doanh thu cao nhất: {max_revenue_day:,.0f} VNĐ")

# 5. Tính tỷ trọng doanh thu của từng sản phẩm
print("\n" + "-" * 70)
print("5. TỶ TRỌNG DOANH THU CỦA TỪNG SẢN PHẨM")
print("-" * 70)

total_revenue = np.sum(sum_product)
ratio = sum_product / total_revenue

print(f"\nTổng doanh thu toàn cửa hàng: {total_revenue:,.0f} VNĐ")
print("\nTỷ trọng doanh thu từng sản phẩm:")
for i, (r, pct) in enumerate(zip(ratio, ratio * 100), 1):
    print(f"  Sản phẩm {i}: {pct:.2f}%")

print(f"\nTỷ trọng (dạng array):")
print(f"  {np.round(ratio * 100, 2)}%")

# Thêm biểu đồ chi tiết
print("\n" + "-" * 70)
print("6. BẢNG TÓM TẮT DOANH THU CHI TIẾT")
print("-" * 70)

print("\nDoanh thu từng sản phẩm theo từng ngày (VNĐ):")
print(f"{'SP':>6} | {'Ngày 1':>12} | {'Ngày 2':>12} | {'Ngày 3':>12} | {'Ngày 4':>12} | {'Tổng':>15}")
print("-" * 90)
for i in range(3):
    print(f"  SP{i+1}  | {revenue[i,0]:>12,.0f} | {revenue[i,1]:>12,.0f} | {revenue[i,2]:>12,.0f} | {revenue[i,3]:>12,.0f} | {sum_product[i]:>15,.0f}")

print("-" * 90)
print(f"{'Tổng':>6} | {sum_day[0]:>12,.0f} | {sum_day[1]:>12,.0f} | {sum_day[2]:>12,.0f} | {sum_day[3]:>12,.0f} | {total_revenue:>15,.0f}")

print("\n" + "=" * 70)
