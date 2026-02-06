data = open('inp').read()
def encode_runs(s):
    result = ""
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            result += f"{count}{s[i - 1]}"
            count = 1
    return result + f"{count}{s[-1]}"
for _ in range(40):
    data = encode_runs(data)
print(len(data))