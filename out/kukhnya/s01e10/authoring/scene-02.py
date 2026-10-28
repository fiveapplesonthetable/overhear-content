# Authoring module for kukhnya-s01e10-scene-02.
ID = 'kukhnya-s01e10-scene-02'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 10
SCENE = 2
TITLE = 'Утренний рассол  (Morning Brine)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'senya': 'Сеня'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.10'
SOURCE_FILE = 'sources/kukhnya/s01/e10.ru.dual.srt'
INTRO = 'Back in the kitchen of Claude Monet, the morning after a football match. Barinov has a hangover, and Senya, the meat cook, arrives with the traditional Russian cure. No need to catch everything on the first pass.'
OPENER = 'Now, step by step.'
TRANSITION = 'Listen to it once more.'
OUTRO = 'Barinov has his brine and his bad mood. Spartak has lost again, so the day will be a hard one for everybody in the kitchen. Talk soon.'
CLOSING = ('senya', 'Пока!')
STORY = [
    ('senya', 'Шеф, как ваше здоровье сегодня утром?', 'Chef, how is your health this morning?', [(4, 'Шеф!')], ''),
    ('barinov', 'Сеня, отойди, у меня болит голова.', 'Senya, step back, my head hurts.', [], ''),
    ('senya', 'Я принёс вам холодный свежий рассол.', 'I brought you cold fresh brine.', [(5, 'Рассольчик!')], ''),
    ('barinov', 'О, Сеня, ты настоящий верный друг.', 'Oh, Senya, you are a true loyal friend.', [], ''),
    ('senya', 'Выпейте немного, сразу станет гораздо легче.', 'Drink a little, it will immediately become much easier.', [], ''),
    ('barinov', 'Этот напиток очень помогает мне.', 'This drink helps me very much.', [], ''),
    ('senya', 'Вчера Спартак снова проиграл важный матч?', 'Did Spartak lose an important match again yesterday?', [], ''),
    ('barinov', 'Не говори мне про этот кошмар.', 'Do not talk to me about that nightmare.', [], ''),
    ('senya', 'Понятно, шеф, больше никаких лишних слов.', 'Understood, chef, no more unnecessary words.', [], ''),
    ('barinov', 'Принеси мне ещё один стакан рассола.', 'Bring me one more glass of brine.', [], ''),
    ('senya', 'Сейчас быстро принесу из нашей кухни.', 'I will quickly bring it now from our kitchen.', [], ''),
    ('barinov', 'И начинайте готовить обед для гостей.', 'And begin preparing lunch for the guests.', [], ''),
    ('senya', 'Всё будет готово вовремя, шеф.', 'Everything will be ready on time, chef.', [], ''),
]
WALK = [
    (0, None, '\'Chef, how is your health this morning?\' Senya says "vashe", the polite "your", to the boss. "Zdorovye", "health", is also what Russians toast with: "za zdorovye". "Segodnya utrom" is "today in the morning".'),
    (1, None, '\'Senya, step back, my head hurts.\' Russian says "u menya bolit golova", "at me hurts head", with no "my". "Otoydi" is "step away", and the ot- in front means "away from".'),
    (2, None, '\'I brought you cold fresh brine.\' Brine from a jar of pickled cucumbers is the classic Russian hangover cure. "Prinyos" is "brought", from "prinesti". And "vam", "to you", is the polite one.'),
    (3, None, '\'Oh, Senya, you are a true loyal friend.\' Two describing words come before "drug", "friend": "nastoyashchy", "real", and "verny", "faithful". "Verny" is a relative of "vera", "faith".'),
    (4, None, '\'Drink a little, it will immediately become much easier.\' "Vypeyte" is the polite "drink", with -te, as Senya speaks to the chef. "Legche", "easier", is "legko" in its "more" form, and "gorazdo" is "much".'),
    (5, None, '\'This drink helps me very much.\' Russian says "pomogaet mne", "helps to me". "Napitok", "drink", is built on "pit", "to drink". Barinov says it like a man giving a review.'),
    (6, None, '\'Did Spartak lose an important match again yesterday?\' "Vchera" is "yesterday". "Match" is borrowed as "match", with no change. Senya knows he is poking a sore spot.'),
    (7, None, '\'Do not talk to me about that nightmare.\' "Koshmar", "nightmare", is used for anything awful, not just bad dreams. "Pro" is "about", and it keeps "koshmar" as it is. Barinov wants the subject closed.'),
    (8, None, '\'Understood, chef, no more unnecessary words.\' "Ponyatno", "it is clear", is the Russian for "understood". "Nikakikh lishnikh slov" is "no extra words": "slovo" becomes "slov" after "no".'),
    (9, None, '\'Bring me one more glass of brine.\' "Prinesi" is "bring", said to one person. "Stakan rassola" is "glass of brine", with "rassol" becoming "rassola". A "stakan" is a tumbler, not a glass on a stem.'),
    (10, None, '\'I will quickly bring it now from our kitchen.\' "Prinesu" is "I will bring", and "prinyos" was "brought". "Iz nashey kukhni" is "from our kitchen": after "iz", "kukhnya" becomes "kukhni".'),
    (11, None, '\'And begin preparing lunch for the guests.\' "Nachinayte" ends in -te, because he is speaking to the whole kitchen. "Obed" is the midday meal, the main one in Russia. "Dlya gostey" is "for the guests".'),
    (12, None, '\'Everything will be ready on time, chef.\' "Vovremya", "on time", is one word made of "v", "in", and "vremya", "time". "Vsyo", "everything", makes it "gotovo" with -o.'),
]
