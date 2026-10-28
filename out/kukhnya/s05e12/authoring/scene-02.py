# Authoring module for kukhnya-s05e12-scene-02.
ID = 'kukhnya-s05e12-scene-02'
SHOW = 'kukhnya'
SEASON = 5
EPISODE = 12
SCENE = 2
TITLE = "Ночной визит к Вике  (A Night Visit to Vika's)"
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'max': 'Макс', 'tanya': 'Таня', 'vika': 'Вика'}
SOURCE_NAME = 'Кухня (Kukhnya) S5.12'
SOURCE_FILE = 'sources/kukhnya/s05/e12.ru.srt'
INTRO = "Max brings the canned meat to Vika's apartment late at night, and Vika apologizes for bothering him because she was afraid to walk to the store alone. Just as Vika invites Max to sleep on a mattress until his shift, her sister Tanya wakes up and sends him home."
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = 'That brings the midnight visit to a close. Notice how Vika first tells Max to stay, then changes her mind after Tanya reminds her that their divorce is the day after tomorrow. See you next time!'
CLOSING = ('max', 'До завтра!')
STORY = [
    ('vika', 'Спасибо. Извини, что побеспокоила.', 'Thank you. Sorry that I bothered you.', [(10, 'Спасибо. Извини, что побеспокоила')], 'adapted'),
    ('vika', 'Сестра недоступна, а самой в магазин идти страшно.', 'My sister is unreachable, and it is scary to go to the store alone.', [(11, 'сестра недоступна, а самой магазин идти страшно')], 'adapted'),
    ('max', 'Звони в любое время! Ладно, я пойду.', 'Call at any time! Alright, I will go.', [(12, 'Звони в любое время'), (13, 'Ладно, я пойду')], 'adapted'),
    ('max', 'Через три часа на работу.', 'I have work in three hours.', [(14, 'Через три часа на работу')], 'adapted'),
    ('vika', 'Ну, погоди. Домой доедешь?', 'Well, wait. Will you make it home?', [(15, 'Ну, погоди'), (16, 'Домой доедешь')], 'adapted'),
    ('vika', 'Оставайся! Вот матрас.', 'Stay! Here is a mattress.', [(17, 'Оставайся'), (18, 'Вот')], 'adapted'),
    ('tanya', 'Макс, ты чего здесь?', 'Max, why are you here?', [(19, 'ты чего')], 'adapted'),
    ('max', 'Так я тушёнку привёз.', 'Well I brought canned stewed meat.', [(20, 'Так я это, тушенку привез')], 'adapted'),
    ('tanya', 'Ты забыла? У вас послезавтра развод!', 'Did you forget? Your divorce is the day after tomorrow!', [(21, 'Ты забыл? У нас послезавтра развод')], 'adapted'),
    ('vika', 'Знаешь что, давай ты лучше дома переночуешь.', 'You know what, you had better spend the night at home.', [(22, 'Знаешь что, давай-ка ты лучше дома переночуешь')], 'adapted'),
    ('max', 'Ладно, спокойной ночи.', 'Alright, good night.', [(13, 'Ладно')], 'adapted'),
    ('vika', 'Спасибо за тушёнку.', 'Thank you for the stewed meat.', [(10, 'Спасибо')], 'adapted'),
]
WALK = [
    (0, None, '\'Thank you. Sorry that I bothered you.\' Vika simply drops this word of thanks in front of Max using "spasibo" ("thank you") — the everyday word for "thank you", which grew out of the old blessing "spasi Bog" ("God save you").'),
    (1, None, "'My sister is unreachable, and it is scary to go to the store alone.' Vika continues quietly toward Max, shifting the mood of the conversation in a single beat."),
    (2, None, '\'Call at any time! Alright, I will go.\' Addressing the time at once, Max brings in "vremya" ("time") to make the meaning unmistakable.'),
    (3, None, '\'I have work in three hours.\' Mentioning the job right here, Max leans on "rabotu" ("job", a form of "rabota") to give the remark its edge.'),
    (4, None, "'Well, wait. Will you make it home?' Vika wonders evenly while looking straight at Max here."),
    (5, None, '\'Stay! Here is a mattress.\' Bringing up a mattress in the exchange, Vika brings in "ostavaysya" ("stay", from "ostavatsya") as the key Russian word here.'),
    (6, None, '\'Max, why are you here?\' Reacting warmly during the talk, Tanya links the Russian words directly in the present with no word for "am", "is", or "are" needed.'),
    (7, None, "'Well I brought canned stewed meat.' Max answers frankly hearing Tanya, leaving no doubt about where he stands."),
    (8, None, '\'Did you forget? Your divorce is the day after tomorrow!\' Touching on the divorce with Vika, Tanya chooses "poslezavtra" ("the day after tomorrow") so Vika gets the point right away.'),
    (9, None, '\'You know what, you had better spend the night at home.\' Reacting frankly during the talk, Vika starts with "davay" ("come on, let\'s") to invite Tanya right into the action.'),
    (10, None, '\'Alright, good night.\' Max smoothly voices this word of agreement at this moment using "ladno" ("alright") — built from the old Russian root for harmony and order, used every day for "okay, fine".'),
    (11, None, '\'Thank you for the stewed meat.\' Vika directly delivers this word of thanks toward Max using "spasibo" ("thank you") — the everyday word for "thank you", which grew out of the old blessing "spasi Bog" ("God save you").'),
]
