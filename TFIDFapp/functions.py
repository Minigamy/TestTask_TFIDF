import collections
import math
import os
import re

from TFIDF.settings import MEDIA_ROOT
from TFIDFapp.models import TF, IDF

corpus = []
uniq_words = set()


def open_file_and_prepair_it(path_to_file):
    """Читаем файл с кодировкой utf-8, удаляем все знаки препинания и разбиваем на список."""
    file = open(os.path.join(MEDIA_ROOT, path_to_file), encoding='utf-8')
    lines = file.read()
    file.close()
    clear_text = re.sub(pattern="[^\w\s]", repl="", string=lines).split()  # Удаляем все символы кроме букв и пробелов.
    clear_text = [x.lower() for x in clear_text]  # Переводим все элементы списка в нижний регистр.
    return clear_text


def take_files_name():
    """Функция возвращает список с именами всех файлов, которые загрузили в директорию files."""
    list_of_files = os.listdir(MEDIA_ROOT + "/files/")  # Список имен файлов в директории files.
    for i in range(len(list_of_files)):
        list_of_files[i] = "files/" + list_of_files[i]  # Добавляем к именам файлов строку "files/", чтобы
        # получилось: files/<doc_name>.
    return list_of_files


def compute_and_fill_db_tf():
    file_names = take_files_name()         # Получаем список имен файлов.
    doc_number = 1                         # Нумерация документов. Необходима для выборки при выводе таблиц.
    for txt_name in file_names:            # Цикл для обработки всех документов в files.
        clear_text = open_file_and_prepair_it(txt_name)
        corpus.append(clear_text)          # Глобальная переменная. В ней содержится текст всех документов.
        tf = dict(compute_tf(clear_text))  # {<слово>: <значение TF>, ...}
        for word in clear_text:            # Добавляем все уникальные слова в множество. Нужно для заполнения таб. IDF.
            if word not in uniq_words:
                uniq_words.add(word)

        for word in tf.keys():             # Заполняем таблицу TF
            TF.objects.create(term=word, tf=tf[word], doc_number=doc_number)
        doc_number += 1

    for word in uniq_words:                # Заполняем таблицу IDF
        idf = compute_idf(word, corpus)
        IDF.objects.create(term=word, idf=idf)
    return None


def make_table(doc_number):
    '''Запрос к БД, объеденяющий обе таблицы'''
    database_query = IDF.objects.raw(
        'SELECT id, "TFIDFapp_idf".term, tf, idf '
        'FROM "TFIDFapp_tf" '
        'INNER JOIN "TFIDFapp_idf" '
        'ON '
        '"TFIDFapp_tf".term="TFIDFapp_idf".term '
        'WHERE doc_number=%s'
        'ORDER BY idf DESC '
        'LIMIT 50', [doc_number])
    return database_query


def compute_tf(text):
    '''Вычисляет TF'''
    tf_text = collections.Counter(text)
    for i in tf_text:
        tf_text[i] = tf_text[i] / float(len(text))
    return tf_text


def compute_idf(word, text_corpus):
    '''Вычисляет IDF'''
    return math.log10(len(text_corpus) / sum([1.0 for i in corpus if word in i]))

















# def my_custom_sql():
#     cursor = connection.cursor()
#     cursor.execute('SELECT id, "TFIDFapp_idf".term, tf, idf '
#                    'FROM "TFIDFapp_tf" '
#                    'INNER JOIN "TFIDFapp_idf" '
#                    'ON '
#                    '"TFIDFapp_tf".term="TFIDFapp_idf".term '
#                    'WHERE doc_number=2')
#     row = dictfetchall(cursor)
#     print(row)
#     return row
#
#
# def dictfetchall(cursor):
#     "Returns all rows from a cursor as a dict"
#     desc = cursor.description
#     return [
#         dict(zip([col[0] for col in desc], row))
#         for row in cursor.fetchall()
#     ]



# import re
"""Вдруг понадобится. Тут мы добавляем в начало файла строку # -*- coding: utf-8 -*-, которая обозначает кодировку файла."""
#
# with open('doc1-test.txt', 'r+') as f:
#     content = f.read()
#     f.seek(0, 0)
#     f.write('# -*- coding: utf-8 -*-'.rstrip('\r\n') + '\n' + content)
#
# file = open('doc1-test.txt')
# text = file.read()
# file.close()
# a = re.sub(pattern="[^\w\s]", repl="", string=text).split()
# print(a)
