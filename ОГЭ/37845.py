n = int(input())
count = 0
for _ in range(n):
    num = int(input())
    if num % 3 == 0:
        count += 1
print(count)