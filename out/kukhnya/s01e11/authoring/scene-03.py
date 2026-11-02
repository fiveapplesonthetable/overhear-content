# Authoring module for kukhnya-s01e11-scene-03.
ID = 'kukhnya-s01e11-scene-03'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 11
SCENE = 3
TITLE = 'Свидание на митинге  (A Date at the Rally)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'kostya': 'Костя', 'nastya': 'Настя'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.11'
SOURCE_FILE = 'sources/kukhnya/s01/e11.ru.dual.srt'
INTRO = 'Away from the critic panic, the bar is quiet. Kostya notices that Nastya, the waitress he likes, is in a low mood, and he asks her why. It plays out like this.'
OPENER = 'Let me show you how it works.'
TRANSITION = 'The same story again, now with meaning.'
OUTRO = 'Nastya has chosen a forest rally for their date, and Kostya has agreed with a good grace. It will not be a calm weekend. Take it easy, and see you in the next scene.'
CLOSING = ('kostya', 'Пока!')
STORY = [
    ('kostya', 'Привет, Настя, почему ты без настроения?', 'Hi, Nastya, why are you in a bad mood?', [(41, 'Привет.'), (43, 'без настроения?')], ''),
    ('nastya', 'Люди сорвали живые цветы ради удовольствия.', 'People tore live flowers for pleasure.', [(44, 'выбьют живые цветы?')], ''),
    ('kostya', 'Не грусти, Настя, всё будет хорошо.', 'Do not be sad, Nastya, everything will be fine.', [], ''),
    ('nastya', 'Это ужасно, так поступают злые люди.', 'This is terrible, wicked people act like that.', [(45, 'Это же ужасно. Изверги.')], ''),
    ('kostya', 'Давай сходим куда-нибудь на этих выходных.', 'Let us go somewhere this weekend.', [(46, 'сходим куда-нибудь?')], ''),
    ('nastya', 'Я тоже хотела предложить тебе встречу.', 'I also wanted to suggest a meeting to you.', [(47, 'Я тебе тоже хотела предложить.')], ''),
    ('kostya', 'Отлично! В какое красивое место пойдём?', 'Great! What beautiful place shall we go to?', [(48, 'Класс. Куда?')], ''),
    ('nastya', 'Мы поедем вместе в Химкинский лес.', 'We will go together to the Khimki forest.', [(48, 'В Химкинский лес.')], ''),
    ('kostya', 'А зачем нам ехать в лес?', 'And why do we need to go to the forest?', [(49, 'А зачем?')], ''),
    ('nastya', 'Там будет большой митинг в защиту леса.', 'There will be a big rally in defense of the forest.', [(50, 'На митинг против вырубки.')], ''),
    ('kostya', 'Я думал, мы пойдём в кино.', 'I thought we would go to the cinema.', [], ''),
    ('nastya', 'Спасать живую природу гораздо важнее кино!', 'Saving living nature is much more important than cinema!', [], ''),
    ('kostya', 'Хорошо, Настя, я с удовольствием поеду.', 'Alright, Nastya, I will gladly go.', [], ''),
]
WALK = [
    (0, None, ["'Hi, Nastya, why are you in a bad mood?' You can say ", ('kostya', 'без'), ('kostya', 'настроения'), ", 'without mood', for a bad mood, as if mood were something you can be short of. ", ('kostya', 'без'), ", 'without', changes the ending of the noun mood."]),
    (1, None, ["'People tore live flowers for pleasure.' Let's focus on the speech: ", ('nastya', 'живые'), ('nastya', 'цветы'), " are 'live flowers', real ones, as opposed to artificial. ", ('nastya', 'сорвали'), " is 'tore off' or 'picked'. ", ('nastya', 'ради'), ('nastya', 'удовольствия'), " is 'for the sake of pleasure'."]),
    (2, None, ["'Do not be sad, Nastya, everything will be fine.' Let's examine this part: ", ('kostya', 'Не'), ('kostya', 'грусти'), ", 'don't be sad', is from the noun for 'sadness'. ", ('kostya', 'всё'), ('kostya', 'будет'), ('kostya', 'хорошо'), ", 'everything will be good', is the local phrase for 'all will be well'."]),
    (3, None, ["'This is terrible, wicked people act like that.' We will inspect the speech: ", ('nastya', 'поступают'), ", 'act', is from the same family as 'deeds', in Barinov's lecture about a man's actions. ", ('nastya', 'злые'), ", 'wicked', is the root of Senya's 'don't anger'."]),
    (4, None, ["'Let us go somewhere this weekend.' Now we can look at the sentence: ", ('kostya', 'куда'), '-', ('kostya', 'нибудь'), " is 'to where' with a suffix: 'to somewhere or other'. ", ('kostya', 'сходим'), " is 'let's go and come back'. ", ('kostya', 'на'), ('kostya', 'этих'), ('kostya', 'выходных'), " is 'on these days off'."]),
    (5, None, ["'I also wanted to suggest a meeting to you.' Now let's inspect the sentence: ", ('nastya', 'хотела'), ", 'wanted', has a feminine ending. ", ('nastya', 'предложить'), ", 'suggest', is the TV woman's 'offer'. ", ('nastya', 'встречу'), ' is a meeting, and here a date.']),
    (6, None, ["'Great! What beautiful place shall we go to?' Now we can inspect the words: ", ('kostya', 'В'), ('kostya', 'какое'), ' ... ', ('kostya', 'место'), " is 'into which place': after the preposition meaning 'into', the noun stays as it is. ", ('kostya', 'пойдём'), " is 'shall we go' on foot. Nastya is thinking of something else."]),
    (7, None, ["'We will go together to the Khimki forest.' She says ", ('nastya', 'поедем'), ", the by-vehicle 'go', so they'll travel there. The place is a town on the edge of Moscow, and its forest was a famous protest site."]),
    (8, None, ["'And why do we need to go to the forest?' We can look at this line: ", ('kostya', 'зачем'), " asks 'what for'. ", ('kostya', 'нам'), ('kostya', 'ехать'), " is 'to us to go', again the by-vehicle word. ", ('kostya', 'в'), ('kostya', 'лес'), " is 'into the forest'. Kostya is puzzled."]),
    (9, None, ["'There will be a big rally in defense of the forest.' Let us look at the dialogue: ", ('nastya', 'митинг'), " is the English 'meeting' borrowed here, but it means a political rally. ", ('nastya', 'в'), ('nastya', 'защиту'), ('nastya', 'леса'), " is 'in defence of the forest': the noun for forest gets a new ending."]),
    (10, None, ["'I thought we would go to the cinema.' Let's consider this part: ", ('kostya', 'кино'), ' never changes its ending, whatever the sentence. ', ('kostya', 'думал'), ", 'thought', has the masculine ending. ", ('kostya', 'пойдём'), " is 'we will go' on foot."]),
    (11, None, ["'Saving living nature is much more important than cinema!' Let us inspect the speech: ", ('nastya', 'Спасать'), ", 'saving', is from the family of the term for 'to save'. Notice puts the second item straight after ", ('nastya', 'важнее'), ", 'more important', without 'than': ", ('nastya', 'важнее'), ('nastya', 'кино'), '.']),
    (12, None, ["'Alright, Nastya, I will gladly go.' Now let's focus on the phrase: ", ('kostya', 'с'), ('kostya', 'удовольствием'), ", 'with pleasure', is how you say 'gladly'. ", ('kostya', 'поеду'), ", 'I will go', is the by-vehicle word, because they're travelling. Kostya gives in at once."]),
]
