def atm(tk, password, tien, gioihanrut, changesodu, changehanmuc, stt):
    mapin = int(input('Hãy nhập mã PIN, nếu muốn ngừng sử dụng dịch vụ hãy nhập số 0: '))
    dem = 0
    while True:
        if mapin == 0:
            break
        if mapin != password:
            dem += 1
            if dem == 3:
                print('Bạn đã nhập sai mã PIN quá số lần quy định')
                break
        if mapin == password:
            print(f'Chủ thẻ: {tk} \nSố dư: {tien} VNĐ \nHạn mức giao dịch: {gioihanrut} VNĐ')
            ruttien = float(input('Hãy nhập số tiền cần rút: '))
            if ruttien == 0:
                break
            if ruttien <= tien:
                if gioihanrut < ruttien:
                    print('Số tiền rút vượt quá hạn mức giao dịch, xin vui lòng thử lại')
                else:
                    tien = tien - ruttien
                    changesodu[stt] = tien
                    print(f'Bạn đã rút thành công {ruttien} VNĐ \nSố dư: {tien} VNĐ')
                    gioihanrut = gioihanrut - ruttien
                    changehanmuc[stt] = gioihanrut
                    if gioihanrut == 0:
                        break
                    q = str(input('Bạn có muốn tiếp tục giao dịch không: '))
                    if q == 'Không':
                        break
            else:
                print('Bạn không có đủ tiền trong tài khoản, xin vui lòng thử lại')
        else:
            mapin = int(input('Xin vui lòng nhập lại mã PIN, nếu muốn ngừng sử dụng dịch vụ hãy nhập số 0: '))
