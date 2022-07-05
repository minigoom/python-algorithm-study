count_line = int(input())
list_line = []
for i in range(count_line):
    line = input()
    line = line.lower()
    list_line.append(line)
# print(list_line)
str_line = ''.join(list_line)
# print(str_line)
count_s = 0
count_t = 0
for i in str_line:
    if i == 's':
        count_s = count_s + 1
    elif i == 't':
        count_t = count_t + 1
# print(count_s, count_t)

if count_s >= count_t:
    print('French')
else:
    print('English')
