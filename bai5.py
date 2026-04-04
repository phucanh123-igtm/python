import pandas as pd

print("=" * 70)
print("BÀI 5: DỮ LIỆU KHẢO SÁT HỌC TẬP")
print("=" * 70)

data = {
    "MaSV": ["SV01", "SV02", "SV03", "SV04", "SV05", "SV06", "SV07", "SV08", "SV09", "SV10"],
    "GioTuHoc": [3, 2, 1, 4, 2.5, 1.5, 3.5, 2, 1, 4],
    "SoBuoiNghi": [1, 2, 4, 0, 1, 3, 0, 2, 5, 1],
    "DiemCC": [9, 8, 6, 10, 8, 6, 9, 8, 5, 10],
    "DiemCuoiKy": [8, 7.5, 6, 9, 8, 6.5, 8.5, 7, 5.5, 9]
}

df = pd.DataFrame(data)

df["DiemTB"] = 0.3 * df["DiemCC"] + 0.7 * df["DiemCuoiKy"]

def nhom_hoc_tap(row):
    if row["GioTuHoc"] >= 3 and row["SoBuoiNghi"] <= 1:
        return "Tich cuc"
    elif row["GioTuHoc"] >= 2 and row["SoBuoiNghi"] <= 2:
        return "Binh thuong"
    else:
        return "Can ho tro"

df["NhomHocTap"] = df.apply(nhom_hoc_tap, axis=1)

print("\nDataFrame khảo sát học tập:")
print(df)

print("\nSinh viên tự học > 2 giờ và nghỉ <= 2 buổi:")
print(df[(df["GioTuHoc"] > 2) & (df["SoBuoiNghi"] <= 2)])

print("\nNhận xét:")
print("- Những sinh viên học tự học nhiều và nghỉ ít thường có DiemTB cao.")
print("- Nhóm tích cực thường đạt kết quả tốt nhất.")
print("- Nhóm bình thường vẫn có thể đạt điểm khá nếu duy trì chuyên cần.")
print("- Nhóm cần hỗ trợ có giờ tự học thấp và số buổi nghỉ nhiều.")
print("- Dữ liệu cho thấy tự học đều và chuyên cần giúp nâng cao điểm.")

print("\n" + "=" * 70)
