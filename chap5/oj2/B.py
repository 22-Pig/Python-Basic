a = list(map(int, input().split()))
del a[0]
# ๅ่กจๅๅ
a.reverse()
for i in a:
    print(i, end=' ')
