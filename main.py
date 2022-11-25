n = int(input('Nhập vào số hạng N: '))
f0 = 0
f1 = 1
fn = 1
if n <= 0:
    print('Số hạng không xác định')
elif n == 1:
    print(f'Số hạng thứ {n} trong dãy Fibonacci là: {n}')
else:
    for i in range(2, n):
        f0 = f1
        f1 = fn
        fn = f0 + f1
    print(f'Số hạng thứ {n} trong dãy Fibonacci là: {fn}')
#djaisjdoasdjsaijodsa