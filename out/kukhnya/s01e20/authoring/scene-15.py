ID = "kukhnya-s01e20-scene-15"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 20
SCENE = 15
TITLE = "В ресторане  (In the Restaurant)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {'narrator': 'sky', 'anya': 'alisa', 'max': 'anja', 'guest': 'angelina'}
LABELS = {'anya': 'Вика', 'max': 'Макс', 'guest': 'Гость'}
SOURCE_NAME = "Кухня (Kukhnya) S1.20"
SOURCE_FILE = "sources/kukhnya/s01/e20.ru.dual.srt"
SOURCE_NOTE = "Scene 15"

INTRO = "Victoria drags Max outside after he interrupts her conversation with the important guest. They have a big argument about jealousy and expensive gifts. Max is too drunk to listen to her."
OPENER = "Now let's examine this conversation line by line."
TRANSITION = "Now let's listen to the conversation again without interruption."
OUTRO = "Victoria gets very angry at Max's stupid words and decides to leave him. Max realizes he made a big mistake, but it is already too late."

STORY = [
    ("anya", "Пойдем, Макс, пойдем на улицу сейчас.", "Come on, Max, let's go outside now.", [], "adapted"),
    ("max", "Что я сделал? Я просто дал тебе подарок.", "What did I do? I just gave you a gift.", [], "adapted"),
    ("anya", "Как ты себя ведешь? Мне очень стыдно.", "How are you behaving? I am very ashamed.", [], "adapted"),
    ("max", "А тебе не стыдно, что он целует твои руки?", "And aren't you ashamed that he kisses your hands?", [], "adapted"),
    ("anya", "Он хороший человек и он нормально себя ведет.", "He is a good man and he behaves normally.", [], "adapted"),
    ("max", "Может быть, ты будешь встречаться с ним?", "Maybe you will date him?", [], "adapted"),
    ("anya", "Ты говоришь глупости, Макс. Я не понимаю тебя.", "You speak nonsense, Max. I don't understand you.", [], "adapted"),
    ("max", "Он дарит тебе дорогие подарки. Будь благодарной.", "He gives you expensive gifts. Be grateful.", [], "adapted"),
    ("anya", "Хорошо, если ты так хочешь, я так сделаю.", "Fine, if you want so, I will do so.", [], "adapted"),
    ("max", "Отлично, иди к нему и целуй его руки.", "Excellent, go to him and kiss his hands.", [], "adapted"),
    ("anya", "Ты просто дурак, Макс. Я ухожу отсюда.", "You are just a fool, Max. I am leaving here.", [], "adapted"),
    ("max", "Извините, это нормально? Вы думаете, это нормально?", "Excuse me, is this normal? Do you think this is normal?", [], "adapted"),
    ("guest", "Я думаю, что ты просто пьяный дурак.", "I think that you are just a drunken fool.", [], "adapted"),
    ("max", "Никто меня не понимает сегодня. Я пойду спать.", "Nobody understands me today. I will go sleep.", [], "adapted"),
]

WALK = [
    (0, None, "'Come on, Max, let's go outside now.' -- She tells Max to go outside."),
    (1, None, "'What did I do? I just gave you a gift.' -- He says he just gave her a gift."),
    (2, None, "'How are you behaving? I am very ashamed.' -- She says she is very ashamed."),
    (3, None, "'And aren't you ashamed that he kisses your hands?' -- He asks if she is ashamed about the guest."),
    (4, None, "'He is a good man and he behaves normally.' -- She says the guest behaves normally."),
    (5, None, "'Maybe you will date him?' -- He asks if she will date him."),
    (6, None, "'You speak nonsense, Max. I don't understand you.' -- She tells him he speaks nonsense."),
    (7, None, "'He gives you expensive gifts. Be grateful.' -- He tells her to be grateful for the gifts."),
    (8, None, "'Fine, if you want so, I will do so.' -- She says she will do so."),
    (9, None, "'Excellent, go to him and kiss his hands.' -- He tells her to go to him."),
    (10, None, "'You are just a fool, Max. I am leaving here.' -- She tells Max he is a fool."),
    (11, None, "'Excuse me, is this normal? Do you think this is normal?' -- He asks if this is normal."),
    (12, None, "'I think that you are just a drunken fool.' -- He says Max is a drunken fool."),
    (13, None, "'Nobody understands me today. I will go sleep.' -- He says nobody understands him today."),
]

CLOSING = ("max", "Никто меня не понимает сегодня. Я пойду спать.")
