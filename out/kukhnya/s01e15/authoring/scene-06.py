# Authoring module for kukhnya-s01e15-scene-06.
ID = 'kukhnya-s01e15-scene-06'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 15
SCENE = 6
TITLE = 'Трудный разговор  (A Difficult Conversation)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'max': 'Макс', 'vika': 'Вика'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.15'
SOURCE_FILE = 'sources/kukhnya/s01/e15.ru.dual.srt'
INTRO = "Still in Vika's flat, Max answers her question. He would like to move in, he says, but there is Kostya and the rent to think about. Vika isn't convinced. Hear it in Russian first."
OPENER = 'Their conversation, slowly.'
TRANSITION = 'Here is the conversation again.'
OUTRO = "Max promises to talk to Kostya today. Vika has heard excuses before, and she'll want to know how that talk goes. Speak soon."
CLOSING = ('vika', 'Пока!')
STORY = [
    ('max', 'Понимаешь, я не могу к тебе переехать.', 'You see, I cannot move in with you.', [(32, 'Понимаешь, я не могу к тебе переехать.')], ''),
    ('vika', 'Почему ты не хочешь жить со мной?', 'Why do you not want to live with me?', [], ''),
    ('max', 'Мы с Костей вместе за квартиру платим.', 'Kostya and I pay for the flat together.', [(33, 'Мы с Костей вместе за квартиру платим.')], ''),
    ('vika', 'Это просто глупая отговорка.', 'That is just a silly excuse.', [], ''),
    ('max', 'Один он её не потянет.', 'He cannot afford it on his own.', [(34, 'Один он ее не потянет.')], ''),
    ('vika', 'Макс, если ты не хочешь жить со мной, так и скажи.', 'Max, if you do not want to live with me, just say so.', [(35, 'Макс, если ты не хочешь жить со мной, так и скажи.')], ''),
    ('max', 'Да я хочу. Это Костя не хочет.', 'I do want to. It is Kostya who does not want to.', [(36, 'Да я хочу. Это Костян не хочет.')], 'adapted: Костя for the slangy Костян'),
    ('vika', 'Тогда поговори с ним сегодня.', 'Then talk to him today.', [], ''),
    ('max', 'Я его понимаю. Но я с ним поговорю.', 'I understand him. But I will talk to him.', [(37, 'Я его понимаю. Но я с ним поговорю обязательно.')], 'adapted: обязательно dropped'),
    ('vika', 'Ты обещаешь?', 'Do you promise?', [], ''),
    ('max', 'Обещаю.', 'I promise.', [(38, 'Обещаю.')], ''),
]
WALK = [
    (0, None, "'You see, I cannot move in with you.' 'Ponimaesh', literally 'you understand', is a softener, like 'you see'. 'K tebe' is 'to you', and with a verb of moving it means 'to your place'."),
    (1, None, "'Why do you not want to live with me?' 'So mnoy' is 'with me': 's' becomes 'so' in front of 'mnoy', which is easier to say. 'Zhit', to live, follows 'khochesh' in its basic form."),
    (2, None, "'Kostya and I pay for the flat together.' Russian says 'my s Kostey', 'we with Kostya', for 'Kostya and I'. After 'za', pay for, 'kvartira' becomes 'kvartiru'."),
    (3, None, "'That is just a silly excuse.' 'Otgovorka' comes from 'otgovorit', to talk your way out of something. It's feminine, so 'silly' is 'glupaya'."),
    (4, None, "'He cannot afford it on his own.' 'Ne potyanet' is literally 'won't pull', everyday Russian for 'can't manage' or 'can't afford'. 'Odin', alone, comes first for weight."),
    (5, None, "'Max, if you do not want to live with me, just say so.' 'Tak i skazhi' is literally 'so and say', a set way to say 'then just say it'. 'Esli' is 'if'."),
    (6, None, "'I do want to. It is Kostya who does not want to.' The 'da' here isn't 'yes'; it pushes back, like 'but I do'. 'Eto Kostya ne khochet' points the finger: 'it's Kostya who doesn't'."),
    (7, None, "'Then talk to him today.' 'Pogovori' is the order form of 'pogovorit', to have a talk. 'S nim' is 'with him', and 'on' turns into 'nim' after 's'."),
    (8, None, "'I understand him. But I will talk to him.' 'Ego' is 'him' as the thing understood. 'Pogovoryu' is a single word for 'I will have a talk': the 'po' form has no present, so it points ahead."),
    (9, None, "'Do you promise?' No word order change, no helper word: in Russian a statement becomes a question just by rising at the end."),
    (10, None, "'I promise.' 'Obeshchayu' is one word, and its ending already means 'I', so nobody says the 'ya'."),
]
