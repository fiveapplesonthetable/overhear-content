# Authoring module for kukhnya-s01e13-scene-17.
ID = 'kukhnya-s01e13-scene-17'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 13
SCENE = 17
TITLE = 'Неловкая встреча  (An Awkward Encounter)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'nastya': 'Настя', 'vika': 'Вика'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.13'
SOURCE_FILE = 'sources/kukhnya/s01/e13.ru.dual.srt'
INTRO = "Vika is trying to slip out of Max's flat unnoticed, but Nastya is standing in the hallway. Here is how that goes, in Russian."
OPENER = 'The awkward conversation again, slowly.'
TRANSITION = 'Here is the hallway meeting from the top.'
OUTRO = "Nastya promises to keep quiet, with the same triple 'no' Kostya used at the bar. Bye for now."
CLOSING = ('vika', 'Пока!')
STORY = [
    ('nastya', 'Здравствуйте, Виктория Сергеевна.', 'Hello, Victoria Sergeyevna.', [(240, 'Здрасте, Виктория Сергеевна')], ''),
    ('vika', 'Доброе утро, Настя.', 'Good morning, Nastya.', [(240, 'Привет, Настя')], ''),
    ('nastya', 'Проходите, я уже всё закончила.', 'Come in, I am already done.', [(241, 'Проходите, я уже закончила')], ''),
    ('vika', 'Спасибо, я просто ухожу на работу.', 'Thank you, I am just leaving for work.', [], ''),
    ('nastya', 'Извините, я сегодня немного опоздаю.', 'Excuse me, I will be a little late today.', [(242, 'извините, пожалуйста, я, наверное, сегодня немножко задержусь')], ''),
    ('vika', 'Да, я всё прекрасно понимаю.', 'Yes, I understand everything perfectly.', [(243, 'Да-да, я понимаю')], ''),
    ('vika', 'Я сегодня тоже задержусь немного.', 'I will also be delayed a bit today.', [(243, 'Я, наверное, тоже')], ''),
    ('nastya', 'Вы провели здесь всю ночь?', 'Did you spend the whole night here?', [], ''),
    ('nastya', 'Вы теперь встречаетесь с Максимом?', 'Are you seeing Maxim now?', [(244, 'а вы с Максимом?')], ''),
    ('vika', 'Настя, не задавай глупых вопросов.', 'Nastya, do not ask silly questions.', [(245, 'Настя')], ''),
    ('nastya', 'Всё, я молчу и всё поняла.', 'That is all, I am silent and understood everything.', [(245, 'Все-все, я поняла')], ''),
    ('vika', 'В ресторане об этом никто не знает.', 'No one at the restaurant knows about this.', [], ''),
    ('nastya', 'Я никому ничего не скажу, обещаю.', 'I will not tell anyone anything, I promise.', [], ''),
]
WALK = [
    (0, None, ["'Hello, Victoria Sergeyevna.' Let us break down the words: ", ('nastya', 'Здравствуйте'), " gives the polite, long hello. Nastya uses name plus father's name, as she would for her boss."]),
    (1, None, ["'Good morning, Nastya.' Vika answers with just the first name, while Nastya used the full name. ", ('vika', 'Доброе'), ' ends in an extra vowel to match morning, ', ('vika', 'утро'), '.']),
    (2, None, ["'Come in, I am already done.' Let's look at the words: ", ('nastya', 'Проходите'), ' means go through, so it works for letting someone pass. ', ('nastya', 'закончила'), " means finished, with a woman's ending."]),
    (3, None, ["'Thank you, I am just leaving for work.' Let's consider this line: ", ('vika', 'ухожу'), ' says I am going away, adding the prefix that means away. To work is ', ('vika', 'на'), ('vika', 'работу'), ', and work changes to show the direction.']),
    (4, None, ["'Excuse me, I will be a little late today.' Now let's inspect the words: ", ('nastya', 'опоздаю'), ' is I will be late. ', ('nastya', 'Извините'), ' supplies the polite excuse me, and ', ('nastya', 'немного'), ' means a little.']),
    (5, None, ["'Yes, I understand everything perfectly.' Now we can focus on the speech: ", ('vika', 'прекрасно'), ' means beautifully, but here it just says perfectly well. ', ('vika', 'понимаю'), ' is I understand.']),
    (6, None, ["'I will also be delayed a bit today.' We can consider the words: ", ('vika', 'задержусь'), ' means I will hold myself back, and it ends with a short self ending. Also is ', ('vika', 'тоже'), '.']),
    (7, None, ["'Did you spend the whole night here?' Now we can inspect the sentence: ", ('nastya', 'провели'), ' is spent, for time. The whole night is ', ('nastya', 'всю'), ('nastya', 'ночь'), ', where night picks up a different ending.']),
    (8, None, ["'Are you seeing Maxim now?' Word for word, ", ('nastya', 'встречаетесь'), ' means are you meeting each other, and that is how Russians ask whether two people are a couple. ', ('nastya', 'Максимом'), ' is the full form of Max.']),
    (9, None, ["'Nastya, do not ask silly questions.' Russian says give a question for ask a question, so do not ask is ", ('vika', 'не'), ('vika', 'задавай'), ', and ', ('vika', 'глупых'), ' means of silly.']),
    (10, None, ["'That is all, I am silent and understood everything.' We can focus on this line: ", ('nastya', 'Всё'), ' at the start is that is it. ', ('nastya', 'молчу'), ' is I am silent, and ', ('nastya', 'поняла'), " is I understood, in a woman's form."]),
    (11, None, ["'No one at the restaurant knows about this.' Nobody and not sit next to each other in the sentence. Russian wants both, so ", ('vika', 'никто'), ('vika', 'не'), ('vika', 'знает'), ' is nobody does not know.']),
    (12, None, ["'I will not tell anyone anything, I promise.' Let us focus on the phrase: ", ('nastya', 'никому'), ('nastya', 'ничего'), ('nastya', 'не'), ' has three negatives in a row. I will say, ', ('nastya', 'скажу'), ', and I promise, ', ('nastya', 'обещаю'), ', each do the job of several English words.']),
]
