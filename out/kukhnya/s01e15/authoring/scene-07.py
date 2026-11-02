# Authoring module for kukhnya-s01e15-scene-07.
ID = 'kukhnya-s01e15-scene-07'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 15
SCENE = 7
TITLE = 'Услуга за услугу  (Favor for a Favor)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'lyova': 'Лёва'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.15'
SOURCE_FILE = 'sources/kukhnya/s01/e15.ru.dual.srt'
INTRO = "Barinov is on his way out when he spots Lyova eating pancakes, and he has a favour to ask. It is not really a favour, and it doesn't end well for Lyova. Listen to it in Russian first."
OPENER = 'The deal, slowly.'
TRANSITION = 'Now the deal from start to finish.'
OUTRO = "Lyova agrees to the swap and loses his job title in the same breath. Speak soon."
CLOSING = ('barinov', 'Пока!')
STORY = [
    ('barinov', 'Лёва, не увлекайся блинами.', 'Lyova, do not get carried away with pancakes.', [(39, 'Лёва, Лёва, Лёва, не увлекайся блинами.')], ''),
    ('lyova', 'А что плохого в этих вкусных блинах?', 'And what is bad about these tasty pancakes?', [], ''),
    ('barinov', 'Вспомни про свой последний анализ.', 'Remember your last test.', [], ''),
    ('lyova', 'Мой уровень холестерина был почти в норме.', 'My cholesterol level was almost in range.', [], ''),
    ('barinov', 'Зайди в химчистку и возьми мой костюм.', 'Go to the dry cleaners and take my suit.', [], ''),
    ('lyova', 'Я не успеваю. Это в другую сторону.', 'I do not have time. That is the other way.', [], ''),
    ('barinov', 'Лёва, давай, услуга за услугу.', 'Lyova, come on, favor for a favor.', [], ''),
    ('lyova', 'Какая от вас может быть полезная услуга?', 'What useful favor can there be from you?', [], ''),
    ('barinov', 'Ты мне костюм, а я разрешаю опоздать.', 'You get me the suit, and I allow you to be late.', [], ''),
    ('lyova', 'Хорошо, я согласен на эти странные условия.', 'Alright, I agree to these strange conditions.', [], ''),
    ('barinov', 'Все, ты больше не су-шеф.', 'That is it, you are no longer sous-chef.', [], ''),
    ('lyova', 'Как вы можете так поступать со мной?', 'How can you act like this with me?', [], ''),
    ('barinov', 'Марш в подсобку.', 'March to the utility room.', [], ''),
]
WALK = [
    (0, None, ["'Lyova, do not get carried away with pancakes.' Now we can consider this part: ", ('barinov', 'увлекайся'), " ends in 'sya', for 'carry yourself away'. The pancakes take a special ending in ", ('barinov', 'блинами'), " to do the job of 'with' on its own."]),
    (1, None, ["'And what is bad about these tasty pancakes?' Now we can break down the words: ", ('lyova', 'что'), ('lyova', 'плохого'), " is a handy phrase meaning 'what is wrong with'. ", ('lyova', 'в'), ('lyova', 'этих'), " is 'in these'."]),
    (2, None, ["'Remember your last test.' Russians say 'remember about' something, so the particle ", ('barinov', 'про'), ", 'about', sits in the middle. A medical test is ", ('barinov', 'анализ'), '.']),
    (3, None, ["'My cholesterol level was almost in range.' Now let's focus on the phrase: ", ('lyova', 'в'), ('lyova', 'норме'), " is 'in the norm', which Russians use for 'normal range'. ", ('lyova', 'холестерина'), " takes an ending to say 'of'."]),
    (4, None, ["'Go to the dry cleaners and take my suit.' Let us break down the dialogue: ", ('barinov', 'химчистку'), " comes from 'chemical cleaning', which is what Russians call a dry cleaner. ", ('barinov', 'Зайди'), ' is a command to pop in.']),
    (5, None, ["'I do not have time. That is the other way.' We will focus on the speech: ", ('lyova', 'не'), ('lyova', 'успеваю'), " means 'I am not managing to be in time'. ", ('lyova', 'в'), ('lyova', 'другую'), ('lyova', 'сторону'), " is 'to another side', meaning 'the other way'."]),
    (6, None, ["'Lyova, come on, favor for a favor.' We can inspect the dialogue: ", ('barinov', 'услуга'), ('barinov', 'за'), ('barinov', 'услугу'), " means 'service for service'. Russians say it for a swap, and it uses no action word."]),
    (7, None, ["'What useful favor can there be from you?' Lyova speaks politely with his boss, so 'from you' is ", ('lyova', 'от'), ('lyova', 'вас'), '. ', ('lyova', 'полезная'), ' comes from the term for benefit, matching the form of ', ('lyova', 'услуга'), '.']),
    (8, None, ["'You get me the suit, and I allow you to be late.' The first half, ", ('barinov', 'Ты'), ('barinov', 'мне'), ('barinov', 'костюм'), ", has no action word, just 'you to me suit'. Barinov doesn't say 'bring' because both of them know what he means."]),
    (9, None, ["'Alright, I agree to these strange conditions.' We can look at the phrase: ", ('lyova', 'согласен'), ('lyova', 'на'), " means 'agreed onto'. ", ('lyova', 'условия'), ' is the usual word for the terms of a deal.']),
    (10, None, ["'That is it, you are no longer sous-chef.' Now let's inspect this line: ", ('barinov', 'больше'), ('barinov', 'не'), ", or 'more not', is how Russian says 'no longer'. ", ('barinov', 'су'), '-', ('barinov', 'шеф'), " is the French 'sous-chef', borrowed with a hyphen."]),
    (11, None, ["'How can you act like this with me?' Now we can look at this part: ", ('lyova', 'поступать'), " can mean both 'act' and 'treat'. ", ('lyova', 'Как'), ('lyova', 'вы'), ('lyova', 'можете'), " gives the polite 'how can you'."]),
    (12, None, ["'March to the utility room.' We can focus on the dialogue: ", ('barinov', 'Марш'), " is the military 'march!', borrowed whole. ", ('barinov', 'в'), ('barinov', 'подсобку'), " is 'into the back room', a word for a small storeroom."]),
]
