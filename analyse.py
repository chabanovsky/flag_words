# encoding:utf-8
import csv
import collections

from utils import process_text

def do_analyse():
    comment_text = parse_comment_file()
    comment_words = comment_text.split(" ")
    print ("Parsing of comments was done. Number of words: ", len(comment_words))
    question_text = parse_question_file()
    question_words = question_text.split(" ")
    print ("Parsing of questions was done. Number of words: ", len(question_words))

    diff_words = list(set(comment_words) - set(question_words))
    print ("Diff len: ", len(diff_words))

    answer_text = parse_answer_file()
    answer_words = answer_text.split(" ")
    print ("Parsing of answers was done. Number of words: ", len(answer_text))

    diff_words = list(set(diff_words) - set(answer_words))
    print ("Diff len: ", len(diff_words))

    data, count, dictionary, reversed_dictionary = build_dataset(diff_words, len(diff_words))

    print (count[:15])
    print ("-----------------------------")
    print (count[-15:])

    dump_result(count)
    just_list_of_words = list()
    for item, num in count:
        just_list_of_words.append(item)

    dump_result(just_list_of_words, 'result_list.csv')

def dump_result(result, filename='result.csv'):
    with open(filename, 'w') as result_file:
        wr = csv.writer(result_file, quoting=csv.QUOTE_ALL)
        wr.writerow(result)    

def parse_comment_file(filename="comments.csv"):
    full_text = ""
    with open(filename, 'rt', encoding="utf8") as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')
        for row in csv_reader:
            body, post_id = row
            full_text += " " + process_text(body)
    return full_text

def parse_question_file(filename="questions.csv"):
    full_text = ""
    with open(filename, 'rt', encoding="utf8") as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')
        for row in csv_reader:
            _, _, _, title, body, tags = row
            full_text += " " + process_text(body)
    return full_text

def parse_answer_file(filename="answers.csv"):
    full_text = ""
    with open(filename, 'rt', encoding="utf8") as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')
        for row in csv_reader:
            _, _, body, _ = row
            full_text += " " + process_text(body)
    return full_text

def build_dataset(words, n_words):
    count = [['UNK', -1]]
    count.extend(collections.Counter(words).most_common(n_words))
    dictionary = dict()
    for word, _ in count:
        dictionary[word] = len(dictionary)
    data = list()
    unk_count = 0
    for word in words:
        if word in dictionary:
            index = dictionary[word]
        else:
            index = 0  # dictionary['UNK']
            unk_count += 1
        data.append(index)
    count[0][1] = unk_count
    reversed_dictionary = dict(zip(dictionary.values(), dictionary.keys()))
    return data, count, dictionary, reversed_dictionary

