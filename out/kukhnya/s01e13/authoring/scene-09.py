# Authoring module for kukhnya-s01e13-scene-09.
ID = 'kukhnya-s01e13-scene-09'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 13
SCENE = 9
TITLE = 'Ссора перед отъездом  (An Argument Before Leaving)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'max': 'Макс', 'vika': 'Вика'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.13'
SOURCE_FILE = 'sources/kukhnya/s01/e13.ru.dual.srt'
INTRO = 'Vika has been about to fly to Milan for work, and Max has been avoiding her all day. He finally corners her before she leaves. Hear the argument in Russian first.'
OPENER = "Line by line, to follow Vika's mood."
TRANSITION = 'Now the argument, uncut.'
OUTRO = "Vika blames Max for the missed trip, and the coffee doesn't help. Next scene, someone else's problems."
CLOSING = ('vika', 'Пока!')
STORY = [
    ('max', 'Почему ты не сказала, что уезжаешь?', "Why didn't you tell me you were leaving?", [(124, 'что')], ''),
    ('vika', 'Давай позже поговорим.', "Let's talk later.", [(117, 'Давай позже поговорим')], ''),
    ('max', 'Нет, поговорим сейчас!', "No, we're talking now!", [(117, 'поговорим')], ''),
    ('max', 'Разреши мне объяснить, в чём дело.', "Let me explain what's going on.", [(114, 'мне объяснить, в чем дело')], ''),
    ('vika', 'Ты весь день от меня бегаешь!', "You've been avoiding me all day!", [(115, 'Ты сегодня весь день от меня бегаешь')], ''),
    ('vika', 'Мне надо подумать.', 'I need to think.', [(116, 'Мне надо подумать')], ''),
    ('vika', 'Поговорим через три дня, когда прилечу.', "We'll talk in three days when I get back.", [(117, 'Через три дня, когда я прилечу')], ''),
    ('max', 'Вика, доброе утро!', 'Vika, good morning!', [(118, 'Вик, доброе утро')], ''),
    ('max', 'Я тебе кофе принёс.', 'I brought you coffee.', [(119, 'Я тебе кофе принес')], ''),
    ('vika', 'Я тебя ненавижу!', 'I hate you!', [(120, 'Я тебя ненавижу')], ''),
    ('max', 'Ты не любишь кофе?', "You don't like coffee?", [(121, 'Ты не любишь кофе')], ''),
    ('vika', 'Да какой к чёрту кофе!', 'What the hell coffee!', [(121, 'Да какой к черту кофе')], ''),
    ('vika', 'Я из-за тебя не полетела в Милан!', 'I missed the Milan trip because of you!', [(122, 'Я из-за тебя не полетела на выставку в Милан')], ''),
]
WALK = [
    (0, None, ["'Why didn't you tell me you were leaving?' We can break down this line: ", ('max', 'сказала'), " takes a woman's ending given the person spoken to is Vika. ", ('max', 'уезжаешь'), ", you're leaving, has a prefix for 'away', on an action for going by vehicle."]),
    (1, None, ["'Let's talk later.' We can consider the phrase: ", ('vika', 'Давай'), ' begins a suggestion. ', ('vika', 'позже'), " is 'later', and ", ('vika', 'поговорим'), " is 'let's have a talk'. Vika wants the talk to happen, but not now."]),
    (2, None, ["'No, we're talking now!' It's the same ", ('max', 'поговорим'), ' as before, and the only thing that changes is ', ('max', 'сейчас'), ", 'now'. Max copies her words, which is a good way to answer."]),
    (3, None, ["'Let me explain what's going on.' Here we have for 'what's going on', ", ('max', 'в'), ('max', 'чём'), ('max', 'дело'), ", reads 'in what is the matter'. It's a set expression, so learn it as a lump and use it whenever you want an explanation."]),
    (4, None, ["'You've been avoiding me all day!' 'Running around' is how Russian says 'avoiding', so she says you run ", ('vika', 'от'), ('vika', 'меня'), ". English uses 'have been' for this, but Russian just uses the present."]),
    (5, None, ["'I need to think.' We can inspect the dialogue: ", ('vika', 'подумать'), " has a prefix that makes the thinking short, as in 'think for a bit'. ", ('vika', 'Мне'), ('vika', 'надо'), " is 'to me it's necessary', Russian for 'I need'."]),
    (6, None, ["'We'll talk in three days when I get back.' The prefix on ", ('vika', 'прилечу'), " means 'arrive', and the rest is the action of flying. So Vika says 'I'll arrive by air', which suits a plane trip."]),
    (7, None, ["'Vika, good morning!' The term for morning is a neuter word, so 'good' becomes ", ('max', 'доброе'), '. Here, and on the coffee line, Max talks as if nothing has happened.']),
    (8, None, ["'I brought you coffee.' Notice order is 'to you coffee brought', and Russian is perfectly happy with that. ", ('max', 'принёс'), " is 'brought', and ", ('max', 'кофе'), ' never changes its ending.']),
    (9, None, ["'I hate you!' Let us look at the sentence: ", ('vika', 'ненавижу'), " is 'I hate', and it's every bit as strong as the English. ", ('vika', 'тебя'), " is the form for 'you' on the receiving end."]),
    (10, None, ["'You don't like coffee?' Max is baffled. ", ('max', 'любишь'), " is 'you like' or 'you love', depending on what's coming. For liking a thing, Russians also use a different phrase meaning 'to you it is pleasing'."]),
    (11, None, ["'What the hell coffee!' We can break down this part: ", ('vika', 'какой'), " plus a naming word gives a scornful 'what do you mean, ...!'. ", ('vika', 'к'), ('vika', 'чёрту'), " means 'to the devil', a mild way of dismissing the coffee."]),
    (12, None, ["'I missed the Milan trip because of you!' We can consider the speech: ", ('vika', 'не'), ('vika', 'полетела'), " ends in a special sound for a woman. Here we have 'because of you' is the one Russians use for blame."]),
]
