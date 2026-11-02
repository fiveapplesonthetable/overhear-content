# Authoring module for domashniy-arest-s01e01-scene-01.
ID = 'domashniy-arest-s01e01-scene-01'
SHOW = 'domashniy-arest'
SEASON = 1
EPISODE = 1
SCENE = 1
TITLE = 'Подарки из Венгрии  (Gifts from Hungary)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'arkady': 'Аркадий', 'father': 'Отец Самсона', 'samson': 'Самсон'}
SOURCE_NAME = 'Домашний арест (Domashniy Arest) S1.01'
SOURCE_FILE = 'sources/domashniy-arest/s01/e01.ru.dual.srt'
INTRO = "This series is called House Arrest, and its hero is Arkady, the mayor of Sineozersk, a small Russian town; he grew up in a communal flat, one flat shared by several families. But we start in the nineteen eighties: Samson, then just little Vanya, sees his father come home from Hungary with presents, and little Arkady can only watch. Let's listen in Russian first."
OPENER = "Let's go back through it slowly. The door bangs, and the whole corridor knows that Vanya's father is home from abroad."
TRANSITION = 'Now the whole scene again, from the knock at the door.'
OUTRO = "That's the first scene, and the show's whole story starts with this one suitcase of presents. Next time we'll find out what happens to that little toy car. See you next time!"
CLOSING = ('arkady', 'Пока!')
STORY = [
    ('samson', 'Привет, папа!', 'Dialogue line.', [(20, 'Привет')], ''),
    ('father', 'Привет! Смотри, что у меня есть.', 'Dialogue line.', [(52, 'смотри')], ''),
    ('samson', 'Ого, магнитофон! Японский!', 'Dialogue line.', [(58, 'Ого')], ''),
    ('arkady', 'Здравствуйте! Как там в Венгрии?', 'Dialogue line.', [(27, 'как там в Венгрии')], ''),
    ('father', 'Хорошо! Там всё нормально.', 'Dialogue line.', [(49, 'нормально')], ''),
    ('samson', 'Папа, а жвачку ты привёз?', 'Dialogue line.', [(31, 'привез')], ''),
    ('father', 'Жвачку? Денег не хватило.', 'Dialogue line.', [(32, 'не хватило')], ''),
    ('samson', 'Ну, папа!', 'Dialogue line.', [(33, 'Ну, пап')], ''),
    ('father', 'Ладно, держи. Вот, смотри.', 'Dialogue line.', [(35, 'Ладно'), (52, 'держи, вот, смотри')], ''),
    ('samson', 'Сколько жвачки! Класс!', 'Dialogue line.', [(47, 'Класс')], ''),
    ('father', 'А это тебе. Машинка!', 'Dialogue line.', [(38, 'это тебе')], ''),
    ('samson', 'Спасибо, папа!', 'Dialogue line.', [], ''),
    ('father', 'Со всеми поделись поровну, понял?', 'Dialogue line.', [(61, 'со всеми'), (61, 'поровну'), (61, 'понял')], ''),
    ('samson', 'Понял.', 'Dialogue line.', [], ''),
    ('arkady', 'А можно я пойду посмотрю?', 'Dialogue line.', [(65, 'А можно я пойду посмотрю')], ''),
    ('arkady', 'Нельзя? Ладно, пойду учить уроки.', 'Dialogue line.', [(66, 'Уроки')], ''),
]
WALK = [
    (0, None, "'Hi, Dad!' \"Privet\" is the casual hello you use with family and friends. Dad has something to show him."),
    (1, 'Смотри, что у меня есть.', "'Look what I've got.' Literally, 'look, what is at me'. That's how you say you have something: at me there is. The first thing out of the suitcase is a big one."),
    (2, None, "'Wow, a tape recorder! A Japanese one!' \"Magnitofon\" was a real treasure in the Soviet nineteen eighties, and \"ogo\" is the cry of 'wow!'. Little Arkady is watching from the doorway, and he greets the father politely."),
    (3, 'Здравствуйте!', "'Hello!' \"Zdravstvuyte\" is the long, polite hello a child uses with a grown-up; it literally wishes the other person good health. Then he asks a question a neighbour asked."),
    (3, 'Как там в Венгрии?', "'How was it there in Hungary?' Literally, 'how is it there, in Hungary'. After \"v\" ('in'), \"Vengriya\" shifts its ending to \"Vengrii\". The father keeps it short."),
    (4, None, "'Good! Everything's fine over there.' \"Normalno\" sounds a lot like 'normal', and Russians use it constantly for 'fine' or 'all good'. Vanya only cares about one thing."),
    (5, None, "'Dad, did you bring any gum?' Russian needs no helper like 'did' here: rising intonation turns \"ty privyoz\" straight into a question, and \"privyoz\" is the male speaker's form. Dad likes to tease."),
    (6, None, "'Gum? I didn't have enough money.' In Russian, \"dengi\" ('money') is always treated like 'funds', and \"ne khvatilo\" literally says 'it didn't suffice'. Vanya is not having it."),
    (7, None, "'Oh, come on, Dad!' Tiny \"nu\" at the front does all the pleading work of 'oh, come on'. So Dad gives in."),
    (8, 'Ладно, держи.', "'All right, here you go.' \"Derzhi\" literally means 'hold', and Russians say it whenever they hand something over. Then he points."),
    (8, 'Вот, смотри.', "'There, look.' \"Vot\" is the pointing word Russians use as they show or hand you something, paired with \"smotri\" ('look'). Vanya can't believe his luck."),
    (9, None, "'So much gum! Cool!' \"Klass\" literally means 'class', and kids shout it for 'cool!' or 'awesome!'. There's one more present."),
    (10, None, "'And this is for you. A toy car!' \"Mashinka\" is built from \"mashina\" ('car') with a little '-ka' ending that shrinks it into a toy car. Vanya remembers his manners."),
    (11, None, "'Thanks, Dad!' \"Spasibo\" is the everyday Russian 'thank you', historically shortened from 'may God save you'. Then Dad gives an instruction."),
    (12, None, "'Share it all equally with everyone, understand?' \"Porovnu\" means 'in equal shares', and \"ponyal\" at the end asks 'got it?'. Vanya promises."),
    (13, None, "'Got it.' Repeating \"ponyal\" by itself turns 'did you understand?' straight into 'understood'. Keep an eye on that promise, because Arkady has a question too."),
    (14, None, "'Can I go and have a look?' \"Mozhno\" up front asks 'is it allowed?', followed by \"poydu posmotryu\" — literally 'I'll go, I'll look' side by side. An adult in his room says no."),
    (15, None, "'Not allowed? All right, I'll go and do my homework.' \"Nelzya\" means 'not allowed', the exact opposite of \"mozhno\", and doing homework in Russian is literally \"uchit uroki\" — 'to learn lessons'."),
]
