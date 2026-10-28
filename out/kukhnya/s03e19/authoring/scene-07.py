# Authoring module for kukhnya-s03e19-scene-07.
ID = 'kukhnya-s03e19-scene-07'
SHOW = 'kukhnya'
SEASON = 3
EPISODE = 19
SCENE = 7
TITLE = 'Проверка телефонным номером  (The Phone Number Test)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'hostess': 'Хостес', 'max': 'Макс', 'vika': 'Вика'}
SOURCE_NAME = 'Кухня (Kukhnya) S3.19'
SOURCE_FILE = 'sources/kukhnya/s03/e19.ru.srt'
INTRO = 'While Vika is away from the table, a young woman slips Max her phone number. Max throws the napkin away without telling Vika—and discovers that Vika sent the woman to test whether he tells her the whole truth!'
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = 'Now that Max knows Vika stages secret loyalty tests, he becomes suspicious of every woman who speaks to him. Until next time!'
CLOSING = ('vika', 'До встречи!')
STORY = [
    ('hostess', 'Вот мой номер, позвони мне сегодня вечером.', 'Here is my number, call me tonight.', [(112, 'вот, позвони мне')], 'adapted'),
    ('max', 'Девушка, вообще-то я здесь сижу не один.', 'Miss, actually I am not sitting here alone.', [(113, 'Вообще-то я не один')], 'adapted'),
    ('hostess', 'Ну ничего, позвони мне, когда будешь один.', 'Well that is fine, call me when you are alone.', [(114, 'Ну, позвони, когда будешь один')], 'adapted'),
    ('vika', 'Ну как ты тут, ещё не умер от тоски?', 'Well how are you here, have you not died of boredom yet?', [(115, 'Ну как, не умер от тоски')], 'adapted'),
    ('max', 'От тоски нет, а вот от голода сейчас умру.', 'Not of boredom, but I am about to die of hunger right now.', [(117, 'А вот от голода сейчас умру')], 'adapted'),
    ('max', 'Давай скорее нашего официанта сюда позовём.', 'Let us quickly call our waiter over here.', [(120, 'официанта же надо позвать')], 'adapted'),
    ('vika', 'Макс, скажи, с тобой сейчас всё в порядке?', 'Max, tell me, is everything alright with you right now?', [(121, 'Макс, с тобой все в порядке')], 'adapted'),
    ('max', 'Да, всё хорошо, а чего ты вдруг спрашиваешь?', 'Yes, everything is fine, why are you suddenly asking?', [(122, 'Да'), (123, 'Чего ты спрашиваешь')], 'adapted'),
    ('vika', 'Может, потому что я хотела услышать от тебя правду?', 'Maybe because I wanted to hear the truth from you?', [(124, 'потому что я хотела услышать от тебя правду')], 'adapted'),
    ('vika', 'Вон та девушка к тебе приставала и телефончик дала.', 'That girl over there hit on you and gave you her number.', [(125, 'к тебе приставала'), (126, 'Свой телефончик дала')], 'adapted'),
    ('vika', 'Это я её попросила, хотела проверить, как ты говоришь правду.', 'I asked her to do it, I wanted to test how you tell the truth.', [(128, 'Это я ее попросила'), (129, 'Я просто хотела проверить, как ты говоришь правду')], 'adapted'),
    ('max', 'Ничего же не было, я этот телефон сразу выкинул!', 'Nothing happened, I threw that phone number away immediately!', [(130, 'Ничего же не было. Я ничего не сказал'), (131, 'Телефон выкинул')], 'adapted'),
    ('vika', 'Макс, говорить правду — это значит говорить мне всё.', 'Max, telling the truth means telling me everything.', [(131, 'Макс, говорить правду'), (132, 'это значит говорить все')], 'adapted'),
]
WALK = [
    (0, None, '\'Here is my number, call me tonight.\' Talking about her number at once, the hostess brings in "nomer" ("number") to make the meaning unmistakable.'),
    (1, None, '\'Miss, actually I am not sitting here alone.\' Touching on the girlfriend in front of the hostess, Max drops in "voobshche" ("in general, altogether") to sum up the whole situation at once.'),
    (2, None, "'Well that is fine, call me when you are alone.' The hostess speaks frankly hearing Max, watching Max's face to see how the news lands."),
    (3, None, '\'Well how are you here, have you not died of boredom yet?\' Underscoring the longing on the spot, Vika chooses "yeshchyo" ("more, still") so Max gets the point right away.'),
    (4, None, '\'Not of boredom, but I am about to die of hunger right now.\' Addressing the hunger in the exchange, Max uses "goloda" ("from hunger", from "golod") to make the point stick.'),
    (5, None, "'Let us quickly call our waiter over here.' Max continues steadily in this moment, to clear the air between them once and for all."),
    (6, None, '\'Max, tell me, is everything alright with you right now?\' Discussing the order before Max, Vika uses "poryadke" ("order", from "poryadok") to make the point stick.'),
    (7, None, "'Yes, everything is fine, why are you suddenly asking?' Weighing in smoothly in this beat, Max keeps normal statement word order here, turning the line into a question for Vika purely through rising pitch."),
    (8, None, "'Maybe because I wanted to hear the truth from you?' Vika questions wryly where this conversation is heading next."),
    (9, None, '\'That girl over there hit on you and gave you her number.\' Addressing the phone during the talk, Vika puts the emphasis on "telefonchik" ("little phone") in the middle of the talk.'),
    (10, None, "'I asked her to do it, I wanted to test how you tell the truth.' Vika opens up earnestly with a nod, keeping the focus on what actually matters here."),
    (11, None, "'Nothing happened, I threw that phone number away immediately!' Max opens up evenly across the room, before Vika can change the subject."),
    (12, None, '\'Max, telling the truth means telling me everything.\' Emphasizing the truth in the exchange, Vika chooses "pravdu" ("truth", from the root "pravda") so Max hears the exact meaning.'),
]
