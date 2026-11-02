# Authoring module for kukhnya-s01e05-scene-01.
ID = 'kukhnya-s01e05-scene-01'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 5
SCENE = 1
TITLE = 'Ссора из-за поцелуя  (A Quarrel Over a Kiss)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'kostya': 'Костя', 'max': 'Макс'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.05'
SOURCE_FILE = 'sources/kukhnya/s01/e05.ru.dual.srt'
INTRO = "This is Kukhnya, which means The Kitchen: a Russian comedy set in a smart Moscow restaurant called Claude Monet, where the chef shouts and everyone else tries to get through the shift. In this story, from episode five, the bartender Kostya has just heard that his best friend Max kissed Nastya, the waitress he likes. Max has to talk his way out of it. Listen to it in Russian first, and don't worry about catching every word."
OPENER = "Let's go back through it line by line. Kostya is too angry for long sentences, which makes him easy to follow."
TRANSITION = "Here's the whole quarrel again, without stopping."
OUTRO = "Keep two lines from this one: the short question for when you're blamed and don't know why, and the expression for waving something away. Kostya's last word is a common way to say goodbye, and you'll hear it once more at the end."
CLOSING = ('kostya', 'Пока!')
STORY = [
    ('max', 'Костя, привет. Почему ты сердишься?', 'Kostya, hi. Why are you angry?', [], ""),
    ('kostya', 'Отвали, или я сломаю тебе нос!', 'Back off, or I will break your nose!', [(6, 'Отвали, или я тебе нос сломаю')], ""),
    ('max', 'За что? Что я тебе сделал?', 'What for? What did I do to you?', [(7, 'За что')], ""),
    ('kostya', 'Ты вчера целовался с моей девушкой!', 'Yesterday you kissed my girl!', [(7, 'ты целовался с моей девушкой')], ""),
    ('max', 'Это было совершенно случайное недоразумение.', 'It was a completely accidental misunderstanding.', [(11, 'это вообще недоразумение было')], ""),
    ('kostya', 'Вы целовались прямо в ресторане!', 'You were kissing right in the restaurant!', [], ""),
    ('max', 'Я вчера весь день хотел спать.', 'I wanted to sleep all day yesterday.', [(12, 'Я вчера весь день'), (12, 'спать хотел')], ""),
    ('max', 'Кстати, технически она пока не твоя.', 'By the way, technically she is not yours yet.', [(13, 'Кстати, технически она пока не твоя')], ""),
    ('kostya', 'Для меня это не имеет значения.', 'For me that does not matter.', [], ""),
    ('max', 'Между мной и Настей ничего нет!', 'There is nothing between me and Nastya!', [(15, 'между нами ничего нет')], ""),
    ('kostya', 'Ты предал нашу дружбу, Макс.', 'You betrayed our friendship, Max.', [], ""),
    ('max', 'Я докажу, что она мне безразлична.', 'I will prove that she literally translates to nothing to me.', [], ""),
    ('kostya', 'Посмотрим, как ты это докажешь.', 'We will see how you prove it.', [], ""),
]
WALK = [
    (0, None, ['\'Kostya, hi. Why are you angry?\' is the everyday ', ('max', 'Почему'), " 'why'. ", ('max', 'сердишься?'), " is the 'you' form of the verb for 'to be angry', and the reflexive ending belongs to the verb, so it stays on in every form."]),
    (1, None, ['\'Back off, or I will break your nose!\' is a rude \'get lost\', not ', ('kostya', 'Отвали,'), " something to say to your boss. Then Russian says 'I will break to-you the nose': ", ('kostya', 'тебе'), " expresses 'to you' and does the work of 'your'."]),
    (2, None, ['\'What for? What did I do to you?\' are two short words you say ', ('max', 'За'), ('max', 'что?'), " when you're blamed and can't see why. The second question has the same ", ('max', 'тебе'), " in the middle: ", ('max', 'Что'), ('max', 'я'), ('max', 'тебе'), ('max', 'сделал?')]),
    (3, None, ['\'Yesterday you kissed my girl!\' In Russian you kiss \'with\' someone: ', ('kostya', 'целовался'), ('kostya', 'с'), ('kostya', 'моей'), ('kostya', 'девушкой!'), ", and after ", ('kostya', 'с'), " the words take instrumental endings. The base word for 'girl' covers both 'young woman' and 'girlfriend'."]),
    (4, None, ['\'It was a completely accidental misunderstanding.\' Max goes for long, official-sounding words. ', ('max', 'случайное'), " comes from the noun for 'a chance' or 'an occasion', and ", ('max', 'недоразумение.'), " is the standard term for a misunderstanding."]),
    (5, None, ['\'You were kissing right in the restaurant!\' Now the \'you\' is ', ('kostya', 'Вы'), ", Max and Nastya together, and the verb turns plural: ", ('kostya', 'целовались'), ". ", ('kostya', 'прямо'), " stands for 'right' or 'straight', and ", ('kostya', 'в'), ('kostya', 'ресторане!'), " takes a prepositional ending because it says where."]),
    (6, None, ['\'I wanted to sleep all day yesterday.\' , \'the whole day\', needs no ', ('max', 'весь'), ('max', 'день'), " little word in front, just as in English. ", ('max', 'хотел'), " is the man's form of 'wanted'; Nastya would use the woman's form."]),
    (7, None, ['\'By the way, technically she is not yours yet.\' represents \'by the way\', perfect for ', ('max', 'Кстати,'), " slipping in an awkward point. ", ('max', 'пока'), " here serves as 'yet' or 'for now', and the same word is also an everyday 'bye'."]),
    (8, None, ['\'For me that does not matter.\' Word for word: \'for me this not has meaning\'. ', ('kostya', 'Для'), ('kostya', 'меня'), " acts as 'for me', and ", ('kostya', 'не'), ('kostya', 'имеет'), ('kostya', 'значения.'), " is a ready-made way to say something doesn't matter."]),
    (9, None, ['\'There is nothing between me and Nastya!\' After ', ('max', 'Между'), ", 'between', both names take instrumental endings: ", ('max', 'Между'), ('max', 'мной'), ('max', 'и'), ('max', 'Настей'), ". The combination ", ('max', 'ничего'), ('max', 'нет!'), " uses two negatives, and in Russian that's correct."]),
    (10, None, ['\'You betrayed our friendship, Max.\' The base word for \'friendship\' is built on the word for \'friend\'. Here it takes an accusative ending: ', ('kostya', 'дружбу,'), " because it's the thing being betrayed."]),
    (11, None, ['\'I will prove that she translates to nothing to me.\' functions as \'I will prove\'. Then ', ('max', 'докажу,'), " she is ", ('max', 'мне'), ('max', 'безразлична.'), ", 'indifferent to me', with the prefix for 'without' stuck on the front."]),
    (12, None, ['\'We will see how you prove it.\' which is the word for \'we\'ll ', ('kostya', 'Посмотрим,'), " see', is what you say when you don't believe a word. Max's claim comes back as ", ('kostya', 'докажешь.'), ", the form for 'you'."]),
]
