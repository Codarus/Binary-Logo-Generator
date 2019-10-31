

def convert(string):

    container = map(bin, bytearray(string, 'utf8'))
    # remove the line below (and modify return statement) t o  w r i t e  l i k e  t h i s
    new_container = [c.replace("b", "") for c in container]

    return new_container


binary = convert("thanks for playing")

for i in binary:
    print(i, end=" ")
