# Authoring module for kukhnya-s06e05-scene-02.
ID = 'kukhnya-s06e05-scene-02'
SHOW = 'kukhnya'
SEASON = 6
EPISODE = 5
SCENE = 2
TITLE = "Проигрыш Михаила  (Mikhail's Gambling Loss)"
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'kostya': 'Костя', 'mikhail': 'Михаил'}
SOURCE_NAME = 'Кухня (Kukhnya) S6.05'
SOURCE_FILE = 'sources/kukhnya/s06/e05.ru.srt'
INTRO = 'Just as the fortune teller predicted, identical twin bellboys summon Chef Barinov upstairs to room two-oh-seven, where Mikhail Dzhekovich has gambled away everything he owns.'
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = "While Chef Barinov hauls a broke Mikhail out of the card game, Kostya grows suspicious of Nastya's secretive morning errands. See you next time!"
CLOSING = ('kostya', 'Всего хорошего!')
STORY = [
    ('barinov', 'Прошу прощения, здесь мой друг.', 'Excuse me, my friend is in here.', [(25, 'Прошу прощения, у вас здесь мой друг')], 'adapted'),
    ('mikhail', 'Витя, это правда ты пришёл?', 'Vitya, is it really you who came?', [(26, 'Витя, Витенька, это ты')], 'adapted'),
    ('mikhail', 'Ты представляешь, я всё проиграл.', 'Can you imagine, I lost everything.', [(27, 'ты представляешь, я всё проиграл')], 'adapted'),
    ('mikhail', 'Я проиграл всё, что у меня было.', 'I lost everything that I had.', [(28, 'Всё, что у меня было')], 'adapted'),
    ('mikhail', 'Зачем я вообще с ним сел играть?', 'Why did I even sit down to play with him?', [(30, 'Зачем я вообще с ним сел играть')], 'adapted'),
    ('barinov', 'Вы его самого не выиграли?', 'Did you not win him too?', [(31, 'а вы его самого в рабство не выиграли')], 'adapted'),
    ('barinov', 'Жаль, тогда я его забираю.', 'Too bad, then I am taking him away.', [(32, 'Жаль. Ну тогда его забирают')], 'adapted'),
    ('kostya', 'Настя, ты телефон дома забыла.', 'Nastya, you forgot your phone at home.', [(35, 'Настя, а ты телефон дома забыла')], 'adapted'),
    ('barinov', 'Спасибо тебе большое, дорогой.', 'Thank you very much, my dear.', [(36, 'Спасибо')], 'adapted'),
    ('kostya', 'Скажи мне правду, пожалуйста.', 'Tell me the truth, please.', [(37, 'Скажи мне, пожалуйста')], 'adapted'),
    ('barinov', 'Гости за столиком уже ждут.', 'The guests at the table are already waiting.', [(38, 'Гости за восьмым столиком постарели уже')], 'adapted'),
    ('barinov', 'Иди быстрее прими у них заказ.', 'Go quickly and take their order.', [(39, 'Иди прими заказ')], 'adapted'),
]
WALK = [
    (0, None, "'Excuse me, my friend is in here.' Admitting that his friend is in here shows Barinov being honest for a change."),
    (1, None, '\'Vitya, is it really you who came?\' By checking whether it really Barinov who came, Mikhail presses Barinov for a straight answer. Speaking with the close, informal "you" strips away any polite distance between them.'),
    (2, None, "'Can you imagine, I lost everything.' Once can Barinov imagines he lost everything, Mikhail can finally tell Barinov what he means."),
    (3, None, '\'I lost everything that I had.\' Adding that he lost everything that he had fills in the missing piece for Barinov. Russian expresses having something as "by me is", keeping the phrase short and grounded.'),
    (4, None, '\'Why did I even sit down to play with him?\' Here wondering why he even sits down to play with him shows Mikhail looking for the real truth. In Russian, he does not need helper words like "do" or "did"—rising pitch alone turns it into a question.'),
    (5, None, "'Did you not win him too?' By asking whether Kostya not win him, Barinov presses Kostya for a straight answer."),
    (6, None, "'Too bad, then I am taking him away.' Mentioning that too bad then he is taking him away moves the talk in a new direction."),
    (7, None, '\'Nastya, you forgot your phone at home.\' Kostya reminds Barinov that Barinov forgot Barinov\'s phone at home before the moment passes. Speaking with the close, informal "you" strips away any polite distance between them.'),
    (8, None, "'Thank you very much, my dear.' Over the room and the phone, Barinov answers Kostya without a second thought."),
    (9, None, "'Tell me the truth, please.' Telling Barinov to tell him the truth please is how Kostya lays out the situation for Barinov."),
    (10, None, "'The guests at the table are already waiting.' Barinov mentions that the guests at the table are already waiting so Kostya sees what is at stake."),
    (11, None, "'Go quickly and take their order.' Going quickly and take their order moves the conversation forward without extra drama."),
]
