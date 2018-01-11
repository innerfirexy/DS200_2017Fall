import sys
import os


def main(input_file):
    output_file = os.path.splitext(input_file)[0] + '_URLs_replaced.csv'

    count1 = 0
    count2 = 0
    with open(input_file, 'r') as fread, open(output_file, 'w') as fwrite:
        for line in fread:
            items = line.strip().split(',')
            text, label = items

            words = []
            for w in text.split():
                if 'http' in w:
                    count1 += 1
                    words.append('URL')
                elif w.startswith('@'):
                    count2 += 1
                    words.append('USER_MENTION')
                else:
                    words.append(w)
            text_cleaned = ' '.join(words)
            fwrite.write(text_cleaned + ',' + label + '\n')

    print(f'{count1} URLs are replaced')
    print(f'{count2} user mentions are replaced')


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Please provide one input file name')
    else:
        input_file = sys.argv[1]
        if not os.path.isfile(input_file):
            print(f'{input_file} does not exist')
        else:
            main(input_file)
            print('URLs and user mentions are replaced')
