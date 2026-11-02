# Authoring module for domashniy-arest-s01e01-scene-14.
ID = 'domashniy-arest-s01e01-scene-14'
SHOW = 'domashniy-arest'
SEASON = 1
EPISODE = 1
SCENE = 14
TITLE = 'Стоять!  (Freeze!)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'arakelyan': 'Аракелян', 'arkady': 'Аркадий', 'captain': 'Капитан'}
SOURCE_NAME = 'Домашний арест (Domashniy Arest) S1.01'
SOURCE_FILE = 'sources/domashniy-arest/s01/e01.ru.dual.srt'
INTRO = "Back with Arkady now, who arrives at the Santa Fe café. While Marina was standing up to her dean, the mayor was on his way here to meet Arakelyan, the businessman who phoned to say the money for the shopping centre was ready. We'll hear it in Russian first; don't worry about catching every word."
OPENER = "Let's go through it slowly. The café is dim, and at first Arkady can't even see the man he's come to meet."
TRANSITION = "Let's hear it all again, start to finish."
OUTRO = "So the mayor's busy day ends with his arrest. You don't need every word; if you remember the shout of 'freeze' and the line about having nobody to fear, you've got the heart of it. See you next time!"
CLOSING = ('captain', 'Пока!')
STORY = [
    ('arkady', 'Ну, ты где?', 'So, where are you?', [(560, 'Ну, ты где')], "'есть-то' dropped"),
    ('arakelyan', 'Я здесь.', "I'm here.", [(561, 'Я здесь')], ''),
    ('arkady', 'Почему ты сидишь в углу?', 'Why are you sitting in the corner?', [], "new: a plain version of cue 562 ('Ты че сюда засел, ара?', why have you holed up here)"),
    ('arakelyan', 'Конспирация.', 'Secrecy.', [(563, 'Конспирация')], ''),
    ('arakelyan', 'Здравствуйте, Аркадий Борисович.', 'Hello, Arkady Borisovich.', [(564, 'Аркадий Борисович')], "'Здравствуйте' added (he says 'Здрасте' in cue 559)"),
    ('arkady', 'А что грустный такой?', 'So why so gloomy?', [(565, 'грустный такой')], "'Слышь, конспиратор, а чё' -> 'А что'"),
    ('arakelyan', 'Многовато. Кризис же.', "It's a bit much. There's a crisis, you know.", [(566, 'Многовато. Кризис же')], ''),
    ('arkady', 'Ты эти деньги через полгода вернёшь.', "You'll get this money back in six months.", [(568, 'Ты эти'), (568, 'через полгода')], "slang 'бабки' -> 'деньги', 'отобьешь' -> 'вернёшь'"),
    ('arakelyan', 'Тише, пожалуйста.', 'Quiet, please.', [], 'new: shows his nerves, which Arkady laughs at in cue 569'),
    ('arkady', 'Ты что, шпион?', 'What are you, a spy?', [], 'new: a short version of cue 569 (have you watched too many spy films?)'),
    ('arkady', 'Это наш город. Нам здесь бояться некого.', 'This is our town. We have nobody to fear here.', [(570, 'Это наш город'), (571, 'Нам здесь бояться некого')], "'Ара' (a nickname) dropped"),
    ('captain', 'Стоять!', 'Freeze!', [(572, 'Стоять')], ''),
    ('captain', 'Капитан Гнездо, следственный комитет.', 'Captain Gnezdo, Investigative Committee.', [(573, 'Капитан Гнездо, следственный комитет')], ''),
    ('captain', 'Гражданин Аникеев, вы арестованы.', 'Citizen Anikeev, you are under arrest.', [(574, 'Гражданин Аникеев, вы арестованы')], ''),
    ('arkady', 'Что? За что?', 'What? What for?', [], "new: Arkady's reaction is not in the subtitles"),
    ('captain', 'За взятку. За очень большую взятку.', 'For a bribe. For a very large bribe.', [], "new: simplifies cues 574-575 ('по подозрению в получении взятки в особо крупных размерах')"),
]
WALK = [
    (0, None, ["'So, where are you?' Arkady uses the informal word for 'you', ", ('arkady', 'ты'), ", here with which translates to 'where', ", ('arkady', 'где'), ", as friends and close colleagues do."]),
    (1, None, ["'I'm here.' One of the first things you learn is the translation for 'I', ", ('arakelyan', 'Я'), ", and the term for 'here', ", ('arakelyan', 'здесь'), ". No 'is' at all. Arkady is puzzled."]),
    (2, None, ["'Why are you sitting in the corner?' the translation for 'in the corner', ", ('arkady', 'в углу'), ", has a special ending: a few masculine words end in a stressed 'oo' sound after 'in'. Arakelyan's answer is one mysterious word."]),
    (3, None, ["'Secrecy.' meaning 'secrecy', ", ('arakelyan', 'Конспирация'), ", is a rather grand term for keeping things hidden, the way spies do. Then he greets the mayor properly."]),
    (4, None, ["'Hello, Arkady Borisovich.' He uses the polite word for 'hello', ", ('arakelyan', 'Здравствуйте'), ", and the first name with the father's name. Arkady sees he looks unhappy."]),
    (5, None, ["'So why so gloomy?' In everyday speech the translation for 'what', ", ('arkady', 'что'), ", literally translates to 'why'. And the describing word, ", ('arkady', 'грустный'), ", takes a matching ending to fit Arakelyan. He's handing over a bag of money, and he doesn't like it."]),
    (6, None, ["'It's a bit much. There's a crisis, you know.' which translates to 'a bit much', ", ('arakelyan', 'Многовато'), ", is built from 'a lot', softened with an ending that means 'a bit'. The small word at the end, ", ('arakelyan', 'же'), ", translates to 'after all' or 'you know'. Arkady is not sympathetic."]),
    (7, None, ["'You'll get this money back in six months.' the term meaning 'money', ", ('arkady', 'деньги'), ", is always plural in Russian, so 'this' matches it. And the action word, ", ('arkady', 'вернёшь'), ", is in the future: 'you will return'. Arakelyan glances around nervously."]),
    (8, None, ["'Quiet, please.' It begins with which translates to 'quieter', ", ('arakelyan', 'Тише'), ", which translates to 'shh' in Russian. Arkady just laughs at him."]),
    (9, None, ["'What are you, a spy?' which translates to 'spy' is ", ('arkady', 'шпион'), ". A teasing question. Then he says the line that will come back to haunt him."]),
    (10, 'Это наш город.', ["'This is our town.' Again, no equivalent for 'is'. the term for 'our', ", ('arkady', 'наш'), ", matches the town, which is a masculine word."]),
    (10, 'Нам здесь бояться некого.', ["'We have nobody to fear here.' Literally, 'to us here to fear nobody'. The last word, ", ('arkady', 'некого'), ", translates to 'there is nobody to', and it goes with the action word, ", ('arkady', 'бояться'), ", in its basic form. A second later, someone shouts."]),
    (11, None, ["'Freeze!' It's the Russian for 'to stand', ", ('captain', 'Стоять'), ", an action word in its basic form, used as a sharp order. You'll hear it from police in every Russian film."]),
    (12, None, ["'Captain Gnezdo, Investigative Committee.' That's the agency that investigates serious crimes. His surname, ", ('captain', 'Гнездо'), ", literally translates to 'nest'. He is here to arrest the mayor."]),
    (13, None, ["'Citizen Anikeev, you are under arrest.' The officer uses meaning 'citizen', ", ('captain', 'Гражданин'), ", which is the official way to address someone, and the polite word for 'you', ", ('captain', 'вы'), ". Arkady can hardly believe it."]),
    (14, None, ["'What? What for?' The second question, ", ('arkady', 'За что'), ", literally translates to 'for what?'. The captain tells him."]),
    (15, None, ["'For a bribe. For a very large bribe.' The little word for 'for', ", ('captain', 'За'), ", appears again, and which translates to 'bribe', ", ('captain', 'взятку'), ", takes the ending of a target. So the meeting was a trap, and only a minute after he said he had nobody to fear."]),
]
