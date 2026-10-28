# domashniy-arest/s01e01/scene-06.py
ID = "domashniy-arest-s01e01-scene-06"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 1
SCENE = 6
TITLE = "Старый знакомый  (An Old Acquaintance)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.01"
SOURCE_FILE = "sources/domashniy-arest/s01/e01.ru.dual.srt"
VOICES = {"narrator": "sky", "samson": "anja", "anya": "alisa", "lydia": "angelina"}
LABELS = {"samson": "Самсон", "anya": "Аркадий", "lydia": "Лидия Алексеевна"}
INTRO = "Now we're in the mayor's office. Last time, Arkady told his wife he had an emergency meeting tonight, though the caller was clearly a woman. Today his secretary, Lidia Alekseyevna, comes in with a visitor who won't take no for an answer: Samson, the big boy who bullied little Arkady in the communal flat. Let's listen in Russian first."
STORY = [
    ("lydia", "Аркадий Борисович, извините, тут к вам человек.", "Arkady Borisovich, I'm sorry, there's a man here to see you.", [(212, 'Аркадий Борисович, извините')], "'тут к вам человек' new (cue 213 'вот человек, который...')"),
    ("lydia", "Я ему сказала, что сегодня вы не принимаете.", "I told him you're not seeing anyone today.", [(214, 'я ему сказала, что')], "'у вас сегодня неприёмный день' -> 'сегодня вы не принимаете'"),
    ("anya", "Всё нормально, Лидия Алексеевна.", "It's all right, Lidia Alekseyevna.", [(216, 'Все нормально')], "garbled name 'Олегия' -> 'Лидия'"),
    ("anya", "Ну, здравствуй, Самсон.", "Well, hello, Samson.", [(217, 'Ну, здравствуй, Самсон')], ""),
    ("samson", "Узнал. Спасибо, что принял меня.", "You recognised me. Thanks for seeing me.", [(219, 'Узнал'), (220, 'Спасибо, что принял меня')], ""),
    ("samson", "Я думал, может, не примешь.", "I thought maybe you wouldn't see me.", [(221, 'Я думал, может')], "'пошлёшь' (tell me to get lost) -> 'не примешь'"),
    ("anya", "Ну что ты? Я очень рад тебя видеть.", "Oh, come on! I'm very glad to see you.", [(222, 'Ну что ты'), (224, 'Я очень рад тебя видеть')], ""),
    ("anya", "Ну, рассказывай, как дела?", "So, tell me, how are you doing?", [(225, 'Ну, рассказывай, как дела')], ""),
    ("samson", "Всё нормально. Работаю на стройке.", "Everything's fine. I work on a building site.", [(226, 'Все нормально'), (239, 'Работаю на стройке')], ""),
    ("samson", "Аркаш, попросить тебя хотел.", "Arkash, I wanted to ask you something.", [(250, 'Аркаш'), (251, 'Попросить тебя хотел')], ""),
    ("samson", "Экскаваторщик — это не мой уровень. Может, поможешь?", "Excavator driver isn't my level. Maybe you could help?", [(253, 'экскаваторщик не мой уровень'), (254, 'Может, поможешь')], "'это' added"),
    ("anya", "Конечно, помогу. Кто у вас сейчас начальник?", "Of course I'll help. Who's your boss now?", [(256, 'Конечно, помогу'), (261, 'у вас сейчас начальник')], "'там' dropped"),
    ("samson", "Ну, это Головамзюк.", "Well, it's Golovamzyuk.", [(262, 'Ну, это Головамзюк')], ""),
    ("anya", "Давай мы его уволим, а тебя на его место назначим.", "Let's fire him and put you in his place.", [(264, 'мы его уволим'), (265, 'а тебя на его место назначим')], "'давай-ка' -> 'давай', crude 'к чертям' dropped"),
    ("samson", "Да ладно, что, серьёзно?", "No way, what, seriously?", [(267, 'Да ладно, что серьезно')], ""),
    ("anya", "Конечно. Звони ему.", "Of course. Call him.", [(268, 'конечно'), (272, 'Звони ему')], ""),
    ("samson", "Николай Филиппович, я сейчас в кабинете у мэра.", "Nikolai Filippovich, I'm in the mayor's office right now.", [(280, 'Николай Филиппович'), (283, 'Я сейчас'), (283, 'в кабинете у мэра')], "'нахожусь' dropped"),
    ("samson", "Теперь я начальник нашей стройки. Ты уволен!", "Now I'm the boss of our building site. You're fired!", [(285, 'теперь я начальник нашей стройки'), (286, 'Ты уволен')], "crude insults at 287-289 dropped"),
]
OPENER = "Let's go back through it. The secretary is clearly annoyed with this visitor."
WALK = [
    (0, None, "'Arkady Borisovich, I'm sorry, there's a man here to see you.' Literally, 'here, to you, a man'. No verb at all, and it's perfectly natural. She explains that she tried to stop him."),
    (1, None, "'I told him you're not seeing anyone today.' The verb 'told' ends in 'a' because the secretary is a woman. And she uses the polite 'you' with her boss. But Arkady waves it away."),
    (2, None, "'It's all right, Lidia Alekseyevna.' Literally 'everything is normal', a phrase you'll hear all the time. Then he looks at his visitor."),
    (3, None, "'Well, hello, Samson.' Notice the greeting: it's the casual form of hello, for someone you know well. Samson is surprised."),
    (4, 'Узнал.', "'You recognised me.' Just one word, a past-tense verb, and the 'you' is understood. Then he says thank you."),
    (4, 'Спасибо, что принял меня.', "'Thanks for seeing me.' Literally, 'thank you that you received me'. A useful pattern: thank you, then 'that', then what the person did. He admits he was worried."),
    (5, None, "'I thought maybe you wouldn't see me.' After all, he once pushed Arkady's head into a toilet. Arkady acts as if it never happened."),
    (6, None, "'Oh, come on! I'm very glad to see you.' The word for 'glad' is masculine here, because Arkady is a man. A woman would add an 'a'. Then he asks for news."),
    (7, None, "'So, tell me, how are you doing?' The first verb is a friendly command, 'tell me', and the last two words are the everyday 'how are things'. Samson answers simply."),
    (8, None, "'Everything's fine. I work on a building site.' Here's the grammar point: 'on a building site' uses the location ending, an 'e' on the end. You'll meet it after 'in' and 'on' whenever you say where something is. Then Samson gets to the point."),
    (9, None, "'Arkash, I wanted to ask you something.' The name is cut short, the friendly way to call someone. And the verb comes last, which sounds relaxed and a bit shy. So what does he want?"),
    (10, None, "'Excavator driver isn't my level. Maybe you could help?' A long word for his job, then 'not my level'. The last verb is in the future, 'will you help?'. Arkady doesn't hesitate."),
    (11, None, "'Of course I'll help. Who's your boss now?' The question begins with 'who', and the word for 'boss' comes last. Samson names him."),
    (12, None, "'Well, it's Golovamzyuk.' That's the boss's surname. Arkady has a bold idea."),
    (13, None, "'Let's fire him and put you in his place.' 'Let's' plus 'we will': a very common way to suggest doing something together. And 'him' and 'you' sit before the verbs. Samson can't believe his luck."),
    (14, None, "'No way, what, seriously?' The first two words are a very common way to say 'you're kidding'. Arkady pushes him on."),
    (15, None, "'Of course. Call him.' A short, casual command. So Samson dials the number and speaks to his boss, using the boss's first name and his father's name."),
    (16, None, "'Nikolai Filippovich, I'm in the mayor's office right now.' Literally 'in the office at the mayor's'. And then the big news."),
    (17, None, "'Now I'm the boss of our building site. You're fired!' No word for 'am' again: 'now I boss'. And to his old boss he suddenly uses the casual, rude 'you'. Arkady watches with a smile."),
]
TRANSITION = "Let's hear the whole thing again from the start."
OUTRO = "Samson has just quit his job on the spot, trusting the boy he once bullied. Listen for 'I'm very glad to see you' when you watch, and. See you next time!"
CLOSING = ("samson", "Всё, до свидания!")
