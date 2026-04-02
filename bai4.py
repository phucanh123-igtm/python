import numpy as np

print("=" * 70)
print("BÀI 4: ĐẠI SỐ TUYẾN TÍNH CƠ BẢN VỚI NUMPY")
print("=" * 70)

# Dữ liệu đầu vào
A = np.array([
    [2, 1],
    [1, 3]
])

B = np.array([
    [4, 2],
    [1, 5]
])

print("\n" + "-" * 70)
print("DỮ LIỆU ĐẦU VÀO")
print("-" * 70)

print("\nMa trận A:")
print(A)

print("\nMa trận B:")
print(B)

# 1. Tính A + B
print("\n" + "-" * 70)
print("1. PHÉP CỘNG MA TRẬN: A + B")
print("-" * 70)

sum_AB = A + B
print(f"\nA + B =")
print(sum_AB)

# 2. Tính A - B
print("\n" + "-" * 70)
print("2. PHÉP TRỪ MA TRẬN: A - B")
print("-" * 70)

diff_AB = A - B
print(f"\nA - B =")
print(diff_AB)

# 3. Tính tích ma trận A @ B
print("\n" + "-" * 70)
print("3. TÍCH MA TRẬN: A @ B")
print("-" * 70)

product_AB = A @ B
print(f"\nA @ B =")
print(product_AB)

print("\nGiải thích:")
print("  [2*4 + 1*1, 2*2 + 1*5]   [9,  9]")
print("  [1*4 + 3*1, 1*2 + 3*5] = [7, 17]")

# 4. Tính định thức của ma trận A
print("\n" + "-" * 70)
print("4. ĐỊNH THỨC CỦA MA TRẬN A")
print("-" * 70)

det_A = np.linalg.det(A)
print(f"\ndet(A) = {det_A:.4f}")
print(f"Giải thích: det(A) = 2*3 - 1*1 = 6 - 1 = {det_A:.0f}")

# 5. Tính ma trận nghịch đảo của A
print("\n" + "-" * 70)
print("5. MA TRẬN NGHỊCH ĐẢO CỦA A")
print("-" * 70)

if abs(det_A) < 1e-10:
    print("⚠️  Ma trận A không khả nghịch vì det(A) = 0")
    print("    (Khi đó, các dòng/cột của ma trận phụ thuộc tuyến tính)")
else:
    inv_A = np.linalg.inv(A)
    print(f"\nA^(-1) =")
    print(np.round(inv_A, 4))
    
    print(f"\nGiải thích: A^(-1) = (1/det(A)) * adj(A)")
    print(f"           = (1/5) * [[3, -1], [-1, 2]]")
    
    # Kiểm tra: A @ A^(-1) = I
    identity = A @ inv_A
    print(f"\nKiểm tra: A @ A^(-1) =")
    print(np.round(identity, 4))
    print("(Ma trận đơn vị I ✓)")

# 6. Giải hệ phương trình
print("\n" + "-" * 70)
print("6. GIẢI HỆ PHƯƠNG TRÌNH TUYẾN TÍNH")
print("-" * 70)

print("\nHệ phương trình:")
print("  2x + y = 5")
print("  x + 3y = 7")

print("\nDạng ma trận: A @ x = b, với:")
print("  A = [[2, 1],")
print("       [1, 3]]")
print("  b = [5, 7]")

b = np.array([5, 7])
solution = np.linalg.solve(A, b)

print(f"\nNghiệm hệ phương trình:")
print(f"  x = {solution[0]:.4f}")
print(f"  y = {solution[1]:.4f}")

# Mở rộng: Kiểm tra lại nghiệm
print("\n" + "-" * 70)
print("PHẦN MỞ RỘNG: KIỂM TRA LẠI NGHIỆM")
print("-" * 70)

check = A @ solution
print(f"\nThay vào hệ phương trình:")
print(f"  A @ [x, y] = [{check[0]:.4f}, {check[1]:.4f}]")
print(f"  b = {b}")

if np.allclose(check, b):
    print("\n✓ Nghiệm chính xác! (A @ solution ≈ b)")
else:
    print("\n✗ Có lỗi trong tính toán")

# Kiểm tra: thay x, y vào phương trình gốc
print(f"\nKiểm tra chi tiết:")
eq1_result = 2 * solution[0] + solution[1]
eq2_result = solution[0] + 3 * solution[1]
print(f"  Phương trình 1: 2*{solution[0]:.4f} + {solution[1]:.4f} = {eq1_result:.4f} (cần = 5)")
print(f"  Phương trình 2: {solution[0]:.4f} + 3*{solution[1]:.4f} = {eq2_result:.4f} (cần = 7)")

# Giải thích khi nào ma trận không khả nghịch
print("\n" + "-" * 70)
print("KHI NÀO MA TRẬN KHÔNG KHẢ NGHỊCH?")
print("-" * 70)

print("\nMa trận vuông A không khả nghịch khi:")
print("  1. det(A) = 0 (định thức bằng 0)")
print("  2. Các dòng (hoặc cột) của A phụ thuộc tuyến tính")
print("  3. Ma trận có hạng (rank) nhỏ hơn số chiều")
print("\nVí dụ ma trận không khả nghịch:")
singular_matrix = np.array([[1, 2], [2, 4]])
print(f"\n  C = {singular_matrix.tolist()}")
print(f"  det(C) = {np.linalg.det(singular_matrix):.4f}")
print("  → Dòng 2 = 2 × Dòng 1 (phụ thuộc tuyến tính)")
print("  → C không khả nghịch")

print("\n" + "=" * 70)