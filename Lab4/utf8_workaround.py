import sys

if __name__ == '__main__':
    input_file = sys.argv[1]
    output_file = input_file.split('.csv')[0] + '_utf8cleaned.csv'

    data = []
    with open(input_file, 'rb') as f:
        lines = f.readlines()
        for i, line in enumerate(lines[:3]):
            newline = line.decode('utf-8', 'ignore')
            data.append(newline)

    with open(output_file, 'w') as f:
        for row in data:
            f.write(row)
