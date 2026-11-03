# Authoring module for kukhnya-s01e06-scene-09.
ID = 'kukhnya-s01e06-scene-09'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 6
SCENE = 9
TITLE = 'Волос в тарелке  (A Hair on the Plate)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'guest': 'Гость', 'nastya': 'Настя'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.06'
SOURCE_FILE = 'sources/kukhnya/s01/e06.ru.dual.srt'
INTRO = "Out in the dining room of Claude Monet, a guest has found a hair in his dinner and has called over Nastya, the waitress. She is very calm. He is not. It's in Russian first, and you'll hear plenty of polite phrases."
OPENER = "Let's go back through the complaint. The guest raises his voice, and Nastya keeps hers very flat, which is where the joke is."
TRANSITION = "Here's the whole complaint again, from the top."
OUTRO = 'Nastya stays unshakably polite from her opening greeting to her promise to fetch the head chef, showing how a calm pro handles an angry diner. See you next time.'
CLOSING = ('nastya', 'Пока!')
STORY = [
    ('guest', 'Девушка, подойдите немедленно к нашему столу!', 'Miss, come over to our table immediately!', [(85, 'Бевушка')], ''),
    ('nastya', 'Добрый день, слушаю вас очень внимательно.', 'Good day, I am listening to you very attentively.', [(86, 'Слушаю вас')], ''),
    ('guest', 'Посмотрите на это, что это такое?', 'Look at this, what is that?', [(86, 'Это что')], ''),
    ('nastya', 'Я вижу, что это обычный волос.', 'I see that this is an ordinary hair.', [(87, 'Это волос')], ''),
    ('guest', 'Я тоже отлично вижу этот длинный волос!', 'I also see this long hair perfectly well!', [(88, 'Я вижу, что это волос')], ''),
    ('nastya', 'Тогда зачем вы об этом спрашиваете?', 'Then why are you asking about it?', [(89, 'А зачем тогда спрашиваете')], ''),
    ('guest', 'Как этот волос попал в тарелку?', 'How did this hair get onto the plate?', [(90, 'Я хочу понять, как этот волос попал ко мне в тарелку')], ''),
    ('nastya', 'Вероятно, он просто выпал из вашей головы.', 'Probably it simply fell out of your head.', [(91, 'Вероятно, выпал из вашей головы')], ''),
    ('guest', 'Такой длинный волос не может быть моим!', 'Such a long hair cannot be mine!', [(92, 'Такой длинный')], ''),
    ('nastya', 'Тогда, наверное, он выпал из бороды.', 'Then probably it fell out of a beard.', [(93, 'Наверное, из вашей бороды')], ''),
    ('guest', 'У меня нет бороды, позовите шефа!', 'I do not have a beard, call the chef!', [(94, 'У меня нет бороды'), (95, 'Позовите ко мне шеф-повара')], ''),
    ('nastya', 'Хорошо, я сейчас позову шеф-повара.', 'Fine, I will call the head chef right now.', [(96, 'Зову')], ''),
]
WALK = [
    (0, None, ["'Miss, come over to our table immediately!' In the first line, the word ", ('guest', 'немедленно'), ' translates to immediately, adding a strong sense of urgency.']),
    (1, None, ["'Good day, I am listening to you very attentively.' Next, the waitress calmly responds with ", ('nastya', 'внимательно'), ', meaning she is listening attentively to the complaint.']),
    (2, None, ["'Look at this, what is that?' The angry customer demands attention using ", ('guest', 'Посмотрите'), ', which translates to a polite but firm request to look.']),
    (3, None, ["'I see that this is an ordinary hair.' She keeps her cool and says ", ('nastya', 'обычный'), ', pointing out that it is just an ordinary hair.']),
    (4, None, ["'I also see this long hair perfectly well!' He clearly does not care, stating ", ('guest', 'отлично'), ' to emphasize that he can see it perfectly well too.']),
    (5, None, ["'Then why are you asking about it?' Then the waitress logically asks him ", ('nastya', 'зачем'), ', wondering what the point of his question was.']),
    (6, None, ["'How did this hair get onto the plate?' To express his utter confusion, he asks how it ", ('guest', 'попал'), ' onto the plate, which means landed or got there.']),
    (7, None, ["'Probably it simply fell out of your head.' Offering a very simple explanation, the word ", ('nastya', 'Вероятно'), ' is used to say that it probably fell from him.']),
    (8, None, ["'Such a long hair cannot be mine!' He rejects this idea completely, because ", ('guest', 'Такой'), ' means that such a long hair could not be his.']),
    (9, None, ["'Then probably it fell out of a beard.' She simply offers another guess with ", ('nastya', 'наверное'), ', suggesting it most likely came from a beard instead.']),
    (10, None, ["'I do not have a beard, call the chef!' Getting even more frustrated, he demands ", ('guest', 'позовите'), ', telling her to call the chef right away.']),
    (11, None, ["'Fine, I will call the head chef right now.' To finally resolve the situation, she says ", ('nastya', 'Хорошо'), ', agreeing to bring the head chef over right now.']),
]
