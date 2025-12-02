attendance = [18, 20, 19, 15, 21]
count = 0

for day in attendance:
    if day >= 20:
        print("full")
        count += 1
    else:
        print("not full")

print(count)
print(sum(attendance))