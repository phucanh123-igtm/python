import pandas as pd

print("=" * 70)
print("BÀI 3: ĐỌC FILE CSV VÀ KHÁM PHÁ DỮ LIỆU")
print("=" * 70)

df = pd.read_csv("diem_sinhvien.csv")

print("\n5 dòng đầu:")
print(df.head())

print("\n5 dòng cuối:")
print(df.tail())

print("\nThông tin dữ liệu:")
print(df.info())

print("\nThống kê mô tả:")
print(df.describe(include="all"))

print("\nKích thước dữ liệu:", df.shape)
print("Tên các cột:", df.columns.tolist())

print("\n" + "=" * 70)
