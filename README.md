# TestTask_TFIDF
Term frequency - Inverse document frequency

## Порядок запуска
1) Устанавливаем зависимости из `requirements.txt`
2) Делаем миграции
3) Запускаем сервер в терминале командой `python manage.py runserver`
4) Открываем `http://127.0.0.1:8000/` в браузере   
   
Далее следуем инструкциям.


## Описание

Данная программа предназначена для расчета TF — term frequency и IDF — inverse document frequency.

TF-IDF (от англ. TF — term frequency, IDF — inverse document frequency) — статистическая мера, используемая для оценки важности слова в контексте документа, являющегося частью коллекции документов или корпуса. Вес некоторого слова пропорционален частоте употребления этого слова в документе и обратно пропорционален частоте употребления слова во всех документах коллекции.

![Главное меню программы](https://github.com/Minigamy/TestTask_TFIDF/blob/master/img/tfidf1.PNG)

После запуска приложения появляется возможность згрузить на сервер коллекцию документов (корпус), записать все слова оттуда в базу данных, и в результатае получить таблицу с термином, важностью термина в пределах одного документа и значение обратной частоты документа для данного термина.

![Выбор документа](https://github.com/Minigamy/TestTask_TFIDF/blob/master/img/tfidf2.PNG)

![Таблица](https://github.com/Minigamy/TestTask_TFIDF/blob/master/img/tfidf3.PNG)