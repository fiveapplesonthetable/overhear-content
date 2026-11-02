# Authoring module for kukhnya-s01e12-scene-17.
ID = 'kukhnya-s01e12-scene-17'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 12
SCENE = 17
TITLE = 'Примирение у бара  (Reconciliation by the Bar)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'kostya': 'Костя', 'nastya': 'Настя'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.12'
SOURCE_FILE = 'sources/kukhnya/s01/e12.ru.dual.srt'
INTRO = 'Kostya has had time to think, and he has gone to find Nastya at the bar to make up. Neither of them really wanted to stay cross. Hear it in Russian first.'
OPENER = 'Now slowly, so you can hear how an apology is put together.'
TRANSITION = 'Here it is once more, from the beginning.'
OUTRO = 'Kostya and Nastya forgive each other, and things are warm again. If you ever need to say sorry in Russian, you now have a few ways. Speak soon.'
CLOSING = ('kostya', 'Пока!')
STORY = [
    ('kostya', 'Настя, пожалуйста, перестань мучить меня.', 'Nastya, please stop torturing me.', [(234, 'Настя, хватит о меня мучить')], ''),
    ('nastya', 'А почему ты сердишься на меня?', 'And why are you angry with me?', [], ''),
    ('kostya', 'Мы с тобой поспорили из-за пустяка.', 'You and I argued over a trifle.', [(235, 'чтобы мы с тобой поругались')], ''),
    ('nastya', 'Для меня этот вопрос был важным.', 'For me this question was important.', [], ''),
    ('kostya', 'Ты сама хотела немного поспорить вчера.', 'You yourself wanted to argue a bit yesterday.', [(235, 'Ты же сама хотела')], ''),
    ('nastya', 'Но я не хотела такой глупой обиды.', 'But I did not want such a foolish offense.', [], ''),
    ('kostya', 'Извини меня, если я сильно обидел тебя.', 'Forgive me if I hurt you badly.', [(236, 'извини, если тебя по-настоящему обидел')], ''),
    ('nastya', 'Ты действительно сожалеешь о своих словах?', 'Do you really regret your words?', [], ''),
    ('kostya', 'Я очень искренне прошу у тебя прощения.', 'I very sincerely ask your forgiveness.', [], ''),
    ('nastya', 'Мне тоже очень тяжело злиться долго.', 'It is also very hard for me to stay angry long.', [], ''),
    ('kostya', 'Давай забудем этот спор прямо сейчас.', 'Let us forget this argument right now.', [], ''),
    ('nastya', 'Хорошо, я согласна помириться с тобой.', 'Good, I agree to make peace with you.', [], ''),
    ('kostya', 'Ты самая добрая и красивая девушка.', 'You are the kindest and most beautiful girl.', [], ''),
]
WALK = [
    (0, None, ["'Nastya, please stop torturing me.' Let's inspect this line: ", ('kostya', 'мучить'), " is a strong word, to torment, for a girlfriend who isn't talking to him. ", ('kostya', 'перестань'), ' is the order stop, and the next action follows in its basic form.']),
    (1, None, ["'And why are you angry with me?' Now we can examine the phrase: ", ('nastya', 'сердишься'), " ends in a self-action sound, so it's something like you anger yourself. ", ('nastya', 'на'), ('nastya', 'меня'), ' is at me, since Russians are angry at people, not with them.']),
    (2, None, ["'You and I argued over a trifle.' Where English says you and I, Russian says ", ('kostya', 'Мы'), ('kostya', 'с'), ('kostya', 'тобой'), ', we with you. ', ('kostya', 'из'), '-', ('kostya', 'за'), ('kostya', 'пустяка'), ' is because of a trifle, and ', ('kostya', 'поспорили'), ' is we argued.']),
    (3, None, ["'For me this question was important.' Russian says was out loud only in the past, and here it is. In the present the same sentence would drop it."]),
    (4, None, ["'You yourself wanted to argue a bit yesterday.' Now we can analyze this line: ", ('kostya', 'сама'), ('kostya', 'хотела'), ' is you yourself wanted, with endings for a woman since Kostya is talking to a woman. ', ('kostya', 'вчера'), ' is yesterday.']),
    (5, None, ["'But I did not want such a foolish offense.' Let us inspect the words: ", ('nastya', 'обиды'), ' means hurt feelings or a grievance. ', ('nastya', 'такой'), ('nastya', 'глупой'), ' is such a foolish, both with the ending that matches offense after not want. ', ('nastya', 'не'), ('nastya', 'хотела'), ' says did not want, adding the sound of a woman speaking.']),
    (6, None, ["'Forgive me if I hurt you badly.' Now we can break down the phrase: ", ('kostya', 'Извини'), ' is sorry in the friendly form. ', ('kostya', 'если'), ' means if, and ', ('kostya', 'обидел'), " means hurt, as in hurt someone's feelings."]),
    (7, None, ["'Do you really regret your words?' Now let's examine this part: ", ('nastya', 'сожалеешь'), ' means you regret and ', ('nastya', 'о'), ('nastya', 'своих'), ('nastya', 'словах'), ' is about your own words. Russian uses its own special word for your own when the owner is the subject of the sentence.']),
    (8, None, ["'I very sincerely ask your forgiveness.' Let us break down the dialogue: ", ('kostya', 'прошу'), ' is I ask, and ', ('kostya', 'прощения'), ' is forgiveness. ', ('kostya', 'у'), ('kostya', 'тебя'), ' is from you. ', ('kostya', 'искренне'), ' means sincerely.']),
    (9, None, ["'It is also very hard for me to stay angry long.' We will focus on the speech: ", ('nastya', 'тяжело'), ' is hard or heavy. ', ('nastya', 'злиться'), ' is to be angry, and ', ('nastya', 'долго'), ' is for a long time.']),
    (10, None, ["'Let us forget this argument right now.' We can inspect the phrase: ", ('kostya', 'забудем'), ' is let us forget. ', ('kostya', 'прямо'), ('kostya', 'сейчас'), ' is right now, adding emphasis.']),
    (11, None, ["'Good, I agree to make peace with you.' Let us inspect the phrase: ", ('nastya', 'согласна'), ' is I agree, matching a woman speaker. ', ('nastya', 'помириться'), ' is to make peace.']),
    (12, None, ["'You are the kindest and most beautiful girl.' We can inspect this part: ", ('kostya', 'самая'), ' adds the most to what comes next. ', ('kostya', 'добрая'), ' is kind, and ', ('kostya', 'красивая'), ' is beautiful.']),
]
