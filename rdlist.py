with open('data.txt', 'r') as f:
    unique_lines = set(f.readlines())
with open('data_dump.txt', 'w') as f:
    f.writelines(unique_lines)