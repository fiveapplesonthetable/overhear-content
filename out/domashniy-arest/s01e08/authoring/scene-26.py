# Authoring module for domashniy-arest-s01e08-scene-26.
ID = 'domashniy-arest-s01e08-scene-26'
SHOW = 'domashniy-arest'
SEASON = 1
EPISODE = 8
SCENE = 26
TITLE = 'Лишний билет  (Concert Ticket)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'nina': 'Нина', 'samson': 'Самсон'}
SOURCE_NAME = 'Домашний арест, Сезон 1, Эпизод 8'
SOURCE_FILE = 'sources/domashniy-arest/s01/e08.ru.dual.srt'
INTRO = "Previously, Arkady playfully wrestled with Lyosha in the communal apartment and ended up hurting his back. Meanwhile, at Ivan Samsonov's flat, Ivan tries to make peace with Nina by offering her an extra concert ticket."
OPENER = "Let's see how Nina responds to Ivan's awkward peace offering."
TRANSITION = 'Now listen to the marital spat over the concert ticket once more.'
OUTRO = "Nina rebuffs Ivan's peace offering, leaving him with an unwanted ticket and a looming political crisis. See you next time!"
CLOSING = ('samson', 'Пока!')
STORY = [
    ('samson', 'Нина, у меня есть второй билет.', 'Nina, I have a second ticket.', [(449, 'Нина, у меня еще один'), (450, 'билет есть')], 'adapted cues 449-450'),
    ('samson', 'Завтра вечером в городе концерт.', 'Tomorrow evening there is a concert in town.', [], 'transitional dialogue line'),
    ('nina', 'И что ты предлагаешь?', 'And what are you suggesting?', [], 'skeptical question'),
    ('samson', 'Если ты хочешь, пойдём вместе.', "If you want, let's go together.", [(452, 'если ты хочешь')], 'added пойдём вместе'),
    ('nina', 'Вот это настоящий мужчина!', 'Now that is a real man!', [(453, 'Вот это мужчина')], 'added настоящий'),
    ('nina', 'Какой ты деликатный и добрый!', 'How tactful and kind you are!', [(454, 'Деликатный'), (455, 'обходительный')], 'adapted cues 454-455'),
    ('samson', 'Значит, ты согласна пойти?', 'Does that mean you agree to go?', [(451, 'Так что')], 'expanded into question'),
    ('nina', 'Нет, конечно! Я не пойду.', "No, of course not! I won't go.", [], 'sharp refusal'),
    ('nina', 'Лучше сходи с Клавдией Викторовной.', 'Better go with Klavdia Viktorovna.', [(456, 'Ну, с Клавдией Викторовной сходи')], 'adapted cue 456'),
    ('samson', 'Она же меня совсем не любит.', 'She does not like me at all, after all.', [(449, 'меня')], 'echoed cue 422'),
    ('nina', 'А я люблю тебя ещё меньше!', 'And I love you even less!', [], 'sarcastic response'),
    ('samson', 'Спасибо за честный ответ, Нина.', 'Thank you for the honest answer, Nina.', [(449, 'нина')], 'adapted cue 419'),
]
WALK = [
    (0, None, "'Nina, I have a second ticket.' Ivan awkwardly attempts to make peace with an offering."),
    (1, None, "'Tomorrow evening there is a concert in town.' The adverbial phrase sets the time and venue."),
    (2, None, "'And what are you suggesting?' Nina asks skeptically about his real intentions."),
    (3, None, "'If you want, let's go together.' The conditional clause expresses an informal invitation."),
    (4, None, "'Now that is a real man!' Nina responds with heavy dripping sarcasm."),
    (5, None, "'How tactful and kind you are!' The exclamatory adjectives mock Ivan's sudden politeness."),
    (6, None, "'Does that mean you agree to go?' Ivan gullibly misreads her sarcastic remarks as genuine."),
    (7, None, "'No, of course not! I won't go.' Nina quickly dashes his hopes with a blunt refusal."),
    (8, None, "'Better go with Klavdia Viktorovna.' Nina sarcastically suggests the elderly neighbor instead."),
    (9, None, "'She does not like me at all, after all.' Ivan points out the bad blood between them."),
    (10, None, "'And I love you even less!' Nina emphasizes her bitter exasperation with him."),
    (11, None, "'Thank you for the honest answer, Nina.' Ivan accepts the rejection with grim resignation."),
]
