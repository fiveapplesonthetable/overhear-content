# Authoring module for kukhnya-s01e02-scene-18.
ID = 'kukhnya-s01e02-scene-18'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 2
SCENE = 18
TITLE = 'Матч на кухне  (Match in the Kitchen)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'senya': 'Сеня'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.02'
SOURCE_FILE = 'sources/kukhnya/s01/e02.ru.dual.srt'
INTRO = "In his kitchen office, Chef Viktor is glued to the television watching the Moscow football derby between Spartak and CSKA. Line cook Senya asks about dinner service, but the chef is completely absorbed in the tense play near the goal. Let's listen to their exchange in Russian first."
OPENER = "Let's examine the dialogue line by line. Notice the exciting sports vocabulary and the chef's intense football passion."
TRANSITION = "Now let's listen to the conversation again without interruption."
OUTRO = "Chef Barinov's love of football brings lively energy to Claude Monet between stressful dinner orders. See you next time!"
CLOSING = ('barinov', 'Пока!')
STORY = [
    ('senya', 'Шеф, пора начинать готовить горячие блюда?', 'Chef, is it time to start preparing hot dishes?', [], ''),
    ('barinov', 'Тихо, Сеня! Сейчас идёт решающий матч!', 'Quiet, Senya! A decisive match is on right now!', [], ''),
    ('senya', 'Кто сегодня играет на этом матче?', 'Who is playing in this match today?', [], ''),
    ('barinov', 'Наш великий Спартак играет против ЦСКА!', 'Our great Spartak is playing against CSKA!', [], ''),
    ('senya', 'И какой сейчас счёт в игре?', 'And what is the score in the game now?', [], ''),
    ('barinov', 'Пока ничья, но мы должны победить!', 'A draw so far, but we must win!', [], ''),
    ('senya', 'Смотрите, мяч летит к их воротам!', 'Look, the ball is flying toward their goal!', [], ''),
    ('barinov', 'У чужой штрафной площади ЦСКА держит оборону.', 'Near the opponent penalty area CSKA is holding defense.', [(209, 'держит оборону')], ''),
    ('senya', 'Нападающий Спартака получает быстрый пас.', 'The Spartak forward receives a fast pass.', [], ''),
    ('barinov', 'Давай, Ари с мячом сильно бьёт!', 'Come on, Ari with the ball shoots hard!', [(210, 'бьет')], ''),
    ('senya', 'Вратарь с трудом ловит этот мяч.', 'The goalkeeper catches this ball with difficulty.', [], ''),
    ('barinov', 'Какой опасный и красивый был момент!', 'What a dangerous and beautiful moment it was!', [], ''),
    ('senya', 'А теперь пора вернуться к нашей кухне.', 'And now it is time to return to our kitchen.', [], ''),
]
WALK = [
    (0, None, "'Chef, is it time to start preparing hot dishes?' Senya tentatively checks if the kitchen staff should fire up the stoves for the evening rush."),
    (1, None, "'Quiet, Senya! A decisive match is on right now!' Barinov aggressively shushes his cook, refusing to pull his eyes away from the crucial sporting event."),
    (2, None, "'Who is playing in this match today?' Senya tries to engage his boss by asking which teams are currently battling it out on the screen."),
    (3, None, "'Our great Spartak is playing against CSKA!' Barinov passionately declares his allegiance to Spartak as they face off against their fierce rivals."),
    (4, None, "'And what is the score in the game now?' Senya inquires about the current standings to understand why the chef is so tense."),
    (5, None, "'A draw so far, but we must win!' Barinov nervously reports the tied score while expressing his desperate hope for a victory."),
    (6, None, "'Look, the ball is flying toward their goal!' Senya gets caught up in the excitement, pointing out a sudden offensive play on the field."),
    (7, None, "'Near the opponent penalty area CSKA is holding defense.' Barinov intensely narrates the defensive formation of the opposing team near the penalty box."),
    (8, None, "'The Spartak forward receives a fast pass.' Senya describes the fast-paced action as the favored team's striker gains control of the ball."),
    (9, None, "'Come on, Ari with the ball shoots hard!' Barinov screams encouragement at the television as his favorite player takes a powerful shot."),
    (10, None, "'The goalkeeper catches this ball with difficulty.' Senya watches in suspense as the opposing goalie barely manages to block the impressive strike."),
    (11, None, "'What a dangerous and beautiful moment it was!' Barinov exhales in sheer exhilaration at the breathtaking play he just witnessed."),
    (12, None, "'And now it is time to return to our kitchen.' Senya gently reminds his superior that they still have a restaurant to run despite the exciting game."),
]
