# Authoring module for kukhnya-s01e15-scene-08.
ID = 'kukhnya-s01e15-scene-08'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 15
SCENE = 8
TITLE = 'Переезд  (Moving Out)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'max': 'Макс', 'vika': 'Вика'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.15'
SOURCE_FILE = 'sources/kukhnya/s01/e15.ru.dual.srt'
INTRO = "Max has moved out of Kostya's flat, and he tells Vika about it. She isn't sure what to make of it. Here is their talk in Russian first."
OPENER = "Let's go through it again, slowly."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = 'Max is now between flats, and Vika will not do him any favours. When you watch, notice who is more stubborn. Catch you next time.'
CLOSING = ('vika', 'Пока!')
STORY = [
    ('vika', 'Ну что? Поговорил с Костей?', 'Well? Did you talk to Kostya?', [(156, 'Ну что? Поговорил с Костей?')], ''),
    ('max', 'Да, он умоляет меня не переезжать.', 'Yes, he begs me not to move.', [], ''),
    ('vika', 'Почему он так сильно этого не хочет?', 'Why does he strongly not want this?', [], ''),
    ('max', 'У него сейчас с деньгами проблема.', 'He has a problem with money now.', [], ''),
    ('vika', 'Но ты все-таки решился и съехал.', 'But you still decided and moved out.', [], ''),
    ('max', 'Да так быстро, что я забыл бумажник.', 'Yes so fast that I forgot the wallet.', [], ''),
    ('vika', 'И где ты живешь?', 'And where do you live?', [], ''),
    ('max', 'Пока нигде.', 'Nowhere for now.', [], ''),
    ('vika', 'То есть лучше нигде, чем со мной?', 'So better nowhere than with me?', [], ''),
    ('max', 'Ну ладно, давай к тебе приеду.', 'Well alright, let me come to you.', [], ''),
    ('vika', 'Нет, мне одолжение делать не надо.', 'No, you do not need to do me a favor.', [], ''),
    ('max', 'То есть ты не приедешь?', 'So you will not come?', [], ''),
    ('vika', 'Ты пойми, важно, чтобы мы хотели.', 'You understand, it is important that we want.', [], ''),
]
WALK = [
    (0, None, "'Well? Did you talk to Kostya?' 'Pogovoril s' is 'had a talk with', and the person goes into the 'with' form, so 'Kostya' becomes 'Kostey'. Vika sounds brisk."),
    (1, None, "'Yes, he begs me not to move.' 'Umolyaet' is 'begs', and it's a strong word. The 'not to move' keeps the repeated-action form, because he begs him not to do it at all."),
    (2, None, "'Why does he strongly not want this?' After 'ne khochet', 'this' changes to 'etogo'. Russian puts the object after a 'not want' in that shape."),
    (3, None, "'He has a problem with money now.' 'U nego' is 'at him', so 'he has'. 'S dengami' is 'with money', and 'dengi' is only ever plural in Russian."),
    (4, None, "'But you still decided and moved out.' 'Reshilsya' ends in 'sya', so it's 'made up your mind'. 'Vsyo-taki' means 'all the same', and 'syekhal' means 'rode off', that is, moved out."),
    (5, None, "'Yes so fast that I forgot the wallet.' 'Tak bystro, chto' is 'so fast that', the pattern for results. 'Bumazhnik' is a wallet, built on 'bumaga', paper."),
    (6, None, "'And where do you live?' 'Gde ty zhivyosh' is 'where you live', with no helper word. 'I' at the start means 'and'."),
    (7, None, "'Nowhere for now.' 'Nigde' is a single word for 'nowhere'. With 'poka', 'for now', it makes a neat answer."),
    (8, None, "'So better nowhere than with me?' 'To est' means 'that is', like 'i.e.'. 'Chem' is 'than', and it's the word that links the two choices."),
    (9, None, "'Well alright, let me come to you.' 'Davay priedu' is 'let's say I'll come', and it's the usual way to offer. 'K tebe' is 'to your place'."),
    (10, None, "'No, you do not need to do me a favor.' 'Odolzhenie' is a favour that one person does another, usually reluctantly. 'Mne ne nado' is 'to me not needed'."),
    (11, None, "'So you will not come?' 'Ne priedesh' is 'won't arrive by vehicle'. The same 'to est' opens the line, like a summing up."),
    (12, None, "'You understand, it is important that we want.' 'Poymi' is the order 'understand!', and it's softer than 'listen'. 'Vazhno, chtoby' is 'important that', and 'chtoby' brings the past form."),
]
