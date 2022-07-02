first = int(input())
second = int(input())
diff = abs(first - second)
child_list = [first,second]
child_list.sort()
print(child_list[1]+diff)