import sys

with open('part-00000.txt', 'r') as file:
    data = file.read().split('\n')
    data = data[:10]
    output = ""
    output = '\n'.join(data)
    print(output)

with open("resultado.txt", 'w') as file:
    file.write(output)
