print("김진우")
print("202106046")
print("김진우", end="")
print("202106046")


sum = 0
for i in range(1, 101):
    if i < 100:
        print(i,"+ ",end="")
    else:
        print(i,"= ",end="")
    sum += i

print(sum)
