# Authoring module for domashniy-arest-s01e12-scene-14.
ID = 'domashniy-arest-s01e12-scene-14'
SHOW = 'domashniy-arest'
SEASON = 1
EPISODE = 12
SCENE = 14
TITLE = 'План и деньги  (The Plan and the Money)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'pasha': 'Паша', 'tech': 'Денис'}
SOURCE_NAME = 'Домашний арест (Domashniy Arest) S1.12'
SOURCE_FILE = 'sources/domashniy-arest/s01/e12.ru.dual.srt'
INTRO = "At the mayor's office, acting mayor Pavel Osipenko goes over the corrupt investment scheme with his associate Denis. Confident that their lucrative kickback deal is finalized, they agree on a discreet meeting location at an abandoned warehouse. Let's listen in Russian."
OPENER = "Let's examine the dialogue sentence by sentence. Notice how the speakers use standard business vocabulary alongside informal proverbs."
TRANSITION = 'Now listen to the full conversation once more at normal conversational speed.'
OUTRO = 'Pavel and Denis finalize their corrupt scheme, unaware of the trap closing around them. See you next time!'
CLOSING = ('pasha', 'До встречи.')
STORY = [
    ('pasha', 'Давайте ещё раз всё спокойно проговорим.', "Let's go over everything calmly once more.", [(246, 'Давайте еще раз все проговорим')], 'adapted'),
    ('pasha', 'В три часа у нас важная встреча.', "At three o'clock we have an important meeting.", [(247, 'в 3 часа у нас встреча')], 'adapted'),
    ('pasha', 'Вы познакомитесь со всеми нашими инвесторами.', 'You will get acquainted with all our investors.', [(248, 'Вы со всеми знакомитесь')], 'adapted'),
    ('pasha', 'После этого мы сразу закроем этот вопрос.', 'After that we will immediately close this matter.', [(249, 'И мы закрываем вопрос')], 'adapted'),
    ('pasha', 'Затем мы подпишем все официальные документы.', 'Then we will sign all official documents.', [(251, 'Подписываем все документы')], 'adapted'),
    ('tech', 'Павел Юрьевич, а где будет встреча?', 'Pavel Yuryevich, and where will the meeting be?', [(260, 'Павел Юрьевич, место')], 'adapted'),
    ('pasha', 'Там очень хорошее и надёжное место.', 'It is a very good and reliable place there.', [(261, 'Хорошее, надежное')], 'adapted'),
    ('pasha', 'Это старый заброшенный склад за городом.', 'It is an old abandoned warehouse outside town.', [(262, 'Заброшенный склад')], 'adapted'),
    ('pasha', 'Я вам позже пришлю точную геолокацию.', 'I will send you the exact geolocation later.', [(263, 'Я позже вам геолокацию скину')], 'adapted'),
    ('tech', 'Вы будете пересчитывать эти деньги?', 'Will you be recounting this money?', [(266, 'деньги перечитывать будете')], 'adapted'),
    ('pasha', 'Зачем пересчитывать? Мы вам полностью доверяем.', 'Why recount? We trust you completely.', [(267, 'Зачем'), (269, 'Мы вам полностью доверяем')], 'adapted'),
    ('tech', 'Но деньги всегда любят точный счёт.', 'But money always likes accurate counting.', [(268, 'Денежка же счет любит')], 'adapted'),
    ('tech', 'Как говорится, всегда доверяй, но проверяй!', 'As they say, always trust but verify!', [(272, 'доверяй, проверяй')], 'adapted'),
    ('pasha', 'Хорошо, тогда встретимся на этом складе.', 'Fine, then we will meet at this warehouse.', [], 'new'),
]
WALK = [
    (0, None, "'Let's go over everything calmly once more.' Back in the present day, acting mayor Pavel rehearses the kickback handover like a nervous director before opening night."),
    (3, None, '\'After that we will immediately close this matter.\' "Closing the question" is standard Russian boardroom talk for wrapping up a deal—or, in Pasha\'s case, pocketing a bribe.'),
    (7, None, '\'It is an old abandoned warehouse outside town.\' Nothing says "legitimate municipal investment" quite like meeting at a deserted warehouse beyond city limits.'),
    (10, None, "'Why recount? We trust you completely.' Pavel plays the smooth gentleman who is above counting cash, though his greed is obvious to everyone."),
    (12, None, '\'As they say, always trust but verify!\' "Doveryay, no proveryay" is the famous rhyming Russian proverb that American presidents once loved quoting during diplomatic talks.'),
    (13, None, "'Fine, then we will meet at this warehouse.' With the time and place locked in, Pasha unknowingly schedules his own arrest."),
]
