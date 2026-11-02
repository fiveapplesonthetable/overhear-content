# Authoring module for kukhnya-s01e04-scene-16.
ID = 'kukhnya-s01e04-scene-16'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 4
SCENE = 16
TITLE = "Просьба друга  (A Friend's Request)"
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'kostya': 'Костя', 'max': 'Макс'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.04'
SOURCE_FILE = 'sources/kukhnya/s01/e04.ru.dual.srt'
INTRO = "Behind the bar, Kostya is gloomy: his attempt to charm Nastya went badly. Max teases him a little, and then Kostya asks Max to talk to her on his behalf. Max, who thinks he is a born diplomat, agrees. Here's the Russian first."
OPENER = "Let's go back to the bar."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = ["Max promises to be gentle, which is not what he's known for. A nice phrase to remember is ", ('max', 'минут семь'), ", where putting the number after the Russian expression for minutes means \"about\"."]
CLOSING = ('max', 'Пока!')
STORY = [
    ('max', 'Я понял, свидания у тебя не будет?', "I take it you won't have a date?", [(211, 'свидания у тебя не будет')], ''),
    ('kostya', 'Да, я опять сказал полную глупость.', 'Yes, I said something completely stupid again.', [], ''),
    ('max', 'Ты слишком сильно нервничаешь перед ней.', 'You get way too nervous around her.', [], ''),
    ('kostya', 'Не получается у меня красиво говорить!', 'I cannot manage to speak beautifully!', [(213, 'Не получается у меня красиво')], ''),
    ('max', 'Этому нужно долго и терпеливо учиться.', 'One needs to learn this long and patiently.', [], ''),
    ('kostya', 'Слушай, а может ты с ней поговоришь?', 'Listen, maybe you could talk with her?', [(215, 'может ты с ней')], ''),
    ('max', 'Что именно я должен ей сказать?', 'What exactly am I supposed to tell her?', [], ''),
    ('kostya', 'Объясни, что она мне очень нравится.', 'Explain that I really like her.', [], ''),
    ('max', 'Ладно, я попробую поговорить с Настей.', 'Okay, I will try to talk with Nastya.', [(216, 'Ладно')], ''),
    ('kostya', 'Спасибо, друг, ты меня очень выручишь!', 'Thank you, friend, you will really help me out!', [], ''),
    ('max', 'У меня как раз минут семь есть.', 'I have about seven minutes right now.', [(217, 'минут семь есть')], ''),
    ('kostya', 'Только скажи всё максимально нежно.', 'Just say everything as gently as possible.', [], ''),
    ('max', 'Не волнуйся, я прирождённый дипломат!', 'Do not worry, I am a natural diplomat!', [], ''),
]
WALK = [
    (0, None, ["'I take it you won't have a date?' The phrase for 'I understood', ", ('max', 'Я понял,'), ", opens the line as 'I take it'. Literally, ", ('max', 'у тебя не будет?'), " translates to 'at you there won't be', and the term for 'date', ", ('max', 'свидания'), ", changes its ending because it is not happening."]),
    (1, None, ["'Yes, I said something completely stupid again.' The Russian literally translates to saying a stupidity, as in the word ", ('kostya', 'глупость.'), ". The describing word for 'complete', ", ('kostya', 'полную'), ", changes its ending to show it's the target of the action."]),
    (2, None, ["'You get way too nervous around her.' The expression for 'too' is ", ('max', 'слишком'), ". The action word ", ('max', 'нервничаешь'), " is built from the expression for nerves, and the phrase ", ('max', 'перед ней.'), " literally translates to 'in front of her'."]),
    (3, None, ["'I cannot manage to speak beautifully!' Russians often skip 'I can't' and say ", ('kostya', 'Не получается у меня'), ". This literally translates to 'it doesn't work out at me', as if the speech itself were failing. The describing word ", ('kostya', 'красиво'), " is built from the Russian term for beautiful."]),
    (4, None, ["'One needs to learn this long and patiently.' The expression for patiently, ", ('max', 'терпеливо'), ", is built from the action word for 'to endure'. The term for 'learn', ", ('max', 'учиться.'), ", takes 'to' for the subject being learned, so 'this' changes its ending to match."]),
    (5, None, ["'Listen, maybe you could talk with her?' It's familiar from the first word, as ", ('kostya', 'Слушай,'), " translates to the informal 'listen'. In the action word ", ('kostya', 'поговоришь?'), ", the prefix makes it one short talk, and the ending translates to 'you will'."]),
    (6, None, ["'What exactly am I supposed to tell her?' The translation for 'must' when spoken by a man is ", ('max', 'должен'), ". And the Russian expression for \'to her\', as in ", (\'max\', \'ей сказать?\'), ", literally translates to \'to her to tell\'."]),
    (7, None, ["'Explain that I really like her.' The Russian expression for 'explain' is ", ('kostya', 'Объясни,'), ". In the phrase ", ('kostya', 'она мне очень нравится.'), ", she literally does the pleasing and the speaker receives it."]),
    (8, None, ["'Okay, I will try to talk with Nastya.' After the little word for \'with\', as in ", (\'max\', \'с Настей.\'), ", the name Nastya changes its ending."]),
    (9, None, ["'Thank you, friend, you will really help me out!' The word ", ('kostya', 'выручишь!'), " translates to 'you will get me out of a jam', which is much warmer than the standard word for 'you will help'."]),
    (10, None, ["'I have about seven minutes right now.' Putting the number after the naming word makes it a rough guess: ", ('max', 'минут семь'), " translates to 'about seven', whereas putting the number first means exactly seven."]),
    (11, None, ["'Just say everything as gently as possible.' The word ", ('kostya', 'максимально'), " translates to 'maximally'. The Russian term for 'gently', ", ('kostya', 'нежно.'), ", is built from the describing word for 'tender'."]),
    (12, None, ["'Do not worry, I am a natural diplomat!' The Russian term for 'natural', ", ('max', 'прирождённый'), ", is built from the Russian expression for 'born', meaning 'born to it'. The word ", ('max', 'дипломат!'), " was borrowed into Russian unchanged."]),
]
