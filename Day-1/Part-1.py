import fileinput

total = 0
for line in fileinput.input('input.txt'):
    line = line.strip()
    num = ""
    for i, v in enumerate(line):
        if v.isdigit():
            num += v
            break
    rev_line = line[::-1]
    for i, v in enumerate(rev_line):
        if v.isdigit():
            num += v
            break
    print("num as string: ", num)
    num = int(num)
    total += num
    print('total: ', total)
