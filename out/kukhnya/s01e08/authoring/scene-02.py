# Authoring module for kukhnya-s01e08-scene-02.
ID = 'kukhnya-s01e08-scene-02'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 8
SCENE = 2
TITLE = 'Спор в прямом эфире  (On-Air Debate)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'elena': 'Елена'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.08'
SOURCE_FILE = 'sources/kukhnya/s01/e08.ru.dual.srt'
INTRO = "Live on the morning culinary broadcast 'A Tasty Morning', Chef Viktor Barinov demonstrates preparing a delicate young lamb dish. As the cameras roll, Barinov provokes rival head chef Elena Sokolova by claiming that male chefs inherently prepare meat better and asserting that women lack the stamina for professional restaurant leadership. Let's listen to their heated television exchange in Russian first."
OPENER = "Now let's examine Barinov and Elena's on-air debate line by line."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = "Elena bristles at Barinov's arrogant chauvinism, setting the stage for an explosive confrontation as the live broadcast continues into the commercial break. Next time you watch the episode, listen for the Russian expressions for 'dish' and 'to be' — you will catch every word right away. See you next time!"
CLOSING = ('barinov', 'Пока!')
STORY = [
    ('barinov', 'Сегодня я приготовлю мясо молодого ягнёнка.', 'Today I will prepare meat of a young lamb.', [(20, 'Я приготовлю сегодня жигой гненка')], ''),
    ('elena', 'Какое интересное и сложное мясное блюдо!', 'What an interesting and complex meat dish!', [(22, 'Это блюдо')], ''),
    ('barinov', 'Такое блюдо лучше всего готовят мужчины.', 'Men prepare such a dish best of all.', [(22, 'лучше всего удается поварам-мужчинам')], ''),
    ('elena', 'Почему вы говорите такие странные вещи?', 'Why do you say such strange things?', [(28, 'вы действительно считаете, что')], ''),
    ('barinov', 'Женщины часто режут мясо совсем неправильно.', 'Women often cut meat completely incorrectly.', [(25, 'а женщинам что-то норовят поперек')], ''),
    ('elena', 'Вы просто не уважаете женский талант.', 'You simply do not respect female talent.', [], ''),
    ('barinov', 'Женщина не способна стать великим шефом.', 'A woman is not capable of becoming a great chef.', [(26, 'женщина априори не может быть хорошим поваром')], ''),
    ('elena', 'Я руковожу кухней известного ресторана Аркабалено!', 'I run the kitchen of the famous Arcobaleno restaurant!', [], ''),
    ('barinov', 'Настоящий шеф-повар требует сильной воли.', 'A real head chef requires strong willpower.', [(27, 'Женщина на кухне — это кухарка')], ''),
    ('elena', 'У меня есть опыт и сильная воля.', 'I have experience and strong willpower.', [], ''),
    ('barinov', 'Для вас кухня остаётся обычной работой.', 'For you the kitchen remains an ordinary job.', [], ''),
    ('elena', 'Кухня — это вся моя жизнь, Виктор!', 'The kitchen is my whole life, Viktor!', [], ''),
    ('barinov', 'Мы скоро проверим ваши смелые слова.', 'We will soon check your bold words.', [], ''),
]
WALK = [
    (0, None, "'Today I will prepare meat of a young lamb.' Barinov kicks off the television broadcast with a grand announcement of his culinary plans."),
    (1, None, "'What an interesting and complex meat dish!' Elena jumps in with polite but slightly theatrical praise for his recipe choice."),
    (2, None, "'Men prepare such a dish best of all.' Barinov smoothly pivots to a sexist remark, claiming this level of cooking is for men."),
    (3, None, "'Why do you say such strange things?' Elena questions his sudden hostile turn in front of the live camera."),
    (4, None, "'Women often cut meat completely incorrectly.' He doubles down on his prejudice, specifically attacking women's knife skills."),
    (5, None, "'You simply do not respect female talent.' Elena calls out his blatant disrespect for female professionals."),
    (6, None, "'A woman is not capable of becoming a great chef.' Barinov makes a sweeping statement that women cannot reach the top ranks of the kitchen."),
    (7, None, "'I run the kitchen of the famous Arcobaleno restaurant!' Elena immediately fires back with her own prestigious head chef title as proof."),
    (8, None, "'A real head chef requires strong willpower.' Barinov implies that she lacks the inner strength required to run a real kitchen."),
    (9, None, "'I have experience and strong willpower.' Elena fiercely defends her competence and mental toughness."),
    (10, None, "'For you the kitchen remains an ordinary job.' He dismissively suggests that for her, cooking is just a job, not a calling."),
    (11, None, "'The kitchen is my whole life, Viktor!' Elena passionately corrects him, declaring that gastronomy is her entire existence."),
    (12, None, "'We will soon check your bold words.' Barinov issues a quiet challenge, setting the stage for their upcoming kitchen battle."),
]
