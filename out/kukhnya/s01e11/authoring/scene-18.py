# Authoring module for kukhnya-s01e11-scene-18.
ID = 'kukhnya-s01e11-scene-18'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 11
SCENE = 18
TITLE = 'Неожиданное признание  (An Unexpected Confession)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'guest': 'Гость', 'vika': 'Вика'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.11'
SOURCE_FILE = 'sources/kukhnya/s01/e11.ru.dual.srt'
INTRO = "The woman who ran to the restroom has a husband, and he is waiting to pay the bill. He wants to apologise to Vika for the trouble. Listen first, and I'll explain afterwards."
OPENER = "Let's unpack it."
TRANSITION = 'Back to the full version.'
OUTRO = 'The lady is not the critic, and the mystery is not solved. Vika has another suspect. Take care until then.'
CLOSING = ('vika', 'Пока!')
STORY = [
    ('vika', 'Здравствуйте, вам понравился наш ресторан сегодня?', 'Hello, did you like our restaurant today?', [], ''),
    ('guest', 'Вы уж извините нас, ради бога.', 'Please forgive us, for the love of God.', [(221, 'Вы уж извините нас, ради бога')], ''),
    ('vika', 'Что-то случилось с вашей женой?', 'Did something happen with your wife?', [], ''),
    ('guest', 'Моя жена мне всё подробно рассказала.', 'My wife told me everything in detail.', [(220, 'Мне моя жена все рассказала')], ''),
    ('vika', 'Она отравилась каким-то нашим блюдом?', 'Did she get poisoned by some dish of ours?', [(210, 'после вашего блюда отравилась')], ''),
    ('guest', 'Нет, она вовсе не отравилась едой.', 'No, she was not poisoned by food at all.', [], ''),
    ('vika', 'Почему же ей стало так плохо?', 'Why then did she feel so ill?', [], ''),
    ('guest', 'Она беременна, уже на третьем месяце.', 'She is pregnant, already in the third month.', [(222, 'Она на третьем месяце беременности')], ''),
    ('vika', 'Так у неё просто сильный токсикоз?', 'So she just has bad morning sickness?', [(223, 'токсикоз')], ''),
    ('guest', 'Да, от запахов еды её тошнит.', 'Yes, the smells of food make her nauseous.', [], ''),
    ('vika', 'Мы очень переживали за её здоровье.', 'We were very worried about her health.', [], ''),
    ('guest', 'Спасибо вам за понимание и заботу.', 'Thank you for your understanding and care.', [], ''),
    ('vika', 'Значит, эта женщина точно не критик.', 'So this woman is definitely not the critic.', [(226, 'мы точно знаем, что критик не она')], ''),
]
WALK = [
    (0, None, '\'Hello, did you like our restaurant today?\' "Vam ponravilsya", "to you pleased", is "did you like", and "ponravilsya" ends to agree with "restoran", which is masculine. Vika opens politely.'),
    (1, None, '\'Please forgive us, for the love of God.\' "Uzh" softens the request, like "please do". "Radi boga", "for God\'s sake", has "radi", the word in Nastya\'s "radi udovolstviya", "for pleasure".'),
    (2, None, '\'Did something happen with your wife?\' "Chto-to" is "chto", "what", with -to: "something". "S vashey zhenoy" is "with your wife", with -oy endings after "s".'),
    (3, None, '\'My wife told me everything in detail.\' "Podrobno", "in detail", is the word in Max\'s "ya mogu vsyo podrobno obyasnit". "Rasskazala" is "told", with -la for the wife.'),
    (4, None, '\'Did she get poisoned by some dish of ours?\' "Kakim-to" is "kakoy", "which", with -to: "some". "Otravilas", "got poisoned", has a woman\'s -las. "Blyudom" is "by a dish".'),
    (5, None, '\'No, she was not poisoned by food at all.\' "Vovse ne", "not at all", is Barinov\'s phrase: "vovse ne v moikh stavkakh". "Edoy", "by food", is "eda" in its "by means of" form.'),
    (6, None, '\'Why then did she feel so ill?\' "Pochemu zhe" is "why then", with the little "zhe" again. "Ey stalo tak plokho", "to her became so bad", is the pattern for feeling ill.'),
    (7, None, '\'She is pregnant, already in the third month.\' Russians are "na tretyem mesyatse", "on the third month". "Beremenna", "pregnant", is a short form, and it ends in -a.'),
    (8, None, '\'So she just has bad morning sickness?\' "Toksikoz", "toxicosis", is the medical word Russians use for morning sickness. "U neyo" is "at her", the "she has" pattern. "Tak" is "so".'),
    (9, None, '\'Yes, the smells of food make her nauseous.\' "Ot zapakhov edy" is "from the smells of food", with "ot" for "from" or "because of". "Eyo toshnit", "her nauseates", has no subject.'),
    (10, None, '\'We were very worried about her health.\' "Perezhivali", "worried", is plural, because Vika speaks for the restaurant. "Zdorovye", "health", is Senya\'s word in "kak vashe zdorovye?"'),
    (11, None, '\'Thank you for your understanding and care.\' "Za" is "for". "Zabota", "care", is the word Vika used about children needing "nastoyashchey zaboty", "real care". "Ponimanie" is "understanding".'),
    (12, None, '\'So this woman is definitely not the critic.\' "Znachit", "so", literally means "means". "Tochno ne" is "definitely not". Vika crosses a suspect off her list.'),
]
