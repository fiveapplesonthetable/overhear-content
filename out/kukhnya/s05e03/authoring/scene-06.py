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
    (0, None, '\'And where are you going right now?\' Denis tests bluntly in their exchange, anchoring the Russian line on "kuda" ("where to") and "seychas" ("now") without extra filler.'),
    (1, None, '\'Into our happy future.\' Barinov sets a calm tempo in the conversation, anchoring the Russian line on "schastlivoye" ("happy, lucky") and "budushcheye" ("future, next") without extra filler.'),
    (2, None, '\'They just fired me.\' Denis favors a firm line as the scene unfolds, leaning on "tolko" ("only") before closing the thought with "uvolili" ("to fire, to dismiss").'),
    (3, None, '\'Well, there you go, it has started already.\' Barinov adopts an earnest approach as the scene unfolds, putting "uzhe" ("already, now") alongside "nachalos" ("to begin, to start") in a tight, everyday turn of phrase.'),
    (4, None, '\'Who fired you?\' Barinov questions briskly to make the point, building the phrase around "uvolil" ("to fire, to dismiss") and "kto" ("who") for a crisp, natural delivery.'),
    (5, None, '\'The hotel owner, Eleonora Andreevna.\' Denis establishes an earnest note on the spot, building the phrase around "khozyayka" ("landlady") and "otelya" ("of the hotel") for a crisp, natural delivery.'),
    (6, None, '\'That is my ex-wife\'s name.\' Barinov shows an earnest manner toward Denis, weaving "zovut" ("call") together with "byvshuyu" ("former, ex") just the way native speakers do.'),
    (7, None, '\'Nobody is going to fire you here.\' Barinov shows an honest footing with Eleonora, linking "zdes" ("here"), "uvolit" ("will fire"), and "nikto" ("nobody") in one brisk exchange.'),
    (8, None, '\'Why did you not like Denis?\' Barinov prompts calmly to Denis here, anchoring the Russian line on "ponravilsya" ("was liked, pleased") and "chem" ("than") without extra filler.'),
    (9, None, '\'I actually liked him very much.\' Eleonora shares a candid stance in the scene, pairing "ponravilsya" ("was liked, pleased") with "ochen" ("very much") so the "-sya" ending carries the action.'),
    (10, None, '\'But he does not know how to cook.\' Eleonora maintains a steady approach at once, leaning on "umeyet" ("knows how to") before closing the thought with "gotovit" ("to cook").'),
    (11, None, '\'You will not fire anyone from my team.\' Barinov takes an earnest position right away, linking "uvolish" ("will fire"), "komandy" ("commands"), and "ty" ("you") in one brisk exchange.'),
    (12, None, '\'Under the contract, only I can fire cooks.\' Barinov establishes an emphatic style at this moment, combining "kontraktu" ("by contract") and "tolko" ("only") so the key meaning lands right away.'),
    (13, None, '\'You said you would not work for me.\' Eleonora shares a natural direction during the exchange, putting "skazal" ("said") alongside "budesh" ("will") in a tight, everyday turn of phrase.'),
    (14, None, '\'It was your husband who hired me.\' Barinov brings a serious style in the conversation, pairing "muzh" ("husband") with "nanimal" ("hired") to get the point across in plain spoken Russian.'),
    (15, None, '\'Let him inform me of that in person.\' Barinov conveys a candid tone in the conversation, pairing "soobshchit" ("will inform") with "lichno" ("personally") to get the point across in plain spoken Russian.'),
]
