# domashniy-arest/s01e06/scene-04.py
ID = "domashniy-arest-s01e06-scene-04"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 6
SCENE = 4
TITLE = "Выборы должны пройти честно!  (The Election Must Be Honest!)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.06"
SOURCE_FILE = "sources/domashniy-arest/s01/e06.ru.dual.srt"
VOICES = {"narrator": "sky", "irina": "angelina", "pasha": "anja"}
LABELS = {"irina": "Ирина Петровна", "pasha": "Паша"}
INTRO = "Still in the restaurant after Yulya hurries off to fetch cinnamon for Pasha's cappuccino, acting mayor Pavel Osipenko turns to the election commission chairwoman Irina Petrovna to reassure the nervous local businessmen that Samsonov will be disqualified. Instead, Irina Petrovna delivers a shock from Moscow that sends Pasha's blood pressure soaring. Let's listen to the Russian scene first; don't worry about catching every word."
STORY = [
    ("pasha", "Ирина Петровна, скажите, пожалуйста. Кандидат Самсонов подал подписи с нарушениями, ведь да?", "Irina Petrovna, tell me, please. Candidate Samsonov submitted his signatures with violations, isn't that right?", [(97, 'Ирина Петровна'), (97, 'скажите, пожалуйста'), (98, 'кандидат'), (98, 'подписи'), (98, 'нарушений, ведь да')], "fixed ASR 'кандидат Самсонова в подписи подался' -> 'Кандидат Самсонов подал подписи с нарушениями'"),
    ("irina", "Ведь нет. Подписи собраны и все оформлены верно.", "Actually, no. The signatures are collected and all properly filed.", [(99, 'Ведь нет. Подписи собраны'), (99, 'и все оформлены верно')], "dropped 'предостаточно' for A1"),
    ("pasha", "Подождите, мы же с вами предполагали другое! Там будет множество нарушений.", "Wait, we speculated otherwise together! There would be many violations.", [(100, 'Подождите, мы же с вами предполагали'), (101, 'будет'), (101, 'множество'), (101, 'нарушений')], "split into two short sentences"),
    ("irina", "Предполагали и предполагали.", "We speculated, sure.", [(102, 'Предполагали и предполагали')], ""),
    ("pasha", "Ты же позавчера здесь сидела! Ты коньяк французский пила со мной!", "You were sitting right here the day before yesterday! You were drinking French cognac with me!", [(103, 'Ты же позавчера здесь сидела'), (103, 'французский пила'), (104, 'со мной')], "split into two sentences; 'коньячок' -> 'коньяк'"),
    ("irina", "А вчера мне позвонили из Москвы.", "And yesterday they called me from Moscow.", [(106, 'А вчера мне позвонили из')], "simplified 'из центра избиркома' -> 'из Москвы'"),
    ("irina", "Мне сказали, что выборы должны пройти честно. Честно и прозрачно!", "They told me that the election must be conducted honestly. Honestly and transparently!", [(107, 'сказали, что выборы'), (108, 'должны пройти'), (109, 'честно и прозрачно')], "split into two short sentences"),
    ("irina", "И предупредили очень строго!", "And they warned me very strictly!", [(110, 'И предупредили очень строго')], ""),
    ("pasha", "Это очень интересно. А почему?", "That's very interesting. And why?", [(114, 'Это очень интересно'), (115, 'А почему')], ""),
    ("irina", "Потому что к выборам особое внимание. Самсонов — звезда!", "Because there is special attention on the election. Samsonov is a star!", [(116, 'потому что к выборам'), (117, 'особое внимание'), (118, 'Самсонов звезда')], ""),
    ("irina", "И народ интересуется его судьбой.", "And the people are interested in his fate.", [(119, 'И народ интересуется его судьбой')], ""),
    ("pasha", "Никогда Самсонов не победит! Никогда!", "Samsonov will never win! Never!", [(120, 'Никогда Самсонов не победит'), (121, 'Никогда')], ""),
    ("irina", "Пожалуйста, ваш капучино с корицей.", "Here you go, your cappuccino with cinnamon.", [(128, 'Пожалуйста, с корицей')], "added 'ваш капучино'"),
    ("pasha", "Ну сколько можно каждые три минуты? Туда-сюда, туда-сюда!", "How long can you keep coming every three minutes? Back and forth, back and forth!", [(130, 'Ну сколько можно'), (130, 'каждые три минуты'), (131, 'Туда-сюда, туда-сюда')], ""),
    ("pasha", "Дай поговорить, наконец!", "Let me talk, finally!", [(132, 'Дай поговорить')], "simplified 'в конце концов' -> 'наконец'"),
]
OPENER = "Now let's walk through the scene line by line and see how Moscow's call ruins Pasha's plan."
WALK = [
    (0, 'Ирина Петровна, скажите, пожалуйста.', "Pasha smiles confidently across the table at the election commission chairwoman: 'Irina Petrovna, tell me, please.'"),
    (0, 'Кандидат Самсонов подал подписи с нарушениями, ведь да?', "He prompts her for the answer they agreed on: 'Candidate Samsonov submitted signatures with violations, right?'"),
    (1, 'Ведь нет.', "She calmly contradicts him at the table: 'Actually, no.'"),
    (1, 'Подписи собраны и все оформлены верно.', "'The signatures are collected and all properly filed.' The adverb meaning 'properly' modifies the verb for 'are collected' to sharpen the tone."),
    (2, 'Подождите, мы же с вами предполагали другое!', "Pasha blinks in shock: 'Wait, you and I speculated something else!'"),
    (2, 'Там будет множество нарушений.', "'There would be many violations.' Listen for the word meaning 'there', which leads straight into 'of violations'."),
    (3, None, "Irina Petrovna shrugs: 'We speculated and we speculated' — talk is just talk."),
    (4, 'Ты же позавчера здесь сидела!', "Dropping his polite tone, Pasha switches to the informal 'you': 'You were sitting here the day before yesterday!'"),
    (4, 'Ты коньяк французский пила со мной!', "'You were drinking French cognac with me!' The '-a' ending on the past-tense verb for 'were drinking' shows that the subject is feminine."),
    (5, None, "Irina Petrovna explains what changed: 'And yesterday they called me from Moscow, from the central election commission.'"),
    (6, 'Мне сказали, что выборы должны пройти честно.', "'They told me that the election must be conducted honestly.' In spoken Russian, word order is flexible: 'told' comes first to set the focus, followed by 'honestly'."),
    (6, 'Честно и прозрачно!', "'Honestly and transparently!' Russian leaves out 'am', 'is', or 'are' in the present tense, linking 'honestly' straight to 'transparently'."),
    (7, None, "And she adds firmly: 'And they warned me very strictly not to play any tricks!'"),
    (8, 'Это очень интересно.', "Pasha tries to keep his composure: 'That is very interesting.'"),
    (8, 'А почему?', "'And why?' is Moscow suddenly watching their small town?"),
    (9, 'Потому что к выборам особое внимание.', "'Because there is special attention on the election' from the capital."),
    (9, 'Самсонов — звезда!', "After his viral videos, 'Samsonov is a star!'"),
    (10, None, "'And the people are interested in his fate.' Irina Petrovna puts 'the people' up front and finishes with 'fate' to make the point unmistakable."),
    (11, 'Никогда Самсонов не победит!', "Pasha slams his hand on the table: 'Samsonov will never win!'"),
    (11, 'Никогда!', "'Never!' Yet the businessmen around the table immediately tell Pasha they are backing out until his victory is guaranteed."),
    (12, None, "At that worst possible moment, teenage waitress Yulya approaches the table: here you go, your cappuccino with cinnamon."),
    (13, 'Ну сколько можно каждые три минуты?', "Boiling with frustration, Pasha snaps at the girl: how long can you keep hovering every three minutes?"),
    (13, 'Туда-сюда, туда-сюда!', "Back and forth, back and forth!"),
    (14, None, "He yells at her to leave them alone: let me talk, finally!"),
]
TRANSITION = "Now listen to the entire restaurant conversation again from start to finish."
OUTRO = "While Yulya walks away muttering that Pasha is a real villain and Pasha collapses with a blood-pressure spike, Yulya heads off to her second part-time job at the local meatpacking plant. See you next time!"
CLOSING = ("irina", "Пока!")
