# domashniy-arest/s01e02/scene-26.py
ID = "domashniy-arest-s01e02-scene-26"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 2
SCENE = 26
TITLE = "Путёвки в Крым  (A Trip to Crimea)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.02"
SOURCE_FILE = "sources/domashniy-arest/s01/e02.ru.dual.srt"
VOICES = {"narrator": "sky", "boss": "anja", "foreman": "angelina"}
LABELS = {"boss": "Николай Филиппович", "foreman": "Прораб"}
INTRO = "Now we go over to the building site, where Samson works. Last time, two agents asked Marina to spy on Arkady; she refused, but they left their card. Here Samson's boss, Nikolai, has called him into the site cabin, poured him a drink, and wants to know why Samson can't stand him. We'll hear it in Russian first; don't worry about catching every word."
STORY = [
    ("boss", "Ты смотришь на меня так, как будто убить хочешь.", "You look at me as if you want to kill me.", [(862, 'смотришь на меня так, как будто убить хочешь')], "'вот' dropped"),
    ("boss", "Нормально я на тебя смотрю. Ты чего?", "I'm looking at you normally. What's up with you?", [(863, 'нормально я на тебя смотрю'), (863, 'Ты чего')], ""),
    ("boss", "Скажи мне в глаза. За что ты меня так ненавидишь?", "Say it to my face. Why do you hate me so much?", [(868, 'мне в глаза'), (859, 'за что ты меня так ненавидишь')], "cues 859 and 866-868 joined and reordered; 'говори' -> 'скажи'"),
    ("boss", "Хорошо. Вот смотри, Николай.", "All right. Look, Nikolai.", [(869, 'Хорошо'), (870, 'Вот смотри, Николай')], ""),
    ("boss", "Ты мне сейчас водку наливаешь, да?", "Right now you're pouring me vodka, aren't you?", [(872, 'ты мне сейчас водку наливаешь, да')], "'Вот' dropped"),
    ("boss", "Да.", "Yes.", [(873, 'Да')], ""),
    ("boss", "А сам французский коньяк пьёшь.", "And you're drinking French cognac yourself.", [(874, 'французский')], "'На самом деле ... коньячок потягиваешь' -> 'А сам ... коньяк пьёшь'"),
    ("boss", "Ну, тебе какая разница, что пить?", "Well, what difference does it make to you what you drink?", [(878, 'тебе какая разница')], "slang 'бухать' -> 'пить'"),
    ("boss", "Ты что, думаешь, я жадный?", "What, you think I'm stingy?", [(885, 'Ты что, думаешь, я жадный')], ""),
    ("boss", "Думаю, жадный.", "I think you're stingy.", [(886, 'Думаю, жадный')], ""),
    ("boss", "Я не жадный. Я разумный. Вот, это тебе.", "I'm not stingy. I'm sensible. Here, this is for you.", [(890, 'Я не жадный'), (891, 'Я разумный')], "'Вот, это тебе' is a plain version of cues 895-897"),
    ("boss", "Что это?", "What's this?", [], "glue line"),
    ("boss", "Путёвки на двоих, в Крым. Март, начало сезона.", "Holiday vouchers for two, to Crimea. March, the start of the season.", [(898, 'путевки на двоих'), (899, 'В Крым'), (901, 'начало сезона')], "'Это' and 'месяц' dropped; 'Профсоюз выдал' (the union gave them out) left to the narrator"),
    ("boss", "Подожди, там же в марте холодно!", "Hold on, it's cold there in March!", [(904, 'Подожди, там же в марте')], "slang 'колотун' (freezing) -> 'холодно'"),
    ("foreman", "Плохой бетон привезли. Самсон, ты зря радиаторы носил.", "They've delivered bad concrete. Samson, you carried those radiators for nothing.", [(909, 'бетон привезли'), (910, 'Самсон, ты зря радиаторы')], "'Вместо трёхсотого 150-й' (the wrong grade) -> 'Плохой'; 'таскал' -> 'носил'; 'похоже' dropped"),
    ("foreman", "И ещё. Никто в бригаде не хочет в Крым в марте.", "And another thing. Nobody on the crew wants to go to Crimea in March.", [(914, 'в бригаде'), (915, 'Никто не хочет')], "cues 914-915 simplified, the rude adjective about Crimea and 'ехать' dropped; the boss's swearing (912) left out"),
    ("boss", "Врут. Врут.", "They're lying. They're lying.", [(917, 'Врут. Врут')], ""),
]
OPENER = "Let's go back through it. The two men are sitting at a little table in the cabin, and Nikolai starts with a complaint."
WALK = [
    (0, None, "'You look at me as if you want to kill me.' The phrase in the middle means 'as if'. The verb 'look' takes a little word meaning 'at', just like in English. Samson plays innocent."),
    (1, 'Нормально я на тебя смотрю.', "'I'm looking at you normally.' The first word is the handy everyday word for 'normally', 'fine'. Then two short words back at him."),
    (1, 'Ты чего?', "'What's up with you?' It's very casual, something friends or rivals say when the other one is acting oddly. Nikolai won't let it go."),
    (2, 'Скажи мне в глаза.', "'Say it to my face.' Literally 'say to me into the eyes'. Then the real question."),
    (2, 'За что ты меня так ненавидишь?', "'Why do you hate me so much?' The first two words together ask 'for what', meaning what have I done to deserve it. Samson decides to be honest."),
    (3, None, "'All right. Look, Nikolai.' He just uses the boss's first name, with the casual 'you'. These two clearly go back a long way. Now comes the evidence."),
    (4, None, "'Right now you're pouring me vodka, aren't you?' The little 'yes' at the end turns it into a question, like 'aren't you?'. Nikolai can't deny it."),
    (5, None, "'Yes.' Just one word, but he has walked into the trap."),
    (6, None, "'And you're drinking French cognac yourself.' The word in the middle means 'yourself': the boss keeps the good stuff for himself. Nikolai shrugs it off."),
    (7, None, "'Well, what difference does it make to you what you drink?' The middle part, 'what difference', is a phrase you'll hear all the time. But then the boss gets to the point himself."),
    (8, None, "'What, you think I'm stingy?' The adjective at the end means 'greedy' or 'stingy'. It's a masculine form, because Nikolai is talking about himself. Samson doesn't soften it."),
    (9, None, "'I think you're stingy.' He just repeats the boss's own two words, without the question. Nikolai protests."),
    (10, 'Я не жадный. Я разумный.', "'I'm not stingy. I'm sensible.' Notice there's no word for 'am': in the present tense Russian simply leaves it out. And to prove it, he pulls something out."),
    (10, 'Вот, это тебе.', "'Here, this is for you.' The first word is the one for handing things over, 'here you are'."),
    (11, None, "'What's this?' The simplest question there is, with 'this' at the end."),
    (12, 'Путёвки на двоих, в Крым.', "'Holiday vouchers for two, to Crimea.' The first word is a voucher for a trip, the kind a workers' union used to hand out. The words 'for two' are very useful, for tables and tickets too. And the date sounds lovely, at first."),
    (12, 'Март, начало сезона.', "'March, the start of the season.' The month comes first, and then 'the beginning of the season'. Samson isn't fooled."),
    (13, None, "'Hold on, it's cold there in March!' The first word is the casual way to say 'wait'. The little word after 'there' means 'surely, you know'. Just then a foreman comes in with news."),
    (14, 'Плохой бетон привезли.', "'They've delivered bad concrete.' There's no 'they' in it: the verb ends in the plural, and that's enough. And he turns to Samson."),
    (14, 'Самсон, ты зря радиаторы носил.', "'Samson, you carried those radiators for nothing.' The same word for 'in vain' as earlier. With bad concrete, all that showing off may have been wasted effort. And the foreman has one more piece of news."),
    (15, None, "'And another thing. Nobody on the crew wants to go to Crimea in March.' So the boss's generous present is something nobody else wanted. Nikolai has a two-word answer."),
    (16, None, "'They're lying. They're lying.' The verb means 'to lie', 'to tell lies', and it's in the plural: they all lie. Samson has his vouchers now, whether he likes it or not."),
]
TRANSITION = "Right, once more from the top, in the cabin."
OUTRO = "That's all for now; don't worry if the drinking talk went by fast, just listen for the bit about lying, and the boss's present. See you next time!"
CLOSING = ("boss", "Пока!")
