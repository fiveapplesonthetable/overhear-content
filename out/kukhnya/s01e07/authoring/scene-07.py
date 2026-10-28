# Authoring module for kukhnya-s01e07-scene-07.
ID = 'kukhnya-s01e07-scene-07'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 7
SCENE = 7
TITLE = 'Спасение карпов  (Saving the Carp)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'kostya': 'Костя', 'nastya': 'Настя'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.07'
SOURCE_FILE = 'sources/kukhnya/s01/e07.ru.dual.srt'
INTRO = 'Back at Claude Monet, Nastya the waitress is upset. She tells Kostya, the bartender, what happened at home: she has been thrown out of her flat, and the reason is a pair of live fish. Listen to her tell it in Russian.'
OPENER = "Let's go through it. Nastya explains, and Kostya keeps asking why."
TRANSITION = "Now Nastya's story again, all the way through."
OUTRO = "Kostya's offer is a kind one: 'you can stay at my place'. It's an easy sentence to say, and it opens a lot of doors. See you next time."
CLOSING = ('nastya', 'Пока!')
STORY = [
    ('kostya', 'Настя, что у тебя сегодня случилось?', 'Nastya, what happened with you today?', [(60, 'Значит, что случилось')], ''),
    ('nastya', 'Моя злая хозяйка выгнала меня.', 'My wicked landlady kicked me out.', [(61, 'Хозяйка поругалась')], ''),
    ('kostya', 'За что она выгнала тебя?', 'What did she kick you out for?', [], ''),
    ('nastya', 'Я принесла домой живых карпов.', 'I brought live carp home.', [(62, 'Это карпы')], ''),
    ('kostya', 'Зачем тебе живая рыба дома?', 'Why do you need live fish at home?', [], ''),
    ('nastya', 'В магазине их могли просто убить!', 'In the store they could simply kill them!', [(63, 'В магазине их купят и убьют')], ''),
    ('kostya', 'И где они плавают сейчас?', 'And where are they swimming now?', [], ''),
    ('nastya', 'Они прекрасно живут в ванне.', 'They live wonderfully in the bathtub.', [(64, 'А у меня они скоро размножаться будут')], ''),
    ('kostya', 'Понятно, хозяйка была очень недовольна.', 'I see, the landlady was very unhappy.', [], ''),
    ('nastya', 'Я не могу жить с жестокими людьми.', 'I cannot live with cruel people.', [(66, 'Я не могу жить в квартире убийцы')], ''),
    ('kostya', 'Слушай, ты можешь пока пожить у меня.', 'Listen, you can stay at my place for now.', [(68, 'ты можешь пока пожить у меня')], ''),
    ('nastya', 'Спасибо, Костик, ты настоящий друг!', 'Thank you, Kostik, you are a true friend!', [(70, 'Спасибо, Костик'), (71, 'Ты настоящий друг')], ''),
]
WALK = [
    (0, None, '\'Nastya, what happened to you today?\' "Chto u tebya sluchilos\'" is literally \'what at you happened\', the usual way to ask what\'s wrong. "Segodnya" is written with a g but said sevodnya.'),
    (1, None, '\'My wicked landlady kicked me out.\' "Khozyayka" is the woman of the house, and for a tenant that means the landlady. "Vygnala" joins vy-, \'out\', to the verb for driving, and the -la shows it was a woman.'),
    (2, None, "'What did she kick you out for?' Za chto, 'for what', asks the reason for a punishment, not just any 'why'."),
    (3, None, '\'I brought live carp home.\' "Domoy" means \'homewards\', a different word from doma, \'at home\'. Carp are living things, so karpy changes to karpov as the thing she brought.'),
    (4, None, '\'Why do you need live fish at home?\' Zachem tebe is literally \'what for to you\', which Russians use for \'why do you need\'. "Ryba", fish, is feminine, so live is zhivaya.'),
    (5, None, '\'In the store they could simply kill them!\' "Mogli", \'could\', has the -li ending used for \'they\'. Nobody in particular is meant by \'they\', which is how Russian talks about people in general.'),
    (6, None, '\'And where are they swimming now?\' "Plavayut", \'they swim\', is from plavat\', which also covers floating. "Seychas" means \'now\' or \'right now\'.'),
    (7, None, '\'They live wonderfully in the bathtub.\' "Zhivut", \'they live\', comes from zhit\', which Max uses for living in Moscow. "Vanna" becomes vanne after v.'),
    (8, None, '\'I see, the landlady was very unhappy.\' "Ponyatno", \'understood\', does the job of \'I see\' in conversation. "Nedovol\'na" is ne plus dovol\'na, \'pleased\', with -a because it\'s the landlady.'),
    (9, None, '\'I cannot live with cruel people.\' "Lyudi", people, has an irregular \'with\' form, lyud\'mi. S zhestokimi lyud\'mi is \'with cruel people\'.'),
    (10, None, '\'Listen, you can stay at my place for now.\' "Pozhit\'" adds po- to zhit\', making it \'live for a while\'. U menya, \'at me\', also means \'at my place\'.'),
    (11, None, '\'Thank you, "Kostik", you are a true friend!\' "Kostik" is an affectionate form of Kostya, with -ik on the end. "Nastoyashchiy" can mean real or true, as in nastoyashchiy drug.'),
]
