# domashniy-arest/s01e02/scene-31.py
ID = "domashniy-arest-s01e02-scene-31"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 2
SCENE = 31
TITLE = "Обед с губернатором  (Lunch with the Governor)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.02"
SOURCE_FILE = "sources/domashniy-arest/s01/e02.ru.dual.srt"
VOICES = {"narrator": "sky", "governor": "angelina", "anya": "alisa"}
LABELS = {"governor": "Губернатор", "anya": "Аркадий"}
INTRO = "So when the officers say it's time to go, he packs up and waves goodbye to the flat, sure he is being set free. Instead, they drive him to a restaurant, where the governor is waiting. Let's listen in Russian first."
STORY = [
    ("governor", "Ну привет, артист.", "Well, hello, performer.", [(1128, 'Ну привет, артист')], "«пародист» left out"),
    ("anya", "Здравствуйте.", "Hello.", [(1129, 'Здравствуйте')], ""),
    ("governor", "Садись, не бойся. Я ведь сам чуть тебя не отпустил.", "Sit down, don't be afraid. I very nearly let you go myself.", [(1130, 'не бойся'), (1131, 'чуть тебя не отпустил')], "присаживайся -> садись (plain word)"),
    ("anya", "И что случилось?", "So what happened?", [], "new: Arkady's question links the governor's story"),
    ("governor", "Повезло: Третьяков перезвонил.", "A lucky break: Tretyakov called back.", [(1132, 'повезло'), (1133, 'Третьяков перезвонил')], "«Представляешь» dropped"),
    ("anya", "И что вы ему сказали?", "And what did you tell him?", [], "new"),
    ("governor", "Я говорю: всё нормально, отпускаем Аникеева. Как же он кричал!", "I say: everything's fine, we're releasing Anikeev. How he yelled!", [(1136, 'Все нормально'), (1137, 'Отпускаем Аникеева'), (1138, 'Как же он')], "«рапортую» -> «говорю»; «орал» -> «кричал» (plain word)"),
    ("anya", "Ну, извините.", "Well, sorry.", [(1139, 'Ну извините')], ""),
    ("governor", "Ну ты молодец, очень похоже. А давай-ка ещё разок!", "Well, good for you, it sounded just like him. Come on, do it once more!", [(1140, 'Ну ты молодец'), (1141, 'Очень похоже'), (1142, 'А давай-ка еще разок')], ""),
    ("anya", "Ну что ты молчишь? Ты толстый, ты не спортсмен!", "Well, why are you so quiet? You're fat, you're no athlete!", [], "new: a clean stand-in for the crude impression (1146-1151); «молчишь» echoes the Tretyakov call (945)"),
    ("governor", "Хватит, хватит!", "Enough, enough!", [(1152, 'Хватит, хватит')], ""),
    ("anya", "Простите.", "I'm sorry.", [(1153, 'Простите')], ""),
    ("governor", "Один в один. А теперь отдай деньги.", "Spot on. And now, give back the money.", [(1154, 'Один в один'), (1157, 'отдай')], "«Ну ты денежку-то отдай» -> «А теперь отдай деньги»"),
    ("anya", "А если не отдам?", "And if I don't?", [(1164, 'А если не отдам')], ""),
    ("governor", "Ты сейчас один против всех. Счастливого конца не будет.", "Right now you're alone against everyone. There won't be a happy ending.", [(1166, 'сейчас один против всех'), (1167, 'не будет')], "«Хэппи-энда» -> «Счастливого конца» (Russian words)"),
    ("anya", "А ничего я вам не отдам.", "Well, I'm not giving you anything.", [(1170, 'А ничего')], "«А ничего-то я вам и не отдам» simplified (particles dropped)"),
    ("governor", "Клоун.", "Clown.", [(1174, 'Клоун')], ""),
]
OPENER = "Let's go back through it slowly. Arkady expected freedom, and got lunch with a very unhappy governor."
WALK = [
    (0, None, "'Well, hello, performer.' The second word is the casual 'hi', which shows the governor isn't being polite. And 'performer' is a dig: he knows all about the trick call. Arkady answers carefully."),
    (1, None, "'Hello.' This is the long, polite greeting, the one you use with a boss. The governor waves him into a chair."),
    (2, 'Садись, не бойся.', "'Sit down, don't be afraid.' Two informal commands: the governor says 'you' to Arkady as to an inferior. Then he makes a confession."),
    (2, 'Я ведь сам чуть тебя не отпустил.', "'I very nearly let you go myself.' The word for 'nearly' needs a 'not' with it, which looks odd but is how Russian says it: 'nearly not let you go' means he almost did. Arkady wants to know what went wrong."),
    (3, None, "'So what happened?' The verb is in the neuter past, because 'what' counts as neuter. Bad luck for Arkady."),
    (4, None, "'A lucky break: Tretyakov called back.' The first word means 'it was lucky', with no subject at all. The real Tretyakov phoned, without knowing anything about the fake call. Arkady asks the obvious."),
    (5, None, "'And what did you tell him?' Arkady uses the polite 'you' with the governor. The answer comes as a little scene."),
    (6, 'Я говорю: всё нормально, отпускаем Аникеева.', "'I say: everything's fine, we're releasing Anikeev.' He tells the story in the present tense, as people often do when retelling. Anikeev is Arkady's surname, and it takes the object ending."),
    (6, 'Как же он кричал!', "'How he yelled!' The little word after 'how' just adds force. Arkady offers a weak apology."),
    (7, None, "'Well, sorry.' The polite form of 'forgive'. The governor, oddly, is impressed."),
    (8, 'Ну ты молодец, очень похоже.', "'Well, good for you, it sounded just like him.' The last two words mean 'very similar'. And then a request."),
    (8, 'А давай-ка ещё разок!', "'Come on, do it once more!' The little ending on the first word makes it friendlier, and the last word is a cosy form of 'once'. So Arkady does the voice again."),
    (9, None, "'Well, why are you so quiet? You're fat, you're no athlete!' In the original he says much ruder things about the governor's weight. A judo-loving governor does not enjoy this."),
    (10, None, "'Enough, enough!' The word comes from a verb that means 'to be enough'. Arkady says sorry."),
    (11, None, "'I'm sorry.' Another verb for 'forgive', in its polite form. And the governor gives his verdict."),
    (12, 'Один в один.', "'Spot on.' Literally, 'one in one': a perfect copy. Then the real reason for the lunch."),
    (12, 'А теперь отдай деньги.', "'And now, give back the money.' The command means 'give it away', 'hand it over'. Money is always plural in Russian. He wants Arkady's hidden millions for the Moscow cluster project: he says he really needs it. Arkady tests him."),
    (13, None, "'And if I don't?' Literally, 'and if I won't hand it over?' The future is made from a completed-action verb, with no extra word for 'will'. The governor's answer is a threat."),
    (14, 'Ты сейчас один против всех.', "'Right now you're alone against everyone.' The word for 'against' is followed by the ending meaning 'of'."),
    (14, 'Счастливого конца не будет.', "'There won't be a happy ending.' After 'won't be', the happy ending takes the 'of' ending too. He tells Arkady to go home and think it over. Arkady has already thought."),
    (15, None, "'Well, I'm not giving you anything.' Again a double negative: 'nothing' plus 'not'. He even gives back the focaccia he was offered, and walks out. The governor has one last word for him."),
    (16, None, "'Clown.' The same word as in English, with the stress at the start."),
]
TRANSITION = "Here's the whole lunch once more, from the first line."
OUTRO = "And that's the scene: the trick is out, the governor wants the money, and Arkady goes back to house arrest with nothing but his pride. Until next time!"
CLOSING = ("anya", "Всего хорошего!")
