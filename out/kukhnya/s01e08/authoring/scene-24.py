# Authoring module for kukhnya-s01e08-scene-24.
ID = 'kukhnya-s01e08-scene-24'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 8
SCENE = 24
TITLE = 'Кухонный бунт  (Kitchen Rebellion)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'elena': 'Елена', 'louis': 'Луи'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.08'
SOURCE_FILE = 'sources/kukhnya/s01/e08.ru.dual.srt'
INTRO = "Elena Pavlovna is still running Barinov's kitchen, and she checks every plate at the pass before it goes out. Louis, the French pastry chef, brings her his dessert, and she sends it back. Here it is in Russian first."
OPENER = "Let's go through the clash. Elena wants perfection, and Louis takes it personally."
TRANSITION = "Now the argument from the top."
OUTRO = "Elena ends with 'now I am in charge in this kitchen', saving the word 'I' for the very end of the sentence — right where Russian puts the word it wants to stress most. See you next time."
CLOSING = ('elena', 'Пока!')
STORY = [
    ('elena', 'Я не собираюсь отдавать это блюдо!', 'I am not going to send out this dish!', [(275, 'Я это не собираюсь забирать')], ''),
    ('louis', 'Почему? Десерт получился очень красивым, шеф.', 'Why? The dessert turned out very pretty, Chef.', [], ''),
    ('elena', 'Такое ощущение, будто его уже ели!', 'It feels as if someone already ate it!', [(277, 'Такое ощущение, что его уже ели')], ''),
    ('louis', 'Клянусь, никто этот торт не трогал!', 'I swear, nobody touched this cake!', [(278, 'Никто это не ел')], ''),
    ('elena', 'Тогда быстро сделайте нормальную красивую подачу!', 'Then quickly make a proper handsome presentation!', [], ''),
    ('louis', 'Я лучший кондитер, я знаю дело!', 'I am the best pastry chef, I know the craft!', [], ''),
    ('elena', 'Решайте эту проблему прямо сейчас, Луи!', 'Sort out this problem right now, Louis!', [(280, 'Решайте эту проблему, Луи')], ''),
    ('louis', 'Вот, всё исправил, забирайте на стол.', 'Here, I fixed everything, take it to the table.', [(281, 'Решиль, забирай')], ''),
    ('elena', 'Где су-шеф? Что вообще здесь происходит?', 'Where is the sous-chef? What on earth is happening here?', [(282, 'Где су-шеф'), (284, 'Что вообще здесь происходит')], ''),
    ('louis', 'Эта женщина совсем сошла с ума!', 'This woman has completely lost her mind!', [(285, 'совсем больной девочка стала')], ''),
    ('elena', 'Я требую идеальный порядок на кухне!', 'I demand ideal order in the kitchen!', [], ''),
    ('louis', 'Шеф Баринов никогда так не психовал!', 'Chef Barinov never freaked out like that!', [(286, 'Психует')], ''),
    ('elena', 'Теперь на этой кухне командую я!', 'Now I am in charge in this kitchen!', [], ''),
]
WALK = [
    (0, None, ["'I am not going to send out this dish!' Refusing to accept the plate, Elena uses ", ('elena', 'собираюсь'), ' to say she has absolutely no intention of letting it leave the kitchen.']),
    (1, None, ["'Why? The dessert turned out very pretty, Chef.' Puzzled by her reaction, Louis argues the dessert ", ('louis', 'получился'), ' beautifully, meaning it came out looking great.']),
    (2, None, ["'It feels as if someone already ate it!' Complaining about the messy look, she uses ", ('elena', 'будто'), ' to express that it looks as if someone ruined it.']),
    (3, None, ["'I swear, nobody touched this cake!' Defending his pristine work, he swears that absolutely ", ('louis', 'никто'), ' came near the cake before he brought it over.']),
    (4, None, ["'Then quickly make a proper handsome presentation!' Demanding a much better result, she orders him to fix the ", ('elena', 'подачу'), ' or visual presentation of the food.']),
    (5, None, ["'I am the best pastry chef, I know the craft!' Calling himself a true professional, he uses the word ", ('louis', 'кондитер'), ' for his role as a dessert maker.']),
    (6, None, ["'Sort out this problem right now, Louis!' Ordering him to fix the issue immediately, she uses ", ('elena', 'Решайте'), ' to demand a solution without any further delay.']),
    (7, None, ["'Here, I fixed everything, take it to the table.' Presenting the updated plate, he proudly states that he ", ('louis', 'исправил'), ' all the flaws and made it perfect.']),
    (8, None, ["'Where is the sous-chef? What on earth is happening here?' Frustrated by the ongoing chaos, she adds ", ('elena', 'вообще'), ' to ask what on earth is going on around her.']),
    (9, None, ["'This woman has completely lost her mind!' Shocked by her intense behavior, he calls her ", ('louis', 'совсем'), ' crazy, emphasizing just how entirely unreasonable she is being.']),
    (10, None, ["'I demand ideal order in the kitchen!' Setting strict standards for the workspace, she demands absolute ", ('elena', 'порядок'), ' and total neatness from her staff.']),
    (11, None, ["'Chef Barinov never freaked out like that!' Comparing her to the previous boss, Louis notes that Barinov never ", ('louis', 'психовал'), ' or lost his temper over a dessert.']),
    (12, None, ["'Now I am in charge in this kitchen!' Making her absolute authority very clear, she places ", ('elena', 'я'), ' at the very end to show she is the one making decisions.']),
]
