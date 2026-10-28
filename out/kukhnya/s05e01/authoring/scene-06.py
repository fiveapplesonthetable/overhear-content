# Authoring module for kukhnya-s05e01-scene-06.
ID = 'kukhnya-s05e01-scene-06'
SHOW = 'kukhnya'
SEASON = 5
EPISODE = 1
SCENE = 6
TITLE = 'Макака на кухне  (A Monkey in the Kitchen)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'mikhail': 'Михаил', 'senya': 'Сеня'}
SOURCE_NAME = 'Кухня (Kukhnya) S5.01'
SOURCE_FILE = 'sources/kukhnya/s05/e01.ru.srt'
INTRO = "After Mikhail's warning, Chef Barinov storms toward the back room to punish Senya and Fedya, only to mistake Mikhail and a guest's pet monkey for his cooks. Listen to the Russian scene."
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = "And that finishes the monkey misunderstanding in the kitchen. Notice how the base form is used with negation for a strict command: 'do not dare to lock up'. See you next time!"
CLOSING = ('barinov', 'Пока!')
STORY = [
    ('mikhail', 'Даже не смей так говорить.', 'Do not even dare to say that.', [(96, 'даже не смей говорить')], 'adapted'),
    ('mikhail', 'У тебя не всё нормально.', 'Not everything is fine with you.', [(96, 'что у тебя все нормально')], 'adapted'),
    ('barinov', 'Не сметь от меня закрываться!', 'Do not dare lock yourselves in from me!', [(100, 'Не сметь закрываться!')], 'adapted'),
    ('barinov', 'Я вас всех сегодня уволю!', 'I will fire all of you today!', [(101, 'Без всех')], 'adapted'),
    ('barinov', 'Ах ты, макака такая!', 'Oh, you little macaque monkey!', [(102, 'Ах ты, макака')], 'adapted'),
    ('barinov', 'Извини, я не так подумал.', 'Sorry, I thought the wrong thing.', [(103, 'извини, это не то, что ты подумал')], 'adapted'),
    ('mikhail', 'Это вам не просто макака.', 'This is not just a monkey to you.', [(104, 'Это вам макака')], 'adapted'),
    ('mikhail', 'Сегодня действует всё меню ресторана.', 'Today the entire restaurant menu is active.', [(104, 'действует все меню ресторана')], 'adapted'),
    ('mikhail', 'Гости ждут заказ с сегодняшнего дня.', 'Guests are waiting for orders starting today.', [(104, 'С сегодняшнего дня')], 'adapted'),
    ('barinov', 'Я просто ненавижу это правило.', 'I simply hate this rule.', [(105, 'Ненавижу')], 'adapted'),
    ('senya', 'Шеф, что сейчас здесь было?', 'Chef, what just happened here?', [(97, 'Увы')], 'adapted'),
    ('barinov', 'А что, вкусный банан?', 'Well, is it a tasty banana?', [(106, 'А что, вкусный банан?')], 'verbatim'),
]
WALK = [
    (0, None, "'Do not even dare to say that.' Mikhail follows up bluntly without holding back, without trying to dress up how he really feels."),
    (1, None, '\'Not everything is fine with you.\' Mikhail jumps in promptly before Barinov and leans on "normalno" ("fine, OK") to give the whole sentence its punch.'),
    (2, None, '\'Do not dare lock yourselves in from me!\' Leaning in earnestly beside Mikhail, the "-sya" ending on "zakryvatsya" ("to lock oneself in") marks an action that unfolds mutually or turns back on the speaker.'),
    (3, None, "'I will fire all of you today!' Barinov pushes back at once during the talk, before Mikhail can change the subject."),
    (4, None, '\'Oh, you little macaque monkey!\' Mentioning the macaque monkey in the exchange, Barinov leans on "makaka" ("macaque monkey") to give the whole sentence its punch.'),
    (5, None, '\'Sorry, I thought the wrong thing.\' Barinov lightly directs this informal apology in front of Mikhail using "izvini" ("sorry") — the casual singular apology you use with someone you know well.'),
    (6, None, "'This is not just a monkey to you.' Mikhail weighs in briskly with a sigh, testing Barinov's reaction in the middle of the exchange."),
    (7, None, '\'Today the entire restaurant menu is active.\' Mentioning the entire restaurant on the spot, Mikhail uses "restorana" ("restaurant", from "restoran") to make the point stick.'),
    (8, None, '\'Guests are waiting for orders starting today.\' Highlighting the visitors in this beat, Mikhail chooses "segodnyashnego" ("of today\'s", from the root "segodnyashniy") so Barinov hears the exact meaning.'),
    (9, None, "'I simply hate this rule.' Barinov follows up steadily with a smile, leaving no doubt about where he stands."),
    (10, None, '\'Chef, what just happened here?\' Stepping in dryly at once, Senya puts the question word "chto" right at the start so Barinov hears the focus immediately.'),
    (11, None, '\'Well, is it a tasty banana?\' Making clear how delicious things are at once, Barinov links the Russian words directly in the present with no word for "am", "is", or "are" needed.'),
]
