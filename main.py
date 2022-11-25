from atm import atm
title = 'CHƯƠNG TRÌNH RÚT TIỀN TẠI CÂY ATM'
print(title.center(60))
khachhang = ['Nguyễn Thị Thu Hiền', 'Nguyễn Vĩnh Ý', 'Đinh Hồng Cơ', 'Bùi Đăng Nguyên', 'Đỗ Thành Danh']
tien = [30000000, 40000000, 50000000, 60000000, 70000000]
name = str(input('Vui lòng nhập tên chủ tài khoản: '))
if name == khachhang[0]:
    atm(khachhang[0], 1, tien[0], 10000000)
if name == khachhang[1]:
    atm(khachhang[1], 2, tien[1], 10000000)
if name == khachhang[2]:
    atm(khachhang[2], 3, tien[2], 10000000)
if name == khachhang[3]:
    atm(khachhang[3], 4, tien[3], 10000000)
if name == khachhang[4]:
    atm(khachhang[4], 5, tien[4], 10000000)
