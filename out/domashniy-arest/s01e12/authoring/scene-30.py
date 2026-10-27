"""s01e12 scene 30: Предательство Степаныча (Stepanovich's Betrayal)."""

ID = "domashniy-arest-s01e12-scene-30"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 12
SCENE = 30
TITLE = "Предательство Степаныча  (Stepanovich's Betrayal)"
LEVEL = "beginner"
PAIR = "ru-en"
VOICES = {
    "narrator": "sky",
    "anya": "alisa",
    "viktor": "anja",
}
LABELS = {
    "anya": "Аркадий",
    "viktor": "Степаныч",
}
SOURCE_NAME = "Домашний арест, Сезон 1, Эпизод 12"
SOURCE_FILE = "sources/domashniy-arest/s01/e12.ru.dual.srt"
SOURCE_NOTE = "Cues 758-768. Viktor Stepanovich reveals to Arkady that he will not fulfill his promises."

INTRO = (
    "In a tense private meeting, influential businessman Viktor Stepanovich breaks grim news to Arkady Borisovich. "
    "Instead of helping Arkady regain political power as promised, Stepanovich coldly admits that Arkady has become "
    "a dangerous liability who knows far too much about their corrupt network."
)

STORY = [
    ("viktor", "Слышь, Аркаш, тут такое странное дело.",
     "Listen, Arkash, this is a tricky situation.",
     [(758, "Слышь, Аркаш, тут такое дело")], "adapted cue"),

    ("viktor", "Даже не знаю, с чего начать.",
     "I don't even know where to begin.",
     [(758, "прям даже не знаю, с чего начать-то")], "adapted cue"),

    ("viktor", "Не могу я тебя губернатором сделать.",
     "I cannot make you governor.",
     [(759, "Не могу я тебя губернатором сделать")], "exact cue"),

    ("viktor", "И мэром тоже не могу сделать.",
     "And I cannot make you mayor either.",
     [(760, "И мэром тоже не могу")], "adapted cue"),

    ("anya", "Это шутка такая у вас, Степаныч?",
     "Is this some kind of joke, Stepanych?",
     [(761, "Шутка такая, что ли?")], "adapted cue"),

    ("viktor", "Мне сейчас совсем не до шуток.",
     "I am in no mood for jokes right now.",
     [(762, "Мне-то не до шуток")], "adapted cue"),

    ("viktor", "Ты же у нас главный взяточник.",
     "After all, you are our main bribe-taker.",
     [(763, "Ты же у нас взяточник")], "adapted cue"),

    ("viktor", "А я теперь главный борец с коррупцией.",
     "And I am now the main fighter against corruption.",
     [(763, "а я теперь борец со взятками")], "adapted cue"),

    ("viktor", "И отпустить тебя я тоже не могу.",
     "And I cannot let you go either.",
     [(764, "И отпустить тебя, Аркаша, тоже не могу")], "adapted cue"),

    ("viktor", "Ты слишком много лишнего видел сегодня.",
     "You saw far too much today.",
     [(765, "Видел ты много сегодня")], "adapted cue"),

    ("anya", "Виктор Степанович, вы что, серьёзно говорите?",
     "Viktor Stepanovich, are you speaking seriously?",
     [(768, "Виктор Степанович, вы что, серьезно?")], "adapted cue"),

    ("viktor", "Ну что, там всё уже готово?",
     "Well, is everything ready over there?",
     [(766, "Ну что, там готово?")], "adapted cue"),

    ("viktor", "У нас нет другого выхода, Аркаша.",
     "We have no other choice, Arkasha.",
     [], "Stepanovich's cold decision"),

    ("anya", "Вы совершаете огромную ошибку, Степаныч!",
     "You are making a huge mistake, Stepanych!",
     [], "Arkady's final warning"),
]

OPENER = "Let's see how Viktor Stepanovich turns on his ally in this tense scene."

WALK = [
    (0, None,
     "'Listen, Arkash, this is a tricky situation.' Stepanovich begins the awkward betrayal conversation."),
    (1, None,
     "'I don't even know where to begin.' Viktor pretends to feel uncomfortable about his decision."),
    (2, None,
     "'I cannot make you governor.' Stepanovich shatters Arkady's highest political ambition."),
    (3, None,
     "'And I cannot make you mayor either.' The corrupt oligarch revokes all previous promises."),
    (4, None,
     "'Is this some kind of joke, Stepanych?' Arkady nervously tries to laugh off the shock."),
    (5, None,
     "'I am in no mood for jokes right now.' Stepanovich emphasizes his deadly serious tone."),
    (6, None,
     "'After all, you are our main bribe-taker.' Viktor uses Arkady's scandal as a convenient pretext."),
    (7, None,
     "'And I am now the main fighter against corruption.' A hypocritical claim from a crooked power broker."),
    (8, None,
     "'And I cannot let you go either.' Viktor signals that Arkady will not leave alive."),
    (9, None,
     "'You saw far too much today.' Revealing the true motive behind his sudden betrayal."),
    (10, None,
     "'Viktor Stepanovich, are you speaking seriously?' Panic sets in as Arkady realizes the danger."),
    (11, None,
     "'Well, is everything ready over there?' Viktor turns to his thugs to begin the execution."),
    (12, None,
     "'We have no other choice, Arkasha.' Stepanovich attempts to rationalize his ruthless act."),
    (13, None,
     "'You are making a huge mistake, Stepanych!' Arkady desperately warns his treacherous patron."),
]

TRANSITION = "Now let's listen to the chilling betrayal in the remote warehouse once more."

OUTRO = "Arkady stands stunned and betrayed as Stepanovich summons his ruthless henchmen."

CLOSING = ("anya", "Вы совершаете огромную ошибку, Степаныч!")
