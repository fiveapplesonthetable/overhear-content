# Authoring module for kukhnya-s01e04-scene-22.
ID = 'kukhnya-s01e04-scene-22'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 4
SCENE = 22
TITLE = 'Разговор в кабинете  (Conversation in the Office)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'vika': 'Вика'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.04'
SOURCE_FILE = 'sources/kukhnya/s01/e04.ru.dual.srt'
INTRO = "The chef is alone in his office, still fuming about Max. Vika walks in and claims it was she, not Max, who went to the rival restaurant, and she tells him he never lets his cooks grow. Here's the Russian first."
OPENER = "Now Vika's argument."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = "Vika asks whether she can say Max isn't fired, and the chef is too tired to refuse. Notice she says you don't let him grow."
CLOSING = ('barinov', 'Пока!')
STORY = [
    ('barinov', 'Этого парня больше никуда не возьмут!', 'They will not take this guy anywhere anymore!', [(290, 'не возьмут')], ''),
    ('vika', 'Виктор, нам нужно срочно поговорить.', 'Viktor, we need to talk urgently.', [(292, 'Надо поговорить.')], ''),
    ('barinov', 'Я не хочу говорить об этом поваре.', 'I do not want to talk about this cook.', [], ''),
    ('vika', 'Макс не ходил на то собеседование.', 'Max did not go to that interview.', [(295, 'Макс не ходил на собеседование.')], ''),
    ('barinov', 'Что ты такое сейчас говоришь?', 'What are you saying right now?', [], ''),
    ('vika', 'Это я ходила в чужой ресторан.', 'It was I who went to the other restaurant.', [(297, 'Это я ходила.')], ''),
    ('vika', 'Макс действительно очень талантливый парень.', 'Max really is a very talented guy.', [(301, 'парень')], ''),
    ('vika', 'Но ты совсем не даёшь ему расти.', 'But you do not let him grow at all.', [], ''),
    ('vika', 'Сколько хороших людей ушли отсюда?', 'How many good people have left here?', [(305, 'Сколько талантливых поваров ушли')], ''),
    ('barinov', 'Хватит читать мне свои нравоучения!', 'Stop giving me your moral lectures!', [(313, 'Хватит')], ''),
    ('vika', 'Мне просто искренне жаль этого парня.', 'I simply genuinely feel sorry for this guy.', [], ''),
    ('vika', 'Я могу сказать, что он не уволен?', 'Can I say that he is not fired?', [(316, 'что он не уволен')], ''),
    ('barinov', 'Делай что хочешь, только оставь меня!', 'Do what you want, just leave me alone!', [], ''),
]
WALK = [
    (0, None, ['\'They will not take this guy anywhere anymore!\' The Russian expression for "they will not take" is ', ('barinov', 'не возьмут!'), ' with nobody named. The expression for "nowhere" is ', ('barinov', 'никуда')]),
    (1, None, ['\'Viktor, we need to talk urgently.\' Vika calls him Viktor, without his father\'s name. Literally, it translates to "to us it\'s needed", which is ', ('vika', 'нам нужно')]),
    (2, None, ['\'I do not want to talk about this cook.\' The phrase ', ('barinov', 'об этом поваре.'), ' translates to "about this cook", with a little word for "about" before a vowel sound and an extra ending on the word for cook.']),
    (3, None, ['\'Max did not go to that interview.\' The action word for going means going there and back, so ', ('vika', 'не ходил'), ' says he never made the trip at all. The term for an interview is ', ('vika', 'собеседование.'), ' built from the Russian term for a conversation.']),
    (4, None, ['\'What are you saying right now?\' Literally, he asks ', ('barinov', 'Что ты такое сейчас говоришь?'), ' which translates to "what such are you saying right now?", a surprised question.']),
    (5, None, ['\'It was I who went to the other restaurant.\' The words ', ('vika', 'Это я'), ' put the spotlight on "I". The action word ends with a sound for a woman, and the term for the other restaurant translates to "someone else\'s".']),
    (6, None, ['\'Max really is a very talented guy.\' The describing word for talented, ', ('vika', 'талантливый'), ' is built from the expression for talent. The Russian expression for "really" is ', ('vika', 'действительно')]),
    (7, None, ['\'But you do not let him grow at all.\' Literally, ', ('vika', 'не даёшь ему расти.'), ' translates to "you don\'t give him to grow", similar to earlier phrases.']),
    (8, None, ['\'How many good people have left here?\' The word for "how many" is ', ('vika', 'Сколько'), ' and after it the Russian term for people changes its ending. The action word for "left" is ', ('vika', 'ушли')]),
    (9, None, ['\'Stop giving me your moral lectures!\' The expression for moral lectures is ', ('barinov', 'нравоучения!'), ' built from the words for morals and teaching. The term for "stop" or "enough" is ', ('barinov', 'Хватит')]),
    (10, None, ['\'I simply genuinely feel sorry for this guy.\' Literally, ', ('vika', 'жаль'), ' translates to "a pity", and the person pitied takes a special form. The word for "genuinely" or "sincerely" is ', ('vika', 'искренне')]),
    (11, None, ['\'Can I say that he is not fired?\' The Russian term for "I can" is ', ('vika', 'могу'), ' The short describing word for "not fired" is ', ('vika', 'не уволен?')]),
    (12, None, ['\'Do what you want, just leave me alone!\' The phrase ', ('barinov', 'Делай что хочешь,'), ' translates to "do what you want". The phrase ', ('barinov', 'оставь меня!'), ' translates to "leave me", an order to leave behind, and Russian needs no word for "alone".']),
]
