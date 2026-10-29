# Authoring module for kukhnya-s01e03-scene-16.
ID = 'kukhnya-s01e03-scene-16'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 3
SCENE = 16
TITLE = 'Комплимент от шефа  (A Compliment from the Chef)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'vadim': 'Вадим'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.03'
SOURCE_FILE = 'sources/kukhnya/s01/e03.ru.dual.srt'
INTRO = 'The chef brings a complimentary dish to the birthday table himself, and the guest, Vadim, is charmed, even offering to help him in the city. Then Barinov tastes the sauce and cannot bear what he finds. Here is the Russian first.'
OPENER = "Let's go through the table talk."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = 'The chef whisks the plate away, because even a free dish has to be perfect. Take away "pere-", the prefix for "over" and "again", which you\'ve now met in two words.'
CLOSING = ('barinov', 'Пока!')
STORY = [
    ('barinov', 'Добрый вечер, дорогие гости нашего ресторана!', 'Good evening, dear guests of our restaurant!', [(280, 'Добрый вечер')], ''),
    ('vadim', 'Добрый вечер, шеф-повар!', 'Good evening, head chef!', [(280, 'Добрый вечер')], ''),
    ('barinov', 'Я принёс вам особенный сюрприз.', 'I brought you a special surprise.', [(283, 'маленький сюрприз')], ''),
    ('barinov', 'Это комплимент в честь дня рождения.', 'This is a compliment in honor of the birthday.', [(284, 'Это комплимент от шефа'), (284, 'дня рождения')], ''),
    ('vadim', 'Спасибо большое, всё выглядит очень вкусно!', 'Thank you very much, everything looks very delicious!', [(285, 'Все так вкусно')], ''),
    ('vadim', 'Я вижу, что вы отличный повар.', 'I see that you are an excellent cook.', [(286, 'я вижу')], ''),
    ('vadim', 'Я могу вам помочь в городе.', 'I can help you in the city.', [(287, 'могу вам кое-чем помочь')], ''),
    ('vadim', 'Позвоните мне завтра в любое время.', 'Call me tomorrow at any time.', [(288, 'Позвоните мне завтра')], ''),
    ('barinov', 'Спасибо, для меня это большая честь!', 'Thank you, this is a great honor for me!', [], ''),
    ('barinov', 'Подождите, я сначала сам попробую блюдо.', 'Wait, I will taste the dish myself first.', [(289, 'я сначала попробую')], ''),
    ('barinov', 'Ой, повар слишком сильно переперчил соус!', 'Oh, the cook put way too much pepper in the sauce!', [(290, 'Переперчел')], ''),
    ('vadim', 'А по-моему, получилось довольно вкусно.', 'And in my opinion, it turned out quite delicious.', [(293, 'По-моему, вкусно')], ''),
    ('barinov', 'Нет, я немедленно всё переделаю!', 'No, I will immediately redo everything!', [(292, 'Я переделаю и принесу')], ''),
    ('barinov', 'Я лично принесу вам идеальное блюдо.', 'I will personally bring you an ideal dish.', [(292, 'Я переделаю и принесу')], ''),
]
WALK = [
    (0, None, '\'Good evening, dear guests of our restaurant!\' "Dobryy vecher" is masculine, like "vecher". "Dorogiye", dear, also means "expensive", and "nashego restorana" is "of our restaurant".'),
    (1, None, '\'Good evening, head chef!\' Vadim gives back the same greeting. "Shef-povar" glues "shef" to "povar", cook, and it\'s the formal title.'),
    (2, None, '\'I brought you a special surprise.\' "Prinyos", brought, is a man\'s form; a woman would say "prinesla". "Vam" is "to you", and "syurpriz" came from French.'),
    (3, None, '\'This is a compliment in honor of the birthday.\' In a restaurant a "kompliment" is a free dish from the kitchen. A birthday is "den\' rozhdeniya", day of birth, and after "v chest\'", in honour of, "den\'" becomes "dnya".'),
    (4, None, '\'Thank you very much, everything looks very delicious!\' "Spasibo bol\'shoye" is "thanks big". After "vyglyadit", looks, comes "vkusno", tasty, with an -o.'),
    (5, None, '\'I see that you are an excellent cook.\' "Ya vizhu, chto" is "I see that". "Otlichnyy", excellent, is from "otlichat\'sya", to stand out.'),
    (6, None, '\'I can help you in the city.\' "Pomoch\' vam" is "to help to you", with the "to" form again. "V gorode" is "in the city", with -e after "v".'),
    (7, None, '\'Call me tomorrow at any time.\' "Pozvonite", call, has "zvon", a ringing, at its heart. "V lyuboye vremya" is "at any time", and "zavtra" is "tomorrow".'),
    (8, None, '\'Thank you, this is a great honor for me!\' "Chest\'" is the "honour" from "v chest\'". "Dlya menya" is "for me", and "bol\'shaya" is feminine to match "chest\'".'),
    (9, None, '\'Wait, I will taste the dish myself first.\' "Podozhdite", wait, has the -te of the polite form. "Snachala", first, grows out of "nachalo", beginning, and "sam" is "myself".'),
    (10, None, '\'Oh, the cook put way too much pepper in the sauce!\' "Pereperchil" is "pere-", over, plus "perets", pepper: he over-peppered it. "Slishkom sil\'no" is "too strongly".'),
    (11, None, '\'And in my opinion, it turned out quite delicious.\' "Po-moyemu" is "by mine", the Russian "in my opinion". "Dovol\'no", quite, shares a root with "dovolen", pleased.'),
    (12, None, '\'No, I will immediately redo everything!\' "Peredelayu" uses "pere-" again, now meaning "over again": I\'ll redo it. "Nemedlenno" is "ne" plus "medlenno", slowly.'),
    (13, None, '\'I will personally bring you an ideal dish.\' "Prinesu" is "I\'ll bring", from the same verb as "prinyos". "Lichno" is "personally", and "ideal\'noye blyudo" is "ideal dish".'),
]
