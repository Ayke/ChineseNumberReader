
# Special case: 10
readDigit = ['ling', 'yi', 'er', 'san', 'si', 'wu', 'liu', 'qi', 'ba', 'jiu']
# charDigit = ['零','一', '二', '三', '四', '五', '六', '七', '八', '九']
readPos = ['N/A', '', 'shi', 'bai', 'qian', 'wan', 'shi', 'bai', 'qian', 'yi']
YIYI = 10000000000000000
YI = 100000000
WAN = 10000

def readNum(x, lastZero=False, ignore=False):
    ans = ''
    if x >= YIYI:
        fooAns, lastZero = readNum(x // YIYI, lastZero, ignore and (ans == ''))
        ans += ' ' + fooAns + ' yi yi'
        x %= YIYI
    if x >= YI:
        fooAns, lastZero = readNum(x // YI, lastZero, ignore and (ans == ''))
        ans += ' ' + fooAns + ' yi'
        x %= YI
    if x >= WAN:
        fooAns, lastZero = readNum(x // WAN, lastZero, ignore and (ans == ''))
        ans += ' ' + fooAns + ' wan'
        x %= WAN

    assert x <= 9999
    assert x >= 0
    divisor = int(1000)
    pos = int(4)
    if ignore and (ans == ''):
        while ((x // divisor) == 0):
            divisor /= 10
            pos -= 1
    while pos >= 1:
        dig = int(x / divisor)
        if (dig == 0):
            if not lastZero:
                lastZero = True
        else:
            if lastZero:
                ans += ' ling'
                lastZero = False
            if (ans == '') and (ignore) and (pos == 2) and (dig == 1):
                ans += ' shi'
            else:
                ans += ' ' + readDigit[dig]
                if pos > 1:
                    ans += ' ' + readPos[pos]
        x = x % divisor
        divisor //= 10
        pos -= 1
    return ans.strip(), lastZero

def pronounce(x):
    if x == 0:
        return 'ling', False
    ans, lastZero = readNum(x, False, True)
    return ans.strip()

# for foox in range(1000):
#     ans, _ = readNum(foox)
#     print('{}%:{}'.format(foox, ans))

def search(number, x):
    global fooLen
    global smallAns, smallNum
    if x > fooLen:
        answer = pronounce(number)
        # print(f'{number}: {answer}')
        if answer < smallAns:
            smallAns = answer
            smallNum = number
            print(f'----------------------')
            print(f'Answer update!!!')
            print(f'{smallNum}: {smallAns}')
            print(f'----------------------')
        return
    search(number, x+1)
    number += 8 * 10 ** (x-1)
    search(number, x+1)
    return

smallAns = 'ba shi jiu'
smallNum = 89
for fooLen in range(3, 26):
    print(f'{fooLen}/26')
    num = 9
    search(num, 2)

print('***********************************')
print('THE WINNER IS:')
print(f'{smallNum}')
print(f'{smallAns}')
print('***********************************')
# print(pronounce(12))
# print(pronounce(20))
# print(pronounce(10))
# print(pronounce(2))
# print(pronounce(89))
# print(pronounce(108))

# print(pronounce(888000008888889))
# print(pronounce(888888808888889))
