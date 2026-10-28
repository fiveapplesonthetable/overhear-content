# Authoring module for kukhnya-s05e03-scene-06.
ID = 'kukhnya-s05e03-scene-06'
SHOW = 'kukhnya'
SEASON = 5
EPISODE = 3
SCENE = 6
TITLE = "Контракт Баринова спасает Дениса  (Barinov's Contract Saves Denis)"
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'denis': 'Денис', 'eleonora': 'Элеонора'}
SOURCE_NAME = 'Кухня (Kukhnya) S5.03'
SOURCE_FILE = 'sources/kukhnya/s05/e03.ru.srt'
INTRO = 'On his way out of the hotel, Chef Barinov learns that Eleonora just fired Denis—and immediately storms back to invoke a clause in his contract stating that only the head chef can hire or fire cooks. Listen to the showdown.'
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = "And that brings Chef Barinov roaring back to defend his kitchen brigade. Notice how he uses his contract with Eleonora's late husband to trump her authority. See you next time!"
CLOSING = ('barinov', 'Пока!')
STORY = [
    ('denis', 'И куда вы сейчас идёте?', 'And where are you going right now?', [(90, 'И куда?')], 'adapted'),
    ('barinov', 'В наше счастливое будущее.', 'Into our happy future.', [(90, 'В счастливое будущее')], 'adapted'),
    ('denis', 'Меня только что уволили.', 'They just fired me.', [(91, 'Меня уволили')], 'adapted'),
    ('barinov', 'Ну вот, пожалуйста, уже началось.', 'Well, there you go, it has started already.', [(91, 'Ну вот, пожалуйста, началось')], 'verbatim'),
    ('barinov', 'Кто это тебя уволил?', 'Who fired you?', [(92, 'Кто тебя уволил?')], 'adapted'),
    ('denis', 'Хозяйка отеля, Элеонора Андреевна.', 'The hotel owner, Eleonora Andreevna.', [(92, 'Андреевна')], 'adapted'),
    ('barinov', 'Так зовут мою бывшую жену.', "That is my ex-wife's name.", [(93, 'Так зовут мою бывшую жену')], 'verbatim'),
    ('barinov', 'Никто тебя здесь не уволит.', 'Nobody is going to fire you here.', [(96, 'Никто тебя не уволит')], 'adapted'),
    ('barinov', 'Чем тебе Денис не понравился?', 'Why did you not like Denis?', [(97, 'чем тебе Денис не понравился?')], 'verbatim'),
    ('eleonora', 'Он мне очень даже понравился.', 'I actually liked him very much.', [(99, 'Очень даже понравился')], 'adapted'),
    ('eleonora', 'Но он не умеет готовить.', 'But he does not know how to cook.', [(102, 'Он не умеет готовить')], 'verbatim'),
    ('barinov', 'Ты никого не уволишь из моей команды.', 'You will not fire anyone from my team.', [(107, 'Ты никого не уволишь из моей команды')], 'verbatim'),
    ('barinov', 'По контракту только я могу увольнять.', 'Under the contract, only I can fire cooks.', [(109, 'контракту только я могу нанимать и увольнять')], 'adapted'),
    ('eleonora', 'Ты сказал, что не будешь работать.', 'You said you would not work for me.', [(110, 'Ты же сказал, что больше не будешь на меня работать')], 'adapted'),
    ('barinov', 'Это твой муж меня нанимал.', 'It was your husband who hired me.', [(112, 'Это он меня нанимал')], 'adapted'),
    ('barinov', 'Пусть он сообщит об этом лично.', 'Let him inform me of that in person.', [(113, 'пусть сообщит об этом лично')], 'verbatim'),
]
WALK = [
    (0, None, "'And where are you going right now?' Denis challenges briskly where this conversation is heading next."),
    (1, None, '\'Into our happy future.\' Barinov proceeds evenly right here and centers the thought on "schastlivoye" ("happy, lucky", from "schastlivyy") without wasting a word.'),
    (2, None, "'They just fired me.' Jumping in plainly in this beat, spoken Russian compresses the whole thought into just 4 words, skipping the extra helper words English needs."),
    (3, None, "'Well, there you go, it has started already.' Barinov continues openly without any doubt, so Denis knows he is not just making small talk."),
    (4, None, '\'Who fired you?\' Barinov answers directly before Denis and leans on "uvolil" ("to fire, to dismiss", a form of "uvolit") to give the remark its edge.'),
    (5, None, "'The hotel owner, Eleonora Andreevna.' Discussing the landlady with Eleonora, spoken Russian compresses the whole thought into just 4 words, skipping the extra helper words English needs."),
    (6, None, "'That is my ex-wife's name.' Barinov proceeds earnestly during the talk, without trying to dress up how he really feels."),
    (7, None, '\'Nobody is going to fire you here.\' Barinov chimes in candidly beside Denis and leans on "uvolit" ("will fire") to give the whole sentence its punch.'),
    (8, None, '\'Why did you not like Denis?\' Pressing on candidly right here, the "-sya" ending on "ponravilsya" ("was liked, pleased") marks an action that unfolds mutually or turns back on the speaker.'),
    (9, None, "'I actually liked him very much.' Eleonora pushes back earnestly facing Barinov, shifting the mood of the conversation in a single beat."),
    (10, None, '\'But he does not know how to cook.\' Eleonora chimes in candidly in front of Barinov and reaches for the Russian word "gotovit" ("to cook") right at the heart of the line.'),
    (11, None, "'You will not fire anyone from my team.' Barinov fires back candidly with a sigh, steering the talk right where he wants it."),
    (12, None, "'Under the contract, only I can fire cooks.' Barinov answers candidly with a nod, so Eleonora knows he is not just making small talk."),
    (13, None, '\'You said you would not work for me.\' Eleonora fires back firmly before Barinov and chooses "rabotat" ("to work") so Barinov gets the point right away.'),
    (14, None, "'It was your husband who hired me.' Barinov pushes back evenly without a pause, so Eleonora knows he is not just making small talk."),
    (15, None, "'Let him inform me of that in person.' Barinov counters earnestly without holding back, so Eleonora knows he is not just making small talk."),
]
