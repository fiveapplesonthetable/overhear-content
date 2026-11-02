# Authoring module for kukhnya-s01e14-scene-02.
ID = 'kukhnya-s01e14-scene-02'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 14
SCENE = 2
TITLE = 'Жажда веселья  (Thirst for Fun)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'max': 'Макс', 'sasha': 'Саша'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.14'
SOURCE_FILE = 'sources/kukhnya/s01/e14.ru.dual.srt'
INTRO = 'At the restaurant, Max finds Sasha admiring a new cake she has decorated. He compliments her, and he has an idea for what to do next. Listen to it before we take it apart.'
OPENER = 'Their chat again, slowly.'
TRANSITION = 'Now the whole chat, straight through.'
OUTRO = "Sasha leaves her apron behind, and the two of them head outside. Keep an eye on that cake later in the episode. Bye for now."
CLOSING = ('sasha', 'Пока!')
STORY = [
    ('max', 'Саша, ты видела новый красивый торт?', 'Sasha, did you see the new beautiful cake?', [], ''),
    ('sasha', 'Конечно, я сама его сегодня украшала.', 'Of course, I decorated it myself today.', [], ''),
    ('max', 'Он выглядит просто великолепно.', 'It looks simply magnificent.', [], ''),
    ('sasha', 'Спасибо, я очень сильно старалась.', 'Thank you, I tried very hard.', [], ''),
    ('max', 'Шеф уже видел твою новую работу?', 'Has the chef already seen your new work?', [], ''),
    ('sasha', 'Да, он был очень доволен мной.', 'Yes, he was very satisfied with me.', [], ''),
    ('max', 'И это у тебя получилось.', 'And you pulled it off.', [(4, 'И это у вас получилось.')], 'adapted: тебя for вас, so Max keeps calling Sasha ты'),
    ('sasha', 'А теперь можно немного отдохнуть.', 'And now we can rest a little.', [], ''),
    ('max', 'Кто тут хочет повеселиться?', 'Who wants to have some fun?', [(5, 'Кто тут хочет повеселиться?')], ''),
    ('sasha', 'Я хочу.', 'I do.', [(6, 'Я хочу.')], ''),
    ('max', 'Тогда пойдём со мной на улицу.', 'Then let us go outside with me.', [], ''),
    ('sasha', 'Подожди, я только сниму свой фартук.', 'Wait, I will just take off my apron.', [], ''),
]
WALK = [
    (0, None, ["'Sasha, did you see the new beautiful cake?' Now let's inspect the speech: ", ('max', 'видела'), ' has a feminine ending since the question is to a woman. The cake, ', ('max', 'торт'), ', is masculine, so ', ('max', 'новый'), ('max', 'красивый'), ' match it.']),
    (1, None, ["'Of course, I decorated it myself today.' We will focus on the phrase: ", ('sasha', 'сама'), " has a feminine ending. And the cake is masculine again, so 'it' is ", ('sasha', 'его'), ", meaning 'him'."]),
    (2, None, ["'It looks simply magnificent.' The language says ", ('max', 'Он'), ('max', 'выглядит'), ", meaning 'he looks', about the cake. This is followed by ", ('max', 'великолепно'), " where English uses 'magnificent'."]),
    (3, None, ["'Thank you, I tried very hard.' We will focus on the sentence: ", ('sasha', 'старалась'), " means 'tried hard', with a shortened ending after a vowel. ", ('sasha', 'очень'), ('sasha', 'сильно'), " reads as 'very strongly'."]),
    (4, None, ["'Has the chef already seen your new work?' The work, ", ('max', 'работу'), ', changes ending as the thing seen, and ', ('max', 'твою'), ('max', 'новую'), ' take matching endings.']),
    (5, None, ["'Yes, he was very satisfied with me.' After ", ('sasha', 'доволен'), ", meaning 'pleased', the person takes a 'with' form, so 'I' becomes ", ('sasha', 'мной'), '. The word for pleased has no ending because the chef is a man.']),
    (6, None, ["'And you pulled it off.' This reads as 'and this at you turned out'. People say ", ('max', 'у'), ('max', 'тебя'), ('max', 'получилось'), " for 'you managed it': the success happens 'at you' rather than being done by you."]),
    (7, None, ["'And now we can rest a little.' We will look at the words: ", ('sasha', 'можно'), " means 'it is allowed' or 'one can', and it works without any 'we' or 'I'. ", ('sasha', 'отдохнуть'), ", meaning 'to have a rest', follows it in the basic form."]),
    (8, None, ["'Who wants to have some fun?' Let's focus on this part: ", ('max', 'повеселиться'), " is built on a word for cheerful, with pieces added to mean 'enjoy oneself for a bit'."]),
    (9, None, ["'I do.' The answer is just ", ('sasha', 'Я'), ('sasha', 'хочу'), ", meaning 'I want'. It is common to answer a question by repeating its verb instead of saying 'yes'."]),
    (10, None, ["'Then let us go outside with me.' Outside here is ", ('max', 'на'), ('max', 'улицу'), ", reading as 'onto the street'. ", ('max', 'пойдём'), " means 'let us go', and ", ('max', 'со'), ('max', 'мной'), " is 'with me'."]),
    (11, None, ["'Wait, I will just take off my apron.' Let us consider the dialogue: ", ('sasha', 'сниму'), " means 'I will take off', with no 'will' word needed. ", ('sasha', 'свой'), ('sasha', 'фартук'), " uses a word meaning 'one's own' instead of 'my'."]),
]
