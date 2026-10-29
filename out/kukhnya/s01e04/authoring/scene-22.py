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
    (0, None, '\'They will not take this guy anywhere anymore!\' "Ne voz\'mut" is "they won\'t take", with nobody named. "Nikuda" is "nowhere".'),
    (1, None, '\'Viktor, we need to talk urgently.\' Vika calls him "Viktor", without his father\'s name. "Nam nuzhno" is "to us it\'s needed".'),
    (2, None, '\'I do not want to talk about this cook.\' "Ob etom povare" is "about this cook", with "ob" before a vowel and -e on "povar".'),
    (3, None, '\'Max did not go to that interview.\' The verb "khodit\'" means going there and back, so "ne khodil" says he never made the trip at all. "Sobesedovaniye", an interview, is built on "beseda", a conversation.'),
    (4, None, '\'What are you saying right now?\' "Chto ty takoye govorish\'?" is "what such are you saying?", a surprised question.'),
    (5, None, '\'It was I who went to the other restaurant.\' "Eto ya" puts the spotlight on "I". "Khodila" ends in -la for a woman, and "chuzhoy" is "someone else\'s".'),
    (6, None, '\'Max really is a very talented guy.\' "Talantlivyy" is "talant" made into an adjective. "Deystvitel\'no" is "really".'),
    (7, None, '\'But you do not let him grow at all.\' "Ne dayosh\' yemu rasti" is "you don\'t give him to grow", the same pattern as "ne dayote mne gotovit\'".'),
    (8, None, '\'How many good people have left here?\' "Skol\'ko" is "how many", and after it "lyudi" becomes "lyudey". "Ushli" is "left".'),
    (9, None, '\'Stop giving me your moral lectures!\' "Nravoucheniya" joins "nrav", morals, and "uchit\'", to teach. "Khvatit" is "enough".'),
    (10, None, '\'I simply genuinely feel sorry for this guy.\' "Mne zhal\'" is "to me it\'s a pity", and the person pitied takes the "of" form, "etogo parnya". "Iskrenne" is "sincerely".'),
    (11, None, '\'Can I say that he is not fired?\' "Mogu" is "I can". "Ne uvolen" is the short "not fired".'),
    (12, None, '\'Do what you want, just leave me alone!\' "Delay chto khochesh\'" is "do what you want". "Ostav\' menya", leave me, is the command of "ostavit\'", to leave behind, and Russian needs no word for "alone".'),
]
