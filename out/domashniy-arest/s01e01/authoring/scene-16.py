# Authoring module for domashniy-arest-s01e01-scene-16.
ID = 'domashniy-arest-s01e01-scene-16'
SHOW = 'domashniy-arest'
SEASON = 1
EPISODE = 1
SCENE = 16
TITLE = 'Снова дома, с браслетом  (Home Again, with a Tag)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'arkady': 'Аркадий', 'klavdia': 'Клавдия Викторовна', 'officer': 'Офицер'}
SOURCE_NAME = 'Домашний арест (Domashniy Arest) S1.01'
SOURCE_FILE = 'sources/domashniy-arest/s01/e01.ru.dual.srt'
INTRO = "Back in the communal flat, a little later. Now two officers from the prison service knock on the door with Arkady between them; we'll hear it in Russian first, so don't worry about catching every word."
OPENER = "Let's walk through it. The officer starts at the front door, all business."
TRANSITION = "Right, here's the whole scene once more."
OUTRO = 'So the mayor is back in the flat he grew up in, with a box on a stool and a tag on his ankle. Next he meets an old acquaintance from his childhood, so see you then. See you next time!'
CLOSING = ('officer', 'Счастливо!')
STORY = [
    ('officer', 'Откройте дверь. Квартира девять?', 'Open the door. Is this flat nine?', [(603, 'Откройте дверь'), (606, 'Квартира девять')], 'cue 606 is a statement; here the officer checks it'),
    ('klavdia', 'Да. Господи, Аркашка!', 'Yes. Good Lord, Arkasha!', [(607, 'Да'), (609, 'Господи, Аркашка')], ''),
    ('arkady', 'Здравствуйте.', 'Hello.', [], "colloquial 'Здрасьте' (cue 608) written as the full polite greeting"),
    ('klavdia', 'А что случилось?', 'What happened?', [(610, 'А что')], 'стряслось-то -> случилось (plain word)'),
    ('officer', 'Гражданин Аникеев будет жить здесь.', 'Citizen Anikeev will live here.', [(611, 'гражданин Аникеев')], "'будет находиться здесь до окончания следствия' (612) simplified to 'будет жить здесь'"),
    ('officer', 'Где ваша комната?', 'Where is your room?', [(613, 'Где ваша комната')], ''),
    ('arkady', 'Где-то здесь была, а теперь нет.', "It used to be somewhere here, and now it's gone.", [(618, 'Где-то здесь была, а теперь')], "colloquial 'нету' -> 'нет'"),
    ('klavdia', 'За шкафом дверь.', 'The door is behind the wardrobe.', [(619, 'За шкафом дверь')], 'speaker of cue 619 not clear in the source; given to the neighbour'),
    ('officer', 'Заходите. Поставьте, пожалуйста, правую ногу на кровать.', 'Come in. Please put your right foot on the bed.', [(625, 'Заходите'), (634, 'поставьте, пожалуйста, правую ногу на кровать')], "name 'Аркадий Борисович' dropped"),
    ('arkady', 'Пожалуйста.', 'There you go.', [(635, 'Пожалуйста')], ''),
    ('officer', 'Это браслет. А это аппарат.', 'This is the tag. And this is the base unit.', [(628, 'браслет')], 'simplified from cues 627-628 (the stationary unit and the bracelet on the ankle)'),
    ('officer', 'Пятьдесят метров, не больше. Иначе будет сигнал.', "Fifty metres, no more. Otherwise there'll be a signal.", [(629, 'сигнал')], "simplified from cue 629 ('more than 50 metres from the unit and our control room gets a signal')"),
    ('arkady', 'Всё понятно.', 'All clear.', [(632, 'Все понятно')], ''),
    ('officer', 'Тут кнопки вызова: скорая, полиция и мы.', 'Here are the call buttons: ambulance, police, and us.', [(642, 'кнопки вызова'), (643, 'Скорая, полиция')], "'Тут' new; 'ну и мы' -> 'и мы'"),
    ('arkady', 'И всё?', "And that's it?", [(644, 'И все')], ''),
    ('officer', 'И всё. До свидания.', "That's it. Goodbye.", [(646, 'До свидания')], "'И всё.' new (replaces the officer's crude joke, cue 645)"),
    ('klavdia', 'Ну, Аркашка, с возвращением.', 'Well, Arkasha, welcome back.', [], "new: the neighbour's ironic welcome"),
]
WALK = [
    (0, 'Откройте дверь.', "'Open the door.' A command, but in the polite form, the one you use with an adult you don't know. Then he checks the number."),
    (0, 'Квартира девять?', "'Is this flat nine?' Just the word for 'flat' and the number, with a question in the voice. The old neighbour opens up, and she knows this face."),
    (1, None, "'Yes. Good Lord, Arkasha!' She uses the name she called him when he was a little boy, a fond but slightly cheeky form of Arkady. He greets her politely."),
    (2, None, "'Hello.' The long, polite greeting, the one for older people and strangers. She wants to know what's going on."),
    (3, None, "'What happened?' A very useful question. The verb is in the past tense, with the ending for 'it', because 'what' counts as 'it'. The officer answers in official language."),
    (4, None, "'Citizen Anikeev will live here.' 'Citizen' plus a surname is how officials talk. The future is easy here: 'will' plus the plain verb, just like in English. Then he turns to Arkady."),
    (5, None, "'Where is your room?' He says the polite 'your', as an official should. It's a harder question than it sounds."),
    (6, None, "'It used to be somewhere here, and now it's gone.' 'Was' has the feminine ending, to match the room. Arkady hasn't lived here for years. The neighbour helps."),
    (7, None, "'The door is behind the wardrobe.' After the word for 'behind', the wardrobe takes the same ending it would take after 'with'. Somebody pushed a wardrobe in front of his old door, so it has to be moved."),
    (8, 'Заходите.', "'Come in.' Another polite command. Inside, the officer gets down to business."),
    (8, 'Поставьте, пожалуйста, правую ногу на кровать.', "'Please put your right foot on the bed.' One word covers both 'leg' and 'foot'. The tag goes on his right ankle. Arkady does as he's told."),
    (9, None, "'There you go.' The word for 'please' again, this time meaning 'here you are'. The officer shows him two things."),
    (10, None, "'This is the tag. And this is the base unit.' The tag is called a bracelet in Russian, and the small box stays in the room. Then comes the rule."),
    (11, None, "'Fifty metres, no more. Otherwise there'll be a signal.' If Arkady walks more than fifty metres from the box, the prison service will know at once. Arkady is a quick learner."),
    (12, None, "'All clear.' Literally, 'everything is understood'. Handy whenever someone explains something to you. One last thing."),
    (13, None, "'Here are the call buttons: ambulance, police, and us.' The word for ambulance literally means 'fast', short for a fast medical car. Arkady was hoping for more."),
    (14, None, "'And that's it?' Two little words and a rising voice. The officer is in a hurry."),
    (15, None, "'That's it. Goodbye.' The standard polite goodbye; literally, 'until we see each other'. And the neighbour has the last word."),
    (16, None, "'Well, Arkasha, welcome back.' Literally, 'with the return'. You say it to someone coming home after a long time away, and here it comes with a little irony."),
]
