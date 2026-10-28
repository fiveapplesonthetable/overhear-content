# domashniy-arest/s01e09/scene-09.py
ID = "domashniy-arest-s01e09-scene-09"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 9
SCENE = 9
TITLE = "Три папки  (Three Folders)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.09"
SOURCE_FILE = "sources/domashniy-arest/s01/e09.ru.dual.srt"
VOICES = {"narrator": "sky", "governor": "angelina", "pasha": "anja"}
LABELS = {"governor": "Губернатор", "pasha": "Паша"}
INTRO = "Back in Sineozersk, Pavel Osipenko arrives at the office of Governor Viktor Stepanovich to deliver an illicit bribe. Hoping to secure the governor's help against Samsonov, Osipenko hands over a bag full of cash. Cautious about surveillance, the experienced governor insists the bribe is merely three folders of official paperwork. Let's listen to their tense exchange in Russian first."
STORY = [
    ("pasha", "Здравствуйте, Виктор Степанович.", "Hello, Viktor Stepanovich.", [], "polite greeting"),
    ("governor", "Что это такое, Павел Юрьевич?", "What is this, Pavel Yuryevich?", [(269, 'Что это такое')], ""),
    ("pasha", "Это деньги.", "This is money.", [(270, 'Деньги')], ""),
    ("governor", "Какие ещё деньги?", "What money are you talking about?", [(271, 'Какие деньги')], ""),
    ("pasha", "Те самые, о которых говорили.", "The very money we talked about.", [(272, 'Те, о которых мы с вами говорили')], ""),
    ("governor", "По-моему, вы сильно ошибаетесь.", "In my opinion, you are sorely mistaken.", [(274, 'По-моему, вы ошибаетесь')], ""),
    ("governor", "Вы должны были привезти документы.", "You were supposed to bring documents.", [(275, 'Вы должны были привезти документы мне')], ""),
    ("governor", "Вы привезли документы?", "Did you bring the documents?", [(276, 'Привезли')], ""),
    ("pasha", "Да, конечно. Три бабки.", "Yes, of course. Three grand.", [(277, 'Привез'), (278, 'Конечно, да'), (279, 'Три бабки')], ""),
    ("governor", "Прекрасно! Оставьте эти три папки.", "Excellent! Leave these three folders.", [(280, 'Прекрасно. Оставьте три папки')], ""),
    ("governor", "Я посмотрю их позже.", "I will examine them later.", [(280, 'я их позже посмотрю')], ""),
    ("pasha", "Теперь всё в порядке?", "Is everything in order now?", [(281, 'теперь все в порядке, да')], ""),
    ("pasha", "Вы поможете разобраться с Самсоновым?", "Will you help deal with Samsonov?", [(283, 'Ну, вы же мне теперь поможете разобраться с Самсоновым')], ""),
    ("governor", "У нас всё в порядке. Всего доброго!", "Everything is in order with us. Goodbye!", [(282, 'У нас и было все в порядке. Всего доброго')], ""),
]
OPENER = "Now let's examine the covert bribe delivery line by line. Osipenko and the governor speak in careful bureaucratic code."
WALK = [
    (0, None, "'Hello, Viktor Stepanovich.' Osipenko enters the governor's office politely."),
    (1, None, "'What is this, Pavel Yuryevich?' The governor feigns surprise using polite address."),
    (2, None, "'This is money.' Osipenko bluntly names the contents of the bag."),
    (3, None, "'What money are you talking about?' The governor immediately questions the phrasing for legal safety."),
    (4, None, "'The very money we talked about.' Osipenko refers back to their previous private agreement."),
    (5, None, "'In my opinion, you are sorely mistaken.' The parenthetical word introduces a formal polite denial."),
    (6, None, "'You were supposed to bring documents.' The modal construction describes expected official paperwork."),
    (7, None, "'Did you bring the documents?' The past tense verb checks whether the paperwork arrived."),
    (8, None, "'Yes, of course. Three grand.' Osipenko uses slang that sounds phonetically like folders."),
    (9, None, "'Excellent! Leave these three folders.' The governor humorously plays along with the phonetic pun."),
    (10, None, "'I will examine them later.' The future-tense form promises future attention."),
    (11, None, "'Is everything in order now?' Osipenko seeks assurance about their political alliance."),
    (12, None, "'Will you help deal with Samsonov?' Osipenko asks for political retaliation against his rival."),
    (13, None, "'Everything is in order with us. Goodbye!' The governor closes the conversation and politely dismisses him."),
]
TRANSITION = "Now let's listen to Osipenko and the governor's coded meeting once more without pauses."
OUTRO = "The governor cleverly accepts the bribe disguised as official folders while promising nothing in return. See you next time!"
CLOSING = ("governor", "Пока!")
