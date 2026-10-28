# domashniy-arest/s01e07/scene-22.py
ID = "domashniy-arest-s01e07-scene-22"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 7
SCENE = 22
TITLE = "В лесу — только дровами  (In the Forest, Only Firewood)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.07"
SOURCE_FILE = "sources/domashniy-arest/s01/e07.ru.dual.srt"
VOICES = {"narrator": "sky", "samson": "anja", "nina": "angelina"}
LABELS = {"samson": "Самсон", "nina": "Нина"}
INTRO = "While Arkady was slipping on milk and rice in the communal kitchen, Samsonov mocked Danya's small city car in the courtyard and promised to tow him through the deep snow ruts. Instead, Samsonov's own car broke down on the forest road, and Danya had to tow him to the clearing. Listen to the Russian conversation first, and do not worry about catching every word."
STORY = [
    ("samson", "Два цилиндра не работают. Свечи плохие мне подсунули!", "Two cylinders are not working. They slipped me bad spark plugs!", [(825, 'Два'), (826, 'Свечи'), (826, 'подсунули')], "ASR 'силидра' -> 'цилиндра'; slang 'паленые' -> 'плохие'"),
    ("samson", "Ну что мы сидим? Выходим!", "Well, why are we sitting here? Let's get out!", [(827, 'сидим'), (828, 'Выходим')], "crude 'сисемнём' omitted"),
    ("samson", "Да, ладно, выходим.", "Yes, alright, let's get out.", [(829, 'Да'), (830, 'Выходим'), (831, 'Ладно')], ""),
    ("samson", "Вот оно, наше местечко!", "Here it is, our little spot!", [(832, 'наше местечко')], ""),
    ("nina", "Ой, тут кругом снег! А где мы сидеть будем?", "Oh, there is snow all around here! And where are we going to sit?", [(834, 'Ой'), (835, 'А где мы сидеть')], ""),
    ("samson", "Сын, давай помогай мне! Сейчас это бревно катанём и снег уберём.", "Son, come help me! Right now we will roll this log over and clear the snow.", [(839, 'Давай помогай, давай бревно катанём'), (841, 'Сейчас снег')], ""),
    ("samson", "А зачем нам бревно? Я вот стулья взял!", "And why do we need a log? I brought folding chairs right here!", [(847, 'бревно'), (848, 'Я вот'), (850, 'взял')], "ASR 'чем бревно-то... тулья взял' -> 'зачем бревно... стулья взял'"),
    ("samson", "Ты зачем эти китайские стулья с собой таскаешь, Даня?", "Why are you dragging these Chinese chairs around with you, Danya?", [(853, 'с собой'), (853, 'таскаешь')], "crude 'говно' replaced with 'стулья'"),
    ("samson", "Это не Китай, а Норвегия! Сто пятьдесят килограммов держат. Прошу!", "This is not China, it is Norway! They hold a hundred and fifty kilograms. Please, have a seat!", [(855, 'А Норвегия'), (856, 'Прошу')], "number '150 кило' written out as 'сто пятьдесят килограммов'"),
    ("samson", "Детский сад какой-то.", "Like some kind of kindergarten.", [(857, 'Детский сад какой-то')], ""),
    ("nina", "Знаете, Даня просто волшебник! Спасибо!", "You know, Danya is simply a wizard! Thank you!", [(858, 'Знаете'), (858, 'волшебник')], "colloquial 'прям' -> 'просто'"),
    ("samson", "Так, ладно, мужики, за дровами! Подъём, пошли!", "Right, fine, men, let's go for firewood! Up you get, let's go!", [(859, 'Так, ладно'), (861, 'Мужики, за дровами'), (862, 'Подъем. Пошли')], ""),
    ("samson", "А зачем идти за дровами? Я вот уголь взял.", "And why go for firewood? I brought charcoal right here.", [(863, 'А зачем за дровами'), (864, 'Я вот уголь взял')], ""),
    ("samson", "Выкинь, Даня, это же химия! В лесу — только дровами! Ну, вперёд!", "Throw it out, Danya, that is pure chemicals! In the forest, only with firewood! Come on, forward!", [(865, 'Выкинь'), (865, 'Это же химия'), (866, 'В лесу'), (866, 'только дровами'), (868, 'Ну, вперёд')], "slang 'голимая' omitted"),
]
OPENER = "Let's walk through the snowy forest clearing line by line."
WALK = [
    (0, 'Два цилиндра не работают.', "'Two cylinders are not working.' After the numeral 'two', Russian nouns take the 'of'-form singular form."),
    (0, 'Свечи плохие мне подсунули!', "'They slipped me bad spark plugs!' Samsonov fumes after Danya's tiny car had to tow his broken SUV into the woods."),
    (1, 'Ну что мы сидим?', "'Well, why are we sitting here?' Samsonov tries to take charge again."),
    (1, 'Выходим!', "'Let's get out!' Literally 'we are going out'."),
    (2, None, "'Yes, alright, let's get out.' Danya unbuckles his seatbelt and steps out of the car."),
    (3, None, "'Here it is, our little spot!' Samsonov gestures proudly at a snow-covered clearing."),
    (4, 'Ой, тут кругом снег!', "'Oh, there is snow all around here!' Nina looks around at the deep drifts."),
    (4, 'А где мы сидеть будем?', "'And where are we going to sit?' There is not a single dry bench in sight."),
    (5, 'Сын, давай помогай мне!', "'Son, come help me!' Samsonov calls Slavik over to a frozen fallen tree."),
    (5, 'Сейчас это бревно катанём и снег уберём.', "'Right now we'll roll this log over and clear the snow.' He wants everyone to sit on a cold log."),
    (6, 'А зачем нам бревно?', "'And why do we need a log?' Danya opens his boot with a smile."),
    (6, 'Я вот стулья взял!', "'I brought chairs right here!' He unfolds neat camping chairs for everyone."),
    (7, None, "'Why are you dragging these Chinese chairs around with you, Danya?' Samsonov scoffs at the folding chairs."),
    (8, 'Это не Китай, а Норвегия!', "'This is not China, it's Norway!' Danya replies politely."),
    (8, 'Сто пятьдесят килограммов держат.', "'They hold one hundred and fifty kilograms.' Even Samsonov cannot break them."),
    (8, 'Прошу!', "'Please, go ahead!' Literally 'I ask', a polite way to invite someone to sit down."),
    (9, None, "'Some kind of kindergarten.' Samsonov mutters sourly as the family sits down in comfort."),
    (10, 'Знаете, Даня просто волшебник!', "'You know, Danya is simply a wizard!' Nina beams with gratitude."),
    (10, 'Спасибо!', "'Thank you!' That praise makes Samsonov even more determined to prove his toughness."),
    (11, 'Так, ладно, мужики, за дровами!', "'Right, fine, men, off for firewood!' Notice the 'with'-form plural after the preposition meaning 'for'."),
    (11, 'Подъём, пошли!', "'Up you get, let's go!' He barks the order like an army sergeant."),
    (12, 'А зачем идти за дровами?', "'And why go for firewood?' Danya holds up a neat paper bag."),
    (12, 'Я вот уголь взял.', "'I brought charcoal right here.' Once again Danya has thought of everything."),
    (13, 'Выкинь, Даня, это же химия!', "'Throw it out, Danya, that's chemicals!' Samsonov refuses to be outdone again."),
    (13, 'В лесу — только дровами!', "'In the forest, only with firewood!' Even when Slavik asks what is wrong with charcoal, Samsonov will not budge."),
    (13, 'Ну, вперёд!', "'Well, forward!' He marches Danya and Slavik into the trees with an axe."),
]
TRANSITION = "Now listen to the whole forest scene again from start to finish."
OUTRO = "Determined to prove who is the real man in the woods, Samsonov marches Danya and Slavik off to chop firewood by hand. Meanwhile, back in the communal flat, Arkady's porridge is finally ready. See you next time!"
CLOSING = ("samson", "Пока!")
