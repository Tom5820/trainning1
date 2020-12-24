def sum_str(string, total):
    if len(string) == 0:
        return [""] if total == 0 else []

    result = []
    for i in range(len(string) - 1, -1, -1):
        num = int(string[i:])
        r = sum_str(string[0:i], total - num)
        result.extend(map(lambda x: f"{x}+{num}" if x != "" else string[i:], r))

        r = sum_str(string[0:i], total + num)
        result.extend(map(lambda x: f"{x}-{num}", r))
    return result

if __name__ == "__main__":
    print(sum_str("123456789", 100))
