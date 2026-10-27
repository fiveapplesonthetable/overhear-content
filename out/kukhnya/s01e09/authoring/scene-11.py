"""s01e09 scene 11: Игра в Рататуя (Playing Ratatouille)."""

ID = "kukhnya-s01e09-scene-11"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 9
SCENE = 11
TITLE = "Игра в Рататуя  (Playing Ratatouille)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "nastya": "anja", "alisa": "angelina"}
LABELS = {"anya": "Макс", "nastya": "Настя", "alisa": "Алиса"}
SOURCE_NAME = "Кухня (Kukhnya) S1.09"
SOURCE_FILE = "sources/kukhnya/s01/e09.ru.dual.srt"
SOURCE_NOTE = "Cues 245-263. Max and little Alisa play Ratatouille in the kitchen while the staff frantically searches for her."

INTRO = (
    "Tucked away in a quiet corner of Claude Monet's kitchen, Max and young Alisa play a lively cooking game inspired by the movie Ratatouille. "
    "While the pair happily decorate their culinary creation with chocolate, waitress Nastya runs around the restaurant in a total panic searching for the girl. "
    "Let's listen to their playful kitchen adventure in Russian."
)

STORY = [
    ("anya", "Остался самый последний штрих.", "Only the very last touch remains.",
     [(245, "Остался последний штрих")], ""),
    ("alisa", "Смотри, я сама это приготовила!", "Look, I made this myself!",
     [(248, "И я это приготовил!")], ""),
    ("anya", "Это я управляю тобой, как в мультике!", "It is I who control you, like in the cartoon!",
     [(249, "Не ты, а я управляю тобой!"), (250, "Как в мультике «Рататуйя»!")], ""),
    ("alisa", "То есть ты хитрая маленькая крыса?", "So you are a clever little rat?",
     [(251, "То есть ты крыса? Уи!")], ""),
    ("anya", "Художники всегда подписывают свой шедевр.", "Artists always sign their masterpiece.",
     [(253, "Что делают художники, когда заканчивают свой шедевр?"), (255, "Ну, ставят автограф!")], ""),
    ("anya", "Куда пропал наш жидкий шоколад?", "Where has our liquid chocolate gone?",
     [(256, "Где мой жидкий шоколад?")], ""),
    ("alisa", "Ты сам его только что съел!", "You ate it yourself just now!",
     [(257, "Ты сожрал?"), (258, "Не я, а ты")], ""),
    ("anya", "Неправда, я оставил его для украшения.", "Not true, I left it for decoration.",
     [], ""),
    ("nastya", "Макс, ты не видел маленькую Алису?", "Max, have you not seen little Alisa?",
     [(262, "Настя, что там у вас?"), (263, "Алисы нигде нет")], ""),
    ("anya", "Она сидит здесь и помогает мне.", "She is sitting here helping me.",
     [], ""),
    ("nastya", "Шеф уже ищет её по всему ресторану!", "The chef is already looking for her all over the restaurant!",
     [(259, "ее нигде нет"), (261, "Ищи!")], ""),
    ("alisa", "Мы готовим самое вкусное блюдо на свете!", "We are cooking the most delicious dish in the world!",
     [], ""),
    ("nastya", "Беги скорее к папе, пока он добрый.", "Run to dad quickly, while he is kind.",
     [], ""),
]

OPENER = "Let's explore how Max and Alisa cook together in the kitchen while avoiding Chef Barinov's search."

WALK = [
    (2, None,
     "'It is I who control you, like in the cartoon!' An emphatic pronoun construction with an instrumental comparative simile in the sentence."),
    (4, None,
     "'Artists always sign their masterpiece.' The general statement uses a present tense verb and an accusative object for the idea."),
    (6, None,
     "'You ate it yourself just now!' The child playfully accuses the cook using an emphatic pronoun and a past tense verb."),
    (10, None,
     "'The chef is already looking for her all over the restaurant!' An urgent present tense statement with a prepositional locative phrase for the listener."),
]

TRANSITION = "Now, let's listen to Max and Alisa's playful kitchen dialogue once more."

OUTRO = (
    "Now you know how to talk about childhood games, cooking creative dishes, and managing frantic workplace searches in Russian. "
    "Listen for these expressive phrases in the next scene."
)

CLOSING = ("anya", "Дети умеют превратить работу в праздник.")
