# Authoring module for domashniy-arest-s01e05-scene-21.
ID = 'domashniy-arest-s01e05-scene-21'
SHOW = 'domashniy-arest'
SEASON = 1
EPISODE = 5
SCENE = 21
TITLE = 'Два документа  (Two Documents)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'andryusha': 'Андрюша', 'gennady': 'Геннадий Андреевич', 'ilona': 'Илона'}
SOURCE_NAME = 'Домашний арест (Domashniy Arest) S1.05'
SOURCE_FILE = 'sources/domashniy-arest/s01/e05.ru.dual.srt'
INTRO = "Back at the Society of the Blind a few minutes later. Armed with the documents that Arkady helped her find in City Hall's archives, Ilona marches past Andryusha into chairman Gennady Andreyevich's office to prove who really stole the money for their new building. We'll hear it in Russian first; don't worry about catching every word."
OPENER = "Let's go through the scene line by line. First, Andryusha tries to block Ilona at the office door."
TRANSITION = "Now let's hear the whole scene once more, from start to finish."
OUTRO = "So Ilona has proved that Osipenko stole the money for the blind society's building, yet Gennady Andreyevich is too cynical to back Samson against the likely winner. Well done following that argument in Russian. See you next time!"
CLOSING = ('gennady', 'Пока!')
STORY = [
    ('andryusha', 'Я же вам объяснил, что он занят.', "I already explained to you that he's busy.", [(810, 'Я же вам объяснил, что он занят')], ''),
    ('ilona', 'У меня есть важная информация про ваше здание.', 'I have important information about your building.', [(811, 'у меня есть важная информация'), (811, 'здания')], "'по поводу вашего здания' -> 'про ваше здание' to keep sentence <= 8 words"),
    ('ilona', 'Его строительство задерживал не Аникеев, а Осипенко!', "It wasn't Anikeev who held up its construction, it was Osipenko!", [(812, 'Его строительство задерживал не Аникеев, а Осипенко')], ''),
    ('ilona', 'А вот приказ о строительстве вашего нового здания.', 'And here is the construction order for your new building.', [(813, 'А вот приказ о строительстве вашего нового здания')], ''),
    ('ilona', 'Его подписал Аникеев полтора года назад. — И что?', 'Anikeev signed it a year and a half ago. — So what?', [(814, 'полтора года назад'), (815, 'И что')], "ASR 'Подписанные Аникейовым' turned into active A1 clause 'Его подписал Аникеев'"),
    ('ilona', 'А это значит, что деньги были выделены.', 'And that means the money was allocated.', [(816, 'А это значит, что деньги были выделены')], ''),
    ('ilona', 'Но они, к сожалению, не дошли до вас.', 'But unfortunately, it never reached you.', [(818, 'но, к сожалению, не дошли до')], "'до адресата' -> 'до вас'"),
    ('ilona', 'А вот другой документ. Пожалуйста, посмотрите.', 'And here is another document. Please take a look.', [(819, 'А вот другой документ. Пожалуйста, посмотрите')], ''),
    ('gennady', 'Я слепой. — Да, конечно, простите! Я зачитаю.', "I'm blind. — Yes, of course, forgive me! I'll read it aloud.", [(821, 'Я слепой'), (822, 'Да, конечно, простите. Я зачитаю')], ''),
    ('ilona', 'Это договор на покупку строительного оборудования.', 'This is a contract for the purchase of construction equipment.', [(823, 'договор на покупку строительного оборудования')], 'shortened from cue 823-824'),
    ('ilona', 'А это компания брата Осипенко!', "And that is Osipenko's cousin's company!", [(825, 'это компания'), (825, 'брата Осипенко')], "'СМУ №2, между прочим' and 'троюродного' dropped for A1"),
    ('ilona', 'Вы понимаете, что Осипенко ваши деньги просто забрал?', 'Do you understand that Osipenko simply took your money?', [(827, 'Вы понимаете, что Осипенко ваши деньги просто')], "'крутит' -> 'забрал'"),
    ('gennady', 'Андрюша, посмотри, пожалуйста. — Пожалуйста.', 'Andryusha, take a look, please. — Here you go.', [(828, 'Андрюша, посмотри, пожалуйста'), (829, 'Пожалуйста')], ''),
    ('ilona', 'Он что, не слепой? — Он слабовидящий.', "Wait, he's not blind? — He has low vision.", [(830, 'Он что, не слепой'), (831, 'Он слабовидящий')], ''),
    ('gennady', 'Вы никогда не выиграете! Ваш кандидат слабый.', 'You will never win! Your candidate is weak.', [(833, 'Вы никогда не выиграете'), (834, 'Ваш кандидат')], "'придурок' -> 'слабый'"),
    ('gennady', 'А я испорчу отношения с будущим мэром.', "And I'll ruin my relationship with the future mayor.", [(835, 'А я испорчу отношения с будущим мэром')], ''),
    ('gennady', 'Да все вы одинаковые! Разговор окончен, идите!', "You're all the same! The conversation is over, leave!", [(840, 'Да все вы одинаковые'), (841, 'Разговор окончен'), (842, 'Идите')], ''),
]
WALK = [
    (0, None, "'I already explained to you that he's busy.' Notice the emphatic little word right after 'I': 'I already told you'. Ilona steps right past him."),
    (1, None, "'I have important information about your building.' Literally, 'at me there is important information about your building'."),
    (2, None, "'It wasn't Anikeev who held up its construction, it was Osipenko!' Notice the contrast construction 'not X, but Y'."),
    (3, None, "'And here is the construction order for your new building.' After the word for 'order', the little word 'about' takes the location form."),
    (4, None, "'Anikeev signed it a year and a half ago. — So what?' Russian has a single word for 'one and a half', which here takes the 'of'-form singular of 'year'."),
    (5, None, "'And that means the money was allocated.' Because 'money' is plural in Russian, the passive verbal describing word 'allocated' is plural too."),
    (6, None, "'But unfortunately, it never reached you.' Literally, 'they did not walk as far as you'."),
    (7, None, "'And here is another document. Please take a look.' In her haste, Ilona holds the sheet out toward the blind chairman."),
    (8, None, "'I'm blind. — Yes, of course, forgive me! I'll read it aloud.' The prefix on the action word 'to read' means 'to read out to an audience'."),
    (9, None, "'This is a contract for the purchase of construction equipment.' The contract is for the exact same amount of money that City Hall allocated."),
    (10, None, "'And that is Osipenko's cousin's company!' The money went straight from City Hall into Osipenko's family firm."),
    (11, None, "'Do you understand that Osipenko simply took your money?' At this point, Gennady Andreyevich pauses and calls his assistant over."),
    (12, None, "'Andryusha, take a look, please. — Here you go.' Meanwhile, Andryusha peers closely through his thick glasses and nods that the signatures and stamps are genuine."),
    (13, None, "'Wait, he's not blind? — He has low vision.' The compound describing word literally means 'weak-seeing'. Yet even after seeing the proof, the chairman shakes his head."),
    (14, None, "'You will never win! Your candidate is weak.' Notice the double negative in Russian: 'you never will not win'."),
    (15, None, "'And I'll ruin my relationship with the future mayor.' He knows Osipenko is a thief, but expects Osipenko to win the election anyway."),
    (16, None, "'You're all the same! The conversation is over, leave!' He points his white cane toward the door."),
]
