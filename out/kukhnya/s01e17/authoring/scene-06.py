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
INTRO = "After work, Max has brought his new girlfriend, Vika, to a bar to meet his friends Kostya and Nastya. It is a little awkward, since Vika is also their boss. We'll hear it in Russian first."
OPENER = "Let's take it apart a line at a time."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = "The evening is sinking fast. The toast 'za vstrechu', literally 'to the meeting', is the easiest Russian toast you can learn. See you next time!"
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
    (0, None, "'Meet Vika.' Russian says 'get acquainted', with the 'sya' ending meaning 'with each other'. The little word for 'this is' introduces her."),
    (1, None, "'Actually, we know each other.' The first word has a small 'to' tacked on, which sharpens the correction. 'Acquainted' is plural, as she means both of them."),
    (2, None, "'This is just Vika, my girlfriend.' The word for 'girl' also serves for 'girlfriend'. 'My' ends in 'ya' to match the feminine word."),
    (3, None, "'And this is Nastya, my friend.' A female friend and a male friend have different words, so this one ends in 'a'. The opening 'and' just switches to the next person."),
    (4, None, "'Let's drink to the meeting.' The small word for 'to' in a toast is the same one that means 'for'. 'Meeting' takes a 'u' ending after it."),
    (5, None, "'Why didn't you tell me she would be here?' The 'a' stays off, and 'told' ends in a bare 'l' for Max. 'Will be' is a short word that comes just after 'she'."),
    (6, None, "'We spend a lot of time together.' After 'a lot', 'time' takes a different ending. 'Spend' is built from 'to lead through'."),
    (7, None, "'We should probably be going.' 'Probably' is one word, and 'we will go' is the soft way to say 'we're off'. It's a polite excuse."),
    (8, None, "'It's time for us to go home.' 'To us' stands for 'we', and the word for 'time' means 'it's time'. 'Home' is a single word of direction."),
    (9, None, "'You stay, and we're leaving.' The command is the plural polite one. The small 'a' in the middle sets the two groups against each other."),
    (10, None, "'Kostya, let's go.' The past form of 'go' is used as a casual 'let's go'. It's short, brisk and rude."),
    (11, None, "'Kostya, hey, where are you going?' The first word is a filler like 'come on'. There's no verb at all, just 'where to', and that's enough."),
]
