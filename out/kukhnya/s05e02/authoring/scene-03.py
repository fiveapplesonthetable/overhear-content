# Authoring module for kukhnya-s05e02-scene-03.
ID = 'kukhnya-s05e02-scene-03'
SHOW = 'kukhnya'
SEASON = 5
EPISODE = 2
SCENE = 3
TITLE = 'Жалоба на холод в номере  (Complaint About the Cold Room)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'mikhail': 'Михаил', 'vika': 'Вика'}
SOURCE_NAME = 'Кухня (Kukhnya) S5.02'
SOURCE_FILE = 'sources/kukhnya/s05/e02.ru.srt'
INTRO = 'Mikhail warns that a bad review from the secret guest will result in fines for the entire staff, Vika tips off Barinov to stay alert, and a complaint arrives from room 205 about the cold. Listen to the conversation.'
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = 'And that finishes the warning before the morning staff meeting. Until next time!'
CLOSING = ('vika', 'Увидимся!')
STORY = [
    ('mikhail', 'Если что-то не так, персонал штрафуют.', 'If something goes wrong, they fine the staff.', [(22, 'персонал'), (22, 'штрафуют')], 'adapted'),
    ('barinov', 'За своих подчинённых я не волнуюсь.', 'I do not worry about my subordinates.', [(23, 'За своих подчиненных я не волнуюсь')], 'verbatim'),
    ('barinov', 'Миша, иди ты в свой кабинет.', 'Misha, go to your own office.', [(24, 'иди ты')], 'adapted'),
    ('mikhail', 'Через десять минут у нас собрание.', 'In ten minutes we have a meeting.', [(25, 'на собрании через'), (25, 'минут')], 'adapted'),
    ('mikhail', 'Там будет всё наше руководство.', 'All our management will be there.', [(26, 'руководство')], 'adapted'),
    ('vika', 'Мне сообщили важную новость.', 'They informed me of important news.', [(27, 'Мне сообщили')], 'adapted'),
    ('vika', 'Тайный гость будет сегодня или завтра.', 'The secret guest will be here today or tomorrow.', [(27, 'тайный гость будет сегодня-завтра')], 'adapted'),
    ('vika', 'Будьте сегодня начеку.', 'Be on alert today.', [(28, 'Будьте начеку')], 'adapted'),
    ('vika', 'Михаил, там небольшая проблемка.', 'Mikhail, there is a small problem there.', [(29, 'там небольшая проблемка')], 'adapted'),
    ('vika', 'Гости жалуются на сильный холод.', 'The guests are complaining about the bitter cold.', [(30, 'Гости жалуются на')], 'adapted'),
    ('mikhail', 'Ну, отправьте туда нашего инженера.', 'Well, send our engineer up there.', [(31, 'Ну, отправьте туда инженера')], 'adapted'),
    ('mikhail', 'Он сам не мог подумать?', 'Could he not think of that himself?', [(32, 'Сам не мог')], 'adapted'),
]
WALK = [
    (0, None, "'If something goes wrong, they fine the staff.' Mikhail steps in wryly with a shrug, steering the talk right where he wants it."),
    (1, None, '\'I do not worry about my subordinates.\' Bringing up his subordinates at once, Barinov chooses "podchinyonnykh" ("subordinates", from the root "podchinyonnyy") so Mikhail hears the exact meaning.'),
    (2, None, "'Misha, go to your own office.' Barinov speaks earnestly with a shrug, shifting the mood of the conversation in a single beat."),
    (3, None, "'In ten minutes we have a meeting.' Mikhail weighs in promptly on the spot, shifting the mood of the conversation in a single beat."),
    (4, None, '\'All our management will be there.\' Bringing up the leadership beside Vika, Mikhail centers the remark on "rukovodstvo" ("leadership") without any extra fuss.'),
    (5, None, "'They informed me of important news.' Focusing on the news beside Mikhail, spoken Russian compresses the whole thought into just 4 words, skipping the extra helper words English needs."),
    (6, None, "'The secret guest will be here today or tomorrow.' Vika opens up honestly with a sigh, leaving no doubt about where she stands."),
    (7, None, '\'Be on alert today.\' Vika answers directly before Mikhail and puts the emphasis on "segodnya" ("today") in the middle of the talk.'),
    (8, None, '\'Mikhail, there is a small problem there.\' Underscoring how small things are in this beat, Vika links the Russian words directly in the present with no word for "am", "is", or "are" needed.'),
    (9, None, "'The guests are complaining about the bitter cold.' Vika speaks up candidly without any doubt, before Mikhail can change the subject."),
    (10, None, '\'Well, send our engineer up there.\' Bringing up his engineer in this beat, Mikhail leans on "inzhenera" ("engineer", a form of "inzhener") to give the remark its edge.'),
    (11, None, "'Could he not think of that himself?' Jumping in warmly during the talk, Mikhail keeps normal statement word order here, turning the line into a question for Vika purely through rising pitch."),
]
