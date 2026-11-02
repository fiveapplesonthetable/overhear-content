# Authoring module for kukhnya-s01e14-scene-07.
ID = 'kukhnya-s01e14-scene-07'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 14
SCENE = 7
TITLE = "Байки Макса  (Max's Tall Tales)"
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'max': 'Макс', 'sasha': 'Саша'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.14'
SOURCE_FILE = 'sources/kukhnya/s01/e14.ru.dual.srt'
INTRO = "In the dining room, Max is showing off to the waitresses with a story about a famous French actor who loved his cooking. Of course, none of it is true. Let's hear his story in Russian first."
OPENER = 'The tall tale again, one boast at a time.'
TRANSITION = 'Now the whole story, uninterrupted.'
OUTRO = "Max is called back to the kitchen before he can get to Paris. 'Once', is how plenty of Russian stories start, true or not. Until the next one."
CLOSING = ('max', 'Пока!')
STORY = [
    ('max', 'Жерар Депардье доедает моё блюдо и говорит.', 'Gerard Depardieu finishes my dish and says.', [(136, 'доедает Депардье ему родоту и говорит.')], ''),
    ('sasha', 'Неужели ему так сильно всё понравилось?', 'Did he really like everything so much?', [], ''),
    ('max', 'Он сказал, что это просто невероятно вкусно!', 'He said that it is simply incredibly tasty!', [(137, 'офигеть!')], ''),
    ('sasha', 'Что, он прямо так тебе и сказал?', 'What, did he say it to you exactly like that?', [(139, 'Что, прям так и сказала?')], ''),
    ('max', 'Да, именно так, только на французском языке.', 'Yes, exactly like that, only in the French language.', [(140, 'Да. Ну, то по-французски.')], ''),
    ('sasha', 'Какой же ты талантливый повар, Макс!', 'What a talented cook you are, Max!', [], ''),
    ('max', 'Такую вкусную еду не готовит даже мама!', 'Even a mother does not cook such tasty food!', [(138, 'Такой родоту не готовит даже моя мама!')], ''),
    ('sasha', 'Вы с ним теперь хорошие друзья?', 'Are you now good friends with him?', [], ''),
    ('max', 'С тех пор мы с Жераром дружим.', 'Since then Gerard and I are friends.', [(141, 'С тех пор мы с Жераром дружим.')], ''),
    ('sasha', 'Расскажи нам ещё что-нибудь интересное, пожалуйста!', 'Tell us something else interesting, please!', [(145, 'расскажите еще что-нибудь там?')], ''),
    ('max', 'С большим удовольствием, милые дамы.', 'With great pleasure, lovely ladies.', [(143, 'дамы'), (146, 'Удовольствие.')], ''),
    ('max', 'Однажды, когда я работал в Париже...', 'Once, when I worked in Paris...', [(146, 'Как-то раз в Париже.')], ''),
    ('sasha', 'Какой чудесный и невероятно красивый город!', 'What a wonderful and incredibly beautiful city!', [], ''),
    ('max', 'Ой, прошу прощения, мне пора бежать.', 'Oh, I beg your pardon, it is time for me to run.', [(147, 'Прошу прощения')], ''),
]
WALK = [
    (0, None, ["'Gerard Depardieu finishes my dish and says.' Put ", ('max', 'до'), ', up to the end, in front of the verb for eating and you get ', ('max', 'доедает'), ", eats up. Dish is neuter, so 'my' becomes ", ('max', 'моё'), '.']),
    (1, None, ["'Did he really like everything so much?' Now we can analyze the words: ", ('sasha', 'Неужели'), " is a surprised 'really?'. ", ('sasha', 'ему'), ' ... ', ('sasha', 'понравилось'), " says 'to him it was pleasing': the thing liked is the subject and the person is 'to him'."]),
    (2, None, ["'He said that it is simply incredibly tasty!' Probably becomes ", ('max', 'невероятно'), ", meaning 'improbably', the usual 'incredibly'. ", ('max', 'это'), ' ... ', ('max', 'вкусно'), " means 'it tasty', needing no 'is'."]),
    (3, None, ["'What, did he say it to you exactly like that?' Let's consider the phrase: ", ('sasha', 'прямо'), ('sasha', 'так'), " means 'straight so'. The small ", ('sasha', 'и'), ' in ', ('sasha', 'так'), ('sasha', 'тебе'), ('sasha', 'и'), ('sasha', 'сказал'), " adds doubt, like 'he actually said that?'"]),
    (4, None, ["'Yes, exactly like that, only in the French language.' Russians speak ", ('max', 'на'), " a language, so 'in French' is ", ('max', 'на'), ('max', 'французском'), ('max', 'языке'), ", meaning 'on the French tongue'. ", ('max', 'именно'), ('max', 'так'), " is 'precisely so'."]),
    (5, None, ["'What a talented cook you are, Max!' Let's break down this part: ", ('sasha', 'Какой'), ('sasha', 'же'), ('sasha', 'ты'), " is the warm 'what a ... you are!'; the ", ('sasha', 'же'), ' adds the feeling. ', ('sasha', 'талантливый'), ' is built on talent.']),
    (6, None, ["'Even a mother does not cook such tasty food!' Food is feminine and it is the thing cooked, so all three words end in 'u': ", ('max', 'Такую'), ('max', 'вкусную'), ('max', 'еду'), '. ', ('max', 'даже'), " is 'even'."]),
    (7, None, ["'Are you now good friends with him?' We can examine the words: ", ('sasha', 'Вы'), ('sasha', 'с'), ('sasha', 'ним'), " reads 'you with him', meaning the two of you. One friend becomes ", ('sasha', 'друзья'), ', with a new middle for plural.']),
    (8, None, ["'Since then Gerard and I are friends.' Russians say ", ('max', 'мы'), ('max', 'С'), ('max', 'Жераром'), ", 'we with Gerard', for 'Gerard and I'. ", ('max', 'дружим'), " is a verb, 'we friend', from the same root as friend."]),
    (9, None, ["'Tell us something else interesting, please!' We can inspect the speech: ", ('sasha', 'Расскажи'), " is the order 'tell!', from the same family as a story. In ", ('sasha', 'что'), '-', ('sasha', 'нибудь'), ('sasha', 'интересное'), ", 'interesting' takes 'oe' since 'something' counts as neuter."]),
    (10, None, ["'With great pleasure, lovely ladies.' Let's examine the speech: ", ('max', 'С'), ('max', 'большим'), ('max', 'удовольствием'), " is the stock 'gladly'; 'with' puts pleasure into the 'em' form. ", ('max', 'милые'), ('max', 'дамы'), " is an old-fashioned flourish, 'dear ladies'."]),
    (11, None, ["'Once, when I worked in Paris...' Let's consider this line: ", ('max', 'Однажды'), " is 'one time', built like twice. After ", ('max', 'в'), ", in, the city takes an 'e': Paris becomes ", ('max', 'в'), ('max', 'Париже'), '.']),
    (12, None, ["'What a wonderful and incredibly beautiful city!' Let us focus on this line: ", ('sasha', 'чудесный'), " comes from a miracle. City is masculine, so both describing words end in 'y'."]),
    (13, None, ["'Oh, I beg your pardon, it is time for me to run.' Now we can look at the words: ", ('max', 'прошу'), ('max', 'прощения'), " word-for-word means 'I ask forgiveness'. ", ('max', 'мне'), ('max', 'пора'), " is 'to me it is time', the standard way to say you have to go."]),
]
