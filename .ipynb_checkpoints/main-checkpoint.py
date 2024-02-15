import AndroMoney.andro_control

start = '20210201'
end = '20210228'

def func(start, end):
    AndroMoney.andro_control.start_andro(start, end)


if __name__ == '__main__':
    func(start, end)