# Authoring module for kukhnya-s02e01-scene-07.
ID = 'kukhnya-s02e01-scene-07'
SHOW = 'kukhnya'
SEASON = 2
EPISODE = 1
SCENE = 7
TITLE = 'Серьёзный разговор  (A Serious Conversation)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'max': 'Макс', 'vika': 'Вика'}
SOURCE_NAME = 'Кухня (Kukhnya) S2.01'
SOURCE_FILE = 'sources/kukhnya/s02/e01.ru.dual.srt'
INTRO = 'In the dining room of Claude Monet, Max tries to apologize to Victoria for his awful mistake. Victoria refuses to listen to him, so Max decides to take drastic action to make her stay and talk.'
OPENER = 'Listen to Max begging Victoria for a chance to explain himself.'
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = "Max is determined to make Victoria listen, even if his impulsive plan only makes her angrier. Next time you watch the episode, listen for the Russian expressions for 'to wait' and 'minute' — you will catch every word right away. See you next time!"
CLOSING = ('max', 'Пока!')
STORY = [
    ('max', 'Вика, подожди меня одну минуту!', 'Vika, wait for me for one minute!', [(135, 'Вик, нам нужно поговорить')], ''),
    ('max', 'Нам очень нужно серьёзно поговорить.', 'We really need to talk seriously.', [(135, 'нам нужно поговорить')], ''),
    ('vika', 'У меня сейчас много работы в зале.', 'I have a lot of work in the hall right now.', [(135, 'Мне не о чем с тобой разговаривать')], ''),
    ('vika', 'И мне не о чем с тобой говорить.', 'And I have nothing to talk to you about.', [(135, 'Мне не о чем с тобой разговаривать')], ''),
    ('max', 'Пожалуйста, выслушай меня хотя бы раз!', 'Please listen to me at least once!', [(135, 'нам нужно поговорить')], ''),
    ('vika', 'Я уже всё видела своими глазами.', 'I already saw everything with my own eyes.', [(135, 'с тобой разговаривать')], ''),
    ('max', 'Это была ужасная и глупая ошибка.', 'It was a terrible and foolish mistake.', [(136, 'А я думаю, есть о чем')], ''),
    ('vika', 'Оставь меня в покое, Максим.', 'Leave me alone, Maxim.', [(135, 'Мне не о чем')], ''),
    ('max', 'Нет, я так просто не уйду!', 'No, I will not leave so easily!', [(136, 'А я думаю')], ''),
    ('max', 'А я думаю, нам надо поговорить, Вика.', 'And I think we need to talk, Vika.', [(136, 'А я думаю, есть о чем, Вик')], ''),
    ('vika', 'Что ты делаешь у двери?', 'What are you doing by the door?', [(136, 'есть о чем, Вик')], ''),
    ('max', 'Теперь ты точно меня спокойно выслушаешь.', 'Now you will definitely listen to me calmly.', [(136, 'А я думаю, есть о чем')], ''),
    ('vika', 'Открой эту дверь прямо сейчас!', 'Open this door right now!', [(135, 'с тобой разговаривать')], ''),
]
WALK = [
    (0, None, "'Vika, wait for me for one minute!' Max hurries after Vika and asks her to wait for just a minute."),
    (1, None, "'We really need to talk seriously.' The impersonal construction with the matching word ending word expresses strong necessity."),
    (2, None, "'I have a lot of work in the hall right now.' Victoria uses her duties as a reason not to speak with him."),
    (3, None, "'And I have nothing to talk to you about.' Victoria makes it clear she does not want to hear his excuses."),
    (4, None, "'Please listen to me at least once!' He begs her to let him explain himself at least once."),
    (5, None, "'I already saw everything with my own eyes.' Vika retorts that she already saw everything with her own eyes."),
    (6, None, "'It was a terrible and foolish mistake.' Max admits that what he did was completely wrong."),
    (7, None, "'Leave me alone, Maxim.' She tells Maxim to leave her in peace."),
    (8, None, "'No, I will not leave so easily!' Max refuses to give up and walk away so easily."),
    (9, None, "'And I think we need to talk, Vika.' Max insists that their relationship is worth discussing."),
    (10, None, "'What are you doing by the door?' Vika notices him tampering with the door and demands to know what he is doing."),
    (11, None, "'Now you will definitely listen to me calmly.' Max believes he can force her to hear him out."),
    (12, None, "'Open this door right now!' Victoria angrily orders him to step aside. Now listen to the confrontation in the hall again."),
]
