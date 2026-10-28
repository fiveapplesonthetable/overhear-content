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
    (0, None, "'Victoria Sergeevna, here is what I just thought.' Saying that here is what he just thought is how Kostya sets the tone with Denis."),
    (1, None, "'What if the real secret guest suddenly shows up?' Kostya asks whether what if the real secret guest suddenly shows up, refusing to let the point slide."),
    (2, None, '\'Those two will not believe you anymore.\' Explaining that those two will not believe Denis anymore lays the cards on the table for Denis. Notice how he sticks to the formal "you", keeping a professional line between them.'),
    (3, None, '\'Please do not tell them anything.\' Kostya mentions that do not tell them anything so Denis sees what is at stake. Russian stacks "never" or "nothing" together with "not", doubling the refusal for extra weight.'),
    (4, None, "'And if that is not the secret guest, then who is he?' Questioning whether if that is not the secret guest then who is he is how Vika tests Denis's story."),
    (5, None, "'Just an ordinary person, nobody.' Over the inspector and the moment, Vika answers Denis without a second thought."),
    (6, None, "'It seems to me she still has not watched it.' Denis mentions that it seems to him she still has not watched it so Kostya sees what is at stake."),
    (7, None, "'I already regret that I confessed.' Realizing that he already regrets that he confessed changes how Denis handles the situation."),
    (8, None, '\'You were completely right.\' Noting that Kostya was completely right keeps Denis\'s side of the story simple and clear. Speaking with the close, informal "you" strips away any polite distance between them.'),
    (9, None, '\'Kostya, can you distract her a little?\' Checking whether Kostya distract her a little is how Denis puts Kostya on the spot. In Russian, he does not need helper words like "do" or "did"—rising pitch alone turns it into a question.'),
    (10, None, "'I want to delete the video quickly.' Because he wants to delete the video quickly, Denis treats the matter as settled."),
    (11, None, "'Listen, Denis, I will try.' Saying that he will try is how Kostya sets the tone with Denis."),
]
