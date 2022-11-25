title = 'CHƯƠNG TRÌNH RÚT TIỀN TẠI CÂY ATM'
print(title.center(60))
mapin = int(input('Hãy nhập mã PIN, nếu muốn ngừng sử dụng dịch vụ hãy nhập số 0: '))
nvy = ['Nguyễn Vĩnh Ý', 1234, 50000000, 10000000]
dem = 0
if mapin == nvy[1]:
    print(f'Chủ thẻ: {nvy[0]} \nSố dư: {nvy[2]} VNĐ \nHạn mức giao dịch: {nvy[3]} VNĐ')
while True:
    if mapin != nvy[1]:
        dem += 1
        if dem == 3:
            print('Bạn đã nhập sai mã PIN quá số lần quy định')
            break
    if mapin == 0:
        break
    if mapin == nvy[1]:
        ruttien = float(input('Hãy nhập số tiền cần rút: '))
        if ruttien == 0:
            break
        if ruttien <= nvy[2]:
            if nvy[3] < ruttien:
                print('Số tiền rút vượt quá hạn mức giao dịch, xin vui lòng thử lại')
            else:
                nvy[2] = nvy[2] - ruttien
                print(f'Bạn đã rút thành công {ruttien} VNĐ \nSố dư: {nvy[2]} VNĐ')
                nvy[3] = nvy[3] - ruttien
                if nvy[3] == 0:
                    break
        else:
            print('Bạn không có đủ tiền trong tài khoản, xin vui lòng thử lại')
    else:
        mapin = int(input('Xin vui lòng nhập lại mã PIN, nếu muốn ngừng sử dụng dịch vụ hãy nhập số 0: '))
