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
OUTRO = 'Vika asks whether she can say Max isn\'t fired, and the chef is too tired to refuse. Notice "ne dayosh\' yemu rasti", "you don\'t let him grow".'
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
    (0, None, '\'They will not take this guy anywhere anymore!\' "Ne voz\'mut" is "they won\'t take", with no one named. "Nikuda" is "nowhere", so the double negative is complete.'),
    (1, None, '\'Viktor, we need to talk urgently.\' Vika drops the father\'s name and just says "Viktor", which is closer than the formal version. "Nam nuzhno" is "to us necessary".'),
    (2, None, '\'I do not want to talk about this cook.\' "Ob etom povare" is "about this cook", with "ob" before a vowel and -e on the cook.'),
    (3, None, '\'Max did not go to that interview.\' Vika says Max "didn\'t go", with the round-trip kind of going, and "na to sobesedovaniye" is "to that interview".'),
    (4, None, '\'What are you saying right now?\' "Chto ty takoye govorish\'" is the surprised "what are you saying?". Russian has no "-ing" form.'),
    (5, None, '\'It was I who went to the other restaurant.\' "Eto ya" puts the spotlight on "I". "Khodila" has the "-la" of a woman.'),
    (6, None, '\'Max really is a very talented guy.\' "Talantlivyy" comes from "talant". Vika is making her case.'),
    (7, None, '\'But you do not let him grow at all.\' "Ne dayosh\' yemu rasti" is "you don\'t give him to grow", Russian for "you don\'t let him". The same pattern was "you don\'t let me cook".'),
    (8, None, '\'How many good people have left here?\' "Skol\'ko" asks "how many", and the verb comes in the plural, "ushli". "Lyudey" is the plural "of" form.'),
    (9, None, '\'Stop giving me your moral lectures!\' "Nravoucheniye" is built from "nrav", character, and "uchit\'", to teach. It is a lecture on morals.'),
    (10, None, '\'I simply genuinely feel sorry for this guy.\' "Mne zhal\'" is "to me pity", and the thing pitied goes in the "of" form. "Iskrenne" is "sincerely".'),
    (11, None, '\'Can I say that he is not fired?\' "Uvolen" is the short "fired". "Ne uvolen" is "not fired".'),
    (12, None, '\'Do what you want, just leave me alone!\' The chef gives up with "do what you want", and then "leave me", the same "ostav\' menya" as "leave me alone". The shortest surrender possible.'),
]
