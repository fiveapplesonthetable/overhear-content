# domashniy-arest/s01e01/scene-11.py
ID = "domashniy-arest-s01e01-scene-11"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 1
SCENE = 11
TITLE = "Ты же слово дал!  (You Gave Your Word!)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.01"
SOURCE_FILE = "sources/domashniy-arest/s01/e01.ru.dual.srt"
VOICES = {"narrator": "sky", "anya": "alisa", "samson": "anja", "lydia": "angelina"}
LABELS = {"anya": "Аркадий", "samson": "Самсон", "lydia": "Лидия Алексеевна"}
INTRO = "Back at the town hall, Arkady has just finished a phone call planning City Day, with free beer and pop stars from Moscow, all to win votes. Last time, Samson's wife told him he should have accepted the mayor's job offer, silly, humiliating condition and all, so now Samson is back in the mayor's office. Let's listen in Russian first."
STORY = [
    ("anya", "О, Самсон. Зачем пришёл?", "Oh, Samson. What have you come for?", [(445, 'О, Самсон'), (447, 'пришел')], "slangy 'Че' -> 'Зачем'"),
    ("samson", "Один раз.", "Just once.", [(448, 'Один раз')], ""),
    ("anya", "Что один раз?", "What do you mean, once?", [(449, 'Что один раз')], ""),
    ("samson", "Ну, то, что ты говорил.", "Well, the thing you said.", [(450, 'то, что ты говорил')], "'это' dropped; the word 'kiss' left to the narrator"),
    ("anya", "Ну, как хочешь. Лидия Алексеевна, зайдите, пожалуйста!", "Well, as you like. Lidia Alekseyevna, come in, please!", [(451, 'Ну, как хочешь'), (455, 'Лидия Алексеевна, зайдите, пожалуйста')], "two cues joined; 'и охрану пригласите' (and call security) dropped"),
    ("samson", "Зачем это?", "What's that for?", [(456, 'Зачем это')], ""),
    ("anya", "Чтобы свидетели были, Самсон.", "So that there are witnesses, Samson.", [(457, 'свидетели были, Самсон')], "colloquial 'Чтоб' -> 'Чтобы'"),
    ("anya", "Лидия Алексеевна, вы всё видели?", "Lidia Alekseyevna, did you see everything?", [], "new: a clean stand-in for cue 463 (the crude question about 'contact')"),
    ("lydia", "Да, Аркадий Борисович. Всё видела.", "Yes, Arkady Borisovich. I saw everything.", [], "new: stands in for her one-word answer in cue 464"),
    ("anya", "Вот теперь мир.", "Now we're at peace.", [(468, 'Вот теперь мир')], ""),
    ("samson", "Мир, мир. А когда на работу?", "Peace, peace. So when do I start work?", [(469, 'Мир, мир')], "second sentence new: a clean version of cues 470-472 (when do I take over the post?)"),
    ("anya", "Слушай, Самсон, я тут подумал. Твой начальник — такой опытный специалист.", "Listen, Samson, I've been thinking. Your boss is such an experienced specialist.", [(474, 'Слушай, Самсон, я тут подумал'), (475, 'такой опытный специалист')], "the boss's surname replaced by 'Твой начальник'"),
    ("anya", "Мы не можем его уволить. Это нехорошо.", "We can't fire him. It's not nice.", [(476, 'уволить'), (479, 'Нехорошо')], "cue 476 simplified ('Не можем мы с тобой его взять и уволить'); 'Это' added"),
    ("samson", "А кем тогда я буду?", "Then what am I going to be?", [(480, 'Кем тогда я')], "'А' and 'буду' added"),
    ("anya", "А ты иди на биржу труда. Там есть работа.", "You go to the job centre. There's work there.", [(482, 'на биржу труда')], "'ступай' -> 'иди'; second sentence simplifies cue 483 (there'll surely be some vacancies)"),
    ("samson", "Ты же слово дал!", "But you gave your word!", [(484, 'Ты же слово дал')], ""),
    ("anya", "А что я за мэр такой, который держит своё слово?", "And what kind of mayor would I be if I kept my word?", [(485, 'что я за мэр такой, который держит свое слово')], ""),
]
OPENER = "Let's go back through it slowly. Arkady has just sent a visitor away when he notices Samson standing at the door, and he's not exactly welcoming."
WALK = [
    (0, 'О, Самсон.', "'Oh, Samson.' Just a little sound of surprise and the name. Then a short, rather cold question."),
    (0, 'Зачем пришёл?', "'What have you come for?' The first word asks 'what for'. The verb means 'came', and it is in the masculine past form, because Samson is a man. Samson answers with just two words."),
    (1, None, "'Just once.' The first word is the number one. He means he'll do it, but only one time. Arkady pretends not to understand."),
    (2, None, "'What do you mean, once?' He simply repeats Samson's words with 'what' in front, which makes Samson spell it out."),
    (3, None, "'Well, the thing you said.' He means the humiliating kiss Arkady demanded as the price of the job. The verb 'said' is past tense again, with 'you' in front. Arkady shrugs and calls someone in."),
    (4, 'Ну, как хочешь.', "'Well, as you like.' The verb means 'you want'. It's a handy phrase whenever you leave a choice to someone else. Then he calls his secretary."),
    (4, 'Лидия Алексеевна, зайдите, пожалуйста!', "'Lidia Alekseyevna, come in, please!' This is the polite command form, the one you use with a boss, a stranger, or an older colleague. Samson doesn't like the idea of an audience."),
    (5, None, "'What's that for?' The same 'what for' as before, plus a little word for 'that'. Arkady has his answer ready."),
    (6, None, "'So that there are witnesses, Samson.' The first word means 'so that'. He wants proof that the deal is done. And so it happens, off stage. Afterwards, Arkady turns to his secretary."),
    (7, None, "'Lidia Alekseyevna, did you see everything?' He uses the polite form of 'you' with her, as he always does. She answers like a perfect secretary."),
    (8, None, "'Yes, Arkady Borisovich. I saw everything.' She calls her boss by his first name and his father's name, which is the respectful way. And her verb ends in the feminine form, because she is a woman. Arkady is pleased."),
    (9, None, "'Now we're at peace.' The last word means both 'peace' and 'the world'. Samson echoes it straight back."),
    (10, 'Мир, мир.', "'Peace, peace.' He's not really interested in peace, though. He has only one question on his mind."),
    (10, 'А когда на работу?', "'So when do I start work?' Literally just 'and when to work?'. Russian often drops the verb when the meaning is clear. Now Arkady has something to tell him."),
    (11, 'Слушай, Самсон, я тут подумал.', "'Listen, Samson, I've been thinking.' The verb for 'thought' is in the masculine past tense, marked by the '-l' ending."),
    (11, 'Твой начальник — такой опытный специалист.', "'Your boss is such an experienced specialist.' There's no word for 'is' in it: Russian simply leaves it out in the present tense. This is the very boss Samson phoned and insulted the day before."),
    (12, None, "'We can't fire him. It's not nice.' The first sentence is 'we cannot him fire'. Short words like 'him' often move to the middle. Samson finally sees where this is going."),
    (13, None, "'Then what am I going to be?' The word for 'what' here takes a special ending, because it is about a job or a role you will have. Arkady has a suggestion."),
    (14, None, "'You go to the job centre. There's work there.' The first verb is a simple command, 'go'. It's a cruel joke: the mayor sends his old enemy to look for work like anyone else. Samson can't believe it."),
    (15, None, "'But you gave your word!' The small word after 'you' adds force, something like 'but you did'. And here comes Arkady's answer."),
    (16, None, "'And what kind of mayor would I be if I kept my word?' He turns the normal idea of an honest politician upside down, on purpose. So the promise was revenge, not a job offer, just as he swore as a boy."),
]
TRANSITION = "Right, let's hear the whole scene again from the beginning."
OUTRO = "That's it for this one. If the vocabulary felt heavy, don't worry: just listen out for the cry about giving your word, and Arkady's cheeky answer. See you next time!"
CLOSING = ("anya", "Пока!")
