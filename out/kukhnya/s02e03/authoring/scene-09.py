# Authoring module for kukhnya-s02e03-scene-09.
ID = 'kukhnya-s02e03-scene-09'
SHOW = 'kukhnya'
SEASON = 2
EPISODE = 3
SCENE = 9
TITLE = 'Девушка в зеленом  (The Girl in Green)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'ilya': 'Илья', 'nastya': 'Настя'}
SOURCE_NAME = 'Кухня (Kukhnya) S2.03'
SOURCE_FILE = 'sources/kukhnya/s02/e03.ru.dual.srt'
INTRO = "Ilya is looking for someone in the restaurant. He asks Nastya if she has seen a specific girl, but Nastya is confused by his question. Let's listen closely to their exchange in Russian first, and then walk through each line together."
OPENER = "Let's review the conversation line by line."
TRANSITION = "Now let's listen to the conversation again without interruption."
OUTRO = "And that's it for this scene. When you watch the episode, listen out for the exchange around the girl in green, and for the words meaning 'was' and 'girlfriend'. You'll catch them now. See you next time."
CLOSING = ('ilya', 'До встречи!')
STORY = [
    ('ilya', 'Привет.', 'Hi.', [], ''),
    ('nastya', 'Привет, Илья.', 'Hi, Ilya.', [], ''),
    ('ilya', 'Здесь была девушка в зеленом платье?', 'Was there a girl in a green dress here?', [(153, 'А разве здесь была девушка в зеленом платье')], ''),
    ('nastya', 'Вообще да.', 'Yes, actually.', [(154, 'Вообще да')], ''),
    ('ilya', 'Где она?', 'Where is she?', [], ''),
    ('nastya', 'Я не знаю.', "I don't know.", [], ''),
    ('ilya', 'Ты ее не видела?', "You didn't see her?", [], ''),
    ('nastya', 'Странно, я не видела.', "That's strange, I didn't see.", [(155, 'Странно, я не видела')], ''),
    ('ilya', 'Может, она ушла?', 'Maybe she left?', [], ''),
    ('nastya', 'Может быть.', 'Maybe.', [], ''),
    ('ilya', 'Мне нужно ее найти.', 'I need to find her.', [], ''),
    ('nastya', 'Посмотри в баре.', 'Look in the bar.', [], ''),
]
WALK = [
    (0, None, "'Hi.' Walking up to the host stand, Ilya greets Nastya. Nastya answers straight away."),
    (1, None, "'Hi, Ilya.' Nastya smiles and says hello back to him."),
    (2, None, "'Was there a girl in a green dress here?' Ilya asks if she noticed a girl in a green dress in the dining room earlier."),
    (3, None, "'Yes, actually.' Nastya thinks for a second and says yes, she actually did see her. Then Ilya replies."),
    (4, None, "'Where is she?' Ilya eagerly asks where that girl went."),
    (5, None, "'I don't know.' Nastya shrugs and says she does not know."),
    (6, None, "'You didn't see her?' Ilya asks if Nastya saw her walk out. And Nastya jumps in."),
    (7, None, "'That's strange, I didn't see.' Nastya admits it is strange, because she never saw the girl leave."),
    (8, None, "'Maybe she left?' Ilya wonders aloud if she slipped out while nobody was looking."),
    (9, None, "'Maybe.' Nastya agrees that she might have left. Ilya answers straight away."),
    (10, None, "'I need to find her.' Ilya says he really needs to track her down."),
    (11, None, "'Look in the bar.' Nastya suggests he check over by the bar. Let's hear it again."),
]
