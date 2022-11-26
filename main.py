from atm import atm
title = 'CHƯƠNG TRÌNH RÚT TIỀN TẠI CÂY ATM'
print(title.center(60))
tenkh = ['Ý', 'Hiền', 'Cơ', 'Nguyên', 'Danh']
mk = [1, 2, 3, 4, 5]
sodu = [30000000, 40000000, 50000000, 60000000, 70000000]
hanmuc = [5000000, 10000000, 15000000, 20000000, 30000000]
name = str(input('Vui lòng nhập tên chủ tài khoản: '))
i = 0
for ten in tenkh:
    if name == tenkh:
        i = tenkh.index(ten)
        atm(tenkh[i], mk[i], sodu[i], hanmuc[i])
