# Authoring module for domashniy-arest-s01e08-scene-18.
ID = 'domashniy-arest-s01e08-scene-18'
SHOW = 'domashniy-arest'
SEASON = 1
EPISODE = 8
SCENE = 18
TITLE = 'Лёша берёт вину на себя  (Lyosha Takes the Blame)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'arkady': 'Аркадий', 'lyosha': 'Лёша', 'marina': 'Марина'}
SOURCE_NAME = 'Домашний арест, Сезон 1, Эпизод 8'
SOURCE_FILE = 'sources/domashniy-arest/s01/e08.ru.dual.srt'
INTRO = "Previously, after Arkady accidentally stepped on Lyosha's plastic toy tank, the boy threatened to tell his mother. Now, in the communal hallway, Arkady admits that he only wanted to repair the toy to impress Marina, just as Marina suddenly walks in searching for her son."
OPENER = "Let's see how Lyosha unexpectedly protects Arkady in this tense scene."
TRANSITION = 'Now listen to the conversation in the hallway again.'
OUTRO = "Marina scolds Lyosha for being clumsy, leaving Arkady grateful and surprised by the boy's loyalty. See you next time!"
CLOSING = ('arkady', 'Пока!')
STORY = [
    ('lyosha', 'Я всё маме расскажу!', "I'm telling Mom everything!", [(264, 'Я все маме расскажу')], ''),
    ('arkady', 'Ну давай, расскажи своей маме.', 'Go ahead, tell your mom.', [(265, 'Ну давай, расскажи своей маме')], ''),
    ('arkady', 'Она меня и так ненавидит.', 'She already hates me anyway.', [(266, 'Она меня и так ненавидит')], ''),
    ('arkady', 'Я этот танк для неё чинил.', 'I fixed that tank for her.', [(267, 'этот танк'), (267, 'чинил, а для нее')], 'simplified cue 267'),
    ('lyosha', 'Мама в танки не играет.', "Mom doesn't play tanks.", [(268, 'Мама в танки не играет')], ''),
    ('arkady', 'Чтобы она за тебя порадовалась! И меня простила.', "So she'd be happy for you! And forgive me.", [(269, 'она за тебя порадовалась'), (270, 'Меня простила')], 'combined cues 269-270'),
    ('arkady', 'Твоя мама мне очень нравится.', 'I like your mom very much.', [(271, 'Твоя мама мне нравится')], 'added очень'),
    ('lyosha', 'Моя мама добрая.', 'My mom is kind.', [(273, 'Мама добрая')], 'added Моя'),
    ('arkady', 'Для тебя она добрая. А меня она выгонит!', "She's kind to you. But she'll kick me out!", [(274, 'Для тебя она добрая'), (275, 'А меня она')], 'cleaned crude cue 275'),
    ('marina', 'Лёша, ты что здесь делаешь?', 'Lyosha, what are you doing here?', [(278, 'ты что здесь делаешь')], 'shortened cue 278'),
    ('marina', 'Я тебя по всей квартире ищу!', "I've been looking all over the apartment for you!", [(278, 'Я тебя по всей квартире ищу')], ''),
    ('marina', 'С танком что? Опять ваши проделки?', 'What happened to the tank? Your tricks again?', [(279, 'С танком что? Опять ваши проделки?')], ''),
    ('lyosha', 'Нет, мам! Дядя Аркадий танк починил.', 'No, Mom! Uncle Arkady fixed the tank.', [(280, 'Нет, мам. Дядя Аркадий'), (280, 'танк починил')], 'shortened cue 280'),
    ('lyosha', 'А я наступил на него случайно.', 'And I stepped on it by accident.', [(281, 'а я наступил на него случайно')], ''),
    ('marina', 'Подарки надо ценить! А вы не вмешивайтесь.', 'You must appreciate gifts! And you, stay out of it.', [(282, 'Подарки надо ценить'), (285, 'А вы не вмешивайтесь')], 'combined cues 282 and 285'),
]
WALK = [
    (0, None, "'I am telling Mom everything!' Furious over his crushed tank, Lyosha threatens to go straight to his mother."),
    (1, None, "'Go ahead, tell your mom.' Arkady shrugs helplessly and tells the boy to go right ahead."),
    (2, None, "'She already hates me anyway.' In Arkady's gloomy view, Marina's opinion of him could not sink any lower anyway."),
    (3, None, "'I fixed that tank for her.' He confesses that he wanted to win over Marina."),
    (4, None, "'Mom does not play tanks.' The boy points out the obvious flaw in his logic."),
    (5, 'Чтобы она за тебя порадовалась!', "'So she would be happy for you!' He explains his roundabout logic: making the son happy was supposed to make the mother smile."),
    (6, None, "'I like your mom very much.' Arkady openly reveals his feelings to the boy."),
    (7, None, "'My mom is kind.' Lyosha defends his mother warmly — she isn't the monster Arkady makes her out to be."),
    (9, None, "'Lyosha, what are you doing here?' Marina's sudden question catches them both off guard."),
    (11, None, "'What happened to the tank? Your tricks again?' She immediately suspects Arkady."),
    (12, None, "'No, Mom! Uncle Arkady fixed the tank.' Lyosha surprises him by speaking up."),
    (13, None, "'And I stepped on it by accident.' The boy takes the entire blame onto himself."),
    (14, 'А вы не вмешивайтесь.', "'And you, stay out of it.' Even after Lyosha covers for him, Marina still shoots Arkady a frosty look and tells him to butt out."),
]
