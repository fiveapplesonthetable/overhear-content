# domashniy-arest/s01e01/scene-14.py
ID = "domashniy-arest-s01e01-scene-14"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 1
SCENE = 14
TITLE = "Стоять!  (Freeze!)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.01"
SOURCE_FILE = "sources/domashniy-arest/s01/e01.ru.dual.srt"
VOICES = {"narrator": "sky", "anya": "alisa", "arakelyan": "anja", "captain": "angelina"}
LABELS = {"anya": "Аркадий", "arakelyan": "Аракелян", "captain": "Капитан"}
INTRO = "Back with Arkady now, who arrives at the Santa Fe café. While Marina was standing up to her dean, the mayor was on his way here to meet Arakelyan, the businessman who phoned to say the money for the shopping centre was ready. We'll hear it in Russian first; don't worry about catching every word."
STORY = [
    ("anya", "Ну, ты где?", "So, where are you?", [(560, 'Ну, ты где')], "'есть-то' dropped"),
    ("arakelyan", "Я здесь.", "I'm here.", [(561, 'Я здесь')], ""),
    ("anya", "Почему ты сидишь в углу?", "Why are you sitting in the corner?", [], "new: a plain version of cue 562 ('Ты че сюда засел, ара?', why have you holed up here)"),
    ("arakelyan", "Конспирация.", "Secrecy.", [(563, 'Конспирация')], ""),
    ("arakelyan", "Здравствуйте, Аркадий Борисович.", "Hello, Arkady Borisovich.", [(564, 'Аркадий Борисович')], "'Здравствуйте' added (he says 'Здрасте' in cue 559)"),
    ("anya", "А что грустный такой?", "So why so gloomy?", [(565, 'грустный такой')], "'Слышь, конспиратор, а чё' -> 'А что'"),
    ("arakelyan", "Многовато. Кризис же.", "It's a bit much. There's a crisis, you know.", [(566, 'Многовато. Кризис же')], ""),
    ("anya", "Ты эти деньги через полгода вернёшь.", "You'll get this money back in six months.", [(568, 'Ты эти'), (568, 'через полгода')], "slang 'бабки' -> 'деньги', 'отобьешь' -> 'вернёшь'"),
    ("arakelyan", "Тише, пожалуйста.", "Quiet, please.", [], "new: shows his nerves, which Arkady laughs at in cue 569"),
    ("anya", "Ты что, шпион?", "What are you, a spy?", [], "new: a short version of cue 569 (have you watched too many spy films?)"),
    ("anya", "Это наш город. Нам здесь бояться некого.", "This is our town. We have nobody to fear here.", [(570, 'Это наш город'), (571, 'Нам здесь бояться некого')], "'Ара' (a nickname) dropped"),
    ("captain", "Стоять!", "Freeze!", [(572, 'Стоять')], ""),
    ("captain", "Капитан Гнездо, следственный комитет.", "Captain Gnezdo, Investigative Committee.", [(573, 'Капитан Гнездо, следственный комитет')], ""),
    ("captain", "Гражданин Аникеев, вы арестованы.", "Citizen Anikeev, you are under arrest.", [(574, 'Гражданин Аникеев, вы арестованы')], ""),
    ("anya", "Что? За что?", "What? What for?", [], "new: Arkady's reaction is not in the subtitles"),
    ("captain", "За взятку. За очень большую взятку.", "For a bribe. For a very large bribe.", [], "new: simplifies cues 574-575 ('по подозрению в получении взятки в особо крупных размерах')"),
]
OPENER = "Let's go through it slowly. The café is dim, and at first Arkady can't even see the man he's come to meet."
WALK = [
    (0, None, "'So, where are you?' Arkady uses the informal singular 'you' here with 'where', as friends and close colleagues do."),
    (1, None, "'I'm here.' One of the first things you learn: 'I', and 'here'. No verb at all. Arkady is puzzled."),
    (2, None, "'Why are you sitting in the corner?' The last word, 'in the corner', has a special ending: a few masculine words end in a stressed 'oo' sound after 'in'. Arakelyan's answer is one mysterious word."),
    (3, None, "'Secrecy.' A rather grand word for keeping things hidden, the way spies do. Then he greets the mayor properly."),
    (4, None, "'Hello, Arkady Borisovich.' The polite 'hello' and the first name with the father's name. Arkady sees he looks unhappy."),
    (5, None, "'So why so gloomy?' In everyday speech the word 'what' can mean 'why'. And the adjective is masculine, to match Arakelyan. He's handing over a bag of money, and he doesn't like it."),
    (6, None, "'It's a bit much. There's a crisis, you know.' The first word is 'a lot', softened with an ending that means 'a bit'. The small word at the end means 'after all' or 'you know'. Arkady is not sympathetic."),
    (7, None, "'You'll get this money back in six months.' The word for money is always plural in Russian, so 'this' is plural too. And the verb is in the future: 'you will return'. Arakelyan glances around nervously."),
    (8, None, "'Quiet, please.' The first word is 'quieter', which is how Russians say 'shh'. Arkady just laughs at him."),
    (9, None, "'What are you, a spy?' A teasing question. Then he says the line that will come back to haunt him."),
    (10, 'Это наш город.', "'This is our town.' Again, no word for 'is'. The word for 'our' matches the town, which is masculine."),
    (10, 'Нам здесь бояться некого.', "'We have nobody to fear here.' Literally, 'to us here to fear nobody'. The last word means 'there is nobody', and it goes with a verb in its dictionary form. A second later, someone shouts."),
    (11, None, "'Freeze!' It's the verb 'to stand' in its dictionary form, used as a sharp order. You'll hear it from police in every Russian film."),
    (12, None, "'Captain Gnezdo, Investigative Committee.' That's the agency that investigates serious crimes. His surname means 'nest'. He is here to arrest the mayor."),
    (13, None, "'Citizen Anikeev, you are under arrest.' The officer says 'citizen', the official way to address someone, and the polite 'you'. Arkady can hardly believe it."),
    (14, None, "'What? What for?' The second question literally means 'for what?'. The captain tells him."),
    (15, None, "'For a bribe. For a very large bribe.' The same little word, 'for', again, and the bribe takes the ending of the object. So the meeting was a trap, and only a minute after he said he had nobody to fear."),
]
TRANSITION = "Let's hear it all again, start to finish."
OUTRO = "So the mayor's busy day ends with his arrest. You don't need every word; if you remember the shout of 'freeze' and the line about having nobody to fear, you've got the heart of it. See you next time!"
CLOSING = ("captain", "Пока!")
