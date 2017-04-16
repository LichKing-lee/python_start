import sys

option = sys.argv[1]
name = sys.argv[2]
if len(sys.argv) > 3:
    memo = sys.argv[3]

if option == "-a":
    with open(name, "a") as f:
        f.write(memo + "\n")
elif option == "-w":
    with open(name, "w") as f:
        f.write(memo + "\n")
else:
    with open(name, "r") as f:
        lines = f.readlines()
        for line in lines:
            print(line, end="")
