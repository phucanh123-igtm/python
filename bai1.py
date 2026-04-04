import pandas as pd

print("=" * 70)
print("BÀI 1: LÀM QUEN VỚI SERIES")
print("=" * 70)

# Tạo Series lưu điểm của 5 sinh viên với chỉ mục mã sinh viên
diem = pd.Series(
    [7.5, 8.0, 6.5, 9.0, 8.5],
    index=["SV01", "SV02", "SV03", "SV04", "SV05"],
    name="Diem"
)

print("\nDanh sách điểm:")
print(diem)

print("\nHai phần tử đầu:")
print(diem.head(2))

print("\nĐiểm lớn nhất:", diem.max())
print("Điểm trung bình:", diem.mean())

print("\nSinh viên có điểm >= 8:")
print(diem[diem >= 8])

print("\n" + "=" * 70)
