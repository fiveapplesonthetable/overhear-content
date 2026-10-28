# Authoring module for kukhnya-s01e08-scene-28.
ID = 'kukhnya-s01e08-scene-28'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 8
SCENE = 28
TITLE = 'Порядок на кухне  (Order in the Kitchen)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'elena': 'Елена'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.08'
SOURCE_FILE = 'sources/kukhnya/s01/e08.ru.dual.srt'
INTRO = "Back in the kitchen at Claude Monet, Elena Pavlovna has lost control: plates are coming back and nothing goes out on time. Then Barinov walks in and fixes the whole kitchen in a minute by giving each cook what he needs. Here it is in Russian first."
OPENER = "Let's go through the rescue. Every order Barinov gives is short and exact."
TRANSITION = "Now the rescue at full speed."
OUTRO = "Barinov's orders are a name, a command and a time: \"Fedya, idi pokuri tri minuty\". That is the shape of every order in a busy kitchen. See you next time."
CLOSING = ('barinov', 'Пока!')
STORY = [
    ('elena', 'У нас уже три возврата блюд!', 'We already have three returned dishes!', [(324, 'три отката от блюд.')], ''),
    ('elena', 'Повара ничего не успевают вовремя отдавать.', 'The cooks cannot serve anything on time.', [(325, 'Вы ничего не успеваете вовремя подавать.')], ''),
    ('barinov', 'Елена Павловна, что здесь случилось?', 'Elena Pavlovna, what happened here?', [(327, 'Елена Павловна, что случилось?')], ''),
    ('elena', 'Шеф, я совсем не справляюсь.', 'Chef, I am not coping at all.', [(328, 'Ну, в общем...')], ''),
    ('barinov', 'Спокойно, сейчас я наведу порядок.', 'Calm down, now I will restore order.', [], ''),
    ('barinov', 'Федя, иди покури три минуты.', 'Fedya, go have a smoke for three minutes.', [(330, 'Федя, иди покури, у тебя три минуты.')], ''),
    ('barinov', 'Ему нужен перекур каждые полтора часа.', 'He needs a smoke break every hour and a half.', [(331, 'Ему надо давать перекур каждые полтора часа.')], ''),
    ('barinov', 'Сеня, переходи готовить мясо.', 'Senya, switch to preparing meat.', [(332, 'Сеня, переходи на мясо.')], ''),
    ('barinov', 'Он совершенно не умеет готовить птицу.', 'He does not know how to cook poultry at all.', [(334, 'Он не может готовить птицу.')], ''),
    ('barinov', 'Луи, позвони другу на две минуты.', 'Louis, call your friend for two minutes.', [(339, 'Пара минут трепа по телефону, и он в норме.')], ''),
    ('elena', 'А почему Мазар ничего не делает?', 'And why is Mazar doing nothing?', [(340, 'А это почему не справляется?')], ''),
    ('barinov', 'Потому что он никогда ничего не умеет.', 'Because he never knows how to do anything.', [(341, 'А это вообще никогда не справляется.')], ''),
    ('barinov', 'Мазар, ты уволен!', 'Mazar, you are fired!', [(342, 'Мазар, ты уволен.')], ''),
    ('barinov', 'Вот теперь кухня работает идеально.', 'Now the kitchen works perfectly.', [], ''),
]
WALK = [
    (0, None, "'We already have three returned dishes!' After \"tri\", three, Russian uses the 'of a single one' shape, so \"vozvrat\" becomes \"tri vozvrata\". And \"blyud\", of dishes, has no ending at all: that bare shape is 'of dishes', from \"blyudo\"."),
    (1, None, "'The cooks cannot serve anything on time.' To manage something in time is \"uspevat\", and \"ne uspevayut\" is the cooks falling behind. The word \"vovremya\", on time, is \"v\" plus \"vremya\", time, written as one word."),
    (2, None, "'Elena Pavlovna, what happened here?' Barinov uses her first name and her father's name, Pavlovna, the respectful way to address a colleague. And \"sluchilos\", happened, ends in -os to match \"chto\", what."),
    (3, None, "'Chef, I am not coping at all.' Elena's \"spravlyayus\" is the word Ainura used about the cooks, now said about herself. And \"sovsem ne\" means 'not at all'."),
    (4, None, "'Calm down, now I will restore order.' On its own, \"spokoyno\", calmly, works as 'easy, calm down'. To bring order is \"navesti poryadok\", a fixed pairing, and \"navedu\" is 'I will bring'."),
    (5, None, "'Fedya, go have a smoke for three minutes.' Two commands sit side by side in \"idi pokuri\", 'go, smoke'. The \"po-\" in \"pokuri\" makes it 'smoke a little', and \"tri minuty\" has the same 'after three' shape as \"tri vozvrata\"."),
    (6, None, "'He needs a smoke break every hour and a half.' Barinov says \"nuzhen\", needed, the 'he' shape that matches \"perekur\". After \"poltora\", one and a half, comes the 'of one' shape, \"chasa\"."),
    (7, None, "'Senya, switch to preparing meat.' Earlier \"perekhodit\" moved the cooks onto chicken, and now Barinov's \"perekhodi\" sends Senya back the other way. Note that \"gotovit\" is both 'to cook' and 'to prepare'."),
    (8, None, "'He does not know how to cook poultry at all.' Literally, \"ptitsa\" is a bird, and on a menu it means poultry. Then \"ne umeet\", can't, is about skill, not permission."),
    (9, None, "'Louis, call your friend for two minutes.' Russian rings 'to' someone, so it's \"pozvoni drugu\", call to a friend. With \"na dve minuty\", the \"na\" marks a planned length of time."),
    (10, None, "'And why is Mazar doing nothing?' Literally 'does not do nothing', \"nichego ne delaet\" is normal Russian. The opening \"a\" pushes the question in: 'and what about Mazar?'"),
    (11, None, "'Because he never knows how to do anything.' Barinov's \"nikogda nichego ne\" stacks three negatives, never, nothing, not, and Russian keeps all of them. And \"potomu chto\" is 'because', literally 'by that, that'."),
    (12, None, "'Mazar, you are fired!' Fired is \"uvolen\", a short shape from \"uvolit\", to dismiss. So \"ty uvolen\" is the whole sentence; there is no 'are'."),
    (13, None, "'Now the kitchen works perfectly.' You hear a satisfied 'there, now' in \"vot teper\". And \"idealno\", perfectly, shares its root with English 'ideal'."),
]
