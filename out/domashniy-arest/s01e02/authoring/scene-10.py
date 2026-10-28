# Authoring module for domashniy-arest-s01e02-scene-10.
ID = 'domashniy-arest-s01e02-scene-10'
SHOW = 'domashniy-arest'
SEASON = 1
EPISODE = 2
SCENE = 10
TITLE = 'Времени нет  (No Time for Elections)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'arkady': 'Аркадий', 'nina': 'Нина', 'samson': 'Самсон'}
SOURCE_NAME = 'Домашний арест (Domashniy Arest) S1.02'
SOURCE_FILE = 'sources/domashniy-arest/s01/e02.ru.dual.srt'
INTRO = "Back in the communal flat, Arkady has just been brought home from Pasha's office. Last time, Pasha demanded Arkady's hidden millions for the Moscow deal and gave him until evening, or the guards would get rough. Now Arkady has a hangover, and Samson is keen to start his election campaign. We'll hear it in Russian first; don't worry about catching every word."
OPENER = "Let's go back through it slowly. Last night Arkady and Samson drank together, and Samson is the first to ask how he's doing."
TRANSITION = "Now let's hear the whole scene again, without stopping."
OUTRO = "So Samson's campaign is over before it began, and Arkady still has no way to reach the governor. Take it easy, and. See you next time!"
CLOSING = ('arkady', 'Пока!')
STORY = [
    ('samson', 'Аркаш, ну как ты?', 'Arkasha, so how are you feeling?', [(263, 'Аркаш')], "'поправишься?' (will you have a drink to feel better?) -> 'ну как ты?'"),
    ('arkady', 'Очень плохая водка, Самсон.', 'That was very bad vodka, Samson.', [(265, 'Очень плохая водка, Самсон')], ''),
    ('samson', 'Вот скажи, Нина не верит.', "Go on, tell her. Nina doesn't believe it.", [(266, 'Вот скажи'), (267, 'не верит')], "'Она' -> 'Нина' so the listener knows who"),
    ('nina', 'Не верю. Какой из него мэр?', "I don't. What kind of mayor would he make?", [], "new: Nina's doubt, which cue 267 reports"),
    ('samson', 'Скажи, что я мэром могу стать.', 'Tell her I could become mayor.', [(268, 'Скажи, что я мэром могу стать')], ''),
    ('arkady', 'Он может, да.', 'He could, yes.', [(269, 'Он может, да')], ''),
    ('samson', 'Ну вот! Когда начнём?', 'There you go! When do we start?', [(270, 'когда начнем')], "'Ну вот!' new; 'Ну так. Что,' dropped"),
    ('arkady', 'Что начнём?', 'Start what?', [(271, 'Что начнем')], ''),
    ('samson', 'Как что? Выборы!', 'What do you mean, what? The election!', [(272, 'выборы')], 'simplified from cue 272 (you have to put yourself forward)'),
    ('arkady', 'Слушай, Самсон. Схема рабочая, но времени на неё совсем нет.', "Listen, Samson. The plan works, but there's no time for it at all.", [(273, 'Слушай, Самсон'), (275, 'рабочая'), (275, 'времени на неё совсем нет')], "'действительно' dropped; cue 274 'Я здесь подумал' left out"),
    ('samson', 'Как нет? Ты же сам это всё придумал!', 'What do you mean, no time? You came up with all this yourself!', [(277, 'Ты же сам это всё')], "'Как нет?' new; 'придумал' completes the cut-off cue 277"),
    ('arkady', 'Всё, выборы закончились. Тебя начальник ждёт.', "That's it, the election is over. Your boss is waiting for you.", [(278, 'Всё, выборы закончились')], "'А главам Зюк ждёт' (= Головамзюк, Samson's boss) -> 'Тебя начальник ждёт'"),
    ('samson', 'А ты что будешь делать?', 'And what are you going to do?', [], 'new: link line'),
    ('arkady', 'Мне нужно позвонить губернатору. Дай телефон.', 'I need to call the governor. Give me a phone.', [(279, 'дай телефон'), (279, 'губернатору')], "cue 279 reordered: 'Позвонить нужно' -> 'Мне нужно позвонить'"),
    ('samson', 'А где твой айфон?', "And where's your iPhone?", [], 'new: prompts cues 281-282'),
    ('arkady', 'Он заблокирован. Ниночка, дайте, пожалуйста, телефон позвонить.', "It's blocked. Ninochka, please let me use your phone to make a call.", [(282, 'он заблокирован'), (283, 'Ниночка, дайте, пожалуйста, телефон позвонить')], 'two cues joined'),
    ('nina', 'Вот когда выйдешь, тогда и дам. Шагай.', "When you get out of here, then I'll give it to you. Off you go.", [(285, 'вот когда выйдешь, тогда и дам'), (286, 'Шагай')], "'Ну' dropped"),
]
WALK = [
    (0, None, "'Arkasha, so how are you feeling?' Here, Arkasha is the friendly form of Arkady, and here Samson even clips off the last sound, the way people do when they call someone in casual speech. Arkady is clearly suffering."),
    (1, None, "'That was very bad vodka, Samson.' There's no 'was' at all: just 'very bad vodka'. The describing word ends in the same sound as the feminine word it describes. Samson has more important things on his mind."),
    (2, None, "'Go on, tell her. Nina doesn't believe it.' The first word, a little pointing word, makes the order sound more urgent, like 'go on'. And Nina is ready to say so herself."),
    (3, 'Не верю.', "'I don't believe it.' No 'I' is needed: the ending of the action word already says who. Then a scornful question."),
    (3, 'Какой из него мэр?', "'What kind of mayor would he make?' Word for word, 'what kind of mayor out of him'. It's a handy pattern for doubting that someone is up to a job. Samson turns to Arkady for support."),
    (4, None, "'Tell her I could become mayor.' Notice the word for 'mayor' gets an extra ending after the action word 'become'. Russians say you become 'as a mayor', using the 'with/as' form, the one that often means 'with' or 'as'. Arkady, too tired to argue, agrees."),
    (5, None, "'He could, yes.' Three short words, and the 'yes' comes last, almost as an afterthought. Samson is delighted."),
    (6, None, "'There you go! When do we start?' The action word has the ending for 'we', and it's a single-action form, so it points to the future, even though it looks like a present form. Arkady seems to have forgotten all about it."),
    (7, None, "'Start what?' He simply repeats Samson's action word with the word for 'what' in front. Samson can't believe it."),
    (8, None, "'What do you mean, what? The election!' The first two words are the classic way to say 'what do you mean?' when the answer seems obvious. Now Arkady has to explain."),
    (9, 'Слушай, Самсон.', "'Listen, Samson.' A very common way to start saying something the other person won't like. Then the bad news."),
    (9, 'Схема рабочая, но времени на неё совсем нет.', "'The plan works, but there's no time for it at all.' The word for 'time' changes its ending after 'there is no'; that's the 'of' form, the one that means 'of'. Samson protests."),
    (10, None, "'What do you mean, no time? You came up with all this yourself!' The little word after 'you' adds a reproach, something like 'after all'. Arkady cuts him short."),
    (11, None, "'That's it, the election is over. Your boss is waiting for you.' The boss is Nikolai Filippovich on the building site, the man Samson insulted and was told to apologise to. Samson is curious."),
    (12, None, "'And what are you going to do?' The future here is built from 'will' plus the action word 'to do', just like English. Arkady has a plan of his own."),
    (13, None, "'I need to call the governor. Give me a phone.' Literally, 'to me it is necessary to call'. The person who needs something goes into the 'to/for' form, and the governor, the one being called, is in the 'to/for' form too. Samson asks the obvious question."),
    (14, None, "'And where's your iPhone?' Same word as in English, just spelled in Russian letters. Arkady explains, and tries his luck with Nina."),
    (15, 'Он заблокирован.', "'It's blocked.' The phone is masculine, so it's 'he' in Russian. The authorities have cut it off."),
    (15, 'Ниночка, дайте, пожалуйста, телефон позвонить.', "'Ninochka, please let me use your phone to make a call.' Ninochka is a sweet, affectionate form of Nina, and he uses the polite form of 'give', laying on the charm. Nina isn't charmed."),
    (16, 'Вот когда выйдешь, тогда и дам.', "'When you get out of here, then I'll give it to you.' A neat 'when, then' pair; since he's under house arrest, it means never. And one more word to send him away."),
    (16, 'Шагай.', "'Off you go.' Literally 'step', or 'march'. It's a brisk way to tell someone to leave."),
]
