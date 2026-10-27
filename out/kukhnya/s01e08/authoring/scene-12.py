"""s01e08 scene 12: Воспоминания о Провансе (Memories of Provence)."""

ID = "kukhnya-s01e08-scene-12"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 8
SCENE = 12
TITLE = "Воспоминания о Провансе  (Memories of Provence)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "elena": "anja"}
LABELS = {"anya": "Луи", "elena": "Елена"}
SOURCE_NAME = "Кухня (Kukhnya) S1.08"
SOURCE_FILE = "sources/kukhnya/s01/e08.ru.dual.srt"

INTRO = (
    "Elena Sokolova approaches pastry station where French chef Louis is delicately assembling gourmet desserts. "
    "Recognizing his regional accent, Elena strikes a chord by reminiscing about his native home of Provence and the famous desserts in Saint-Paul-de-Vence. "
    "Let's listen to their conversation in Russian first."
)

STORY = [
    ("elena", "Луи, чем вы сейчас занимаетесь на десертах?",
     "Louis, what are you doing on the desserts right now?",
     [(129, "Луи, чем занимаетесь")], "checking on the pastry section"),
    ("anya", "Какое вам вообще дело до моих десертов?",
     "What business is it of yours regarding my desserts?",
     [(130, "Какое вам дело, чем я занимаюсь")], "bristling defensively"),
    ("elena", "У вас такой тёплый и знакомый акцент.",
     "You have such a warm and familiar accent.",
     [(131, "Какой знакомый акцент")], "complimenting his voice"),
    ("anya", "Да, я приехал сюда из самой Франции.",
     "Yes, I came here from France itself.",
     [], "stating his origin proudly"),
    ("elena", "Это же Прованс, я абсолютно права?",
     "It is Provence, am I absolutely right?",
     [(132, "Прованс? Я права")], "guessing his region"),
    ("anya", "Да, мадам, вы очень тонко угадали!",
     "Yes, madame, you guessed very subtly!",
     [(133, "Да")], "admitting she was correct"),
    ("elena", "Я просто обожаю прекрасный Сен-Поль-де-Ванс!",
     "I simply adore wonderful Saint-Paul-de-Vence!",
     [(133, "Я обожаю Прованс"), (134, "Особенно я люблю Сан-Поль-де-Ванс")], "expressing her affection for the town"),
    ("anya", "Невероятно, вся моя семья живёт именно там!",
     "Incredible, my whole family lives right there!",
     [(135, "Моя семья там живет")], "sharing his family connection"),
    ("elena", "А какие десерты подают в «Золотой голубке»!",
     "And what desserts they serve at La Colombe d'Or!",
     [(136, "А какие десерты подают золотой голубке")], "reminiscing about the famous restaurant"),
    ("anya", "О, мадам, это моё самое любимое место!",
     "Oh, madame, that is my most favorite place!",
     [(137, "О, мадам")], "gushing with enthusiasm"),
    ("elena", "Там великолепный вид и совершенно волшебная атмосфера.",
     "There is a magnificent view and completely magical atmosphere.",
     [(136, "Какой там вид")], "describing the locale"),
    ("anya", "Спасибо, я словно ненадолго вернулся домой!",
     "Thank you, I felt as if I briefly returned home!",
     [(138, "Я как будто ненадолго вернулся домой")], "thanking her emotionally"),
]

OPENER = "Let's review this heartwarming conversation about France line by line."

WALK = [
    (0, None,
     "'Louis, what are you doing on the desserts right now?' Elena checks in on the pastry chef's preparation."),
    (1, None,
     "'What business is it of yours regarding my desserts?' Louis defensively bristles at the temporary chef's intrusion."),
    (2, None,
     "'You have such a warm and familiar accent.' Elena disarms him by complimenting his regional cadence."),
    (3, None,
     "'Yes, I came here from France itself.' Louis proudly declares his French heritage."),
    (4, None,
     "'It is Provence, am I absolutely right?' Elena guesses his exact homeland with keen accuracy."),
    (5, None,
     "'Yes, madame, you guessed very subtly!' Louis is astonished by her sophisticated ear."),
    (6, None,
     "'I simply adore wonderful Saint-Paul-de-Vence!' Elena names the picturesque village in southeastern France."),
    (7, None,
     "'Incredible, my whole family lives right there!' Louis excitedly confirms that his relatives reside in the town."),
    (8, None,
     "'And what desserts they serve at La Colombe d'Or!' Elena brings up the world-famous historic hotel and restaurant."),
    (9, None,
     "'Oh, madame, that is my most favorite place!' Louis melts with nostalgic joy at the mention."),
    (10, None,
     "'There is a magnificent view and completely magical atmosphere.' Elena describes the scenic terrace overlooking the hills."),
    (11, None,
     "'Thank you, I felt as if I briefly returned home!' Louis thanks her for reviving sweet memories of his homeland."),
]

TRANSITION = "Now let's listen to the whole dialogue again at normal conversational speed."

OUTRO = (
    "Completely won over by Elena's knowledge and charm, Louis happily presents his finest pastries for the dining room. "
    "See you next time!"
)

CLOSING = ("anya", "Спасибо, я словно ненадолго вернулся домой!")
