

"""
QC tools for checking that a text file is ok
"""
fname = r'output\hp\ch3.txt'
# check lines for known-wrong characters
unacceptables = [
    ''
]

# check that no line is > 19 chars (this is the max line-length for phone app)

with open(fname, 'r', encoding='utf-8') as f:
    lines = f.read().splitlines()

counter = 0
for i in range(len(lines)):
    line = lines[i]
    if len(line) > 19:
        print(f'Line {i} of {len(line)} chars: {line}')
        counter +=1
