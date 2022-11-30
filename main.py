from atm import atm
title = 'CHƯƠNG TRÌNH GIAO DỊCH TẠI CÂY ATM'
print(title.center(60))
tenkh = ['Nguyễn Vĩnh Ý', 'Nguyễn Thị Thu Hiền', 'Đinh Hồng Cơ', 'Bùi Đăng Nguyên', 'Đỗ Thành Danh']
tentk = ['ngvinhy', 'thuhien123', 'hongcodinh', 'nguyenbui', 'danh555']
mk = [1, 2, 3, 4, 5]
sodu = [30000000, 40000000, 50000000, 60000000, 70000000]
hanmuc = [5000000, 10000000, 15000000, 20000000, 30000000]
name = str(input('Hãy nhập tên tài khoản, nếu muốn ngừng sử dụng dịch vụ hãy nhập số 0: '))
k = 3
while True:
    if name in tentk:
        i = tentk.index(name)
        atm(tenkh[i], mk[i], sodu[i], hanmuc[i], sodu, hanmuc, i)
    if name == '0':
        break
    if name not in tentk:
        k -= 1
        if k == 0:
            print('Bạn đã nhập sai tên tài khoản quá số lần quy định')
            break
        name = str(input(f'Xin vui lòng nhập lại tên tài khoản, bạn còn {k} lần: '))
    else:
        name = str(input('Hãy nhập tên tài khoản, nếu muốn ngừng sử dụng dịch vụ hãy nhập số 0: '))
