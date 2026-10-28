# domashniy-arest/s01e02/scene-23.py
ID = "domashniy-arest-s01e02-scene-23"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 2
SCENE = 23
TITLE = "Звонок от Третьякова  (A Call from Tretyakov)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.02"
SOURCE_FILE = "sources/domashniy-arest/s01/e02.ru.dual.srt"
VOICES = {"narrator": "sky", "anya": "alisa", "yulia": "angelina", "slavik": "anja"}
LABELS = {"anya": "Аркадий", "yulia": "Юля", "slavik": "Славик"}
INTRO = "Back in the communal flat, Arkady is with the children in the Samsonovs' room. Last time, at the university, Marina lost her job; and before that, the governor told Arkady that only one man in Moscow, a powerful official called Tretyakov, can help him. Now Arkady shows the children what Tretyakov is like. We'll hear it in Russian first; don't worry about catching every word."
STORY = [
    ("anya", "Вот это что такое, я вас спрашиваю!", "What is this, I'm asking you!", [(711, 'Вот это что такое, я вас спрашиваю')], "Arkady playing Tretyakov"),
    ("anya", "Что смотрите, бандерлоги? Вы совсем страх потеряли?", "What are you staring at, you monkeys? Have you lost all fear?", [(712, 'смотрите, бандерлоги'), (713, 'Вы совсем страх потеряли')], "'Че' -> 'Что'"),
    ("anya", "Ну как я позвоню этому Третьякову? Что я ему скажу?", "So how can I call this Tretyakov? What will I say to him?", [(729, 'Ну как я позвоню этому Третьякову? Что я ему скажу')], ""),
    ("anya", "Здравствуйте, Пётр Олегович, это Аникеев.", "Hello, Pyotr Olegovich, it's Anikeev.", [(730, 'здравствуйте, Петр Олегович, это Аникеев')], "'Скажу,' dropped"),
    ("anya", "Аникеев? Ну что, проворовался? Да я тебя посажу!", "Anikeev? Well then, caught stealing? I'll put you in prison!", [(731, 'Аникеев? Ну что, проворовался'), (732, 'Да я тебя посажу')], "the insults in cues 731-732 and the threat in 733 dropped"),
    ("slavik", "Очень похоже!", "That's just like him!", [(736, 'Очень похоже')], "speaker of cue 736 given to Slavik"),
    ("yulia", "Правда похоже. А может, вы сами позвоните губернатору?", "It really is. Why don't you call the governor yourself?", [(737, 'похоже'), (738, 'может, вы сами позвоните')], "'Да, реально похоже' (737) -> 'Правда похоже'; 'этому вашему губернатору' (738) -> 'губернатору'"),
    ("anya", "И что?", "And then what?", [(739, 'И что')], ""),
    ("yulia", "Я один раз позвонила как директор и отменила контрольную.", "Once I phoned pretending to be the headmistress and cancelled a test.", [(741, 'отменила контрольную')], "adapted from cues 740-741 ('развела', 'от имени директрисы' -> 'позвонила как директор')"),
    ("anya", "Со своего телефона? И все поверили?", "From your own phone? And everyone believed it?", [(742, 'со своего телефона'), (743, 'все поверили')], "the rest of cues 742-743 dropped"),
    ("yulia", "Нет, есть такие программы. Они меняют номер.", "No, there are apps for that. They change the number.", [(745, 'номер')], "adapted from cues 744-745 ('программ куча всяких', 'подменяют номер' -> 'меняют номер'); the app names dropped"),
    ("anya", "Бред какой-то. Но, с другой стороны, чем я рискую?", "What nonsense. But on the other hand, what have I got to lose?", [(748, 'Бред какой-то'), (750, 'Но, с другой стороны, чем я рискую')], "cue 749 dropped"),
    ("anya", "Так, давай свою программу попробуем.", "Right, let's try your app.", [(751, 'Так'), (751, 'давай свою программу попробуем')], "'слушай' dropped"),
    ("yulia", "А у меня её нет. Я её удалила.", "But I haven't got it. I deleted it.", [(752, 'у меня её нет'), (753, 'удалила')], "'Так' -> 'А'; 'там такой скандал был, ... нафиг' dropped"),
    ("yulia", "Теперь новую надо покупать.", "Now you'd have to buy a new one.", [(754, 'Теперь новую надо покупать')], ""),
    ("anya", "Сколько?", "How much?", [(755, 'Сколько')], ""),
    ("yulia", "Рублей пятьсот.", "About five hundred roubles.", [(756, 'Рублей пятьсот')], ""),
    ("anya", "Пятьсот. А у меня ни копейки.", "Five hundred. And I haven't got a penny.", [(757, 'Пятьсот')], "'Копейки нету. Чёрт.' -> 'А у меня ни копейки.'"),
]
OPENER = "Let's go through it together. Arkady is putting on a show: he plays Tretyakov, a loud, frightening boss."
WALK = [
    (0, None, "'What is this, I'm asking you!' A boss's favourite question, shouted at a room full of people. The 'you' is the plural, polite form, because he is shouting at everybody."),
    (1, 'Что смотрите, бандерлоги?', "'What are you staring at, you monkeys?' The odd word at the end is the name of the monkey people in Kipling's Jungle Book, a favourite insult of grumpy bosses."),
    (1, 'Вы совсем страх потеряли?', "'Have you lost all fear?' Literally, 'have you completely lost fear?' Then Arkady drops the act and explains his problem."),
    (2, 'Ну как я позвоню этому Третьякову?', "'So how can I call this Tretyakov?' The person you phone takes the form for 'to': this, and the name, both change their endings."),
    (2, 'Что я ему скажу?', "'What will I say to him?' Both verbs in this line are in the future. And he imagines the call."),
    (3, None, "'Hello, Pyotr Olegovich, it's Anikeev.' The long, polite greeting, with the first name and the father's name. And then he plays Tretyakov's answer."),
    (4, None, "'Anikeev? Well then, caught stealing? I'll put you in prison!' The verb in the middle means 'to get caught stealing from your job', and the last verb, literally 'I'll sit you down', is the everyday way to say 'I'll lock you up'. The children love it."),
    (5, None, "'That's just like him!' Literally, 'very similar'. Yulia agrees, and she has an idea."),
    (6, 'Правда похоже.', "'It really is.' Literally, 'truly similar'."),
    (6, 'А может, вы сами позвоните губернатору?', "'Why don't you call the governor yourself?' The children use the polite 'you' with Arkady. The word for 'self' is in the plural, to match. Her idea: Arkady can phone the governor and pretend to be Tretyakov. Arkady isn't convinced."),
    (7, None, "'And then what?' Two tiny words, very useful. Yulia tells him a story from school."),
    (8, None, "'Once I phoned pretending to be the headmistress and cancelled a test.' Both verbs are past and feminine, because Yulia is a girl. The little word in the middle means 'as'. Arkady wants to understand how it works."),
    (9, None, "'From your own phone? And everyone believed it?' The first part means 'from one's own phone': the word for 'own' always points back to the person doing the action. Yulia explains."),
    (10, None, "'No, there are apps for that. They change the number.' The call comes from your phone, but the other person sees someone else's number. Arkady thinks it over."),
    (11, None, "'What nonsense. But on the other hand, what have I got to lose?' The first part is a common way to say 'rubbish'. The last part is literally 'with what do I risk?' He decides to try it."),
    (12, None, "'Right, let's try your app.' 'Let's' is made with a word that literally means 'give', plus the verb in the 'we' form. But there's a problem."),
    (13, None, "'But I haven't got it. I deleted it.' To say 'I don't have it', Russian says 'at me there isn't it'. There was a scandal at school, so she got rid of it."),
    (14, None, "'Now you'd have to buy a new one.' The word in the middle means 'it's necessary'. So Arkady asks the obvious question."),
    (15, None, "'How much?' One word, and you'll use it in every shop."),
    (16, None, "'About five hundred roubles.' Putting the number after the noun makes it approximate, so this means 'roughly five hundred'."),
    (17, None, "'Five hundred. And I haven't got a penny.' The smallest Russian coin stands in for 'a penny'. The former mayor is completely broke."),
]
TRANSITION = "Now listen to the whole scene again, impression and all."
OUTRO = "So there's a plan: a fake call from Tretyakov, but no money even for the app. If the impression went by too fast, that's fine; it's loud and quick in the show too. See you next time!"
CLOSING = ("anya", "Пока!")
