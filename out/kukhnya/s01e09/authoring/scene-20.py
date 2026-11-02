# Authoring module for kukhnya-s01e09-scene-20.
ID = 'kukhnya-s01e09-scene-20'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 9
SCENE = 20
TITLE = 'Новые открытия  (New Discoveries)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'louis': 'Луи', 'max': 'Макс'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.09'
SOURCE_FILE = 'sources/kukhnya/s01/e09.ru.dual.srt'
INTRO = 'The restaurant is quiet now, and Max stays on in the pastry section with Louis. Max owes him an apology. They have a late-night talk about misjudging people, and about how much there is still to find out. Here goes.'
OPENER = "Now let's take it slowly."
TRANSITION = 'Here it is, all together.'
OUTRO = 'That is the end of the episode, and it ends on a warm note: Max has learned something, and Louis has been heard. Next episode, there is more to discover. See you in a moment.'
CLOSING = ('max', 'Пока!')
STORY = [
    ('max', 'Луи, ты всё ещё работаешь на кухне?', 'Louis, are you still working in the kitchen?', [], ''),
    ('louis', 'Да, я делаю нежный шоколадный крем.', 'Yes, I am making delicate chocolate cream.', [], ''),
    ('max', 'Тебе кажется, что он ко всему равнодушен.', 'It seems to you that he is indifferent to everything.', [(350, 'Тебе кажется, что он ко всему равнодушен.')], ''),
    ('max', 'Но понимаешь, что мало знаешь о нём.', 'Then you realize you know little about him.', [(351, 'Но понимаешь, что мало знаешь о нем.')], ''),
    ('max', 'Луи, не обижайся на мои глупые слова.', 'Louis, do not take offense at my silly words.', [(352, 'Слушай, Луи, ты, если что, не обижайся на меня.')], ''),
    ('max', 'Я был совсем не прав насчёт тебя.', 'I was completely wrong about you.', [(353, 'Я не прав был.')], ''),
    ('louis', 'Ничего страшного, Макс, я понимаю.', 'Nothing terrible, Max, I understand.', [(355, 'О, ну.')], ''),
    ('max', 'Готовить такие десерты — это реально сложно.', 'Cooking such desserts is really difficult.', [(354, 'То, что ты делаешь, это реально сложно.')], ''),
    ('louis', 'Многие думают, что это простые сладости.', 'Many think that these are simple sweets.', [(356, 'Первым, да. Подумаешь, какие-то десертики.')], ''),
    ('louis', 'Но кондитерское искусство требует большого терпения.', 'But confectionery art requires great patience.', [], ''),
    ('max', 'Теперь я очень уважаю твой труд.', 'Now I respect your work very much.', [], ''),
    ('louis', 'Спасибо, Макс, попробуй этот свежий десерт.', 'Thank you, Max, try this fresh dessert.', [], ''),
    ('max', 'Как много открытий нам ещё предстоит.', 'How many discoveries still lie ahead for us.', [(357, 'Как много открытий нам предстоит.')], ''),
    ('max', 'И это по-настоящему здорово для нас!', 'And this is truly wonderful for us!', [(358, 'И это здорово.')], ''),
]
WALK = [
    (0, None, ["'Louis, are you still working in the kitchen?' In this question we can hear ", ('max', 'работаешь'), ', which simply means you work.']),
    (1, None, ["'Yes, I am making delicate chocolate cream.' He uses the descriptive and soft ", ('louis', 'нежный'), ' to talk about the delicate cream.']),
    (2, None, ["'It seems to you that he is indifferent to everything.' When someone does not care much, ", ('max', 'равнодушен'), ' is the perfect word for indifferent.']),
    (3, None, ["'Then you realize you know little about him.' To express a small amount here, ", ('max', 'мало'), ' is used for knowing very little.']),
    (4, None, ["'Louis, do not take offense at my silly words.' Apologizing for his previous foolish remarks, ", ('max', 'глупые'), ' describes his own silly words.']),
    (5, None, ["'I was completely wrong about you.' Admitting his mistake openly right now, ", ('max', 'прав'), ' shows he was not right before.']),
    (6, None, ["'Nothing terrible, Max, I understand.' Reassuring his friend that all is well, ", ('louis', 'страшного'), ' implies nothing terrible has happened.']),
    (7, None, ["'Cooking such desserts is really difficult.' Creating these desserts is definitely difficult, and ", ('max', 'сложно'), ' expresses this high level of difficulty.']),
    (8, None, ["'Many think that these are simple sweets.' People often mistakenly believe these are just ", ('louis', 'простые'), ' things, meaning they are very simple.']),
    (9, None, ["'But confectionery art requires great patience.' Pastry making is clearly an art form, so ", ('louis', 'искусство'), ' is chosen to describe this craft.']),
    (10, None, ["'Now I respect your work very much.' Showing his newly found deep respect, ", ('max', 'уважаю'), ' means he truly appreciates the work.']),
    (11, None, ["'Thank you, Max, try this fresh dessert.' Offering a plate of something new, ", ('louis', 'свежий'), ' highlights that the treat is fresh.']),
    (12, None, ["'How many discoveries still lie ahead for us.' Looking forward to learning more things, ", ('max', 'открытий'), ' refers to the many coming discoveries.']),
    (13, None, ["'And this is truly wonderful for us!' Ending on a very positive note, ", ('max', 'здорово'), ' shows how great this realization is.']),
]
