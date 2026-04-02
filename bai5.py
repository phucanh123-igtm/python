import numpy as np
import matplotlib.pyplot as plt

print("=" * 70)
print("BÀI 5: MỎ PHỎNG RANDOM WALK")
print("=" * 70)

# =====================================================================
# PHẦN 1: RANDOM WALK MỘT CHIỀU - 100 BƯỚC
# =====================================================================

print("\n" + "-" * 70)
print("PHẦN 1: RANDOM WALK MỘT CHIỀU (100 BƯỚC)")
print("-" * 70)

# Set seed để có kết quả tái lập
np.random.seed(42)

# 1. Tạo 100 bước ngẫu nhiên (+1 hoặc -1)
steps = np.random.choice([-1, 1], size=100)

print("\n1. Tạo 100 bước ngẫu nhiên:")
print(f"   10 bước đầu tiên: {steps[:10]}")
print(f"   (+1 = bước phải, -1 = bước trái)")

# 2. Tính vị trí sau mỗi bước (cumsum = cumulative sum)
walk = np.cumsum(steps)

print("\n2. Vị trí sau mỗi bước:")

# 3. In 10 giá trị đầu tiên của dãy vị trí
print("\n3. 10 vị trí đầu tiên:")
print(f"   {walk[:10]}")

# 5. Thống kê
print("\n4. Thống kê chuyển động:")
final_position = walk[-1]
max_position = np.max(walk)
min_position = np.min(walk)

print(f"   Vị trí cuối cùng: {final_position}")
print(f"   Vị trí cao nhất đạt được: {max_position}")
print(f"   Vị trí thấp nhất đạt được: {min_position}")
print(f"   Quãng đường di chuyển: {max_position - min_position}")

# 4. Vẽ đồ thị random walk
print("\n5. Vẽ biểu đồ Random Walk một chiều...")

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.plot(walk, linewidth=1.5, color='blue', alpha=0.7)
plt.axhline(y=0, color='red', linestyle='--', alpha=0.5, label='Điểm xuất phát')
plt.axhline(y=final_position, color='green', linestyle='--', alpha=0.5, label=f'Vị trí cuối ({final_position})')
plt.title("Random Walk một chiều (100 bước)", fontsize=12, fontweight='bold')
plt.xlabel("Bước")
plt.ylabel("Vị trí")
plt.grid(True, alpha=0.3)
plt.legend()

# Biểu đồ phân bố
plt.subplot(1, 2, 2)
plt.hist(walk, bins=20, color='skyblue', edgecolor='black', alpha=0.7)
plt.axvline(x=np.mean(walk), color='red', linestyle='--', linewidth=2, label=f'Trung bình: {np.mean(walk):.2f}')
plt.title("Phân bố vị trí", fontsize=12, fontweight='bold')
plt.xlabel("Vị trí")
plt.ylabel("Tần số")
plt.legend()
plt.grid(True, alpha=0.3, axis='y')

plt.tight_layout()
plt.savefig('random_walk.png', dpi=100, bbox_inches='tight')
print("   ✓ Đã lưu biểu đồ vào: random_walk.png")
plt.show()

# =====================================================================
# PHẦN 2: MỐ PHỎNG 100 RANDOM WALK
# =====================================================================

print("\n" + "-" * 70)
print("PHẦN 2: MỐ PHỎNG 100 RANDOM WALK (MỖI WALK 100 BƯỚC)")
print("-" * 70)

# Tạo 100 random walk, mỗi walk có 100 bước
np.random.seed(42)
steps_many = np.random.choice([-1, 1], size=(100, 100))

# Tính vị trí cho tất cả walks
walks_many = np.cumsum(steps_many, axis=1)

print("\n1. Mô phỏng 100 random walk:")
print(f"   Ma trận kích thước: {walks_many.shape} (100 walk × 100 bước)")

# Vị trí cuối cùng của từng walk
final_positions = walks_many[:, -1]

print("\n2. Thống kê vị trí cuối cùng:")
print(f"   Trung bình: {np.mean(final_positions):.2f}")
print(f"   Std Dev: {np.std(final_positions):.2f}")
print(f"   Min: {np.min(final_positions)}")
print(f"   Max: {np.max(final_positions)}")

# 3. Đếm số walk kết thúc dương
positive_walks = np.sum(final_positions > 0)
negative_walks = np.sum(final_positions < 0)
zero_walks = np.sum(final_positions == 0)

print("\n3. Số walk kết thúc dương, âm, và bằng 0:")
print(f"   Kết thúc dương (> 0): {positive_walks} walks ({positive_walks/100*100:.1f}%)")
print(f"   Kết thúc âm (< 0): {negative_walks} walks ({negative_walks/100*100:.1f}%)")
print(f"   Kết thúc bằng 0: {zero_walks} walks ({zero_walks/100*100:.1f}%)")

# 4. Đếm số walk chạm ngưỡng ±10
hit_threshold = np.any(np.abs(walks_many) >= 10, axis=1)
num_hit_threshold = np.sum(hit_threshold)

