# Authoring module for kukhnya-s01e18-scene-15.
ID = 'kukhnya-s01e18-scene-15'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 18
SCENE = 15
TITLE = 'Ошибочная бутылка  (The Wrong Bottle)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'kostya': 'Костя', 'max': 'Макс'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.18'
SOURCE_FILE = 'sources/kukhnya/s01/e18.ru.dual.srt'
INTRO = "Senya is ill, and Max suspects the bar's fake cognac is to blame. At the same moment Barinov asks Kostya for a bottle of cognac, and Kostya hands him exactly the wrong one. We'll hear it in Russian first."
OPENER = "Now let's go through it in order."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = "Kostya has to get a bottle back from the chef's table, which is easier said than done. As you listen again, notice that Russians say a bottle 'stands': it is a thing that stands up. See you next time!"
CLOSING = ('max', 'Пока!')
STORY = [
    ('max', 'Костя, это просто ужас!', 'Kostya, this is just a nightmare!', [(285, 'просто')], ''),
    ('max', 'Сеня отравился нашим коньяком.', 'Senya got poisoned by our cognac.', [(281, 'что Сеня отравился этим коньяком.')], ''),
    ('kostya', 'О нет, что делать?', 'Oh no, what to do?', [], ''),
    ('barinov', 'Костя, дай мне бутылку коньяка.', 'Kostya, give me a bottle of cognac.', [(289, 'мне')], ''),
    ('barinov', 'Ту, которая стоит справа.', 'The one that stands on the right.', [], ''),
    ('kostya', 'Вот эту бутылку?', 'This bottle right here?', [(282, 'вот')], ''),
    ('barinov', 'Нет, дай мне другую. Да, эту.', 'No, give me another one. Yes, this one.', [(289, 'мне'), (289, 'мне')], ''),
    ('max', 'Шеф забрал наш коньяк!', 'Chef took our cognac!', [], ''),
    ('max', 'Надо забрать эту бутылку назад.', 'We need to take this bottle back.', [(291, 'Надо забрать бутылку, Костян.')], ''),
    ('kostya', 'Я не могу к нему подойти.', 'I can not approach him.', [(293, 'Я же не могу к ней подойти.')], ''),
    ('max', 'Давай, Костя, ты должен.', 'Come on, Kostya, you must.', [(294, 'Давай, Костян, давай, дружок.')], ''),
    ('kostya', 'Хорошо, я пойду.', 'All right, I will go.', [], ''),
]
WALK = [
    (0, None, "'Kostya, this is just awful!' 'Horror' is used to mean 'awful'. 'Just' sits right before it."),
    (1, None, "'Senya has been poisoned by our cognac.' 'Poisoned' ends in 'sya', so it's 'poisoned himself'. Russian has no word for 'by': the cognac simply takes an 'im' ending."),
    (2, None, "'Oh no, what do we do?' 'What to do' is the plain form, with no 'we'. 'Oh no' is two tiny words."),
    (3, None, "'Kostya, give me a bottle of cognac.' 'Give' is the casual command. 'A bottle of cognac' has no word for 'of': the cognac just takes an 'a' ending."),
    (4, None, "'The one on the right.' A bottle in Russian 'stands', so 'stands' is used. 'On the right' is a single word."),
    (5, None, "'This bottle right here?' 'Bottle' is feminine, so 'this' ends in 'u' as the object. The pointing word 'vot' starts it."),
    (6, None, "'No, give me another one. Yes, that one.' 'Another' ends in 'uyu', matching the feminine bottle. Barinov changes his mind in mid-sentence."),
    (7, None, "'The chef has taken our cognac!' 'Took away' ends in the masculine 'l'. 'Our cognac' is masculine too."),
    (8, None, "'We need to take this bottle back.' 'Take away' has the prefix 'za', and 'back' is a single word. 'Necessary' is followed by the plain form."),
    (9, None, "'I can't go up to him.' The prefix 'pod' on the word for 'go' means 'approach'. 'To him' picks up an 'n', so it's 'nemu'."),
    (10, None, "'Come on, Kostya, you have to.' 'Davay' means 'come on' here. 'Must' ends in 'en' for a man."),
    (11, None, "'All right, I'll go.' 'I'll go' is a plain future of going on foot. 'All right' is the usual sigh of giving in."),
]
