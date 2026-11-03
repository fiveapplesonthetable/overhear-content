# Authoring module for kukhnya-s01e14-scene-08.
ID = 'kukhnya-s01e14-scene-08'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 14
SCENE = 8
TITLE = "Обещание Нагиева  (Nagiyev's Promise)"
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'diana': 'Диана', 'nagiyev': 'Нагиев'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.14'
SOURCE_FILE = 'sources/kukhnya/s01/e14.ru.dual.srt'
INTRO = 'A rich guest, Diana, is chatting with the owner, Nagiyev, in the dining room. She loves the head chef she just met, but he is talking about Barinov and she is talking about somebody else. Have a listen to them in Russian.'
OPENER = 'Again, line by line.'
TRANSITION = 'And the conversation, start to finish.'
OUTRO = "Nagiyev promises that the chef will cook for her, without realising who she means. Hold on to the Russian phrase for 'in a good mood'. Speak soon."
CLOSING = ('nagiyev', 'Пока!')
STORY = [
    ('nagiyev', 'Диана, вы как всегда прекрасно пахнете!', 'Diana, you smell wonderful as always!', [(152, 'Дианочка, как всегда, прекрасно, цветете, пахнете.')], ''),
    ('diana', 'Дмитрий, вы такой смешной.', 'Dmitry, you are so funny.', [(155, 'Невечка, вы такой смешной.')], ''),
    ('diana', 'Кстати, я уже познакомилась с шеф-поваром.', 'By the way, I already met the head chef.', [(156, 'мы уже познакомились с вашим шеф-поваром.')], ''),
    ('nagiyev', 'Ой, Господи, и как он вам?', 'Oh, Lord, and what do you make of him?', [(157, 'Ой, господи, а?')], ''),
    ('diana', 'Он супер, просто такой красавчик!', 'He is super, just such a handsome man!', [(158, 'Он супер, такой красавчик.')], ''),
    ('nagiyev', 'Это вы вообще о ком говорите?', 'Who are you talking about anyway?', [(159, 'Это вы о ком?')], ''),
    ('diana', 'Он такой милый и очень общительный!', 'He is so sweet and very sociable!', [(161, 'Такой общительный!'), (162, 'И вообще просто душка.')], ''),
    ('nagiyev', 'Наверное, он сегодня в хорошем настроении.', 'Probably, he is in a good mood today.', [], ''),
    ('diana', 'Мне подарили книгу с французскими рецептами.', 'I was gifted a book with French recipes.', [(163, 'мне подарили книгу с редкими французскими рецептами.')], ''),
    ('nagiyev', 'Это очень интересный подарок.', 'This is a very interesting gift.', [], ''),
    ('diana', 'Он мог бы приготовить для нас?', 'Could he cook for us?', [(164, 'мог бы приготовить что-нибудь из нее')], ''),
    ('nagiyev', 'Если он в таком настроении, да.', 'If he is in such a mood, yes.', [(165, 'но если его'), (166, 'и он в таком прекрасном настроении, думаю, да.')], ''),
    ('diana', 'Я хочу, чтобы он готовил здесь!', 'I want him to cook here!', [(164, 'прямо перед моими гостями?')], ''),
    ('nagiyev', 'Хорошо, он всё сделает для вас.', 'All right, he will do everything for you.', [], ''),
]
WALK = [
    (0, None, ["'Diana, you smell wonderful as always!' We can inspect this part: ", ('nagiyev', 'как'), ('nagiyev', 'всегда'), " is 'as always'. ", ('nagiyev', 'пахнете'), ", you smell, ends with the polite 'you' ending, because Nagiyev is polite with a guest."]),
    (1, None, ["'Dmitry, you are so funny.' She pairs his full first name with the polite ", ('diana', 'вы'), ', friendly but proper. ', ('diana', 'вы'), ('diana', 'такой'), ('diana', 'смешной'), " literally says 'you such funny', with no 'are'."]),
    (2, None, ["'By the way, I already met the head chef.' We can consider the speech: ", ('diana', 'Кстати'), " is 'by the way'. You get acquainted ", ('diana', 'с'), ", with, someone, so 'head chef' becomes ", ('diana', 'шеф'), '-', ('diana', 'поваром'), '. ', ('diana', 'познакомилась'), ' has the feminine ending.']),
    (3, None, ["'Oh, Lord, and what do you make of him?' We will inspect the sentence: ", ('nagiyev', 'Господи'), " is the old calling form of 'Lord', kept alive in this exclamation. ", ('nagiyev', 'как'), ('nagiyev', 'он'), ('nagiyev', 'вам'), "? literally means 'how is he to you?'."]),
    (4, None, ["'He is super, just such a handsome man!' We will examine the sentence: ", ('diana', 'красавчик'), " shares its root with handsome, and the ending makes it playful, like 'a real looker'. ", ('diana', 'супер'), ' is borrowed and never changes.']),
    (5, None, ["'Who are you talking about anyway?' Now we can look at the speech: ", ('nagiyev', 'о'), ('nagiyev', 'ком'), " is 'about whom': 'who' turns into ", ('nagiyev', 'ком'), ' after ', ('nagiyev', 'о'), '. ', ('nagiyev', 'вообще'), ", literally 'in general', here gives the 'anyway'."]),
    (6, None, ["'He is so sweet and very sociable!' Now let's examine the phrase: ", ('diana', 'общительный'), ', sociable, is from the verb to chat or mix with people. ', ('diana', 'милый'), " is 'sweet' or 'nice' about a person."]),
    (7, None, ["'Probably, he is in a good mood today.' Now we can break down the sentence: ", ('nagiyev', 'в'), ('nagiyev', 'хорошем'), ('nagiyev', 'настроении'), " is 'in a good mood'. After ", ('nagiyev', 'в'), ', in, both words change their endings to ', ('nagiyev', 'хорошем'), ' and ', ('nagiyev', 'настроении'), '.']),
    (8, None, ["'I was gifted a book with French recipes.' Let us look at the speech: ", ('diana', 'Мне'), ('diana', 'подарили'), " reads 'to me they gifted', with no one named; Russian uses the 'they' form for this. ", ('diana', 'книгу'), ", book, takes an 'u' as the thing given."]),
    (9, None, ["'This is a very interesting gift.' We can break down the dialogue: ", ('nagiyev', 'подарок'), ', gift, comes from the same verb as ', ('nagiyev', 'подарили'), ' in the line before. ', ('nagiyev', 'интересный'), " ends in 'y' to match it, a masculine noun."]),
    (10, None, ["'Could he cook for us?' We can consider the phrase: ", ('diana', 'мог'), ('diana', 'бы'), " is 'could', the past tense ", ('diana', 'мог'), ' plus ', ('diana', 'бы'), ', and it softens a request. ', ('diana', 'для'), ('diana', 'нас'), " is 'for us'."]),
    (11, None, ["'If he is in such a mood, yes.' Here is the same mood phrase again, now with ", ('nagiyev', 'таком'), ", the 'in' form of such. ", ('nagiyev', 'Если'), " is 'if'."]),
    (12, None, ["'I want him to cook here!' Literally, 'I want so that he cooked here'. After ", ('diana', 'чтобы'), ' the verb takes the past form, ', ('diana', 'готовил'), ', though she means the future.']),
    (13, None, ["'All right, he will do everything for you.' Let's inspect this part: ", ('nagiyev', 'сделает'), " is 'will do', a future in one word. ", ('nagiyev', 'для'), ('nagiyev', 'вас'), " is 'for you', the polite 'you' again."]),
]
