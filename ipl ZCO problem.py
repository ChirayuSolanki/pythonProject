n = input()
N = list(map(int,input().split()))
s = sorted(N)
r = s[: : -1]
for i in range(2,len(r)-1,3):
    r.pop(i)
print(sum(r))

