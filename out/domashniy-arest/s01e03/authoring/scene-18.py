# Authoring module for domashniy-arest-s01e03-scene-18.
ID = 'domashniy-arest-s01e03-scene-18'
SHOW = 'domashniy-arest'
SEASON = 1
EPISODE = 3
SCENE = 18
TITLE = "Подарки декана  (The Dean's Presents)"
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'arkady': 'Аркадий', 'dean': 'Эдуард Владимирович', 'marina': 'Марина'}
SOURCE_NAME = 'Домашний арест (Domashniy Arest) S1.03'
SOURCE_FILE = 'sources/domashniy-arest/s01/e03.ru.dual.srt'
INTRO = "She walks out saying she cannot stand being in the same room with him. In her room, her ex-lover, the dean Eduard Vladimirovich, arrives with presents to beg for forgiveness and spots the small foil packet on her table just as Arkady walks in. Let's listen in Russian first."
OPENER = "Let's go back through the scene line by line. The dean stands in Marina's doorway holding a guitar box and a bag of groceries."
TRANSITION = "Now let's hear the whole scene again from start to finish."
OUTRO = "So Marina's cover story leaves the dean heartbroken and leaves Arkady with a free bottle of Chilean wine and fresh berries. See you next time!"
CLOSING = ('dean', 'Пока!')
STORY = [
    ('dean', 'Пожалуйста, не гони меня. Я знаю, что я виноват.', "Please, don't chase me away. I know it's my fault.", [(548, 'Пожалуйста, не гони меня'), (551, 'Я знаю, что я виноват')], ''),
    ('dean', 'Это электрогитара для Лёши. А тебе я взял чилийское вино и ягоды.', 'Look, this is an electric guitar for Lyosha. And for you I brought Chilean wine and berries.', [(555, 'это электрогитара для Леши'), (557, 'А тебе'), (557, 'я взял чилийское вино и'), (557, 'ягоды')], "'между прочим' and 'вот' trimmed"),
    ('marina', 'Эдик, уходи, пожалуйста.', 'Edik, please leave.', [(559, 'Эдик, уходи, пожалуйста')], ''),
    ('dean', 'Это что такое?', 'What is this?', [(561, 'Это что такое')], 'spotting the small foil packet on the table'),
    ('marina', 'Это не то, что ты подумал. Всё, уходи.', "It's not what you think. That's it, get out.", [(562, 'Это не то, что ты подумал'), (569, 'Все, уходи')], ''),
    ('dean', 'Что значит, уходи? Я требую объяснений, Марина.', 'What do you mean, get out? I demand an explanation, Marina.', [(570, 'Что значит, уходи? Я требую объяснений, Марина')], ''),
    ('marina', 'Каких объяснений? Я что, жена тебе?', 'What explanation? Am I your wife?', [(571, 'Каких объяснений'), (572, 'Я что, жена тебе')], "'что ли' trimmed"),
    ('arkady', 'Эдуард Владимирович, здравствуйте. А Алла Евгеньевна как же?', 'Eduard Vladimirovich, hello. And what about Alla Yevgenyevna?', [(575, 'Эдуард'), (575, 'здравствуйте'), (581, 'а Алла Евгеньевна как же')], "cue 575 says 'Валентинович'; kept 'Владимирович' as in characters.md"),
    ('dean', 'Здравствуйте. Оставьте в покое Аллу Евгеньевну!', 'Hello. Leave Alla Yevgenyevna alone!', [(576, 'Здравствуйте'), (583, 'оставьте в покое Аллу Евгеньевну')], ''),
    ('dean', 'Не надо лезть в нашу личную жизнь. Марина, это для него?', "And don't meddle in our private life. Marina, is this for him?", [(584, 'не надо лезть в нашу личную жизнь'), (594, 'Марина, это'), (595, 'для него')], 'skipping crude cues 586 and 591'),
    ('marina', 'Эдик, я хотела тебе изменить. С ним, чтобы отомстить.', 'Edik, I wanted to cheat on you. With him, to take revenge.', [(601, 'Эдик, я хотела тебе изменить'), (603, 'С ним'), (604, 'Чтобы отомстить')], ''),
    ('marina', 'Но он слишком мерзкий, и я передумала.', 'But he is too disgusting, and I changed my mind.', [(606, 'Но он'), (606, 'слишком мерзкий, и я передумала')], "'оказался' dropped for A1 length"),
    ('arkady', 'Я мерзкий? Марина, послушайте, это я вам отказал!', "I'm disgusting? Marina, listen, I was the one who turned you down!", [(607, 'Я'), (608, 'Марина, послушайте, это я вам'), (608, 'отказал')], "cue 607 'оказался мерзким' -> 'мерзкий'; 'вообще-то' trimmed"),
    ('dean', 'Всё, я ухожу. Ребёнок ни при чём. Передай это Алексею.', "That's it, I'm leaving. The child isn't to blame. Give this to Alexei.", [(611, 'Все, я ухожу'), (613, 'Ребенок ни при чем'), (614, 'Передай'), (614, 'это Алексею')], "'пожалуйста' trimmed"),
    ('arkady', 'А вино с фруктами?', 'And what about the wine and fruit?', [(617, 'А вино с фруктами')], ''),
    ('dean', 'Это вам сейчас необходимо.', 'You need this right now.', [(619, 'Это вам сейчас необходимо')], ''),
    ('marina', 'Эдик, подожди! Я прошу тебя.', "Edik, wait! I'm begging you.", [(620, 'Эдик, подожди'), (621, 'Я прошу тебя')], ''),
]
WALK = [
    (0, 'Пожалуйста, не гони меня.', "'Please, don't chase me away.' He starts with 'please' and a negative command: 'don't drive me out'."),
    (0, 'Я знаю, что я виноват.', "'I know it's my fault.' Word for word: 'I know that I am guilty'. The short form at the end is masculine because Edik is a man. Then he shows his peace offerings."),
    (1, 'Это электрогитара для Лёши.', "'This is an electric guitar for Lyosha.' After 'for', the boy's name takes the 'of' ending."),
    (1, 'А тебе я взял чилийское вино и ягоды.', "'And for you I brought Chilean wine and berries.' Literally 'to you I took'. 'Wine' is neuter in Russian, so the describing word 'Chilean' ends in '-oye'. Marina is not won over."),
    (2, None, "'Edik, please leave.' She uses his short name, Edik, and the informal command 'go away'. Then Edik looks down at the table and sees the small foil wrapper with the hidden bug inside."),
    (3, None, "'What is this?' Three short words of pure shock. Marina tries to brush it off."),
    (4, 'Это не то, что ты подумал.', "'It's not what you think.' Literally 'this is not that which you thought'. And she tries to push him out the door."),
    (4, 'Всё, уходи.', "'That's it, get out.' Literally 'all, go away'. Now the dean is furious."),
    (5, 'Что значит, уходи?', "'What do you mean, get out?' Word for word: 'what means, go away?'."),
    (5, 'Я требую объяснений, Марина.', "'I demand an explanation, Marina.' In Russian he says 'explanations' in the plural, in the 'of' form after the action word 'demand'. Marina fires right back."),
    (6, None, "'What explanation? Am I your wife?' Remember, the dean is married and fired her from the university to save his own skin. At the worst possible moment, Arkady strolls in."),
    (7, 'Эдуард Владимирович, здравствуйте.', "'Eduard Vladimirovich, hello.' Arkady greets the dean politely by name and patronymic, delighted by the drama."),
    (7, 'А Алла Евгеньевна как же?', "'And what about Alla Yevgenyevna?' That is the dean's wife. Arkady loves reminding him that he is a married man."),
    (8, None, "'Hello. Leave Alla Yevgenyevna alone!' Literally 'leave Alla Yevgenyevna in peace'. Then he tells Arkady to mind his own business."),
    (9, 'Не надо лезть в нашу личную жизнь.', "'Don't meddle in our private life.' Literally 'it is not necessary to climb into our personal life'. Then he connects Arkady with the foil packet on the table."),
    (9, 'Марина, это для него?', "'Marina, is this for him?' Since Marina cannot reveal that the packet holds a secret-service microphone, she makes up a story that also hurts Edik."),
    (10, 'Эдик, я хотела тебе изменить.', "'Edik, I wanted to cheat on you.' 'I wanted' has the feminine '-a' ending. The action word 'to betray' or 'cheat on' takes the 'to' case: 'to you'."),
    (10, 'С ним, чтобы отомстить.', "'With him, to take revenge.' 'With' takes the 'with'-form form of 'he', which starts with an 'n' after a little word. Then she adds an insult for Arkady."),
    (11, None, "'But he is too disgusting, and I changed my mind.' The prefix on the action word at the end means 're-think' or 'change one's mind'. Arkady's pride cannot take that."),
    (12, 'Я мерзкий?', "'I'm disgusting?' He drops the feminine ending and uses the masculine '-iy' for himself."),
    (12, 'Марина, послушайте, это я вам отказал!', "'Marina, listen, I was the one who turned you down!' Even while arguing about an imaginary affair, they stay on the formal 'you'. The dean has heard enough."),
    (13, 'Всё, я ухожу.', "'That's it, I'm leaving.' Present tense for an action happening right now."),
    (13, 'Ребёнок ни при чём.', "'The child isn't to blame.' An idiomatic phrase meaning 'the child has nothing to do with this'."),
    (13, 'Передай это Алексею.', "'Give this to Alexei.' He uses Lyosha's full name, Alexei, in the 'to' form, and leaves the guitar behind. Arkady spots an opportunity."),
    (14, None, "'And what about the wine and fruit?' After 'with', 'fruit' is in the 'with/as' form plural. The dean shoves the bag into Arkady's arms."),
    (15, None, "'You need this right now.' Literally 'this to you now is necessary'. And he storms out while Marina calls after him."),
    (16, None, "'Edik, wait! I'm begging you.' Two short pleas, but the door is already shut."),
]
