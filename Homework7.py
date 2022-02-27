import csv
import re
import collections


def read_file(readfile):
    """
    Read file and return content
    :param readfile:
    :return r - file content as string:
    """
    try:
        with open(readfile) as f:
            file_content = f.read()
        return file_content
    except FileNotFoundError:
        print(FileNotFoundError)


def generate_words_count(readfile):
    """
    Get string and write words count in new file
    :param readfile:
    :return:
    """
    try:
        word = re.compile(r'([A-z]+-[A-z]+|[A-z]+)')
        words = collections.Counter(word.findall(readfile.lower()))
        with open(r'words_count.csv', 'w', newline='') as file:
            writer = csv.writer(file, delimiter='-')
            for k, v in words.items():
                writer.writerow([k, v])
    except TypeError as te:
        print(te)
    except FileNotFoundError as fe:
        print(fe)


def generate_letter_summary(readfile):
    """
    Get string and write letter, letter count, uppercase count and percentage of total letter count in new file
    :param readfile:
    :return:
    """
    try:
        letters = re.findall(r'[a-zA-Z]', readfile.lower())
        letters_cnt = collections.Counter(letters)
        uppercase = collections.Counter(re.findall(r'[a-zA-Z]', readfile))
        total_cnt = len(letters)
        fieldnames = ['letter', 'count_all', 'count_uppercase', 'percentage']
        with open(r'letters_count.csv', 'w',newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

            for k, v in letters_cnt.items():
                writer.writerow({'letter': k, 'count_all': v, 'count_uppercase': uppercase[str(k).upper()],
                                 'percentage': str(round((v / total_cnt) * 100, 2)) + '%'})
    except TypeError as te:
        print(te)
    except FileNotFoundError as fe:
        print(fe)


if __name__ == '__main__':
    r = read_file('newsfeed.txt')
    generate_words_count(r)
    generate_letter_summary(r)
