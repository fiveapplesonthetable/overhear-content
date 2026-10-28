ID = 'kukhnya-s05e02-scene-15'
SHOW = "kukhnya"
SEASON = 5
EPISODE = 2
SCENE = 15
TITLE = "Разоблачение обмана и план Дениса  (Exposing the Trick and Denis's Plan)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {'narrator': 'sky', 'anya': 'alisa', 'vika': 'anja', 'kostya': 'angelina'}
LABELS = {'anya': 'Денис', 'vika': 'Вика', 'kostya': 'Костя'}
SOURCE_NAME = "Кухня (Kukhnya) S5.02"
SOURCE_FILE = 'sources/kukhnya/s05/e02.ru.srt'

INTRO = 'In the dining room, Mikhail and Barinov overhear that Vika invented the secret inspector story, while Denis realizes Katya has not watched his confession video yet and asks Kostya to distract her. Listen to the dialogue.'

STORY = [
    ('kostya', 'Виктория Сергеевна, я тут вот что подумал.', 'Victoria Sergeevna, here is what I just thought.', [(178, 'Виктория Сергеевна, а я тут вот что подумал')], 'verbatim'),
    ('kostya', 'А если вдруг объявится настоящий тайный гость?', 'What if the real secret guest suddenly shows up?', [(179, 'А если вдруг объявится настоящий тайный гость?')], 'verbatim'),
    ('kostya', 'Эти двое вам уже не поверят.', 'Those two will not believe you anymore.', [(180, 'вам уже не поверят')], 'adapted'),
    ('kostya', 'Пожалуйста, не говорите им ничего.', 'Please do not tell them anything.', [(182, 'Пожалуйста, не говорите')], 'adapted'),
    ('vika', 'А если это не тайный гость, то кто?', 'And if that is not the secret guest, then who is he?', [(183, 'то кто?')], 'adapted'),
    ('vika', 'Просто обычный человек, никто.', 'Just an ordinary person, nobody.', [(184, 'Никто')], 'adapted'),
    ('anya', 'Мне кажется, она до сих пор не посмотрела.', 'It seems to me she still has not watched it.', [(186, 'Мне кажется, она до сих пор не посмотрела')], 'verbatim'),
    ('anya', 'Я уже жалею, что признался.', 'I already regret that I confessed.', [(188, 'Я уже жалею, что признался')], 'verbatim'),
    ('anya', 'Ты был совершенно прав.', 'You were completely right.', [(189, 'Ты был прав')], 'adapted'),
    ('anya', 'Костя, можешь её немного отвлечь?', 'Kostya, can you distract her a little?', [(190, 'можешь ее как-нибудь отвлечь')], 'adapted'),
    ('anya', 'Я хочу быстро удалить видео.', 'I want to delete the video quickly.', [(191, 'Я хочу удалить видео')], 'adapted'),
    ('kostya', 'Слушай, Денис, я попробую.', 'Listen, Denis, I will try.', [(192, 'Слушай')], 'adapted'),
]

OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."

WALK = [
    (0, None, "'Victoria Sergeevna, here is what I just thought.' Notice how Russian expresses 'proper name' and 'to think' with crisp inflection rather than helper words."),
    (1, None, "'What if the real secret guest suddenly shows up?' Notice the reflexive suffix on the verb meaning 'shows up', turning the action back on the subject."),
    (2, None, "'Those two will not believe you anymore.' The meaning hinges on 'these' working together with 'they will believe' in spoken Russian."),
    (3, None, "'Please do not tell them anything.' The negative particle sits right before the verb meaning 'speak' to negate the statement. Vika answers right away."),
    (4, None, "'And if that is not the secret guest, then who is he?' Vika brings out the contrast between 'and' and 'if' in a few short words."),
    (5, None, "'Just an ordinary person, nobody.' In Russian, the idea of 'simply' flows naturally into 'nobody' without extra filler words."),
    (6, None, "'It seems to me she still has not watched it.' Here the Russian phrasing highlights 'to me' before landing on 'looked'."),
    (7, None, "'I already regret that I confessed.' The '-l' ending on the verb meaning 'confessed' places the action in the masculine past tense."),
    (8, None, "'You were completely right.' The meaning hinges on 'you' working together with 'right' in spoken Russian."),
    (9, None, "'Kostya, can you distract her a little?' Notice how Russian expresses 'Kostya' and 'to distract' with crisp inflection rather than helper words."),
    (10, None, "'I want to delete the video quickly.' Denis anchors the line on 'I', while 'video' completes the thought."),
    (11, None, "'Listen, Denis, I will try.' The grammar packs 'listen' and 'will try' into a tight, idiomatic kitchen exchange."),
]

TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = "And that sets up two simultaneous schemes: Barinov and Mikhail's payback in room 313, and Denis's race to delete the video. See you next time."
CLOSING = ('anya', 'Надо удалить это видео прямо сейчас!')
