# Bài 2. Thống kê dữ liệu bằng dict và set

du_lieu = ["Python", "CSDL", "Python", "Java", "CSDL", "AI", "Python"]

# Loại bỏ phần tử trùng lặp bằng set
mon_hoc_unique = set(du_lieu)
print("Môn học duy nhất:", mon_hoc_unique)

# Đếm số lần xuất hiện của từng môn học bằng dict
dem = {}
for mon in du_lieu:
    dem[mon] = dem.get(mon, 0) + 1
print("Số lần xuất hiện:", dem)

# In ra môn học được đăng ký nhiều nhất
max_mon = max(dem, key=dem.get)
print(f"Môn học được đăng ký nhiều nhất: {max_mon} với {dem[max_mon]} lần")

# Sắp xếp kết quả đếm theo số lần giảm dần
sorted_dem = sorted(dem.items(), key=lambda x: x[1], reverse=True)
print("Sắp xếp theo số lần giảm dần:")
for mon, so_lan in sorted_dem:
    print(f"{mon}: {so_lan}")