def is_d(year):
    st_year = str(year)
    used = []
    for i in st_year:
        if i in used:
            return False
        used.append(i)
    return True

year = int(input())
year = year + 1

# print(type(year))
while not is_d(year):
    year = year + 1
print(year)
