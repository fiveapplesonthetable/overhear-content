# domashniy-arest/s01e01/scene-21.py
ID = "domashniy-arest-s01e01-scene-21"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 1
SCENE = 21
TITLE = "Все деньги у жены  (All the Money Is His Wife's)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.01"
SOURCE_FILE = "sources/domashniy-arest/s01/e01.ru.dual.srt"
VOICES = {"narrator": "sky", "anya": "alisa", "pasha": "anja", "vika": "angelina"}
LABELS = {"anya": "Аркадий", "pasha": "Паша", "vika": "Вика"}
INTRO = "We're still in Arkady's tiny room in the communal flat. Now Arkady is alone with the two of them and asks Pasha for a favour, but the answer is not what he expects. Let's listen in Russian first."
STORY = [
    ("anya", "Паша, слушай. Это были не местные, а московские.", "Pasha, listen. They weren't local police, they were from Moscow.", [(820, 'не местные')], "'Слушай' new; 'не местные, московские' -> 'не местные, а московские'; 'Это были' added"),
    ("anya", "Поговори с Аракеляном. Пусть он заберёт заявление.", "Talk to Arakelyan. Get him to withdraw his statement.", [], "new, retelling cues 821-822 ('надави на Аракеляна, чтоб он забрал своё заявление') in plain words"),
    ("pasha", "Не заберёт он заявление, Аркаша.", "He won't withdraw the statement, Arkasha.", [(824, 'Не заберет он заявление, Аркаша')], ""),
    ("anya", "Значит, сделай так, чтобы забрал.", "Then make sure he does.", [(826, 'Значит, сделай так, чтобы забрал')], ""),
    ("pasha", "А зачем? Я сам сделал так, чтобы он его написал.", "And why would I? I'm the one who made him write it.", [(827, 'А зачем'), (828, 'сделал так, чтобы он его написал')], "'Если я' -> 'Я сам'"),
    ("anya", "Как так, Паша?", "What do you mean, Pasha?", [(835, 'Как так, Паша')], ""),
    ("pasha", "Я тебе утром говорил: не торопись. Это очень важный вопрос.", "I told you this morning: don't rush. It's a very important question.", [(831, 'не торопись'), (833, 'это очень важный вопрос')], "'Я утром что тебе сказал' -> 'Я тебе утром говорил'"),
    ("pasha", "Все в городе хотят этот кластер. Только ты против.", "Everyone in town wants this cluster. Only you are against it.", [(842, 'Все в городе хотят этот кластер'), (844, 'Только ты')], "'в позу встал' -> 'против'"),
    ("pasha", "Ты слишком сентиментальным стал. А лидер должен быть жёстким.", "You've become too sentimental. And a leader has to be tough.", [(839, 'Ты слишком сентиментальным стал'), (840, 'лидер должен быть жестким')], "'Аркашенька' dropped"),
    ("anya", "Ты поняла, Вика? Он нас обманул.", "Did you get that, Vika? He has cheated us.", [(846, 'Ты поняла, Вика'), (847, 'Он нас')], "'кинул' (slang) -> 'обманул'"),
    ("pasha", "Тихо, тихо.", "Easy, easy.", [(849, 'Тихо, тихо')], ""),
    ("anya", "Не трогай меня!", "Don't touch me!", [(851, 'Не трогай')], "'ты' dropped"),
    ("anya", "Ты знаешь, сколько у меня денег? Ты ещё пожалеешь!", "Do you know how much money I have? You'll be sorry!", [(853, 'Ты знаешь, сколько у меня')], "'бабок' (slang) -> 'денег'; the threat 'Я тебя закопаю' retold cleanly as 'Ты ещё пожалеешь!'"),
    ("pasha", "Да нет у тебя никаких денег.", "But you don't have any money.", [(858, 'Да нет у тебя никаких денег')], ""),
    ("pasha", "Все деньги у жены твоей.", "All the money is your wife's.", [(859, 'у жены твоей')], "'Все бабки он' -> 'Все деньги' (slang removed)"),
    ("anya", "Ну и что? Какая разница? Вика — моя жена.", "So what? What difference does it make? Vika is my wife.", [(860, 'Ну и что? Какая разница')], "'Вика — моя жена.' added"),
    ("vika", "Аркаша, я должна тебе сказать…", "Arkasha, there's something I have to tell you...", [], "new, leads into the next scene (cue 862 'Аркаша, я понимаю...')"),
]
OPENER = "Let's go back through it. Arkady starts by telling Pasha what he has worked out about his arrest."
WALK = [
    (0, None, "'Pasha, listen. They weren't local, they were from Moscow.' He means the police who arrested him. The little word in the middle means 'but rather': not this, but that. Then the favour."),
    (1, 'Поговори с Аракеляном.', "'Talk to Arakelyan.' He's the businessman who handed Arkady the bag of money. After the word for 'with', his name takes a new ending."),
    (1, 'Пусть он заберёт заявление.', "'Get him to withdraw his statement.' The first word means 'let': let him take it back. Pasha answers calmly."),
    (2, None, "'He won't withdraw the statement, Arkasha.' The verb comes before 'he' here, which makes it sound flat and final. Arkady doesn't accept that."),
    (3, None, "'Then make sure he does.' Literally, 'then do it so that he takes it back'. And now Pasha drops his bombshell."),
    (4, 'А зачем?', "'And why would I?' Two short words, and they already sound cold."),
    (4, 'Я сам сделал так, чтобы он его написал.', "'I'm the one who made him write it.' The word after 'I' means 'myself'. So the arrest was Pasha's plan from the start. Arkady can hardly believe it."),
    (5, None, "'What do you mean, Pasha?' Literally, 'how so?'. Pasha reminds him of their talk that morning."),
    (6, 'Я тебе утром говорил: не торопись.', "'I told you this morning: don't rush.' The word for 'this morning' is simply 'in the morning'. He means the deal with the people from Moscow."),
    (6, 'Это очень важный вопрос.', "'It's a very important question.' Then he spells it out."),
    (7, None, "'Everyone in town wants this cluster. Only you are against it.' The cluster is the big industrial project Arkady turned down. And Pasha gives him a lesson in leadership."),
    (8, None, "'You've become too sentimental. And a leader has to be tough.' The word for 'has to' changes with the person: here it is masculine, for the leader. Arkady turns to his wife."),
    (9, None, "'Did you get that, Vika? He has cheated us.' He speaks to her as 'you', and the 'a' at the end of 'got' shows she is a woman. Arkady goes for Pasha, and Pasha holds him back."),
    (10, None, "'Easy, easy.' The word really means 'quiet'. Arkady pulls away."),
    (11, None, "'Don't touch me!' A command with the word for 'not' in front. Then he tries to frighten Pasha."),
    (12, 'Ты знаешь, сколько у меня денег?', "'Do you know how much money I have?' To say 'I have', Russians say 'at me there is'. You'll hear that pattern again in a moment."),
    (12, 'Ты ещё пожалеешь!', "'You'll be sorry!' A classic threat. But Pasha is not impressed."),
    (13, None, "'But you don't have any money.' The same pattern: 'at you there is no money'. And here is why."),
    (14, None, "'All the money is your wife's.' Literally, 'all the money is at your wife's'. Notice that 'your' comes after 'wife' here; in speech that puts weight on it. Every account is in Vika's name. Arkady still trusts her."),
    (15, None, "'So what? What difference does it make? Vika is my wife.' The dash stands for the missing 'is'; Russian simply leaves it out in the present. But Vika has news of her own."),
    (16, None, "'Arkasha, there's something I have to tell you.' Arkasha is the warm, short form of his name. The word for 'have to' ends in 'a' this time, because Vika is a woman."),
]
TRANSITION = "Now let's listen to the whole scene once more."
OUTRO = "That's the moment Arkady finds out his deputy is not on his side. Next time we'll hear what Vika has to tell him, so take a short break, and. See you next time!"
CLOSING = ("anya", "Всё. До свидания!")
