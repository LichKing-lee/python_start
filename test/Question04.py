import sys

# tab으로 들어온 입력을 white space 4개로 변경
before = sys.argv[1]
after = sys.argv[2]
result = ""
with open(before, "r") as f:
    lines = f.readlines()
    for line in lines:
        result += line

with open(after, "w") as f:
    f.write(result.replace("\t", " "*4))
