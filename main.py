from atm import atm
title = 'CHƯƠNG TRÌNH RÚT TIỀN TẠI CÂY ATM'
print(title.center(60))
tenkh = ['Ý', 'Hiền', 'Cơ', 'Nguyên', 'Danh', 'Đạt']
mk = [1, 2, 3, 4, 5, 6]
sodu = [30000000, 40000000, 50000000, 60000000, 70000000, 10000000000]
hanmuc = [5000000, 10000000, 15000000, 20000000, 30000000, 40000000]
while True:
    name = str(input('Vui lòng nhập tên chủ tài khoản: '))
    if name in tenkh:
        i = tenkh.index(name)
        atm(tenkh[i], mk[i], sodu[i], hanmuc[i], sodu, hanmuc, i)
    if name == '0':
        break
