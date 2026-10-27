# -*- coding: utf-8 -*-
"""Scene 29 of domashniy-arest s01e10: Samsonov's Good Mood."""

ID = "domashniy-arest-s01e10-scene-29"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 10
SCENE = 29
TITLE = "Хорошее настроение Самсона  (Samsonov's Good Mood)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.10"
SOURCE_FILE = "sources/domashniy-arest/s01/e10.ru.dual.srt"

VOICES = {
    "narrator": "sky",
    "anya": "alisa",
    "nina": "anja",
}

LABELS = {
    "anya": "Самсон",
    "nina": "Нина",
}

INTRO = (
    "Ivan Samsonov returns home to the communal flat whistling cheerfully, believing that his "
    "marital troubles are finally behind them. Nina, however, looks sour and unimpressed by his "
    "carefree attitude, suspecting he spent a great night out while she was left exhausted. "
    "Listen to their Russian conversation first, and do not worry about catching every word."
)

OPENER = "Let's examine line by line how Samsonov has a tense domestic reunion."

STORY = [
    ("anya", "Привет, дорогая жена!",
     "Hello, dear wife!",
     [(901, "Привет, жена")], ""),
    ("anya", "Ну что, наш вопрос закрыт?",
     "Well then, is our issue closed?",
     [(902, "Ну что"), (904, "Вопрос закрыт")], ""),
    ("nina", "А ты чего такой довольный?",
     "And why are you so pleased?",
     [(906, "А ты чего довольный такой")], ""),
    ("nina", "Ходишь тут и песни поёшь!",
     "You walk around here and sing songs!",
     [(906, "Песенки поешь")], ""),
    ("anya", "Я рад, что у нас всё в порядке.",
     "I am glad that everything is in order with us.",
     [(907, "я рад, что у нас все в порядке")], ""),
    ("nina", "Ты думаешь, у нас всё в порядке?",
     "You think everything is fine with us?",
     [(908, "У нас все в порядке")], ""),
    ("anya", "А почему ты такая грустная?",
     "And why are you so gloomy?",
     [(910, "А ты чего смурная такая")], ""),
    ("nina", "Я вчера очень сильно устала.",
     "I got very tired yesterday.",
     [(915, "Я с Даней мучилась")], "simplified from crude colloquial phrasing"),
    ("anya", "Поверь мне, я тоже устал.",
     "Believe me, I got tired too.",
     [(918, "Я тоже мучился")], ""),
    ("nina", "По твоему лицу этого не видно!",
     "From your face, this is not visible!",
     [(919, "По тебе видно")], "ironic negation"),
    ("anya", "Давай не будем снова ссориться.",
     "Let us not quarrel again.",
     [], "Samsonov tries to keep the peace"),
    ("nina", "Дети, мойте руки и идите есть!",
     "Children, wash your hands and come eat!",
     [(922, "Дети, идите есть")], ""),
]

WALK = [
    (0, None,
     "'Hello, dear wife!' Samsonov uses an affectionate address to set a cheerful mood."),
    (1, None,
     "'Well then, is our issue closed?' The short passive participle denotes a resolved topic."),
    (2, None,
     "'And why are you so pleased?' The interrogative pronoun is used colloquially for why."),
    (3, None,
     "'You walk around here and sing songs!' The present tense verbs describe irritating actions."),
    (4, None,
     "'I am glad that everything is in order with us.' The short adjective expresses gladness."),
    (5, None,
     "'You think everything is fine with us?' Nina counters with an ironic rhetorical question."),
    (6, None,
     "'And why are you so gloomy?' The feminine adjective describes a visibly sullen mood."),
    (7, None,
     "'I got very tired yesterday.' The adverb of degree reinforces intense physical fatigue."),
    (8, None,
     "'Believe me, I got tired too.' An imperative formula asking for sincere credibility."),
    (9, None,
     "'From your face, this is not visible!' The predicative adverb notes an obvious contrast."),
    (10, None,
     "'Let us not quarrel again.' A polite cohortative construction seeking domestic truce."),
    (11, None,
     "'Children, wash your hands and come eat!' Nina calls her kids into the communal kitchen."),
]

TRANSITION = "Now listen to Samsonov and Nina's domestic exchange once again."

OUTRO = (
    "Samsonov fails to lift Nina's dark mood, sensing that unspoken tensions remain between them. "
    "In the next scene, the kindergarten craft competition results are announced."
)

CLOSING = ("nina", "Дети, мойте руки и идите есть!")
