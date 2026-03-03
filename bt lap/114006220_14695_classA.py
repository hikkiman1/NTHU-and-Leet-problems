def extract_columns(csv: str, indices: str):
    ind = list(map(int, indices.split()))
    rows = csv.split('\n')
    final=[]
    for row in rows:
        part=row.split(',')
        selected=[]
        for i in ind:
            selected.append(part[i])
        final.append(','.join(selected))
    return '\n'.join(final)
            
# Read the CSV input until EOF
csv_lines = []
while True:
    try:
        line = input()
        if line.strip() == "":
            continue
        csv_lines.append(line)
    except EOFError:
        break

# First line = indices
ind_line = csv_lines[0]


# Remaining lines = CSV data
csv_str = "\n".join(csv_lines[1:])

# Process

print(extract_columns(csv_str, ind_line))