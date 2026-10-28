# domashniy-arest/s01e04/scene-15.py
ID = "domashniy-arest-s01e04-scene-15"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 4
SCENE = 15
TITLE = "Образ кандидата  (The Candidate's Look)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.04"
SOURCE_FILE = "sources/domashniy-arest/s01/e04.ru.dual.srt"
VOICES = {"narrator": "sky", "anya": "alisa", "samson": "anja", "nina": "angelina"}
LABELS = {"anya": "Аркадий", "samson": "Самсон", "nina": "Нина"}
INTRO = "Last time, the governor ordered Pasha to eliminate Samsonov politically, and Pasha barked at his new strategist Ilona. Back in the communal flat, while Yulia answers phone calls from voters, Arkady and Nina dress Samson for his campaign, and Arkady has to stop his candidate from drinking free beer sent by the local brewery. Let's listen in Russian first."
STORY = [
    ("anya", "Ужасно! Очень плохой костюм!", "Terrible! A very bad suit!", [(539, 'Ужасно'), (539, 'Очень плохой костюм')], ""),
    ("samson", "Ты что? Это мой свадебный костюм вообще-то!", "What do you mean? This is my wedding suit, actually!", [(540, 'Ты что'), (548, 'Это мой свадебный костюм вообще-то')], ""),
    ("anya", "Не верю. Похож на какого-то богатого ворюгу.", "I don't buy it. You look like some rich crook.", [(543, 'Не верю'), (544, 'Похож на какого-то'), (544, 'ворюгу')], "cue 544 'зажравшегося' simplified to A1 'богатого'"),
    ("samson", "Чего? Кто из нас ворюга?", "What? Which one of us is a crook?", [(545, 'Чего'), (547, 'Кто из нас ворюга')], ""),
    ("anya", "Да не обижайся ты, Ваня. Сейчас найду подходящую одежду.", "Don't take offence, Vanya. I'll find suitable clothes right now.", [(549, 'Да не обижайся ты'), (550, 'Сейчас найду'), (550, 'подходящую')], "cue 550 crude word dropped; 'через подходящую' -> 'подходящую одежду'"),
    ("samson", "Не знаю, не нравится мне этот свитер.", "I don't know, I don't like this sweater.", [(562, 'Не знаю, не нравится мне этот свитер')], ""),
    ("nina", "Карамельно-сливочный цвет. Очень тебе к лицу! Надень куртку.", "A caramel-cream colour. It really suits you! Put the jacket on.", [(565, 'Карамельно-сливочный цвет'), (566, 'Очень тебе к лицу'), (567, 'Надень куртку')], "crude cues 563-564 omitted"),
    ("anya", "Отлично, Ваня! Вот это твой образ!", "Perfect, Vanya! That right there is your look!", [(571, 'отлично'), (572, 'Вот это твой образ')], ""),
    ("anya", "Теперь скажи свой слоган.", "Now say your slogan.", [(573, 'теперь скажи'), (573, 'слоган свой')], ""),
    ("samson", "Все говорят, а я делаю.", "Everyone talks, while I get things done.", [(574, 'все говорят, а я делаю')], ""),
    ("anya", "Подожди, не надо! Руки прочь от пива!", "Wait, don't! Hands off the beer!", [(583, 'Подожди, не надо'), (585, 'Руки прочь от пива')], "Slavik has just brought bottles of beer from the brewery"),
    ("anya", "Послушай меня, Ваня. Нам нужно чуть-чуть потерпеть и немножко поработать.", "Listen to me, Vanya. We need to be patient a little and work a bit.", [(590, 'послушай меня, Ваня'), (591, 'Нам нужно чуть-чуть потерпеть, немножко поработать')], "'и' added"),
    ("anya", "И в конце нас всех ждёт вкусная морковка!", "And at the end a tasty carrot is waiting for us all!", [(592, 'И в конце нас всех'), (592, 'вкусная морковка')], "'будет ждать' shortened to 'ждёт'"),
    ("anya", "Нина, проконтролируйте его, пожалуйста.", "Nina, keep an eye on him, please.", [(597, 'Нина, проконтролируйте'), (597, 'пожалуйста')], "cue 597 mistranscribes 'его' as 'меня'"),
    ("nina", "Я проконтролирую.", "I'll keep an eye on him.", [(600, 'Я проконтролирую')], ""),
    ("anya", "Будут разные провокации. Все контакты только через меня.", "There will be various provocations. All contacts go only through me.", [(605, 'Будут разные провокации'), (607, 'Все контакты только через меня')], ""),
]
OPENER = "Let's walk through it together. Samson steps out in his tight, shiny old suit, and Arkady shakes his head in horror."
WALK = [
    (0, None, "'Terrible! A very bad suit!' Both 'bad' and 'suit' are masculine singular. Samson is offended."),
    (1, 'Ты что?', "'What do you mean?' Literally 'you what?'."),
    (1, 'Это мой свадебный костюм вообще-то!', "'This is my wedding suit, actually!' The adjective comes from the word for 'wedding', and the word at the end means 'actually' or 'for your information'. Arkady is unmoved."),
    (2, 'Не верю.', "'I don't buy it.' Literally 'I do not believe', the famous phrase of the theatre director Stanislavsky."),
    (2, 'Похож на какого-то богатого ворюгу.', "'You look like some rich crook.' The short adjective at the start is masculine: 'similar to'. And Samson spots the irony right away."),
    (3, None, "'What? Which one of us is a crook?' After all, Arkady is the one wearing an electronic ankle tag for taking a bribe. Arkady quickly changes the subject and rummages through the wardrobe."),
    (4, 'Да не обижайся ты, Ваня.', "'Don't take offence, Vanya.' A negative command."),
    (4, 'Сейчас найду подходящую одежду.', "'I'll find suitable clothes right now.' 'Clothes' in Russian is a singular feminine noun, so the adjective takes the feminine object ending '-uyu'. Meanwhile Yulia answers another voter call on the sofa, and Samson tries on a pale sweater."),
    (5, None, "'I don't know, I don't like this sweater.' Remember how 'to like' works in Russian: 'this sweater does not please to me'. Nina comes to the rescue."),
    (6, 'Карамельно-сливочный цвет.', "'A caramel-cream colour.' Nina sounds like a fashion magazine."),
    (6, 'Очень тебе к лицу! Надень куртку.', "'It really suits you! Put the jacket on.' Literally 'very much to you to the face', an idiom meaning 'it looks great on you'. Then she tells him to put his work jacket over it. Arkady beams."),
    (7, None, "'Perfect, Vanya! That right there is your look!' Now Samson looks like an honest working man. Time to rehearse."),
    (8, None, "'Now say your slogan.' An informal command: 'say'."),
    (9, None, "'Everyone talks, while I get things done.' Literally 'all speak, and I do'. Just then Slavik runs in with bottles of free beer sent by the local brewery, who want the people's candidate to pose with a bottle. Samson reaches for one, and Arkady slaps his hand away."),
    (10, 'Подожди, не надо!', "'Wait, don't!' Two quick words to stop him."),
    (10, 'Руки прочь от пива!', "'Hands off the beer!' Literally 'hands away from the beer', with 'beer' in the 'of' form. Then Arkady gives him a pep talk."),
    (11, 'Послушай меня, Ваня.', "'Listen to me, Vanya.' The key word here means 'listen to', anchored at the close by 'listen to'."),
    (11, 'Нам нужно чуть-чуть потерпеть и немножко поработать.', "'We need to be patient a little and work a bit.' Both verbs have the prefix 'po-', which means doing something for a short while."),
    (12, None, "'And at the end a tasty carrot is waiting for us all!' He means the big prize once Samson wins the election. Knowing Samson's weakness, Arkady turns to Nina."),
    (13, None, "'Nina, keep an eye on him, please.' He uses the polite plural command with Nina."),
    (14, None, "'I'll keep an eye on him.' First-person future-tense form: 'I will supervise'. Before heading out to go door to door, Arkady gives one last warning."),
    (15, 'Будут разные провокации.', "'There will be various provocations.' In spoken Russian, word order is flexible: 'there will be' comes first to set the focus, followed by 'provocations'."),
    (15, 'Все контакты только через меня.', "'All contacts go only through me.' After the preposition 'through', 'me' is in the object form."),
]
TRANSITION = "Now let's hear the whole scene again from the top."
OUTRO = "So Samson has his caramel-cream sweater, his work jacket, and his slogan, and Nina is on guard duty to keep him sober. Listen for the suit, the sweater, and 'hands off the beer' when you watch. See you next time!"
CLOSING = ("samson", "Пока!")
