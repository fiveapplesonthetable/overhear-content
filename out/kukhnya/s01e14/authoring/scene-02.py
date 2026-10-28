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
INTRO = 'At the restaurant, Max finds Sasha admiring a new cake she has decorated. He compliments her, and he has an idea for what to do next. Listen to it in Russian before we take it apart.'
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
    (0, None, "'Sasha, did you see the new beautiful cake?' 'Videla' ends in 'a' because the 'you' is Sasha. 'Tort' is masculine, so 'novy' and 'krasivy' both end in 'y' to match it."),
    (1, None, "'Of course, I decorated it myself today.' 'Sama', myself, has the 'a' of a woman; Max would say 'sam'. And the cake is 'he' again, so 'it' is 'ego', him."),
    (2, None, "'It looks simply magnificent.' Russian says 'on vyglyadit', 'he looks', about the cake. After 'vyglyadit' comes an 'o' word, 'velikolepno', where English uses 'magnificent'."),
    (3, None, "'Thank you, I tried very hard.' 'Staralas' is 'staratsya', to try hard, and after a vowel the 'sya' shrinks to a short 's'. 'Ochen silno' is literally 'very strongly'."),
    (4, None, "'Has the chef already seen your new work?' 'Rabota', work, becomes 'rabotu' as the thing seen, and 'tvoyu novuyu' take the matching 'u' ending."),
    (5, None, "'Yes, he was very satisfied with me.' After 'dovolen', pleased, the person you're pleased with takes the 'with' form, so 'ya' becomes 'mnoy'. 'Dovolen' has no ending because the chef is a man."),
    (6, None, "'And you pulled it off.' Literally, 'and this at you turned out'. Russians say 'u tebya poluchilos' for 'you managed it': the success happens 'at you' rather than being done by you."),
    (7, None, "'And now we can rest a little.' 'Mozhno' means 'it's allowed' or 'one can', and it works without any 'we' or 'I'. 'Otdokhnut', to have a rest, follows it in the basic form."),
    (8, None, "'Who wants to have some fun?' 'Poveselitsya' is built on 'vesyoly', cheerful: 'po' gives 'for a bit' and 'sya' makes it 'enjoy oneself'."),
    (9, None, "'I do.' Sasha just says 'ya khochu', 'I want'. Russians often answer a question by repeating its verb instead of saying 'yes'."),
    (10, None, "'Then let us go outside with me.' Outside in Russian is 'na ulitsu', literally 'onto the street'. 'Poydyom', let's go, is one word, and 'so mnoy' is 'with me', where 'ya' turns into 'mnoy' just as it did a moment ago."),
    (11, None, "'Wait, I will just take off my apron.' 'Snimu' is a future, 'I'll take off', with no 'will' word needed. 'Svoy fartuk', her own apron, uses the word for 'one's own' instead of 'my'."),
]
