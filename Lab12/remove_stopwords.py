import sys
import os


def main(input_file):
    stopwords = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', 'your', 'yours', 'yourself', 'yourselves',\
     'he', 'him', 'his', 'himself', 'she', 'her', 'hers', 'herself', 'it', 'its', 'itself', 'they', 'them', 'their', 'theirs',\
     'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be',\
     'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or',\
     'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through',\
     'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under',\
     'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each',\
     'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too',\
     'very', 's', 't', 'can', 'will', 'just', 'don', 'should', 'now', 'que', '9gag']

    output_file = os.path.splitext(input_file)[0] + '_stopwords_removed.csv'
    with open(input_file, 'r') as fread, open(output_file, 'w') as fwrite:
        # Copy header
        header = fread.readline()
        if '\t' in header:
            header = header.replace('\t', ',')
        fwrite.write(header)

        # Process lines
        for line in fread:
            line = line.strip()
            if '\t' in line:
                items = line.split('\t')
            elif ',' in line:
                items = line.split(',')

            text, label = items
            text = text.lower()
            text = text.replace(',', ' ') # Remove commas in text

            # Remove stop words
            words = []
            for w in text.strip().split():
                if w not in stopwords:
                    words.append(w)
            text_cleaned = ' '.join(words)
            fwrite.write(text_cleaned + ',' + label + '\n')
        pass
    pass


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Please provide one input file name')
    else:
        input_file = sys.argv[1]
        if not os.path.isfile(input_file):
            print(f'{input_file} does not exist')
        else:
            main(input_file)
            print('Removing stop words completed')
