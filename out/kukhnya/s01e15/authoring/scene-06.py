# Authoring module for kukhnya-s01e15-scene-06.
ID = 'kukhnya-s01e15-scene-06'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 15
SCENE = 6
TITLE = 'Трудный разговор  (A Difficult Conversation)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'kostya': 'Костя', 'max': 'Макс'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.15'
SOURCE_FILE = 'sources/kukhnya/s01/e15.ru.dual.srt'
INTRO = "At work, Kostya hears that Max is going to Nastya's. He has a problem with this, and he tries to explain it to Max. Hear it in Russian first."
OPENER = 'Their conversation, slowly.'
TRANSITION = 'Here is the conversation again.'
OUTRO = 'Kostya promises to talk to the one person who can solve it. He avoids saying the real reason. See you next time.'
CLOSING = ('kostya', 'Пока!')
STORY = [
    ('kostya', 'Ну ты куда?', 'Where are you going?', [(31, 'Ну ты куда?')], ''),
    ('max', 'Я иду к Насте.', 'I am going to Nastya.', [], ''),
    ('kostya', 'Понимаешь, я не могу переехать к ней.', 'You see, I cannot move in with her.', [], ''),
    ('max', 'Почему ты не хочешь жить с ней?', 'Why do you not want to live with her?', [], ''),
    ('kostya', 'Мы с Максом вместе за квартиру платим.', 'Max and I split the rent together.', [], ''),
    ('max', 'Это очень глупая и плохая отговорка.', 'This is a very stupid and bad excuse.', [], ''),
    ('kostya', 'Один он ее не потянет.', 'He cannot afford it on his own.', [], ''),
    ('max', 'Если ты не хочешь жить со мной, скажи.', 'If you do not want to live with me, say so.', [], ''),
    ('kostya', 'Да я хочу. Это Макс не хочет.', 'I do want to. Max does not want to.', [], ''),
    ('max', 'Она тебе не поверит.', 'She will not believe you.', [], ''),
    ('kostya', 'Я его понимаю. Но я с ним поговорю.', 'I understand him. But I will talk to him.', [], ''),
    ('max', 'Тебе нужно сделать это сегодня.', 'You need to do this today.', [], ''),
    ('kostya', 'Обещаю.', 'I promise.', [], ''),
]
WALK = [
    (0, None, "'Where are you going?' It's the same short question again, 'you where'. Russian does without the verb for movement."),
    (1, None, "'I am going to Nastya.' 'K Naste' means 'to Nastya', and her name loses an 'a' for an 'e'. The little 'k' means 'towards'."),
    (2, None, "'You see, I cannot move in with her.' 'You understand' works as a filler, like 'you see'. 'To her' is 'k ney', where 'ona' turns into 'ney'."),
    (3, None, "'Why do you not want to live with her?' 'With her' has the same 'ney' shape. 'To live' follows 'you want' directly."),
    (4, None, "'Max and I split the rent together.' Russians say 'we with Max' for 'Max and I'. 'Za kvartiru' is 'for the flat', which is the right way to say what you pay for."),
    (5, None, "'This is a very stupid and bad excuse.' 'Otgovorka' is an excuse, and the word has a slightly dismissive flavour. Both 'glupaya' and 'plokhaya' end in 'aya', matching the feminine noun."),
    (6, None, "'He cannot afford it on his own.' 'Ne potyanet' is literally 'won't pull', slang for 'won't be able to afford'. 'Odin on' is 'he alone'."),
    (7, None, "'If you do not want to live with me, say so.' The order 'say!' is the end of a sentence that begins with 'if'. Max is exasperated."),
    (8, None, "'I do want to. Max does not want to.' 'Da ya khochu' has a 'da' that doesn't mean 'yes'; it pushes the point. 'Eto Maks ne khochet' puts the blame on Max."),
    (9, None, "'She will not believe you.' In Russian you believe 'to' someone, so 'you' appears as 'tebe'. 'Ne poverit' is the future, 'won't believe'."),
    (10, None, "'I understand him. But I will talk to him.' After 'with', 'him' gets an 'n', so it's 'nim'. 'Pogovoryu' squeezes 'I will have a talk' into one word."),
    (11, None, "'You need to do this today.' 'Tebe nuzhno' is 'to you it's needed', and it works for friendly pressure. 'Segodnya' is 'today'."),
    (12, None, "'I promise.' One word, 'obeshchayu', and it ends the scene. Russians say it on its own with no 'I'."),
]
