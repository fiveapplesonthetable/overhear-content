# Authoring module for kukhnya-s01e13-scene-02.
ID = 'kukhnya-s01e13-scene-02'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 13
SCENE = 2
TITLE = "Чужая машина  (Someone Else's Car)"
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'elena': 'Елена'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.13'
SOURCE_FILE = 'sources/kukhnya/s01/e13.ru.dual.srt'
INTRO = "The next morning, Barinov finds a strange car parked in his usual space behind the restaurant. The driver turns out to be Elena, the chef from the Italian place next door. Their first meeting comes in the local language."
OPENER = 'One jab at a time, then.'
TRANSITION = 'Here is the quarrel in one go.'
OUTRO = "Elena wins the first round, politely and without budging. Notice how both of them stay on the polite formal language while they insult each other. Catch you next time."
CLOSING = ('elena', 'Пока!')
STORY = [
    ('barinov', 'Кто поставил сюда эту старую машину?', 'Who parked this old car here?', [(26, 'Какой кретин поставил сюда машину?')], ''),
    ('elena', 'Здравствуйте. Я поставила свою машину.', 'Hello. I parked my car.', [], ''),
    ('barinov', 'Женщина, уберите автомобиль с моего места.', 'Woman, move the automobile from my spot.', [(29, 'моего')], ''),
    ('elena', 'Где написано, что это ваше место?', 'Where does it say this is your spot?', [(15, 'что')], ''),
    ('barinov', 'Здесь висит знак с предупреждением.', 'A warning sign is hanging here.', [(28, 'здесь')], ''),
    ('elena', 'Там написано только про сосульки.', 'It only says about icicles there.', [(18, 'там')], ''),
    ('barinov', 'Я шеф-повар этого известного ресторана.', 'I am the head chef of this famous restaurant.', [], ''),
    ('elena', 'А я шеф-повар соседнего ресторана.', 'And I am the head chef of the neighboring restaurant.', [], ''),
    ('barinov', 'Тогда вы должны понимать правила.', 'Then you must understand the rules.', [], ''),
    ('elena', 'Я не буду переставлять свою машину.', 'I will not move my car.', [(26, 'машину')], ''),
    ('elena', 'Вон там есть другое свободное место.', 'Over there is another open spot.', [(18, 'там')], ''),
    ('barinov', 'Какая упрямая и вредная женщина!', 'What a stubborn and obnoxious woman!', [], ''),
    ('elena', 'Приятного рабочего дня, господин шеф!', 'Have a nice working day, Mr. Chef!', [], ''),
]
WALK = [
    (0, None, ["'Who parked this old car here?' Locals do not 'park' a car, they 'put' it, so the word ", ('barinov', 'поставил'), " is 'put' or 'stood'. The term ", ('barinov', 'сюда'), " means 'to here', as it would in 'come here'."]),
    (1, None, ["'Hello. I parked my car.' The long, polite hello is for strangers. Elena is a woman, so 'parked' ends in 'a', and the term for 'my', ", ('elena', 'свою'), ", is 'my own', the term the language uses when the owner is the subject of the sentence."]),
    (2, None, ["'Woman, move the automobile from my spot.' Calling a woman just ", ('barinov', 'Женщина'), " is rude, like shouting 'Hey, woman!'. Notice for automobile, ", ('barinov', 'автомобиль'), ", is the stiff word for 'car' where the standard word carries an everyday one. Barinov is trying to sound official."]),
    (3, None, ["'Where does it say this is your spot?' The term for 'is written', ", ('elena', 'написано'), ", does not say who wrote it. The term for 'your', ", ('elena', 'ваше'), ", gives the polite 'your', fitting for a stranger."]),
    (4, None, ["'A warning sign is hanging here.' A sign 'hangs' in the local language, ", ('barinov', 'висит'), ", where English just says 'there is'. The expression for 'with a warning', ", ('barinov', 'с'), ('barinov', 'предупреждением'), ", uses the ending for 'with'."]),
    (5, None, ["'It only says about icicles there.' The term for icicles is ", ('elena', 'сосульки'), ". Signs warning of falling icicles are a regular sight on winter buildings, and Elena points out that it says nothing about parking. The term for 'is written' is back, and the term for 'about' is ", ('elena', 'про'), '.']),
    (6, None, ["'I am the head chef of this famous restaurant.' There is no 'am', so it is just 'I head-chef'. The term for 'head chef' is ", ('barinov', 'шеф'), '-', ('barinov', 'повар'), ", and the term for 'well known' is ", ('barinov', 'известного'), '. He is boasting.']),
    (7, None, ["'And I am the head chef of the neighboring restaurant.' The little 'and' at the front, ", ('elena', 'А'), ", carries a hint of 'but', which is the right mood for a comeback. The term for 'neighboring', ", ('elena', 'соседнего'), ', comes from the word for neighbour.']),
    (8, None, ["'Then you must understand the rules.' Barinov uses the polite 'you must' for a stranger. Notice for 'must', ", ('barinov', 'должны'), ", is the plural form that goes with the formal 'you', followed by the plain verb to understand, ", ('barinov', 'понимать'), '.']),
    (9, None, ["'I will not move my car.' Elena's 'I won't' uses ", ('elena', 'буду'), ", the same word that means 'I will be'. The prefix on the moving action, ", ('elena', 'переставлять'), ", means 'over' or 'again'."]),
    (10, None, ["'Over there is another open spot.' The pointing phrase for 'over there', ", ('elena', 'Вон'), ('elena', 'там'), ", is further away than just 'there'. The words for 'another' and 'open' both end in 'oe' because the word for spot is a neuter word."]),
    (11, None, ["'What a stubborn and obnoxious woman!' Let's break down the dialogue: ", ('barinov', 'Какая'), " with an exclamation means 'what a'. Notice for 'stubborn' is ", ('barinov', 'упрямая'), " and the term for 'obnoxious' is ", ('barinov', 'вредная'), ", which means 'harmful' or 'nasty'. Both end in 'aya' because the term for woman is feminine."]),
    (12, None, ["'Have a nice working day, Mr. Chef!' Wishes in the local language use an 'of': 'of a pleasant working day'. The old-fashioned 'Mr.', ", ('elena', 'господин'), ', is how Elena teases him.']),
]
