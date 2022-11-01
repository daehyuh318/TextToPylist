# txt to py-list
file_path = "file"
with open(file_path, 'rt', encoding='UTF8') as f:
    lines = f.readlines()

output = list(set(list(map(lambda s: s.strip(), lines))))
print(output)
print(len(output))