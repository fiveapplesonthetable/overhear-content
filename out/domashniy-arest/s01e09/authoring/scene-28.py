# domashniy-arest/s01e09/scene-28.py
ID = "domashniy-arest-s01e09-scene-28"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 9
SCENE = 28
TITLE = "В аквапарк за счёт ФСБ  (To the Water Park on the FSB)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.09"
SOURCE_FILE = "sources/domashniy-arest/s01/e09.ru.dual.srt"
VOICES = {"narrator": "sky", "commander": "angelina", "agent": "anja"}
LABELS = {"commander": "Командир", "agent": "Сотрудник"}
INTRO = "Back in the town, special operations officers launch a sudden raid on a suspicious daycare facility. The commander decides to clear the premises by treating the bewildered children to a trip to the water park, before breaking down the heavy internal doors. Let's listen to their brief exchange in Russian first; don't worry about catching every word."
STORY = [
    ("agent", "Товарищ командир, здание полностью окружено.", "Comrade commander, the building is completely surrounded.", [], "added operational opening"),
    ("commander", "Отлично. Быстро заходим внутрь.", "Excellent. We go inside quickly.", [], "added commander order"),
    ("agent", "Здесь в коридоре маленькие дети!", "Here in the corridor are small children!", [], "added children sighting"),
    ("commander", "Так, детей сразу в автобус!", "Right, put the children into the bus immediately!", [(751, 'Так, детей в автобус')], "adapted cue 751"),
    ("commander", "Отвезите их в аквапарк.", "Take them to the water park.", [(751, 'в аквапарк')], "adapted cue 751"),
    ("commander", "Всё за счёт ФСБ!", "Everything is on the FSB!", [(751, 'за счет ФСБ')], "verbatim cue 751 with yo"),
    ("agent", "У них же плавочек нет!", "But they do not have swimsuits!", [(752, 'У них же плавочек нет')], "verbatim cue 752"),
    ("commander", "Ничего страшного.", "No big deal.", [(753, 'Ничего страшного')], "verbatim cue 753"),
    ("commander", "На берегу спокойно посидят.", "They will sit quietly on the shore.", [(753, 'на берегу посидят')], "adapted cue 753"),
    ("agent", "Понял. Я посажу их в автобус.", "Understood. I will put them into the bus.", [(754, 'Так')], "expanded cue 754"),
    ("agent", "А что делать с этой дверью?", "And what should we do with this door?", [], "added breach question"),
    ("commander", "Ну-ка, дай кувалду!", "Come on, hand me the sledgehammer!", [(755, 'Ну-ка, дай кувалду')], "verbatim cue 755"),
    ("commander", "Мы сейчас откроем этот вход.", "We will open this entrance right now.", [], "added breach command"),
]
OPENER = "Let us walk through this intense and humorous scene together, step by step, to understand each phrase."
WALK = [
    (0, None, "'Comrade commander, the building is completely surrounded.' The subordinate reports the perimeter status clearly."),
    (1, None, "'Excellent. We go inside quickly.' The commander gives the order to storm the premises without delay."),
    (2, None, "'Here in the corridor are small children!' The Russian word for children is an irregular plural form."),
    (3, None, "'Right, put the children into the bus immediately!' The preposition for 'into' takes the direct-object form here."),
    (4, None, "'Take them to the water park.' The command form command here is the polite plural form of the prefixed motion verb."),
    (5, None, "'Everything is on the FSB!' The fixed Russian expression means at the expense of a specified person or agency."),
    (6, None, "'But they do not have swimsuits!' The word for swim trunks appears here in the plural 'of' form after negation."),
    (7, None, "'No big deal.' This very common Russian conversational idiom literally translates to nothing of frightening."),
    (8, None, "'They will sit quietly on the shore.' The preposition takes a special location noun ending in this landscape expression."),
    (9, None, "'Understood. I will put them into the bus.' The verb form expresses first-person singular future intention."),
    (10, None, "'And what should we do with this door?' The preposition 'with' requires the feminine 'with/as' form."),
    (11, None, "'Come on, hand me the sledgehammer!' The conversational particle prompts quick and decisive physical action."),
    (12, None, "'We will open this entrance right now.' The verb form expresses first-person plural future action."),
]
TRANSITION = "Now let us listen to the complete exchange once more, paying attention to the decisive military orders."
OUTRO = "The children are happily dispatched to the water park, while the officers prepare to enter the inner facility. Well done following this rapid tactical dialogue in Russian. See you next time!"
CLOSING = ("commander", "Пока!")
