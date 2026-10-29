# Authoring module for kukhnya-s01e11-scene-05.
ID = 'kukhnya-s01e11-scene-05'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 11
SCENE = 5
TITLE = 'В поисках критика  (In Search of the Critic)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'kostya': 'Костя', 'max': 'Макс'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.11'
SOURCE_FILE = 'sources/kukhnya/s01/e11.ru.dual.srt'
INTRO = 'The critic could be anyone in the room. Kostya and Max stand at the bar and size up the guests, one table at a time. Have a listen first.'
OPENER = "Let's slow it down."
TRANSITION = "Now let's hear it once more, start to finish."
OUTRO = 'They have a suspect, and she is sitting at table seven. Whether she is the critic or not, the staff will treat her like a queen. Enjoy the rest of the episode.'
CLOSING = ('kostya', 'Пока!')
STORY = [
    ('kostya', 'Макс, смотри внимательно на зал!', 'Max, look carefully at the dining room!', [], ''),
    ('max', 'Кто же из них может быть критиком?', 'Which one of them could be the critic?', [(66, 'Кто же из них может быть критиком?')], ''),
    ('kostya', 'Эти двое работают в соседнем банке.', 'Those two work at the bank next door.', [(67, 'работают в соседнем банке.')], ''),
    ('max', 'Да, они наши постоянные гости.', 'Yes, they are our regular guests.', [(67, 'Эти двое постоянные гости')], ''),
    ('kostya', 'А тот мужчина у окна?', 'And that man by the window?', [], ''),
    ('max', 'Он заказал рыбу и красное вино.', 'He ordered fish and red wine.', [(68, 'Рыба и красное вино.')], ''),
    ('kostya', 'Нет, настоящий критик такого не закажет.', 'No, a real critic will not order that.', [(69, 'Нет.')], ''),
    ('max', 'А парень за столиком номер три?', 'What about the guy at table number three?', [], ''),
    ('kostya', 'Он слишком молод для ресторанного критика.', 'He is too young for a restaurant critic.', [(70, 'Слишком молод')], ''),
    ('max', 'Критики обычно сидят в одиночестве.', 'Critics usually sit in solitude.', [], ''),
    ('kostya', 'И записывают всё в блокнот.', 'And write down everything in a notepad.', [], ''),
    ('max', 'Смотри, женщина за седьмым столиком!', 'Look, the woman at table seven!', [], ''),
    ('kostya', 'Она очень строго смотрит на меню.', 'She is looking very strictly at the menu.', [], ''),
    ('max', 'Кажется, мы нашли нашего критика!', 'It seems we found our critic!', [], ''),
]
WALK = [
    (0, None, '\'Max, look carefully at the dining room!\' "Smotri" is a command to one friend, the ty form of "smotret", "to look". Then "na zal" points that look at the room, with "na" for "at". Kostya speaks in a conspirator\'s voice.'),
    (1, None, '\'Which one of them could be the critic?\' It\'s "kto zhe iz nikh", "who then of them", and "mozhet byt" is "can be". After "byt", "kritik" becomes "kritikom".'),
    (2, None, '\'Those two work at the bank next door.\' Two people here are not "dva" but "dvoe", the word Russians use for a pair of people. After "v" the bank takes an -e ending, and "sosednem", "neighbouring", is built on "sosed", "neighbour".'),
    (3, None, '\'Yes, they are our regular guests.\' Russians call regulars "postoyannye gosti", "constant guests". Max agrees with Kostya\'s logic: regulars cannot be mystery visitors.'),
    (4, None, '\'And that man by the window?\' "U okna" is "at the window": after "u", "okno" becomes "okna". "Muzhchina", "man", is close to "muzh", "husband". Kostya moves on to the next suspect.'),
    (5, None, '\'He ordered fish and red wine.\' Listen to the fish: "ryba" turns into "rybu" because it\'s the thing he ordered. And "krasnoe" ends in -oe to match "vino", a neuter word. Max reads the table like a detective.'),
    (6, None, '\'No, a real critic will not order that.\' "Takogo ne zakazhet" is "of such not will order", with "takoe" changed after "ne". "Zakazhet" is "will order". Kostya is sure of his rules for critics.'),
    (7, None, '\'What about the guy at table number three?\' "A" at the front means "and what about". "Za stolikom" is "at the little table": "stolik" is a small "stol", the usual word for a restaurant table.'),
    (8, None, '\'He is too young for a restaurant critic.\' "Molod" is a short form of "molodoy", "young", used to describe someone in the moment. "Dlya restorannogo kritika" is "for a restaurant critic", with endings after "dlya".'),
    (9, None, '\'Critics usually sit in solitude.\' It sounds grand, but "v odinochestve" is just the usual way to say someone sits alone, and it\'s built on "odin", "one". "Obychno", "usually", comes first, as a general rule.'),
    (10, None, '\'And write down everything in a notepad.\' "Zapisyvayut" is "write down": za- on "pisat", "to write". "Bloknot", "notepad", was borrowed from French. "V bloknot" is "into the notepad".'),
    (11, None, '\'Look, the woman at table seven!\' The table is "za sedmym stolikom", "at the seventh little table", a counting word. "Zhenshchina" is "woman". The suspect is a lady alone, so she fits.'),
    (12, None, '\'She is looking very strictly at the menu.\' "Strogo", "strictly", is "strogy" with -o. "Menyu" never changes in Russian. Kostya is drawing a conclusion from a frown, which is hardly proof.'),
    (13, None, '\'It seems we found our critic!\' "Kazhetsya", "it seems", is a single word. "Nashli", "found", ends in -li for "we". "Nashego kritika" is "our critic" as the one found.'),
]
