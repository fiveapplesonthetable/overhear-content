# domashniy-arest/s01e04/scene-28.py
ID = "domashniy-arest-s01e04-scene-28"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 4
SCENE = 28
TITLE = "Народный герой  (A People's Hero)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.04"
SOURCE_FILE = "sources/domashniy-arest/s01/e04.ru.dual.srt"
VOICES = {"narrator": "sky", "ilona": "angelina", "anya": "alisa", "golovkin": "anja"}
LABELS = {"ilona": "Илона", "anya": "Аркадий", "golovkin": "Головкин"}
INTRO = "Back at the communal flat that night. Now, in Arkady's room, Golovkin has news about Arkady's sentence when Ilona suddenly walks in. Let's listen in Russian first."
STORY = [
    ("golovkin", "Аркадий Борисович, я выполнил свою часть сделки.", "Arkady Borisovich, I kept my part of the deal.", [(1092, 'Аркадий Борисович, я'), (1092, 'выполнил свою часть сделки')], "'же' dropped"),
    ("golovkin", "Теперь я снова ваш адвокат.", "Now I am your lawyer again.", [(1093, 'Теперь'), (1093, 'я'), (1093, 'ваш адвокат')], "mistranscribed 'Санова' -> 'снова'"),
    ("anya", "Прекрасно.", "Excellent.", [(1095, 'Прекрасно')], ""),
    ("golovkin", "Я подумал. Можно получить на год меньше!", "I thought about it. You can get a year less!", [(1096, 'Я подумал'), (1098, 'можно получить на'), (1098, 'год меньше')], "'целый' dropped"),
    ("golovkin", "Не восемь лет, а семь.", "Not eight years, but seven.", [(1099, 'Не восемь, а семь')], "'лет' added"),
    ("anya", "Пошёл вон отсюда! Уходи быстро!", "Get out of here! Leave quickly!", [(1101, 'вон отсюда')], "mistranscribed 'Пошла' -> masculine 'Пошёл' (to Golovkin); 'пока я тебя не придушил' -> 'Уходи быстро!'"),
    ("ilona", "Привет! Принимай подарки.", "Hi! Here are your presents.", [(1100, 'Принимай подарки')], "'Привет!' added as Ilona walks in with a pillow, blanket, and vodka"),
    ("golovkin", "Здравствуйте.", "Hello.", [(1103, 'Здравствуйте')], ""),
    ("ilona", "Я удалила видео с твоим Самсоновым.", "I deleted the video with your Samsonov.", [(1104, 'Я удалила'), (1104, 'с твоим Самсоновым')], "'записи' -> 'видео'"),
    ("anya", "Правда? А это водка?", "Really? And is that vodka?", [(1105, 'Водка')], "'Правда? А это' added"),
    ("ilona", "Да. Я теперь в вашей команде.", "Yes. I'm on your team now.", [], "new: clean A1 for cue 1106 'Решила примкнуть к вашему народному восстанию'"),
    ("ilona", "Но учти: мне проигрывать нельзя.", "But bear in mind: I must not lose.", [(1107, 'Но учти, мне проигрывать нельзя')], ""),
    ("anya", "Мы их всех победим!", "We will defeat them all!", [], "new: clean A1 for cue 1111 'Мы их раздадим, мы их уничтожим'"),
    ("ilona", "Во-первых, надо собрать подписи.", "First of all, we need to collect signatures.", [(1112, 'во-первых, надо собрать подписи')], "'Значит,' dropped"),
    ("anya", "Это легко. Тогда нам дадут деньги!", "That's easy. Then they'll give us money!", [(1113, 'Это легко'), (1115, 'Тогда нам дадут')], "'бабки' -> 'деньги'"),
    ("ilona", "Мы сделаем из него народного героя!", "We will make him a people's hero!", [(1116, 'Мы'), (1116, 'народного героя')], "'создадим образ народного героя, за которым пойдут все' -> 'сделаем из него народного героя!'"),
]
OPENER = "Let's walk through it slowly. Golovkin is trying to cheer up a very gloomy Arkady."
WALK = [
    (0, None, "'Arkady Borisovich, I kept my part of the deal.' Golovkin delivered the bribe to the cemetery manager, as Arkady demanded. 'Of the deal' takes the feminine 'of' ending. He reminds Arkady of what comes next."),
    (1, None, "'Now I am your lawyer again.' Remember that Russian uses no word for 'am' in the present tense. Arkady barely looks up."),
    (2, None, "'Excellent.' One dry word. But Golovkin has a legal idea he is proud of."),
    (3, None, "'I thought about it. You can get a year less!' Literally, 'it is possible to get by a year less'. And he does the arithmetic."),
    (4, None, "'Not eight years, but seven.' After numbers from five upwards, 'years' uses a special plural word that originally meant 'summers'. Seven years in prison does not cheer Arkady up."),
    (5, None, "'Get out of here! Leave quickly!' In the show Arkady threatens to strangle him if he doesn't leave right now. Just then, the door opens and Ilona walks in carrying a white pillow, a blanket, and a bottle."),
    (6, None, "'Hi! Here are your presents.' Literally, 'receive presents!', an informal command to an old friend. Nervous Golovkin greets her politely."),
    (7, None, "'Hello.' Ilona sets the pillow on the bed and drops her bombshell."),
    (8, None, "'I deleted the video with your Samsonov.' The verb has the feminine past ending '-a' because Ilona is a woman, and Samsonov takes the 'with' ending. Arkady stares at the bottle in her hand."),
    (9, None, "'Really? And is that vodka?' After losing everything all day, he can hardly believe his luck. Ilona confirms it."),
    (10, None, "'Yes. I'm on your team now.' Literally, 'in your team'. In the show she jokes that she has decided to join their people's uprising. Then she gives him a warning."),
    (11, None, "'But bear in mind: I must not lose.' Literally, 'to me to lose is forbidden'. Across the courtyard at the listening post, Major Lavrov and Captain Zavarzin hear her voice through the bug and groan: now she is on Arkady's side too, so they will be stuck here for a long time. Arkady is already full of energy."),
    (12, None, "'We will defeat them all!' A completed-action future verb: 'we will win over them all'. Ilona gets straight down to campaign business."),
    (13, None, "'First of all, we need to collect signatures.' To register Samson as an independent candidate for mayor, they need voters' signatures. Arkady nods."),
    (14, None, "'That's easy. Then they'll give us money!' Once they boost Samson's internet fame, sponsors will back the campaign. Ilona sums up the plan."),
    (15, None, "'We will make him a people's hero!' Literally, 'we will make out of him a people's hero', with the animate object taking the '-a' ending."),
]
TRANSITION = "Let's hear the whole scene again, from the beginning."
OUTRO = "So Pasha's best strategist is now in Arkady's room with a pillow, a bottle, and a plan to turn Samson into a people's hero. Meanwhile, Samson himself is behind the wheel of a luxury car. See you next time!"
CLOSING = ("ilona", "Пока!")
