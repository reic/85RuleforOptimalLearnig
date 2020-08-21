# pip install python-docx
# pip install nltk
import docx
import re
from nltk.stem import PorterStemmer


def get_words(data, pattern=r'[a-zA-Z]+'):
    words = re.findall(pattern, data)
    return words


class Wordobj(object):
    def __init__(self, word, counter=1):
        self.counter = counter
        self.word = word

    def __str__(self):
        return " %s \t %d " % (self.word, self.counter)


def word_count(words):
    stems = {}
    ps = PorterStemmer()
    for word in words:
        word = word.lower()
        index = ps.stem(word)
        if index not in stems:
            stems[index] = Wordobj(word)
        else:
            stems[index].counter += 1
            len_word = len(word)
            len_stem_word = len(stems[index].word)
            if len_word < len_stem_word:
                stems[index].word = word
            if len_word == len_stem_word and word != stems[index].word:
                stems[index].word = word
    return stems


def get_doc_words(filename):
    # read docx
    readfile = docx.Document("./"+filename)
    wordlist, unknowlist = [], []
    for para in readfile.paragraphs:
        wordlist.extend(get_words(para.text.lower()))
        for run in para.runs:
            if run.underline and run.underline != True:
                # unknowlist.append(run.text.lower())
                unknowlist.extend(get_words(run.text.lower()))
    return wordlist, unknowlist


def unknownwords_to_file(filename, data):
    text = ', '.join([item.word for item in data.values()])+"\n"
    with open('./'+filename, "a", encoding='utf-8') as f:
        f.write(text)


def main(options):

    # 從 word 檔讀取文字， 不認識的字  double underline (ctrl - shift - d) 的字
    wordall, unknowns = get_doc_words(options['filename'])
    # print(wordall)
    stemlist = word_count(wordall)
    unknown_stemlist = word_count(unknowns)
    counter = 0
    for item in unknown_stemlist:
        counter += stemlist[item].counter
        unknown_stemlist[item].word = stemlist[item].word
        unknown_stemlist[item].counter = stemlist[item].counter
    accident_rate = counter/len(wordall)*100
    print(''.center(100, '-'))
    print("總共單字數 %2d" % len(stemlist))
    print("不熟悉的單字 %2d" % len(unknown_stemlist))
    print("意外率 %.2f %%" % accident_rate)
    print(' 不認識的單字 '.center(94, '-'))
    print({item.word: item.counter for item in unknown_stemlist.values()})
    print(''.center(100, '-'))
    # 將新的單字寫入檔案
    unknownwords_to_file(options['output_filename'], unknown_stemlist)


if __name__ == "__main__":
    #  filename 為 docx 的檔案名稱，預設為 test.docx
    #  output_filename 為輸出的檔案名稱，預設為 wordlearn.txt
    options = {'filename': "test.docx", 'output_filename': 'wordlearn.txt'}
    main(options)
