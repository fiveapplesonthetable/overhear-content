# Authoring module for kukhnya-s01e17-scene-06.
ID = 'kukhnya-s01e17-scene-06'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 17
SCENE = 6
TITLE = 'Двойное свидание  (Double date)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'max': 'Макс', 'nastya': 'Настя', 'vika': 'Вика'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.17'
SOURCE_FILE = 'sources/kukhnya/s01/e17.ru.dual.srt'
INTRO = 'Max brings Vika on a double date to a bar to hang out with Nastya and Kostya. However, the two women immediately clash, and the entire evening quickly ends in complete disaster.'
OPENER = "Now let's go back through the exchange around Double date line by line and unpack how the Russian works."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = "The date ends in a disaster when Nastya gets angry and drags Kostya out of the bar. Next time you watch the episode, listen for the Russian expressions for 'to get acquainted' and 'actually' — you will catch every word right away. See you next time!"
CLOSING = ('vika', 'До свидания.')
STORY = [
    ('max', 'Познакомьтесь, это Вика.', 'Meet Vika.', [(78, 'А, познакомьтесь, это Вика.')], ''),
    ('nastya', 'Вообще-то мы знакомы.', 'Actually, we know each other.', [(79, 'Вообще-то мы знакомы с Викторией Сергеевной.')], ''),
    ('max', 'Это просто Вика, моя девушка.', 'She is just Vika, my girlfriend.', [(80, 'Не-не-не, стоп. Это просто Вика, моя девушка.')], ''),
    ('max', 'А это Настя, моя подруга.', 'And this is Nastya, my friend.', [(81, 'Вика. А это просто Настя и просто Костя, мои друзья.')], ''),
    ('nastya', 'Давайте за встречу.', "Let's drink to seeing each other.", [], ''),
    ('vika', 'Почему не сказал, что она будет?', "Why didn't you tell me she'd be here?", [(82, 'Ты')], ''),
    ('max', 'Мы много времени вместе проводим.', 'We spend a lot of time together.', [], ''),
    ('vika', 'Мы, наверное, пойдем.', 'We should probably get going.', [(76, 'пойдем')], ''),
    ('vika', 'Нам домой уже пора.', 'We should head home.', [], ''),
    ('nastya', 'Вы оставайтесь, а мы уходим.', 'You stay; we are leaving.', [], ''),
    ('nastya', 'Костя, пошли.', "Kostya, let's go.", [(81, 'костя')], ''),
    ('max', 'Костя, ну ты куда?', 'Kostya, where are you going?', [(81, 'костя')], ''),
]
WALK = [
    (0, None, "'Meet Vika.' Max introduces his girlfriend to his best friends at the bar."),
    (1, None, "'Actually, we know each other.' Nastya awkwardly points out that they already know each other."),
    (2, None, "'She is just Vika, my girlfriend.' Max tries to defuse the tension by introducing her simply as his girlfriend."),
    (3, None, "'And this is Nastya, my friend.' Max finishes the introduction by presenting his friend."),
    (4, None, "'Let's drink to seeing each other.' Nastya suggests they raise a glass to the meeting."),
    (5, None, "'Why didn't you tell me she'd be here?' Vika angrily demands to know why her boyfriend hid the guest list."),
    (6, None, "'We spend a lot of time together.' Max defends his choice by pointing out they spend a lot of time together."),
    (7, None, "'We should probably get going.' Vika abruptly decides it is time for them to leave the bar."),
    (8, None, "'We should head home.' Vika uses the late hour as an excuse to head home."),
    (9, None, "'You stay; we are leaving.' Nastya flips the script, telling the couple to stay while she and Kostya leave."),
    (10, None, "'Kostya, let's go.' Nastya commands her boyfriend to follow her out the door."),
    (11, None, "'Kostya, where are you going?' Max reacts with confusion as his friend walks away."),
]