print("\n4. Số walk chạm/vượt ngưỡng |vị trí| ≥ 10:")
print(f"   Walk chạm ±10: {num_hit_threshold} walks ({num_hit_threshold/100*100:.1f}%)")

# Thêm thông tin về bước đầu tiên chạm ngưỡng
first_hit_step = np.zeros(100, dtype=int)
for i in range(100):
    hit_indices = np.where(np.abs(walks_many[i, :]) >= 10)[0]
    if len(hit_indices) > 0:
        first_hit_step[i] = hit_indices[0] + 1  # +1 vì index bắt đầu từ 0

hit_steps = first_hit_step[first_hit_step > 0]
if len(hit_steps) > 0:
    print(f"   Bước trung bình chạm ±10: {np.mean(hit_steps):.1f}")
    print(f"   Bước soonest chạm ±10: {np.min(hit_steps)}")
    print(f"   Bước muộn nhất chạm ±10: {np.max(hit_steps)}")

# 5. Vẽ biểu đồ 100 random walks
print("\n5. Vẽ biểu đồ 100 random walks...")

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Subplot 1: Tất cả 100 walks
ax = axes[0, 0]
for i in range(100):
    ax.plot(walks_many[i, :], alpha=0.15, color='blue')
ax.plot(np.mean(walks_many, axis=0), color='red', linewidth=2.5, label='Trung bình')
ax.set_title("100 Random Walks (mỗi walk 100 bước)", fontsize=12, fontweight='bold')
ax.set_xlabel("Bước")
ax.set_ylabel("Vị trí")
ax.grid(True, alpha=0.3)
ax.legend()

# Subplot 2: Phân bố vị trí cuối cùng
ax = axes[0, 1]
ax.hist(final_positions, bins=20, color='lightgreen', edgecolor='black', alpha=0.7)
ax.axvline(x=0, color='red', linestyle='--', linewidth=2, label='Vị trí 0')
ax.axvline(x=np.mean(final_positions), color='orange', linestyle='--', linewidth=2, label=f'Trung bình: {np.mean(final_positions):.2f}')
ax.set_title("Phân bố vị trí cuối cùng", fontsize=12, fontweight='bold')
ax.set_xlabel("Vị trí cuối cùng")
ax.set_ylabel("Tần số")
ax.legend()
ax.grid(True, alpha=0.3, axis='y')

# Subplot 3: Thống kê vị trí tối đa trong mỗi walk
max_positions = np.max(walks_many, axis=1)
min_positions = np.min(walks_many, axis=1)
ax = axes[1, 0]
ax.hist(max_positions, bins=15, alpha=0.6, label='Vị trí cao nhất', color='red', edgecolor='black')
ax.hist(min_positions, bins=15, alpha=0.6, label='Vị trí thấp nhất', color='blue', edgecolor='black')
ax.set_title("Vị trí cực đại và cực tiểu trong mỗi walk", fontsize=12, fontweight='bold')
ax.set_xlabel("Vị trí")
ax.set_ylabel("Tần số")
ax.legend()
ax.grid(True, alpha=0.3, axis='y')

# Subplot 4: Phân tích khoảng cách
range_distances = max_positions - min_positions
ax = axes[1, 1]
ax.hist(range_distances, bins=15, color='purple', edgecolor='black', alpha=0.7)
ax.axvline(x=np.mean(range_distances), color='red', linestyle='--', linewidth=2, label=f'Trung bình: {np.mean(range_distances):.1f}')
ax.set_title("Khoảng cách (Max - Min) trong mỗi walk", fontsize=12, fontweight='bold')
ax.set_xlabel("Khoảng cách")
ax.set_ylabel("Tần số")
ax.legend()
ax.grid(True, alpha=0.3, axis='y')

plt.tight_layout()
plt.savefig('random_walks_analysis.png', dpi=100, bbox_inches='tight')
print("   ✓ Đã lưu biểu đồ phân tích vào: random_walks_analysis.png")
plt.show()

# =====================================================================
# TÓM TẮT
# =====================================================================

print("\n" + "=" * 70)
print("TÓM TẮT KẾT QUẢ")
print("=" * 70)

print("\n📊 PHẦN 1 (1 Random Walk, 100 bước):")
print(f"   • Vị trí cuối cùng: {walk[-1]}")
print(f"   • Vị trí cao nhất: {np.max(walk)}")
print(f"   • Vị trí thấp nhất: {np.min(walk)}")

print("\n📊 PHẦN 2 (100 Random Walks, mỗi 100 bước):")
print(f"   • Walk kết thúc dương: {positive_walks}/100")
print(f"   • Walk chạm/vượt ±10: {num_hit_threshold}/100")
print(f"   • Vị trí cuối bình quân: {np.mean(final_positions):.2f}")

print("\n💡 Ý NGHĨA:")
print("   Random walk được ứng dụng trong:")
print("   - Vật lý: Chuyển động Brown của hạt")
print("   - Tài chính: Mô hình biến động giá cổ phiếu")
print("   - Sinh học: Lan truyền dịch bệnh")
print("   - IT: Thuật toán tìm kiếm, phân tán")

print("\n" + "=" * 70)
