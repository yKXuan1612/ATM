def atm(tk, password, tien, gioihanrut, changesodu, changehanmuc, stt, sodu_atm):
    mapin = int(input('Hãy nhập mã PIN, nếu muốn ngừng sử dụng dịch vụ hãy nhập số 0: '))
    k = 3
    while True:
        if mapin == 0:
            break
        elif mapin != password:
            k -= 1
            if k == 0:
                print('Bạn đã nhập sai mã PIN quá số lần quy định')
                break
            mapin = int(input(f'Xin vui lòng nhập lại mã PIN, bạn còn {k} lần: '))
        else:
            print(f'Chủ thẻ: {tk} \nSố dư: {tien} VNĐ \nHạn mức giao dịch: {gioihanrut} VNĐ')
            ruttien = int(input('Hãy nhập số tiền cần rút: '))
            if ruttien == 0:
                break
            elif ruttien > sodu_atm[0]:
                print('ATM không đủ tiền thực hiện giao dịch, xin vui lòng thử lại')
            elif ruttien <= tien:
                if gioihanrut < ruttien:
                    print('Số tiền rút vượt quá hạn mức giao dịch, xin vui lòng thử lại')
                else:
                    if ruttien % 50000 == 0:
                        tien = tien - ruttien
                        changesodu[stt] = tien
                        sodu_atm[0] -= ruttien
                        print(f'Bạn đã rút thành công {ruttien} VNĐ \nSố dư: {tien} VNĐ')
                        gioihanrut = gioihanrut - ruttien
                        changehanmuc[stt] = gioihanrut
                        if gioihanrut == 0:
                            break
                        q = str(input('Bạn có muốn tiếp tục giao dịch không: '))
                        if q == 'Không' or q == 'Ko' or q == 'ko' or q == 'không' or q == 'k' or q == 'K':
                            bienlai = str(input('Bạn có muốn nhận hóa đơn không: '))
                            if bienlai == 'Có' or bienlai == 'có':
                                print(f'Chủ thẻ: {tk} \nSố tiền đã giao dịch: {ruttien} \nSố dư: {tien} VNĐ')
                                break
                            if bienlai == 'Không' or bienlai == 'Ko' or bienlai == 'ko' or bienlai == 'không' or bienlai == 'k' or bienlai == 'K':
                                break
                    else:
                        q = str(input('Số tiền giao dịch phải là bội số của 50000, bạn có muốn tiếp tục giao dịch khác không: '))
                        if q == 'Không' or q == 'Ko' or q == 'ko' or q == 'không' or q == 'k' or q == 'K':
                            break
            else:
                print('Bạn không có đủ tiền trong tài khoản, xin vui lòng thử lại')
