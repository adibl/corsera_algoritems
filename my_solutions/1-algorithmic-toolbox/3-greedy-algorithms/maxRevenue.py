number = int(input())
profit_per_click = [int(x) for x in input().split()]
clicks_per_day = [int(x) for x in input().split()]
profit_per_click.sort()
clicks_per_day.sort()
sum = 0
while profit_per_click:
    sum += profit_per_click.pop() * clicks_per_day.pop()
print(sum)
