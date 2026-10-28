# Authoring module for kukhnya-s01e01-scene-06.
ID = 'kukhnya-s01e01-scene-06'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 1
SCENE = 6
TITLE = "Проигрыш Спартака  (Spartak's Loss)"
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'nastya': 'Настя', 'senya': 'Сеня'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.01'
SOURCE_FILE = 'sources/kukhnya/s01/e01.ru.dual.srt'
INTRO = "Back at Claude Monet, the kitchen is oddly silent. Nastya, a waitress, wants to know why, and Senya, one of the cooks, tells her: the chef is coming, and he is in a foul mood because of last night's football. This is the Russian first."
OPENER = 'Now the same scene, slowly.'
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = 'So the rule of the kitchen is simple: when the chef\'s team loses, you keep your head down and work. Take away "za rabotu", "to work!", because you\'ll hear it again.'
CLOSING = ('nastya', 'До встречи!')
STORY = [
    ('nastya', 'Почему на кухне так тихо?', 'Why is the kitchen so quiet?', [], ''),
    ('senya', 'Шеф идёт. Опять злой.', 'Chef is coming. Angry again.', [(60, 'О, опять')], ''),
    ('nastya', 'Что случилось? Опять футбол?', 'What happened? Football again?', [(61, 'Вчера Спартак')], ''),
    ('senya', 'Да, вчера играл Спартак.', 'Yes, yesterday Spartak played.', [(61, 'Вчера Спартак')], ''),
    ('nastya', 'И сколько он проиграл?', 'And how much did he lose?', [(61, 'Сколько')], ''),
    ('senya', 'Сто штук.', 'A hundred grand.', [(62, 'Сто штук')], ''),
    ('nastya', 'Ничего себе! Сто тысяч рублей?', 'Unbelievable! A hundred thousand rubles?', [(63, 'Ничего себе')], ''),
    ('senya', 'Да, ровно сто тысяч.', 'Yes, exactly one hundred thousand.', [], ''),
    ('senya', 'Они всегда проигрывают перед сменой.', 'They always lose before his shift.', [(63, 'всегда перед моей сменой')], ''),
    ('nastya', 'И что теперь делать?', 'And what do we do now?', [], ''),
    ('senya', 'Молчи и просто работай.', 'Stay silent and just work.', [], ''),
    ('senya', 'Не зли шефа сегодня.', 'Do not anger the chef today.', [], ''),
    ('nastya', 'Понятно. Буду очень осторожной.', 'Understood. I will be very careful.', [], ''),
    ('senya', 'Вот и молодец. За работу!', 'Good job. To work!', [], ''),
]
WALK = [
    (0, None, '\'Why is the kitchen so quiet?\' Russian says "na kukhne", "on the kitchen", where English says "in", and it\'s what everyone says about a restaurant kitchen. "Tikho" is "quiet", for a voice or a room.'),
    (1, None, '\'Chef is coming. Angry again.\' Russian covers "is coming" with "idyot", the on-foot kind. The second sentence has no "is" at all: just "again angry". "Shef" is borrowed from French "chef", meaning chief.'),
    (2, None, '\'What happened? Football again?\' "Chto sluchilos\'" is "what happened", and you\'ll use it all the time. "Futbol" is borrowed whole, and "opyat\'", "again", is Senya\'s and Nastya\'s shared word.'),
    (3, None, '\'Yes, yesterday Spartak played.\' "Vchera" is "yesterday", a handy single word. Russian puts the news first, so "igral", "played", comes before the team. Spartak is a Moscow football club, and the chef takes it personally.'),
    (4, None, '\'And how much did he lose?\' "Proigral" is "igral", played, with "pro-" in front, so losing is "playing through". "Skol\'ko" is "how much", the question you ask about prices.'),
    (5, None, '\'A hundred grand.\' "Sto shtuk" is slang: "sto" is a hundred, and "shtuka" means "a piece", which is street slang for a thousand roubles. So it\'s literally "a hundred pieces".'),
    (6, None, '\'Unbelievable! A hundred thousand rubles?\' "Nichego sebe" is literally "nothing to oneself", an exclamation of surprise like "wow". After the number, "rubles" takes a different ending, "rubley".'),
    (7, None, '\'Yes, exactly one hundred thousand.\' "Rovno" means "exactly", and it also means "even" or "level". Senya adds it because the amount is the whole point.'),
    (8, None, '\'They always lose before his shift.\' "Proigryvayut" is "proigrat\'" stretched out with "-yva-" in the middle, which makes it a habit: "they keep losing". "Pered smenoy" is "before the shift".'),
    (9, None, '\'And what do we do now?\' There\'s no "we" in Russian. "Chto delat\'" is "what to do", the plain "to do" with nothing else, and that\'s how people ask for advice.'),
    (10, None, '\'Stay silent and just work.\' "Molchi" and "rabotay" are both commands, and both are short. "Prosto" is the shrug from earlier: just work, don\'t make it complicated.'),
    (11, None, '\'Do not anger the chef today.\' "Ne zli" has "zloy", angry, inside it, which Senya used a moment ago: "don\'t make him angry". "Shefa" has an -a on the end because the chef is the one being angered. And "segodnya" is spelled with a g but said "sevodnya".'),
    (12, None, '\'Understood. I will be very careful.\' "Ponyatno" does the job of "understood". Nastya is a woman, so "careful" ends in "-oy", "ostorozhnoy": the "as a" ending, in the feminine.'),
    (13, None, '\'Good job. To work!\' "Vot i molodets" is "there you go, well done". "Molodets" is the praise word from the soup scene. "Za rabotu" is literally "for work", and it\'s how you say "let\'s get going".'),
]
