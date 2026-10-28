# Authoring module for kukhnya-s05e02-scene-15.
ID = 'kukhnya-s05e02-scene-15'
SHOW = 'kukhnya'
SEASON = 5
EPISODE = 2
SCENE = 15
TITLE = "Разоблачение обмана и план Дениса  (Exposing the Trick and Denis's Plan)"
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'denis': 'Денис', 'kostya': 'Костя', 'vika': 'Вика'}
SOURCE_NAME = 'Кухня (Kukhnya) S5.02'
SOURCE_FILE = 'sources/kukhnya/s05/e02.ru.srt'
INTRO = 'In the dining room, Mikhail and Barinov overhear that Vika invented the secret inspector story, while Denis realizes Katya has not watched his confession video yet and asks Kostya to distract her. Listen to the dialogue.'
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = "And that sets up two simultaneous schemes: Barinov and Mikhail's payback in room 313, and Denis's race to delete the video. Until next time!"
CLOSING = ('denis', 'До встречи!')
STORY = [
    ('kostya', 'Виктория Сергеевна, я тут вот что подумал.', 'Victoria Sergeevna, here is what I just thought.', [(178, 'Виктория Сергеевна, а я тут вот что подумал')], 'verbatim'),
    ('kostya', 'А если вдруг объявится настоящий тайный гость?', 'What if the real secret guest suddenly shows up?', [(179, 'А если вдруг объявится настоящий тайный гость?')], 'verbatim'),
    ('kostya', 'Эти двое вам уже не поверят.', 'Those two will not believe you anymore.', [(180, 'вам уже не поверят')], 'adapted'),
    ('kostya', 'Пожалуйста, не говорите им ничего.', 'Please do not tell them anything.', [(182, 'Пожалуйста, не говорите')], 'adapted'),
    ('vika', 'А если это не тайный гость, то кто?', 'And if that is not the secret guest, then who is he?', [(183, 'то кто?')], 'adapted'),
    ('vika', 'Просто обычный человек, никто.', 'Just an ordinary person, nobody.', [(184, 'Никто')], 'adapted'),
    ('denis', 'Мне кажется, она до сих пор не посмотрела.', 'It seems to me she still has not watched it.', [(186, 'Мне кажется, она до сих пор не посмотрела')], 'verbatim'),
    ('denis', 'Я уже жалею, что признался.', 'I already regret that I confessed.', [(188, 'Я уже жалею, что признался')], 'verbatim'),
    ('denis', 'Ты был совершенно прав.', 'You were completely right.', [(189, 'Ты был прав')], 'adapted'),
    ('denis', 'Костя, можешь её немного отвлечь?', 'Kostya, can you distract her a little?', [(190, 'можешь ее как-нибудь отвлечь')], 'adapted'),
    ('denis', 'Я хочу быстро удалить видео.', 'I want to delete the video quickly.', [(191, 'Я хочу удалить видео')], 'adapted'),
    ('kostya', 'Слушай, Денис, я попробую.', 'Listen, Denis, I will try.', [(192, 'Слушай')], 'adapted'),
]
WALK = [
    (0, None, "'Victoria Sergeevna, here is what I just thought.' Kostya speaks up warmly with a nod, refusing to let the moment slip past."),
    (1, None, '\'What if the real secret guest suddenly shows up?\' Mentioning the guest with Vika, Kostya puts the emphasis on "nastoyashchiy" ("real, genuine") in the middle of the talk.'),
    (2, None, "'Those two will not believe you anymore.' Kostya speaks promptly with a sigh, letting the remark speak for itself."),
    (3, None, '\'Please do not tell them anything.\' Kostya directly offers this courtesy word while facing Vika using "pozhaluysta" ("please") — the all-purpose Russian politeness word that covers both "please" and "you\'re welcome".'),
    (4, None, '\'And if that is not the secret guest, then who is he?\' Underscoring how secret things are around Kostya, Vika centers the remark on "taynyy" ("secret, undercover") without any extra fuss.'),
    (5, None, '\'Just an ordinary person, nobody.\' Stepping in earnestly right here, Vika uses the little word "prosto" ("simply, just") to make the point sound effortless.'),
    (6, None, "'It seems to me she still has not watched it.' Denis continues quietly facing Vika, watching Vika's face to see how the news lands."),
    (7, None, '\'I already regret that I confessed.\' Denis speaks up directly in the exchange and reaches for the Russian word "priznalsya" ("did he confess", built from "priznatsya") right at the center of the line.'),
    (8, None, "'You were completely right.' Following up warmly with Vika, spoken Russian compresses the whole thought into just 4 words, skipping the extra helper words English needs."),
    (9, None, "'Kostya, can you distract her a little?' Denis questions eagerly what Kostya is actually getting at here."),
    (10, None, '\'I want to delete the video quickly.\' Underscoring the video in the exchange, Denis chooses "video" ("video") so Kostya gets the point right away.'),
    (11, None, "'Listen, Denis, I will try.' Pushing back plainly beside Denis, spoken Russian compresses the whole thought into just 4 words, skipping the extra helper words English needs."),
]
