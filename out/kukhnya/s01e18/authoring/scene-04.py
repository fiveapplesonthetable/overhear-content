# Authoring module for kukhnya-s01e18-scene-04.
ID = 'kukhnya-s01e18-scene-04'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 18
SCENE = 4
TITLE = 'Дорогой коньяк  (Expensive Cognac)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'kostya': 'Костя', 'max': 'Макс'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.18'
SOURCE_FILE = 'sources/kukhnya/s01/e18.ru.dual.srt'
INTRO = "Max's money-making lessons for Kostya continue behind the bar. He has another trick, and this one involves expensive cognac. We'll hear it in Russian first."
OPENER = 'Here it is again, line by line.'
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = "Kostya has played along so far, but he is not at all comfortable. As you listen again, spot 'korotche', which means 'in short' and is used to wrap up an explanation. See you next time!"
CLOSING = ('max', 'Пока!')
STORY = [
    ('max', 'Это ещё не всё, слушай дальше.', 'That is not all yet, listen further.', [(129, 'Еще не все. Слушай дальше.')], ''),
    ('kostya', 'Какой ещё секрет ты мне покажешь?', 'What other secret will you show me?', [], ''),
    ('max', 'Сейчас я покажу тебе новый фокус.', 'Now I will show you a new trick.', [], ''),
    ('max', 'Короче, сначала ты берёшь чистый стакан.', 'In short, first you take a clean glass.', [(130, 'берешь стакан')], ''),
    ('kostya', 'Хорошо, я взял большой красивый бокал.', 'Alright, I took a large beautiful glass.', [], ''),
    ('max', 'Теперь представь, что я богатый гость.', 'Now imagine that I am a rich guest.', [], ''),
    ('kostya', 'Что вы желаете заказать сегодня вечером?', 'What would you like to order tonight?', [], ''),
    ('max', 'Налей мне пятьдесят грамм дорогого коньяка.', 'Pour me fifty grams of expensive cognac.', [(131, '50 грамм')], ''),
    ('kostya', 'Отличный выбор, сейчас всё будет сделано.', 'Great choice, everything will be done right now.', [(132, 'Будет сделано.')], ''),
    ('max', 'Но наливай не дорогой, а дешёвый коньяк!', 'But pour cheap cognac, not the expensive one!', [], ''),
    ('kostya', 'Ты думаешь, гость совсем ничего не заметит?', 'Do you think the guest will notice nothing at all?', [], ''),
    ('max', 'Поверь мне, никто не почувствует разницу!', 'Believe me, nobody will feel the difference!', [], ''),
]
WALK = [
    (0, None, "'That's not all, listen on.' 'Still not all' is the Russian for 'that's not all'. 'Further' is a single word."),
    (1, None, "'What other secret will you show me?' 'What other' is made with 'which' and 'else'. 'You'll show' ends in 'esh', the casual 'you'."),
    (2, None, "'Now I'll show you a new trick.' 'Trick' is the word for a conjuring trick. 'I'll show' changes its 'z' into 'zh'."),
    (3, None, "'In short, first you take a clean glass.' 'Shorter' is used here for 'in short'. 'You take' is general, so 'you' means anyone."),
    (4, None, "'Okay, I took a big, beautiful glass.' 'Took' ends in the masculine 'l'. 'Big' and 'beautiful' have matching endings."),
    (5, None, "'Now imagine I'm a rich guest.' 'Imagine' is a casual command. There is no 'am', just 'I rich guest'."),
    (6, None, "'What would you like to order this evening?' 'Wish to order' is the waiter's polite way of asking. 'This evening' is two words."),
    (7, None, "'Pour me fifty grams of expensive cognac.' 'Pour' is a command, and the number takes the 'of' form of 'grams'. 'Expensive' and 'cognac' both take the 'of' endings."),
    (8, None, "'Excellent choice, everything will be done right away.' 'Will be done' is a neuter form, because it agrees with 'everything'. 'Right away' is a very handy word."),
    (9, None, "'But pour the cheap cognac, not the expensive one!' The pattern is 'not X, but Y', with 'a' marking the second part. Cheap cognac is the real order."),
    (10, None, "'Do you think the guest won't notice anything at all?' Russian stacks the negatives: 'at all', 'nothing' and 'not'. The guest is 'the guest', with no 'a'."),
    (11, None, "'Believe me, nobody will feel the difference!' 'Believe' takes 'to me', not 'me'. 'Nobody' and 'not' appear together."),
]
