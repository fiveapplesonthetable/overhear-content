ID = "kukhnya-s04e07-scene-18"
SHOW = "kukhnya"
SEASON = 4
EPISODE = 7
SCENE = 18
TITLE = "Звонок Михалкову  (The Call to Mikhalkov)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "nagiyev": "anja", "guest": "angelina"}
LABELS = {"anya": "Шеф", "nagiyev": "Нагиев", "guest": "Гость"}
SOURCE_NAME = "Кухня (Kukhnya) S4.07"
SOURCE_FILE = "sources/kukhnya/s04/e07.ru.srt"
SOURCE_NOTE = "Cues 275-291. Gavril Ilyich calls director Nikita Mikhalkov on the phone and lets Nagiyev speak to him, while Nagiyev begs Gavril Ilyich not to move the banquet to Arcobaleno."

INTRO = "At the table in Claude Monet, Gavril Ilyich calls legendary director Nikita Mikhalkov on his mobile phone and hands it to an starstruck Dmitry Nagiyev. Afterward, worried by German's outburst, Gavril Ilyich wonders whether they should hold the banquet next door instead."

STORY = [
    ("guest", "Алло, Никита Сергеевич, я сейчас в ресторане.", "Hello, Nikita Sergeyevich, I am at the restaurant right now.", [(275, "Алло, Никита Сергеевич, я сейчас в Клод Мане.")], "adapted"),
    ("guest", "Тут Дмитрий Нагиев хочет с вами пообщаться.", "Here Dmitry Nagiyev wants to chat with you.", [(276, "А тут Дима Нагиев хочет с вами пообщаться.")], "adapted"),
    ("nagiyev", "Никита Сергеевич, я всю жизнь мечтал позвонить!", "Nikita Sergeyevich, I dreamed of calling you my whole life!", [(278, "Никита Сергеевич, я всю жизнь хотел")], "adapted"),
    ("nagiyev", "Хотел сказать вам спасибо за ваше искусство!", "I wanted to say thank you to you for your art!", [(279, "вам сказать спасибо за то, сколько вы есть.")], "adapted"),
    ("nagiyev", "Просто спасибо за то, что вы есть!", "Simply thank you for existing!", [(280, "За то, что вы есть.")], "adapted"),
    ("nagiyev", "Да, конечно, передаю трубку обратно Гавриилу Ильичу.", "Yes, of course, I am handing the phone back to Gavriil Ilyich.", [(282, "Слушай, дай Гаврилу на пару слов."), (283, "Слушаюсь.")], "adapted"),
    ("guest", "Да, Никита Сергеевич, тут есть небольшие проблемы.", "Yes, Nikita Sergeyevich, there are some small problems here.", [(285, "Да есть проблемки.")], "adapted"),
    ("guest", "Не знаю, может, в соседнем ресторане организуем?", "I do not know, maybe we should organize it at the neighboring restaurant?", [(286, "Не знаю, может быть, в соседнем ресторане организуем.")], "adapted"),
    ("nagiyev", "Не надо в соседнем ресторане, я вас умоляю!", "Not in the neighboring restaurant, I beg you!", [(287, "Не надо в соседнем ресторане, я вас умоляю, пожалуйста.")], "adapted"),
    ("guest", "А если ваш странный повар снова выскочит?", "And what if your strange cook jumps out again?", [(288, "Ну, а если ваш подчиненный у нас на банкете выскочит?")], "adapted"),
    ("nagiyev", "Он больше не выскочит, мы его уволим!", "He will not jump out anymore, we will fire him!", [(289, "Не выскочит, что он?")], "adapted"),
    ("nagiyev", "Я вас умоляю, дайте нам один шанс!", "I beg you, please give us one chance!", [(290, "Я вас умоляю, дайте, пожалуйста, один шанс.")], "adapted"),
]

OPENER = "Let's break down the phone call with Nikita Mikhalkov line by line."

WALK = [
    (0, None, "'Hello, Nikita Sergeyevich, I am at the restaurant right now.' Gavril Ilyich reports back to the famous film director."),
    (1, None, "'Here Dmitry Nagiyev wants to chat with you.' Reflexive perfective infinitive 'to chat' governs 'with you'."),
    (2, None, "'Nikita Sergeyevich, I dreamed of calling you my whole life!' Accusative duration 'the whole life' marks his lifelong wish."),
    (3, None, "'I wanted to say thank you to you for your art!' Preposition 'for' with the accusative marks the reason for gratitude."),
    (4, None, "'Simply thank you for existing!' Literally 'for that which you are', a warm Russian compliment."),
    (5, None, "'Yes, of course, I am handing the phone back to Gavriil Ilyich.' When Mikhalkov asks for his deputy back, Nagiyev obeys at once."),
    (6, None, "'Yes, Nikita Sergeyevich, there are some small problems here.' Diminutive plural noun softens the report of German's outburst."),
    (7, None, "'I do not know, maybe we should organize it at the neighboring restaurant?' First-person plural future suggests moving to Arcobaleno."),
    (8, None, "'Not in the neighboring restaurant, I beg you!' Nagiyev panics at the thought of losing the banquet to his rivals."),
    (9, None, "'And what if your strange cook jumps out again?' Perfective future verb 'will jump out' recalls German's scene."),
    (10, None, "'He will not jump out anymore, we will fire him!' Nagiyev promises total order during the banquet."),
    (11, None, "'I beg you, please give us one chance!' Just as Gavril Ilyich is about to agree, a waiter lifts the cloche hiding Denis's pigeon!"),
]

TRANSITION = "Now let's listen to the phone call scene in the dining room again."
OUTRO = "Gavril Ilyich is almost persuaded to keep the banquet at Claude Monet—until a waiter lifts the silver cover hiding Denis's live street pigeon. See you in the next scene."
CLOSING = ("nagiyev", "Я вас умоляю, дайте нам один шанс!")
CLOSING_TRANS = "I beg you, please give us one chance!"
