# -*- coding: utf-8 -*-
"""Scene 21 of domashniy-arest s01e07: Cooking Porridge in Casts."""

ID = "domashniy-arest-s01e07-scene-21"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 7
SCENE = 21
TITLE = "Как вы кашу будете варить?  (How Are You Going to Cook Porridge?)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.07"
SOURCE_FILE = "sources/domashniy-arest/s01/e07.ru.dual.srt"

VOICES = {
    "narrator": "sky",
    "anya": "alisa",
    "marina": "angelina",
    "dean": "anja",
}

LABELS = {
    "anya": "Аркадий",
    "marina": "Марина",
    "dean": "Эдуард Владимирович",
}

INTRO = (
    "Last time, after Arkady interrupted Marina and Eduard's breakfast and went to make "
    "porridge, Samsonov mocked Danya's tiny city car in the courtyard before setting off "
    "for the snowy forest. Now in the communal kitchen, Marina and Eduard walk in to find "
    "Arkady dumping dry rice and milk everywhere with his two plaster casts. Listen to the "
    "Russian first, and do not worry about catching every word."
)

OPENER = "Let's step into the kitchen and unpack each line."

STORY = [
    ("marina", "Боже! Что вы тут делаете?",
     "Good lord! What are you doing here?",
     [(801, "Боже"), (802, "Что вы"), (802, "делаете")], ""),
    ("marina", "Как вы кашу готовить будете? Дайте сюда!",
     "How are you going to cook porridge? Give it here!",
     [(803, "Как вы кашу"), (803, "будете"), (804, "Дайте сюда")], "ASR 'к этому' -> 'готовить'"),
    ("dean", "Что это такое? Это просто кошмар!",
     "What is this? This is simply a nightmare!",
     [(805, "Что это такое"), (811, "Кошмар")], ""),
    ("marina", "Аркадий Борисович, дайте пакет сюда.",
     "Arkady Borisovich, give the packet here.",
     [(806, "Дайте сюда")], ""),
    ("anya", "Я не могу. И рис в глаза попал!",
     "I cannot. And rice got into my eyes!",
     [(807, "Я не могу"), (808, "в глаза попал")], "ASR 'Ирис' restored to 'И рис'"),
    ("anya", "Простите, я сейчас приберу. Я всё сам приберу!",
     "Forgive me, I will clean up now. I will clean everything up myself!",
     [(809, "Простите, я приберу"), (810, "Я все приберу")], ""),
    ("dean", "Подожди, Марина. Оставь это всё в покое.",
     "Wait, Marina. Leave all of this alone.",
     [(812, "Подожди, Марина"), (813, "Оставь это все в покое")], ""),
    ("dean", "Сейчас нужно вызвать социальную службу. Они всё сделают.",
     "Right now we need to call social services. They will do everything.",
     [(814, "Сейчас нужно вызвать социальную службу"), (815, "Они все сделают")], ""),
    ("marina", "Что вы опять делаете? Осторожно, там молоко!",
     "What are you doing again? Careful, there is milk there!",
     [(816, "Что вы делаете"), (821, "Осторожно")], ""),
    ("anya", "Ой, я падаю! Помогите мне!",
     "Oh, I am falling! Help me!",
     [], "new A1 line for cue 818 as Arkady slips on the spilled milk and rice"),
    ("dean", "Смотри, не трогай его! Его сейчас нельзя трогать.",
     "Look, do not touch him! One must not touch him right now.",
     [(817, "Смотри"), (819, "Его нельзя трогать")], "ASR 'если слова поддаваете' dropped"),
    ("anya", "Не трогайте меня так! Поднимите меня скорее!",
     "Do not touch me like that! Help me up quickly!",
     [(820, "Не трогайте меня, поднимите меня скорее")], ""),
    ("marina", "Держитесь, Аркадий Борисович! Осторожно!",
     "Hold on, Arkady Borisovich! Careful!",
     [(821, "Осторожно")], ""),
]

WALK = [
    (0, "Боже!",
     "'Good lord!' Marina gasps as she sees the state of the communal kitchen."),
    (0, "Что вы тут делаете?",
     "'What are you doing here?' Rice and milk are scattered all over the stove and floor."),
    (1, "Как вы кашу готовить будете?",
     "'How are you going to cook porridge?' Both of Arkady's arms are encased in heavy plaster casts."),
    (1, "Дайте сюда!",
     "'Give it here!' Marina tries to take the packet from him."),
    (2, "Что это такое?",
     "'What is this?' Eduard stares in disbelief at the mess."),
    (2, "Это просто кошмар!",
     "'This is simply a nightmare!' The noun for 'nightmare' is a very common everyday exclamation."),
    (3, None,
     "'Arkady Borisovich, give the packet here.' Marina reaches for the spilled groats."),
    (4, "Я не могу.",
     "'I can't.' Arkady tries to wipe his face with his plaster cast."),
    (4, "И рис в глаза попал!",
     "'And rice got into my eyes!' Literally 'fell into the eyes'."),
    (5, "Простите, я сейчас приберу.",
     "'Forgive me, I will tidy up right now.' The perfective verb means 'to clean up' or 'tidy away'."),
    (5, "Я всё сам приберу!",
     "'I will clean everything up myself!' He tries to bend down with his stiff casts."),
    (6, "Подожди, Марина.",
     "'Wait, Marina.' Eduard holds Marina back from cleaning the floor for Arkady."),
    (6, "Оставь это всё в покое.",
     "'Leave all of this in peace.' That is the standard Russian idiom for 'leave it alone'."),
    (7, "Сейчас нужно вызвать социальную службу.",
     "'Right now one needs to call social services.' Eduard wants the city welfare office to deal with him."),
    (7, "Они всё сделают.",
     "'They will do everything.' Meanwhile Arkady takes a step on the wet floor."),
    (8, "Что вы опять делаете?",
     "'What are you doing again?' Marina sees his feet sliding."),
    (8, "Осторожно, там молоко!",
     "'Careful, there is milk there!' Milk and dry rice cover the linoleum."),
    (9, "Ой, я падаю!",
     "'Oh, I am falling!' Arkady's feet fly out from under him and he crashes onto his back."),
    (9, "Помогите мне!",
     "'Help me!' With both arms in plaster, he cannot push himself up."),
    (10, "Смотри, не трогай его!",
     "'Look, don't touch him!' Eduard warns Marina as she rushes over."),
    (10, "Его сейчас нельзя трогать.",
     "'One must not touch him right now.' Notice how the impersonal word for 'not allowed' takes an infinitive."),
    (11, "Не трогайте меня так!",
     "'Do not touch me like that!' Arkady winces on the kitchen floor."),
    (11, "Поднимите меня скорее!",
     "'Lift me up quickly!' The comparative adverb means 'more quickly' or 'right away'."),
    (12, None,
     "'Hold on, Arkady Borisovich! Careful!' Together they struggle to get the mayor back on his feet."),
]

TRANSITION = "Let's hear the whole kitchen disaster once more."

OUTRO = (
    "While Marina and Eduard haul Arkady off the milk-soaked floor, Samsonov and his "
    "family are heading out to the snowy forest for their winter barbecue. We will join "
    "them in the next scene."
)

CLOSING = ("anya", "Поднимите меня скорее!")
