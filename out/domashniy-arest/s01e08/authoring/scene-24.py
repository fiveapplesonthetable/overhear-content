"""s01e08 scene 24: Без поддержки семьи (Ivan's place)."""

ID = "domashniy-arest-s01e08-scene-24"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 8
SCENE = 24
TITLE = "Без поддержки семьи  (No Family Support)"
LEVEL = "beginner"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "nina": "angelina", "yulia": "anja"}
LABELS = {"anya": "Самсон", "nina": "Нина", "yulia": "Юля"}
SOURCE_NAME = "Домашний арест, Сезон 1, Эпизод 8"
SOURCE_FILE = "sources/domashniy-arest/s01/e08.ru.dual.srt"
SOURCE_NOTE = "Cues 369-422 (00:23:31-00:27:02). Ivan asks his family for support at the upcoming debate, but gets rejected."

INTRO = (
    "Previously, Arkady and young Lyosha had fun playing war games in the communal corridor. "
    "Meanwhile, at Ivan Samsonov's flat, Ivan returns home after three days away and asks his family "
    "to support him at the upcoming televised mayoral debate."
)

STORY = [
    ("anya", "Привет, семья! Я вернулся домой.",
     "Hello, family! I returned home.",
     [(374, "Привет, семья!")], "added Я вернулся домой"),
    ("nina", "Ох, живой! Надо же!",
     "Oh, alive! Well, I never!",
     [(375, "Ох ты, живой! Надо же!")], "simplified cue 375"),
    ("nina", "Тебя три дня дома не было!",
     "You were not home for three days!",
     [(401, "Тебя три дня дома не было")], ""),
    ("nina", "Я ночами совсем не спала.",
     "I did not sleep at all at night.",
     [(402, "Я ночами не спала")], "added совсем"),
    ("anya", "Я просто взял короткую паузу.",
     "I simply took a short break.",
     [(405, "Я просто взял паузу")], "added короткую"),
    ("anya", "Завтра вечером у меня дебаты.",
     "Tomorrow evening I have a debate.",
     [(392, "завтра вечером дебаты")], "added у меня"),
    ("anya", "Мне очень нужна поддержка семьи.",
     "I really need the family's support.",
     [(394, "поддержка семьи")], "added Мне очень нужна"),
    ("nina", "Как же я туда пойду?",
     "How on earth will I go there?",
     [(397, "ну как же я пойду?")], "added туда"),
    ("nina", "Я же тебя сейчас ненавижу!",
     "I hate you right now!",
     [(398, "Я ж тебя ненавижу")], "added сейчас"),
    ("anya", "Дети, а вы пойдёте со мной?",
     "Children, and will you go with me?",
     [(411, "Нет, пап, у нас не получится")], "lead-in question"),
    ("yulia", "Нет, папа, у нас экскурсия.",
     "No, Dad, we have a field trip.",
     [(412, "У нас экскурсия на курган")], "simplified cue 412"),
    ("yulia", "Все старшие классы завтра едут.",
     "All the upper grades are going tomorrow.",
     [(412, "Все старшие классы поедут")], "adapted cue 412"),
    ("anya", "Понятно. Значит, никто не поможет.",
     "I see. That means no one will help.",
     [(416, "у тебя тоже один дела")], "adapted cue 416"),
    ("nina", "Ты сам виноват в своих бедах.",
     "You yourself are to blame for your troubles.",
     [(418, "Хотя поступил ты")], "cleaned moral line"),
]

OPENER = "Let's see how Ivan's plea for family loyalty falls completely flat."

WALK = [
    (0, None,
     "'Hello, family! I returned home.' Ivan tries to greet everyone cheerfully after disappearing."),
    (1, None,
     "'Oh, alive! Well, I never!' Nina's sarcastic exclamation greets his unexpected return."),
    (2, None,
     "'You were not home for three days!' The genitive case follows the negative past construction."),
    (3, None,
     "'I did not sleep at all at night.' The instrumental plural expresses the time when something happened."),
    (4, None,
     "'I simply took a short break.' Ivan offers a weak excuse for his long drinking binge."),
    (5, None,
     "'Tomorrow evening I have a debate.' The adverbial phrase establishes the upcoming event."),
    (6, None,
     "'I really need the family's support.' The short adjective expresses necessity in the dative construction."),
    (7, None,
     "'How on earth will I go there?' The emphatic particle conveys Nina's strong reluctance."),
    (8, None,
     "'I hate you right now!' Nina bluntly refuses to stand by his side in public."),
    (9, None,
     "'Children, and will you go with me?' Ivan turns to his offspring hoping for loyalty."),
    (10, None,
     "'No, Dad, we have a field trip.' Yulia immediately provides an excuse to decline."),
    (11, None,
     "'All the upper grades are going tomorrow.' The present tense verb describes scheduled future motion."),
    (12, None,
     "'I see. That means no one will help.' Ivan accepts the harsh reality that he is entirely alone."),
    (13, None,
     "'You yourself are to blame for your troubles.' Nina delivers the final stinging rebuke."),
]

TRANSITION = "Now listen to Ivan's awkward conversation with his family once more."
OUTRO = "Abandoned by his wife and children, Ivan is left to face the political debates on his own."
CLOSING = ("anya", "Мне очень нужна поддержка семьи.")
