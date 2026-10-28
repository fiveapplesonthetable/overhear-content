# Authoring module for domashniy-arest-s01e02-scene-03.
ID = 'domashniy-arest-s01e02-scene-03'
SHOW = 'domashniy-arest'
SEASON = 1
EPISODE = 2
SCENE = 3
TITLE = "Я не вор  (I'm Not a Thief)"
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'arkady': 'Аркадий', 'samson': 'Самсон'}
SOURCE_NAME = 'Домашний арест (Domashniy Arest) S1.02'
SOURCE_FILE = 'sources/domashniy-arest/s01/e02.ru.dual.srt'
INTRO = "Now back to the present, and to the communal flat. So tonight, over a bottle of cheap vodka in the shared kitchen, he gives his candidate a lesson. Let's listen in Russian first."
OPENER = "Let's go through it slowly. The vodka is terrible, but Samson has a kind word for it, and Arkady has big plans for him."
TRANSITION = "Let's hear the whole lesson again."
OUTRO = "Later that night Arkady can't sleep in his old room, he hates every piece of furniture in it, and old Klavdia Viktorovna from down the corridor tells him he's in hell now because he couldn't even steal properly. Let that be the lesson of the evening, and. See you next time!"
CLOSING = ('samson', 'Пока!')
STORY = [
    ('samson', 'Водка — жидкий хлеб.', 'Vodka is liquid bread.', [(88, 'Водка, жидкий хлеб')], 'speaker not marked in the subtitles; given to Samson'),
    ('arkady', 'Классный из тебя мэр получится, Самсон.', "You'll make a great mayor, Samson.", [(89, 'Классный из тебя мэр получится, Самсон')], ''),
    ('arkady', 'Живот у тебя, как у депутата.', "You've got a belly like a member of parliament.", [(91, 'у тебя')], "adapted from cues 91-92: slang 'Булька' -> 'Живот'; 'как будто всю жизнь в Государственной думе просидел' -> 'как у депутата'"),
    ('samson', 'Угу.', 'Uh-huh.', [(93, 'Угу')], ''),
    ('arkady', 'Смотри. Я снимаю кольцо.', "Watch. I'm taking off my ring.", [(99, 'снимаю')], "cue 99 is garbled ('книгу'); its English says 'ring'. 'Смотри' added"),
    ('samson', 'Что ты снимаешь? Почему?', 'What are you taking off? Why?', [(100, 'ты снимаешь? Почему')], "'Чё это' -> 'Что'"),
    ('arkady', 'Потому что я не вор.', "Because I'm not a thief.", [(101, 'Потому что я не вор')], ''),
    ('samson', 'Я ничего не понял, Аркаш.', "I didn't understand a thing, Arkash.", [(104, 'Я ничего не понял, Аркаш')], ''),
    ('arkady', 'Я человек чистый. Я вообще не вор.', "I'm an honest man. I'm not a thief at all.", [(105, 'Я человек чистый'), (106, 'не вор')], "cue 106 'Я вот здесь не вор вообще' -> 'Я вообще не вор'"),
    ('arkady', 'Вот так на митингах говори, запомни.', "That's how you talk at rallies, remember that.", [(107, 'Вот так на митингах говори, запомни')], ''),
    ('samson', 'А, на митингах, да.', 'Ah, at rallies, right.', [(108, 'А, на митингах, да')], ''),
    ('arkady', 'Вор, вор. Откуда это слово?', 'Thief, thief. Where does that word come from?', [(109, 'Вор, вор. Откуда это слово')], ''),
    ('arkady', 'Это бизнес, Самсон. Бизнес.', "It's business, Samson. Business.", [(110, 'Это бизнес, Самсон. Бизнес')], ''),
    ('samson', 'Бизнес?', 'Business?', [], 'new: Samson repeats the word'),
    ('arkady', 'Какая разница, кто будет строить дороги?', 'What does it matter who builds the roads?', [(111, 'Какая разница, кто')], "'дороги тебе будет строить' -> 'будет строить дороги'"),
    ('arkady', 'Моя фирма или дяди из Москвы.', 'My firm, or some guys from Moscow.', [(112, 'Моя фирма'), (114, 'дяди из Москвы')], "'Или' moved to the middle"),
    ('samson', 'Поехали!', 'Here we go!', [(115, 'Поехали')], 'speaker not marked; given to Samson (the toast)'),
]
WALK = [
    (0, None, "'Vodka is liquid bread.' An old drinking joke: it's made from grain, so it must be food. In Russian there is no word for 'is' in a sentence like this; the dash does the job."),
    (1, None, "'You'll make a great mayor, Samson.' Literally, 'a great mayor will come out of you'. The first word is a casual 'great, cool'. Then Arkady looks his candidate up and down."),
    (2, None, "'You've got a belly like a member of parliament.' The phrase in the middle, literally 'at you', is how Russians say 'you have'. In Arkady's world, that's a compliment. Samson just nods."),
    (3, None, "'Uh-huh.' Not a word, just a sound for 'yes'. Now Arkady shows him how a candidate should look."),
    (4, None, "'Watch. I'm taking off my ring.' The first word is a casual command, 'look'. An expensive ring doesn't look good on a man of the people. Samson is puzzled."),
    (5, None, "'What are you taking off? Why?' Two short questions. Notice the verb ending changes: Arkady said it with 'I', Samson says it with 'you'. And the answer comes straight away."),
    (6, None, "'Because I'm not a thief.' The first two words together mean 'because'. Samson still doesn't get it."),
    (7, None, "'I didn't understand a thing, Arkash.' Russian likes a double negative: literally, 'I nothing not understood'. The verb is past tense with no ending, because Samson is a man. So Arkady spells it out."),
    (8, 'Я человек чистый.', "'I'm an honest man.' Literally, 'I am a clean man', with the adjective after the noun for a bit of weight."),
    (8, 'Я вообще не вор.', "'I'm not a thief at all.' The word in the middle means 'at all', and it makes the denial stronger."),
    (9, None, "'That's how you talk at rallies, remember that.' Two commands: 'say' and 'remember'. The phrase about rallies uses the word for 'at, on', and the noun changes its ending after it. Samson repeats it, slowly."),
    (10, None, "'Ah, at rallies, right.' Then Arkady gets philosophical."),
    (11, None, "'Thief, thief. Where does that word come from?' The question word means 'where from'. Arkady has his own answer."),
    (12, None, "'It's business, Samson. Business.' The same word as in English. Samson tries it out."),
    (13, None, "'Business?' He doesn't sound convinced. So Arkady explains how roads get built."),
    (14, None, "'What does it matter who builds the roads?' The first two words mean 'what difference'. The verb is in the future, made with the verb 'to be' plus a basic form: 'will build'."),
    (15, None, "'My firm, or some guys from Moscow.' Literally, 'uncles from Moscow', a casual way to say 'some people'. So the mayor's own company was building the town's roads. Samson raises his glass."),
    (16, None, "'Here we go!' Literally, 'we've set off'. It's what the first man in space said at take-off, and it's a favourite toast."),
]
