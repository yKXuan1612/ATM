def atm(ten, password, tien, gioihanrut):
    mapin = int(input('Hãy nhập mã PIN, nếu muốn ngừng sử dụng dịch vụ hãy nhập số 0: '))
    dem = 0
    if mapin == password:
        print(f'Chủ thẻ: {ten} \nSố dư: {tien} VNĐ \nHạn mức giao dịch: {gioihanrut} VNĐ')
    while True:
        if mapin != password:
            dem += 1
            if dem == 3:
                print('Bạn đã nhập sai mã PIN quá số lần quy định')
                break
        if mapin == 0:
            break
        if mapin == password:
            ruttien = float(input('Hãy nhập số tiền cần rút: '))
            if ruttien == 0:
                break
            if ruttien <= tien:
                if gioihanrut < ruttien:
                    print('Số tiền rút vượt quá hạn mức giao dịch, xin vui lòng thử lại')
                else:
                    tien = tien - ruttien
                    print(f'Bạn đã rút thành công {ruttien} VNĐ \nSố dư: {tien} VNĐ')
                    gioihanrut = gioihanrut - ruttien
                    if gioihanrut == 0:
                        break
            else:
                print('Bạn không có đủ tiền trong tài khoản, xin vui lòng thử lại')
        else:
            mapin = int(input('Xin vui lòng nhập lại mã PIN, nếu muốn ngừng sử dụng dịch vụ hãy nhập số 0: '))
