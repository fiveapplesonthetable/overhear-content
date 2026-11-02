# Authoring module for kukhnya-s01e14-scene-20.
ID = 'kukhnya-s01e14-scene-20'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 14
SCENE = 20
TITLE = 'Сосед из Парижа  (A Neighbor from Paris)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'jacques': 'Жак', 'nagiyev': 'Нагиев'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.14'
SOURCE_FILE = 'sources/kukhnya/s01/e14.ru.dual.srt'
INTRO = 'Barinov and Nagiyev are with a French friend, Jacques, who has arrived for the dinner. Jacques mumbles in French and tries to kiss Barinov. The greeting, first in Russian.'
OPENER = 'Back through the greeting, slowly.'
TRANSITION = 'And the greeting again, uncut.'
OUTRO = "Jacques gets a plate of food instead of a kiss. Barinov enjoys his friend's company. Talk soon."
CLOSING = ('barinov', 'Пока!')
STORY = [
    ('barinov', 'Давайте мы попробуем это.', "Let's try this.", [(283, 'давайте попробуем.')], ''),
    ('barinov', 'Жак, ты где?', 'Jacques, where are you?', [(284, 'Жак!')], ''),
    ('jacques', 'Я здесь, я иду!', 'I am here, I am coming!', [(285, 'Жак! Несу, несу!')], ''),
    ('nagiyev', 'А вы кто такой?', 'And who are you?', [(288, 'А вы кто? Сосед.')], ''),
    ('barinov', 'Он мой сосед.', 'He is my neighbor.', [(288, 'Сосед.')], ''),
    ('barinov', 'Представляешь, мы жили в Париже.', 'Can you imagine, we lived in Paris.', [(290, 'Его. Представляешь, мы с ним жили в Париже на соседних улицах.')], ''),
    ('barinov', 'Подожди, мы не будем целоваться.', 'Wait, we are not going to kiss.', [(293, 'Подожди, целоваться.')], ''),
    ('barinov', 'Сначала надо закусить.', 'First we need to have a bite.', [(294, 'Сначала закусить.')], ''),
    ('barinov', 'На, попробуй это.', 'Here, try this.', [(295, 'На, попробуй.')], ''),
    ('jacques', 'Это очень вкусно.', 'This is very delicious.', [(296, 'Очень вкусно.')], ''),
    ('nagiyev', 'Он говорит, что это вкусно?', 'He says that it is delicious?', [], ''),
    ('barinov', 'Да, ему очень нравится.', 'Yes, he likes it very much.', [], ''),
    ('jacques', 'Спасибо, мой дорогой друг.', 'Thank you, my dear friend.', [], ''),
    ('barinov', 'Пожалуйста, кушай на здоровье.', 'You are welcome, eat to your health.', [], ''),
]
WALK = [
    (0, None, ["'Let's try this.' Now let's break down the sentence: ", ('barinov', 'Давайте'), " with a 'we' future makes a group suggestion. ", ('barinov', 'попробуем'), " covers both 'try' and 'taste'."]),
    (1, None, ["'Jacques, where are you?' Now we can consider the sentence: ", ('barinov', 'ты'), ('barinov', 'где'), " literally means 'you where'. In casual speech the question word can come last."]),
    (2, None, ["'I am here, I am coming!' Now we can look at this part: ", ('jacques', 'иду'), " means 'going on foot', and shouted like this it means 'coming!'. ", ('jacques', 'здесь'), " is 'here' as a place where you are."]),
    (3, None, ["'And who are you?' Nagiyev uses the polite 'you', but keeps ", ('nagiyev', 'такой'), " in the singular because he's asking one man. ", ('nagiyev', 'кто'), ('nagiyev', 'такой'), " is pointed, like asking 'and who might you be?'."]),
    (4, None, ["'He is my neighbor.' The sentence has no verb, just 'he my neighbour'. A woman neighbour would use a different ending for ", ('barinov', 'сосед'), '.']),
    (5, None, ["'Can you imagine, we lived in Paris.' Barinov explains, using ", ('barinov', 'Представляешь'), ", which literally means 'you imagine', as a way to say 'can you believe it'. Notice for Paris becomes ", ('barinov', 'Париже'), " after 'in'."]),
    (6, None, ["'Wait, we are not going to kiss.' The ending on ", ('barinov', 'целоваться'), " means 'each other', so it's 'kiss each other'. ", ('barinov', 'не'), ('barinov', 'будем'), " is 'we won't'."]),
    (7, None, ["'First we need to have a bite.' Now let's look at the sentence: ", ('barinov', 'закусить'), ' means to eat a bite, often after a drink.']),
    (8, None, ["'Here, try this.' Now we can examine this part: ", ('barinov', 'На'), ", said while handing something over, means 'here, take it'. ", ('barinov', 'попробуй'), " is the order form of 'try'."]),
    (9, None, ["'This is very delicious.' This sentence has no verb at all. ", ('jacques', 'вкусно'), " means tasty, and it's a word you'll use a lot at any table."]),
    (10, None, ["'He says that it is delicious?' Now we can inspect this part: ", ('nagiyev', 'что'), " here means 'that', not 'what'. Nagiyev can't understand the French and asks Barinov."]),
    (11, None, ["'Yes, he likes it very much.' Let us examine the dialogue: ", ('barinov', 'нравится'), " means 'is pleasing'. The food is what is pleasing, and the person is ", ('barinov', 'ему'), '.']),
    (12, None, ["'Thank you, my dear friend.' Let's break down this part: ", ('jacques', 'мой'), ('jacques', 'дорогой'), ('jacques', 'друг'), '. If speaking to a woman, they would have different endings.']),
    (13, None, ["'You are welcome, eat to your health.' Now let's inspect the speech: ", ('barinov', 'на'), ('barinov', 'здоровье'), ", 'to health', is the reply when someone thanks you for food. Despite the myth, it isn't the usual toast."]),
]
