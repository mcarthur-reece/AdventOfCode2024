with open("input.txt", "r") as file:
    first_list = []
    second_list = []
    for line in file:
        numbers = str(line).strip().split()
        first_list.append(int(numbers[0]))
        second_list.append( int(numbers[1]))
first_list.sort()
second_list.sort()
ans = 0
n = len(first_list)
for i in range(n):
    ans += abs(first_list[i] - second_list[i])
print(ans)
