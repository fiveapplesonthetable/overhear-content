# Authoring module for kukhnya-s01e10-scene-40.
ID = 'kukhnya-s01e10-scene-40'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 10
SCENE = 40
TITLE = "Звонок владельца  (The Owner's Call)"
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'senya': 'Сеня'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.10'
SOURCE_FILE = 'sources/kukhnya/s01/e10.ru.dual.srt'
INTRO = 'A big football match is on, and Barinov wants to watch it in peace. Senya tells him that the owner is calling for him, urgently. Listen to who says what.'
OPENER = "Let's take the lines one by one."
TRANSITION = "Let's play it through again."
OUTRO = "Barinov goes to see Nagiyev, and Senya stays with the television. The score is two-nil, but not for long. That's it for this one."
CLOSING = ('barinov', 'Пока!')
STORY = [
    ('barinov', 'Сеня, не мешай мне смотреть футбол!', "Senya, don't disturb me watching football!", [], ''),
    ('senya', 'Шеф, вас срочно зовёт Дмитрий Владимирович!', 'Chef, Dmitry Vladimirovich is urgently calling you!', [(289, 'вас Дмитрий Владимирович зовет')], ''),
    ('barinov', 'Почему хозяин звонит именно в этот момент?', 'Why does the owner call at this exact moment?', [(289, 'Дмитрий Владимирович')], ''),
    ('senya', 'Он сказал, что это очень срочное дело.', 'He said that this is a very urgent matter.', [(289, 'зовет')], ''),
    ('barinov', 'Я знаю этого человека целых двадцать лет.', 'I have known this man for a whole twenty years.', [(288, 'Я же вас 20 лет знаю')], ''),
    ('senya', 'Он ждёт вас прямо сейчас возле зала.', 'He is waiting for you right now near the hall.', [(290, 'Шеф')], ''),
    ('barinov', 'Наша команда ведёт в счёте два ноль!', 'Our team is leading in the score two-nil!', [(292, 'Следи за счетом')], ''),
    ('senya', 'Я обещаю внимательно следить за счётом.', 'I promise to watch the score carefully.', [(292, 'Следи за счетом')], ''),
    ('barinov', 'Если наша команда проиграет, я накажу тебя!', 'If our team loses, I will punish you!', [(292, 'Следи за счетом')], ''),
    ('senya', 'Шеф, я не отойду от экрана телевизора.', 'Chef, I will not step away from the TV screen.', [(292, 'Следи за счетом')], ''),
    ('barinov', 'Ладно, я пойду и выслушаю Дмитрия Владимировича.', 'Fine, I will go and hear Dmitry Vladimirovich out.', [(290, 'Шеф')], ''),
    ('senya', 'Удачи вам в разговоре с хозяином!', 'Good luck in your talk with the owner!', [(289, 'Дмитрий Владимирович')], ''),
    ('barinov', 'Смотри в оба и внимательно следи за счётом!', 'Keep your eyes peeled and attentively watch the score!', [(292, 'Следи за счетом')], ''),
]
WALK = [
    (0, None, '\'Senya, don\'t disturb me watching football!\' "Meshat" means both "to stir", as in Louis\'s "Meshay ravnomerno", and "to disturb", as here. "Ne meshay mne" is "don\'t disturb me". "Smotret futbol" is "to watch football".'),
    (1, None, '\'Chef, Dmitry Vladimirovich is urgently calling you!\' "Zovyot" is "calls", to summon someone, from "zvat", the verb of Senya\'s "zovi ofitsianta". Senya uses the owner\'s first name and father\'s name.'),
    (2, None, '\'Why does the owner call at this exact moment?\' "Khozyain" is "owner" or "master", heard in Vika\'s "nastoyashchiy khozyain kukhni". "Imenno v etot moment" is "exactly at this moment". Barinov is annoyed.'),
    (3, None, '\'He said that this is a very urgent matter.\' "Srochnoe delo" is "urgent matter", the words Max used to escape from Vika: "Vika, eto ochen srochnoe delo!". "Skazal" is "he said".'),
    (4, None, '\'I have known this man for a whole twenty years.\' Barinov says "Ya znayu", "I know": twenty years and still counting. After "dvadtsat", "years" is "let". "Tselykh" is "whole", for emphasis.'),
    (5, None, '\'He is waiting for you right now near the hall.\' "Zhdyot vas" is "waits you", with no word for "for". "Vozle zala" is "near the hall". "Pryamo seychas" is "right now".'),
    (6, None, '\'Our team is leading in the score two-nil!\' "Vedyot v schyote" is "leads in the score"; "vesti", "to lead", is also the verb in "vesti sebya", "to behave". "Dva nol" is "two-nil".'),
    (7, None, '\'I promise to watch the score carefully.\' "Sledit za" is "to keep an eye on", the verb in Barinov\'s "Idi i prosledi za goryachim tsekhom". "Obeshchayu" is "I promise", as in Louis\'s "Obeshchayu, tort budet idealnym".'),
    (8, None, '\'If our team loses, I will punish you!\' "Proigraet" is "loses", the word from the first scene: "Papa opyat proigral vse nashi dengi". "Nakazhu" is "I will punish".'),
    (9, None, '\'Chef, I will not step away from the TV screen.\' "Otoydu" is "I will step away", as in Barinov\'s "Senya, otoydi". "Ot ekrana" is "from the screen": "ekran" gets -a after "ot".'),
    (10, None, '\'Fine, I will go and hear Dmitry Vladimirovich out.\' "Vyslushayu" is "I will hear out": vy- on "slushat" means "to the end". After it, "Dmitry Vladimirovich" becomes "Dmitriya Vladimirovicha". The football will have to wait.'),
    (11, None, '\'Good luck in your talk with the owner!\' "Udachi vam" is literally "of luck to you", the way Russian wishes are built. "S khozyainom" is "with the owner", the same "khozyain" as before.'),
    (12, None, '\'Keep your eyes peeled and attentively watch the score!\' "Smotri v oba" is "look into both", meaning both eyes open. "Sledi za schyotom" repeats Senya\'s promise as an order.'),
]
