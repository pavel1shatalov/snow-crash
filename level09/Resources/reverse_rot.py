import sys

with open(sys.argv[1]) as f:
    token = f.read().strip()
new = ''
for ind, char in enumerate(token):
    new = new + chr(ord(char) - ind)
print(new)