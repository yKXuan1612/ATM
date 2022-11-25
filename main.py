from atm import atm
title = 'CHƯƠNG TRÌNH RÚT TIỀN TẠI CÂY ATM'
print(title.center(60))
khachhang1 = ['Hiền', 1, 30000000, 10000000]
khachhang2 = ['Ý', 2, 40000000, 10000000]
khachhang3 = ['Cơ', 3, 50000000, 10000000]
khachhang4 = ['Nguyên', 4, 60000000, 10000000]
khachhang5 = ['Danh', 5, 70000000, 10000000]
name = str(input('Vui lòng nhập tên chủ tài khoản: '))
if name == khachhang1[0]:
    atm(khachhang1[0], khachhang1[1], khachhang1[2], khachhang1[3])
if name == khachhang2[0]:
    atm(khachhang2[0], khachhang2[1], khachhang2[2], khachhang2[3])
if name == khachhang3[0]:
    atm(khachhang3[0], khachhang3[1], khachhang3[2], khachhang3[3])
if name == khachhang4[0]:
    atm(khachhang4[0], khachhang4[1], khachhang4[2], khachhang4[3])
if name == khachhang5[0]:
    atm(khachhang5[0], khachhang5[1], khachhang5[2], khachhang5[3])
