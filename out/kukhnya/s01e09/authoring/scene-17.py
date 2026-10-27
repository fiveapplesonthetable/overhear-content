"""s01e09 scene 17: Где Алиса? (Where Is Alisa?)."""

ID = "kukhnya-s01e09-scene-17"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 9
SCENE = 17
TITLE = "Где Алиса?  (Where Is Alisa?)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {
    "narrator": "sky",
    "anya": "alisa",
    "chef": "anja",
}
LABELS = {
    "anya": "Таня",
    "chef": "Шеф",
}
SOURCE_NAME = "Кухня (Kukhnya) S1.09"
SOURCE_FILE = "sources/kukhnya/s01/e09.ru.dual.srt"

INTRO = (
    "In the dining room of Claude Monet, Chef Barinov's ex-wife Tanya arrives to pick up their young daughter Alisa. "
    "Barinov scrambles to make up excuses to keep Tanya from discovering that Alisa had an allergic reaction under his care. "
    "Listen to their conversation in Russian first, then we will break down each line in English."
)

STORY = [
    ("anya", "Виктор, добрый вечер. Где Алиса?",
     "Viktor, good evening. Where is Alisa?",
     [(314, "Где Алиса?")], "asking for daughter"),
    ("chef", "А мы с ней решили остаться.",
     "And she and I decided to stay.",
     [(314, "А мы с ней решили, что она еще со мной на денек останется.")], "lying about decision"),
    ("chef", "Она побудет со мной ещё денёк.",
     "She will stay with me one more day.",
     [(314, "на денек останется.")], "stalling for time"),
    ("chef", "Ты же не возражаешь, Таня?",
     "You do not mind, Tanya?",
     [(315, "Ты же не возражаешь.")], "seeking consent"),
    ("anya", "Ну, если она сама так решила.",
     "Well, if she decided so herself.",
     [(316, "Ну, если она так решила сама.")], "tentative acceptance"),
    ("anya", "Пойдём, я быстро с ней попрощаюсь.",
     "Let us go, I will quickly say goodbye to her.",
     [(317, "Ладно, пойдем, я с ней попрощаюсь.")], "wanting to see her"),
    ("chef", "Зачем? Я сам всё передам!",
     "What for? I will pass on everything myself!",
     [(317, "Ну, зачем?"), (318, "Я передам.")], "blocking exit"),
    ("chef", "Она там на кухне развлекается.",
     "She is having fun there in the kitchen.",
     [(318, "Она там на кухне развлекается.")], "deflecting concern"),
    ("chef", "Она просила передать тебе пока.",
     "She asked me to say goodbye to you.",
     [(319, "Кстати, она просила передать тебе пока.")], "fabricating message"),
    ("anya", "Так, что с ней случилось?",
     "Wait, what happened to her?",
     [(320, "Что с ней случилось?")], "growing suspicious"),
    ("chef", "Всё нормально, она просто играет.",
     "Everything is fine, she is just playing.",
     [(320, "Все нормально."), (321, "На кухне играется.")], "denying trouble"),
    ("anya", "А врать ты так и не научился.",
     "And you still have not learned how to lie.",
     [(322, "А вот врать ты до сих пор не научился.")], "seeing through lie"),
    ("chef", "Таня, подожди, я всё объясню!",
     "Tanya, wait, I will explain everything!",
     [], "desperate pleading"),
]

OPENER = "Let us practice the key lines together."

WALK = [
    (0, "Виктор, добрый вечер. Где Алиса?",
     "'Viktor, good evening. Where is Alisa?' — a polite greeting followed by an interrogative adverb."),
    (1, "А мы с ней решили остаться.",
     "'And she and I decided to stay.' — plural pronoun construction expressing shared action."),
    (2, "Она побудет со мной ещё денёк.",
     "'She will stay with me one more day.' — future perfective verb with a diminutive time noun."),
    (3, "Ты же не возражаешь, Таня?",
     "'You do not mind, Tanya?' — negative present verb in a conversational tag question."),
    (4, "Ну, если она сама так решила.",
     "'Well, if she decided so herself.' — conditional clause with the emphatic reflexive pronoun."),
    (5, "Пойдём, я быстро с ней попрощаюсь.",
     "'Let us go, I will quickly say goodbye to her.' — hortative imperative followed by a future perfective verb."),
    (6, "Зачем? Я сам всё передам!",
     "'What for? I will pass on everything myself!' — emphatic pronoun followed by a future transitive verb."),
    (7, "Она там на кухне развлекается.",
     "'She is having fun there in the kitchen.' — 3rd person singular reflexive verb of amusement."),
    (8, "Она просила передать тебе пока.",
     "'She asked me to say goodbye to you.' — reporting an informal farewell message."),
    (9, "Так, что с ней случилось?",
     "'Wait, what happened to her?' — an abrupt change of tone expressing suspicion."),
    (10, "Всё нормально, она просто играет.",
     "'Everything is fine, she is just playing.' — short reassurance followed by a continuous present action."),
    (11, "А врать ты так и не научился.",
     "'And you still have not learned how to lie.' — past negative verb describing a persistent shortcoming."),
]

TRANSITION = "Now listen to the full conversation once more."
OUTRO = "Great job! Keep practicing these lively dialogues with us to master everyday Russian."
CLOSING = ("chef", "Таня, подожди, я всё объясню!")
