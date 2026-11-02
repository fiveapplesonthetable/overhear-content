# Authoring module for domashniy-arest-s01e01-scene-06.
ID = 'domashniy-arest-s01e01-scene-06'
SHOW = 'domashniy-arest'
SEASON = 1
EPISODE = 1
SCENE = 6
TITLE = 'Старый знакомый  (An Old Acquaintance)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'arkady': 'Аркадий', 'lydia': 'Лидия Алексеевна', 'samson': 'Самсон'}
SOURCE_NAME = 'Домашний арест (Domashniy Arest) S1.01'
SOURCE_FILE = 'sources/domashniy-arest/s01/e01.ru.dual.srt'
INTRO = "Now we're in the mayor's office. Last time, Arkady told his wife he had an emergency meeting tonight, though the caller was clearly a woman. Today his secretary, Lidia Alekseyevna, comes in with a visitor who won't take no for an answer: Samson, the big boy who bullied little Arkady in the communal flat. Let's listen in Russian first."
OPENER = "Let's go back through it. The secretary is clearly annoyed with this visitor."
TRANSITION = "Let's hear the whole thing again from the start."
OUTRO = "Samson has just quit his job on the spot, trusting the boy he once bullied. Listen for 'I'm very glad to see you' when you watch. See you next time!"
CLOSING = ('samson', 'Всё, до свидания!')
STORY = [
    ('lydia', 'Аркадий Борисович, извините, тут к вам человек.', "Arkady Borisovich, I'm sorry, there's a man here to see you.", [(212, 'Аркадий Борисович, извините')], "'тут к вам человек' new (cue 213 'вот человек, который...')"),
    ('lydia', 'Я ему сказала, что сегодня вы не принимаете.', "I told him you're not seeing anyone today.", [(214, 'я ему сказала, что')], "'у вас сегодня неприёмный день' -> 'сегодня вы не принимаете'"),
    ('arkady', 'Всё нормально, Лидия Алексеевна.', "It's all right, Lidia Alekseyevna.", [(216, 'Все нормально')], "garbled name 'Олегия' -> 'Лидия'"),
    ('arkady', 'Ну, здравствуй, Самсон.', 'Well, hello, Samson.', [(217, 'Ну, здравствуй, Самсон')], ''),
    ('samson', 'Узнал. Спасибо, что принял меня.', 'You recognised me. Thanks for seeing me.', [(219, 'Узнал'), (220, 'Спасибо, что принял меня')], ''),
    ('samson', 'Я думал, может, не примешь.', "I thought maybe you wouldn't see me.", [(221, 'Я думал, может')], "'пошлёшь' (tell me to get lost) -> 'не примешь'"),
    ('arkady', 'Ну что ты? Я очень рад тебя видеть.', "Oh, come on! I'm very glad to see you.", [(222, 'Ну что ты'), (224, 'Я очень рад тебя видеть')], ''),
    ('arkady', 'Ну, рассказывай, как дела?', 'So, tell me, how are you doing?', [(225, 'Ну, рассказывай, как дела')], ''),
    ('samson', 'Всё нормально. Работаю на стройке.', "Everything's fine. I work on a building site.", [(226, 'Все нормально'), (239, 'Работаю на стройке')], ''),
    ('samson', 'Аркаш, попросить тебя хотел.', 'Arkash, I wanted to ask you something.', [(250, 'Аркаш'), (251, 'Попросить тебя хотел')], ''),
    ('samson', 'Экскаваторщик — это не мой уровень. Может, поможешь?', "Excavator driver isn't my level. Maybe you could help?", [(253, 'экскаваторщик не мой уровень'), (254, 'Может, поможешь')], "'это' added"),
    ('arkady', 'Конечно, помогу. Кто у вас сейчас начальник?', "Of course I'll help. Who's your boss now?", [(256, 'Конечно, помогу'), (261, 'у вас сейчас начальник')], "'там' dropped"),
    ('samson', 'Ну, это Головамзюк.', "Well, it's Golovamzyuk.", [(262, 'Ну, это Головамзюк')], ''),
    ('arkady', 'Давай мы его уволим, а тебя на его место назначим.', "Let's fire him and put you in his place.", [(264, 'мы его уволим'), (265, 'а тебя на его место назначим')], "'давай-ка' -> 'давай', crude 'к чертям' dropped"),
    ('samson', 'Да ладно, что, серьёзно?', 'No way, what, seriously?', [(267, 'Да ладно, что серьезно')], ''),
    ('arkady', 'Конечно. Звони ему.', 'Of course. Call him.', [(268, 'конечно'), (272, 'Звони ему')], ''),
    ('samson', 'Николай Филиппович, я сейчас в кабинете у мэра.', "Nikolai Filippovich, I'm in the mayor's office right now.", [(280, 'Николай Филиппович'), (283, 'Я сейчас'), (283, 'в кабинете у мэра')], "'нахожусь' dropped"),
    ('samson', 'Теперь я начальник нашей стройки. Ты уволен!', "Now I'm the boss of our building site. You're fired!", [(285, 'теперь я начальник нашей стройки'), (286, 'Ты уволен')], 'crude insults at 287-289 dropped'),
]
WALK = [
    (0, None, ["'Arkady Borisovich, I'm sorry, there's a man here to see you.' Literally, 'here, to you, a man' — ", ('lydia', 'тут к вам человек'), " — needs no action word at all. She explains that she tried to stop him."]),
    (1, None, ["'I told him you're not seeing anyone today.' The action word for 'told', ", ('lydia', 'сказала'), ", ends in an 'a' sound for a female speaker, and Lidia uses the formal word for 'you', ", ('lydia', 'вы'), ", with her boss. Arkady waves it away."]),
    (2, None, ["'It's all right, Lidia Alekseyevna.' The phrase ", ('arkady', 'Всё нормально'), " — literally 'everything is normal' — is an all-purpose expression meaning 'it's fine'. Then he looks at his visitor."]),
    (3, None, ["'Well, hello, Samson.' Notice the term for 'hello', ", ('arkady', 'здравствуй'), ", without the polite ending: that's the familiar greeting for someone you know well. Samson is surprised."]),
    (4, 'Узнал.', ["'You recognised me.' The single action word ", ('samson', 'Узнал'), " translates to 'recognised', leaving the 'you' unspoken. Then he says thank you."]),
    (4, 'Спасибо, что принял меня.', ["'Thanks for seeing me.' Literally, 'thank you that you received me' — ", ('samson', 'Спасибо, что'), " — is how Russian thanks someone for doing something. He admits he was worried."]),
    (5, None, ["'I thought maybe you wouldn't see me.' the Russian word ", ('samson', 'может'), " is everyday shorthand for 'maybe', followed by ", ('samson', 'не примешь'), ", which translates to 'you won't receive'. Arkady acts as if their childhood never happened."]),
    (6, None, ["'Oh, come on! I'm very glad to see you.' The phrase ", ('arkady', 'Ну что ты'), " translates to 'oh, don't be silly!', brushing away an apology, and the describing word for 'glad', ", ('arkady', 'рад'), ", is the male speaker's form. A woman uses a different ending."]),
    (7, None, ["'So, tell me, how are you doing?' The action word ", ('arkady', 'рассказывай'), " warmly translates to 'tell me all about it', paired with the classic phrase for 'how are things?', ", ('arkady', 'как дела'), ". Samson answers simply."]),
    (8, None, ["'Everything's fine. I work on a building site.' Notice the phrase for 'on a building site', ", ('samson', 'на стройке'), ": after the little word for 'on', the translation for 'building site' shifts its ending to mark location."]),
    (9, None, ["'Arkash, I wanted to ask you something.' Dropping the final sound from the name to make it ", ('samson', 'Аркаш'), " sounds warm and colloquial, and putting the action word for 'wanted', ", ('samson', 'хотел'), ", at the end makes the request sound bashful."]),
    (10, None, ["'Excavator driver isn't my level. Maybe you could help?' The long word for 'excavator driver', ", ('samson', 'экскаваторщик'), ", is built from the machine's name, and the phrase ", ('samson', 'может, поможешь'), " literally translates to 'maybe you'll help?'."]),
    (11, None, ["'Of course I'll help. Who's your boss now?' The question literally asks 'who at you now is boss?' — ", ('arkady', 'кто у вас сейчас начальник'), " — saving the expression for 'boss' for the end. Samson names him."]),
    (12, None, ["'Well, it's Golovamzyuk.' The little word ", ('samson', 'это'), ", which translates to 'this is', introduces the boss's surname after a hesitant start. Arkady has a bold idea."]),
    (13, None, ["'Let's fire him and put you in his place.' the term meaning 'let's', ", ('arkady', 'давай'), ", teams up with the phrase ", ('arkady', 'мы его уволим'), ", which translates to 'we'll fire him', proposing an action together. Samson can't believe his luck."]),
    (14, None, ["'No way, what, seriously?' The phrase ", ('samson', 'Да ладно'), " is a favourite Russian reaction that translates to 'get out of here, really?'. Arkady pushes him on."]),
    (15, None, ["'Of course. Call him.' The phrase ", ('arkady', 'Звони ему'), " translates to 'ring him!', putting the expression meaning 'he' into its 'to him' form. So Samson dials his boss right there."]),
    (16, None, ["'Nikolai Filippovich, I'm in the mayor's office right now.' The phrase ", ('samson', 'в кабинете у мэра'), " literally translates to 'in the office at the mayor's'. And then comes the big news."]),
    (17, None, ["'Now I'm the boss of our building site. You're fired!' Suddenly formal address vanishes: the phrase ", ('samson', 'ты уволен'), " switches to the blunt word for 'you', ", ('samson', 'ты'), ", to tell his old boss 'you're sacked!'."]),
]
