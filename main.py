from atm import atm
title = 'CHƯƠNG TRÌNH RÚT TIỀN TẠI CÂY ATM'
print(title.center(60))
khachhang = ['Nguyễn Thị Thu Hiền', 'Nguyễn Vĩnh Ý', 'Đinh Hồng Cơ', 'Bùi Đăng Nguyên', 'Đỗ Thành Danh']
name = str(input('Vui lòng nhập tên chủ tài khoản: '))
if name == khachhang[0]:
    atm(name, 5555, 500000, 100000)
if name == khachhang[1]:
    atm(name, 2510, 50000000, 10000000)
if name == khachhang[2]:
    atm(name, 1234, 50000000, 10000000)
if name == khachhang[3]:
    atm(name, 1111, 50000000, 10000000)
if name == khachhang[4]:
    atm(name, 2222, 50000000, 10000000)
