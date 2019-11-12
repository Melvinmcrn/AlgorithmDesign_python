from sys import stdin

n,m = [int(e) for e in stdin.readline().split()]
coin = [int(e) for e in stdin.readline().split()]

history = [100000 for e in range(m+1)]
#เงิน 0 บาทใช้ 0 เหรียญ
history[0] = 0

#ไล่ตั้งแต่ค่าเงินเป็น 1 ถึง m
for i in range(1,m+1):
    #ไล่ตั้งแต่เหรียญแรกจนเหรียญสุดท้าย
    for j in range(len(coin)):
        if coin[j] <= i:
            difference = i - coin[j]
            if history[difference]+1 < history[i]:
                history[i] = history[difference]+1

print(history[m])