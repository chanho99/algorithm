while True:
    m = input().split()
    if m[0] == "#" and m[1] == "0" and m[2] == "0":
        break

    if int(m[1]) > 17 or int(m[2]) >= 80:
        category = "Senior"
    else:
        category = "Junior"

    print(m[0], category)