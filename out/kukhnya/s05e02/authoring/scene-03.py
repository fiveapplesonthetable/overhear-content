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
    (0, None, "'If something goes wrong, they fine the staff.' Mikhail reminds Barinov that if something goes wrong they fine the staff before the moment passes."),
    (1, None, "'I do not worry about my subordinates.' Because he does not worry about his subordinates, Barinov treats the matter as settled."),
    (2, None, '\'Misha, go to your own office.\' Going to Mikhail\'s own office moves the conversation forward without extra drama. Speaking with the close, informal "you" strips away any polite distance between them.'),
    (3, None, '\'In ten minutes we have a meeting.\' Mikhail mentions that in ten minutes they have a meeting so Barinov sees what is at stake. In Russian you say "by me" or "with us" rather than "I have", so the situation sits right with the person.'),
    (4, None, "'All our management will be there.' Claiming that all their management will be there sounds confident, even if Barinov has doubts."),
    (5, None, "'They informed me of important news.' With the room and secret in play, Vika keeps this short reply brisk and direct."),
    (6, None, "'The secret guest will be here today or tomorrow.' Vika explains that the secret guest will be here today or tomorrow, keeping her voice calm and direct."),
    (7, None, "'Be on alert today.' Around the room and secret, Vika sets a calm, everyday tone with Barinov."),
    (8, None, "'Mikhail, there is a small problem there.' Noting that there is a small problem there keeps Vika's side of the story simple and clear."),
    (9, None, "'The guests are complaining about the bitter cold.' Even though the guests are complaining about the bitter cold, Vika keeps a steady face in front of Barinov."),
    (10, None, "'Well, send our engineer up there.' Admitting that Barinov should send their engineer up there shows Mikhail being honest for a change."),
    (11, None, '\'Could he not think of that himself?\' By checking whether he not think of that himself, Mikhail presses Barinov for a straight answer. In Russian, he does not need helper words like "do" or "did"—rising pitch alone turns it into a question.'),
]
