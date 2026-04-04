import pandas as pd

print('=' * 70)
print('BÀI 4: LỌC DỮ LIỆU, THÊM CỘT, ĐỔI TÊN VÀ ĐẶT INDEX')
print('=' * 70)

df = pd.read_csv('diem_sinhvien.csv')
df['DiemTB'] = 0.4 * df['DiemQT'] + 0.6 * df['DiemThi']

def xep_loai(diem):
    if diem >= 8.5:
        return 'Gioi'
    elif diem >= 7.0:
        return 'Kha'
    elif diem >= 5.5:
        return 'Trung binh'
    else:
        return 'Yeu'

print('\nSinh viên có DiemTB >= 8:')
df['XepLoai'] = df['DiemTB'].apply(xep_loai)
print(df[df['DiemTB'] >= 8])

df = df.rename(columns={'HoTen': 'TenSinhVien'})
df = df.set_index('MaSV')

print('\nDataFrame sau khi đổi tên cột và đặt MaSV làm index:')
print(df)

print('\n' + '=' * 70)
