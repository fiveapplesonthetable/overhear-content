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
INTRO = "Back in the television studio, the cooking show is on air. Barinov is cooking young lamb, and beside him sits his rival, Elena Sokolova, who runs Arcobaleno, the Italian restaurant across the road. He picks this moment to say what he thinks about women in kitchens. It's in Russian first."
OPENER = "Let's go back through it. Barinov stirs things up, and Elena answers him calmly and firmly."
TRANSITION = "Now let's hear the two of them again without stopping."
OUTRO = "Elena's lines are the ones to keep: 'I have experience' and 'the kitchen is my whole life'. Swap in your own work and they're yours. See you next time."
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
    (0, None, ["'Today I will prepare meat of a young lamb.' Notice how he uses the word ", ('barinov', 'приготовлю'), ' to show he fully intends to finish making the meal.']),
    (1, None, ["'What an interesting and complex meat dish!' To express her strong feelings, she says ", ('elena', 'Какое'), ' to mean what an interesting and complex dish it is.']),
    (2, None, ["'Men prepare such a dish best of all.' By putting the people who cook, ", ('barinov', 'мужчины'), ', at the very end of his remark, he makes his point hit harder.']),
    (3, None, ["'Why do you say such strange things?' She addresses him politely by choosing ", ('elena', 'вы'), ' since they barely know each other yet.']),
    (4, None, ["'Women often cut meat completely incorrectly.' Adding a negative part directly to ", ('barinov', 'неправильно'), ' creates a single word that means completely wrong.']),
    (5, None, ["'You simply do not respect female talent.' Her formal tone is maintained with ", ('elena', 'уважаете'), ' to point out his lack of respect for female talent.']),
    (6, None, ["'A woman is not capable of becoming a great chef.' To claim a woman lacks ability, ", ('barinov', 'способна'), ' ends with a sound that directly links back to a female person.']),
    (7, None, ["'I run the kitchen of the famous Arcobaleno restaurant!' Built from the ideas of leading, ", ('elena', 'руковожу'), ' means she is fully in charge of running her famous kitchen.']),
    (8, None, ["'A real head chef requires strong willpower.' A real head chef simply demands, ", ('barinov', 'требует'), ', that one has strong willpower to survive the pressure.']),
    (9, None, ["'I have experience and strong willpower.' Instead of backing down she claims ", ('elena', 'опыт'), ' to highlight her rich background and personal strength.']),
    (10, None, ["'For you the kitchen remains an ordinary job.' Even while insulting her life choices, ", ('barinov', 'остаётся'), ' implies that cooking simply stays an ordinary job for her.']),
    (11, None, ["'The kitchen is my whole life, Viktor!' Defending her true passion and calling, ", ('elena', 'жизнь'), ' means that the kitchen represents her entire existence.']),
    (12, None, ["'We will soon check your bold words.' Promising a single test very soon, ", ('barinov', 'проверим'), ' means they will soon find out if her bold claims hold up.']),
]
