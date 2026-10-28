# Authoring module for domashniy-arest-s01e03-scene-21.
ID = 'domashniy-arest-s01e03-scene-21'
SHOW = 'domashniy-arest'
SEASON = 1
EPISODE = 3
SCENE = 21
TITLE = 'Привязанный к стулу  (Tied to a Chair)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'arkady': 'Аркадий', 'nina': 'Нина', 'samson': 'Самсон'}
SOURCE_NAME = 'Домашний арест (Domashniy Arest) S1.03'
SOURCE_FILE = 'sources/domashniy-arest/s01/e03.ru.dual.srt'
INTRO = "Last time, Arkady talked young Slavik into stealing Judge Berg's dog from the park so that Lyolya would come to the school party with him. Moments later, Samson and Nina burst in, tie Arkady to a chair, plug in a soldering iron, and demand to know where he hid the forty million roubles. Let's hear it in Russian first; don't worry about catching every word."
OPENER = "Let's go back through it step by step. Samson grabs Arkady and shoves him onto a chair while Nina brings a rope."
TRANSITION = "Now let's hear the whole scene again from start to finish."
OUTRO = "So Arkady is tied to a chair with a hot soldering iron warming up beside him, and nobody in the communal flat comes to his rescue. Listen for 'money', 'soldering iron', and 'neighbours' when you watch. See you next time!"
CLOSING = ('arkady', 'Пока!')
STORY = [
    ('samson', 'Я тебя предупреждал.', 'I warned you.', [(695, 'Я тебя предупреждал')], ''),
    ('arkady', 'О чём предупреждал? Да ты что делаешь?', 'Warned me about what? Hey, what are you doing?', [(696, 'О чем предупреждал'), (698, 'Да ты что')], "cue 698 'наделал' -> 'делаешь'"),
    ('nina', 'Держи его крепче, Ваня!', 'Hold him tighter, Vanya!', [], 'Nina helps Samson tie Arkady to a chair'),
    ('arkady', 'Самсоновы, вы что творите? Хватит, я прошу вас!', 'Samsonovs, what are you doing? Stop it, I beg you!', [(700, 'Самсоновы, вы что творите'), (701, 'хватит, я прошу вас')], ''),
    ('samson', 'Где деньги?', 'Where is the money?', [(706, 'где')], "slang 'бабки' -> 'деньги'"),
    ('arkady', 'Я тебе ещё раз говорю! У меня нет никаких денег, слышишь?', "I'm telling you again! I don't have any money, do you hear?", [(707, 'Я тебе еще раз говорю, у меня нет никаких денег, слышишь')], 'split into two short sentences'),
    ('arkady', 'У меня ничего нет. Я клянусь тебе, я клянусь!', 'I have nothing. I swear to you, I swear!', [(708, 'У меня нет. Я клянусь тебе, я клянусь')], "'ничего' added"),
    ('samson', 'Нинуль, включай паяльник.', 'Ninul, plug in the soldering iron.', [(709, 'включай паяльник')], "cue 709 mistranscribes 'Нинуль' as 'Синуль'"),
    ('nina', 'Сейчас включу. Он у нас быстро всё вспомнит.', "I'll plug it in right now. He'll remember everything quickly with us.", [], 'Nina plugs in the soldering iron'),
    ('arkady', 'Да нет у меня никаких денег! Ну вы слышите меня?', "I don't have any money! Can you hear me?", [(710, 'Да нет, у меня никаких денег'), (711, 'Ну вы слышите меня')], ''),
    ('samson', 'Последний раз спрашиваю. Где деньги?', "I'm asking for the last time. Where is the money?", [(712, 'Спрашиваю'), (713, 'Последний раз. Где')], "slang 'бабки' -> 'деньги'"),
    ('arkady', 'Самсоновы, ну вы очнитесь! Я понимаю, вам очень хочется квартиру.', 'Samsonovs, come to your senses! I understand you really want the flat.', [(714, 'ну вы очнитесь'), (716, 'Я понимаю'), (716, 'вам очень хочется квартиру')], "'Самсонов' -> plural 'Самсоновы'; 'что' trimmed"),
    ('arkady', 'Но вы же нормальные люди. Вы о детях своих подумайте.', "But you're normal people. Think about your children.", [(717, 'Вы же нормальные люди'), (718, 'Вы о детях своих подумайте')], "'Но' added"),
    ('arkady', 'Послушайте, вас посадят за это!', 'Listen, they will put you in prison for this!', [(719, 'Послушайте, вас'), (720, 'Вас посадят за это')], ''),
    ('arkady', 'Соседи! Пожалуйста, помогите! Убивают!', "Neighbours! Please, help! They're killing me!", [(722, 'Соседи'), (723, 'Пожалуйста, убивают')], "'помогите' added"),
]
WALK = [
    (0, None, "'I warned you.' A masculine past-tense verb. Remember, earlier Samson came to ask for the money nicely, and Arkady just laughed at him."),
    (1, 'О чём предупреждал?', "'Warned me about what?' After the preposition 'about', 'what' changes to its location form with the vowel 'yo'."),
    (1, 'Да ты что делаешь?', "'Hey, what are you doing?' Arkady realises this is not a chat. Nina steps in to help."),
    (2, None, "'Hold him tighter, Vanya!' She uses the informal command 'hold' and calls her husband by his real first name, Vanya. Arkady panics as the rope goes round him."),
    (3, 'Самсоновы, вы что творите?', "'Samsonovs, what are you doing?' He addresses the two of them by their plural surname, and uses a strong verb that means 'what are you perpetrating?'."),
    (3, 'Хватит, я прошу вас!', "'Stop it, I beg you!' The first word literally means 'it will suffice', the standard Russian way to say 'enough!'."),
    (4, None, "'Where is the money?' Two blunt words from Samson. Notice that 'money' in Russian is always plural."),
    (5, 'Я тебе ещё раз говорю!', "'I'm telling you again!' Word for word: 'I to you one more time say'."),
    (5, 'У меня нет никаких денег, слышишь?', "'I don't have any money, do you hear?' After 'there is no', both 'any' and 'money' go into the plural 'of' form. Actually, Arkady is telling the truth: his wife Vika and Pasha took everything."),
    (6, 'У меня ничего нет.', "'I have nothing.' Double negation is the rule in Russian: 'by me nothing there-is-not'."),
    (6, 'Я клянусь тебе, я клянусь!', "'I swear to you, I swear!' A self-action verb form ending in '-s', followed by 'to you'. Samson is not convinced."),
    (7, None, "'Ninul, plug in the soldering iron.' He uses an affectionate pet form of Nina's name and the command 'switch on'. Nina obliges."),
    (8, 'Сейчас включу.', "'I'll plug it in right now.' The future-tense form means 'I will switch it on'."),
    (8, 'Он у нас быстро всё вспомнит.', "'He'll remember everything quickly with us.' Another future-tense form: 'he will recall'. Arkady shouts over them."),
    (9, 'Да нет у меня никаких денег!', "'I don't have any money!' Putting 'no' right at the front makes the denial even more desperate."),
    (9, 'Ну вы слышите меня?', "'Can you hear me?' He switches to the plural 'you' for both husband and wife. Samson leans in."),
    (10, None, "'I'm asking for the last time. Where is the money?' Still the same two-word question. Arkady tries appealing to their conscience."),
    (11, 'Самсоновы, ну вы очнитесь!', "'Samsonovs, come to your senses!' Literally 'wake up!'. Then he mentions Pasha's bribe."),
    (11, 'Я понимаю, вам очень хочется квартиру.', "'I understand you really want the flat.' Impersonal phrasing: 'to you it very much wants itself a flat', with 'flat' in the object form."),
    (12, 'Но вы же нормальные люди.', "'But you're normal people.' The little particle after 'you' means 'after all'."),
    (12, 'Вы о детях своих подумайте.', "'Think about your children.' After 'about', 'children' and 'your own' take the location plural."),
    (13, None, "'Listen, they will put you in prison for this!' Literally 'they will seat you for this': in Russian, 'to seat someone' means to put them behind bars. When that fails, he yells for the flatmates."),
    (14, None, "'Neighbours! Please, help! They're killing me!' Across the street in the surveillance room, the agents hear his muffled screams through the wall, remark that a neighbour is yelling as if someone is torturing him, and keep eating their bread rings."),
]
