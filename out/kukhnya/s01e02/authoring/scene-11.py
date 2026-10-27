"""s01e02 scene 11: Визит к столу (A Visit to the Table)."""

ID = "kukhnya-s01e02-scene-11"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 2
SCENE = 11
TITLE = "Визит к столу  (A Visit to the Table)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "elena": "anja", "ainura": "angelina"}
LABELS = {"anya": "Шеф", "elena": "Елена", "ainura": "Айнура"}
SOURCE_NAME = "Кухня (Kukhnya) S1.02"
SOURCE_FILE = "sources/kukhnya/s01/e02.ru.dual.srt"
SOURCE_NOTE = "Cues 149-168. Chef Barinov meets Elena Sokolova in the dining room after she eats the fricassee."

INTRO = (
    "Summoned from his back office by cleaner Ainura, Chef Viktor Barinov walks into the dining room to meet Elena Sokolova. "
    "Elena, the head chef of the competing restaurant Arcobaleno, delivers a surprisingly positive verdict on the fricassee, "
    "though she makes sure to criticize the agonizingly long wait. Let's listen to their encounter in Russian first."
)

STORY = [
    ("ainura", "Шеф! Шеф! Вас зовут в зал!",
     "Chef! Chef! You are being called to the dining hall!",
     [(149, "Шеф! Шеф!")], "delivering the message to Barinov's office"),
    ("anya", "Что ещё? Кто меня там ждёт?",
     "What else? Who is waiting for me there?",
     [(150, "Что еще")], "asking grumpily"),
    ("ainura", "Та симпатичная дама из соседнего ресторана.",
     "That pretty lady from the neighboring restaurant.",
     [(150, "симпатичная"), (150, "соседнего ресторана")], "identifying Elena"),
    ("anya", "Чем я могу быть полезен?",
     "How can I be of service?",
     [(155, "Чем могу быть полезен")], "greeting Elena formally"),
    ("elena", "Я только что попробовала ваше фрикасе.",
     "I have just tasted your fricassee.",
     [(156, "Попробовала ваше фрикассе")], "starting her review"),
    ("anya", "Ну, и как вам наше блюдо?",
     "Well, and how did you like our dish?",
     [(157, "Ну, и как вам")], "probing for reaction"),
    ("elena", "Вы знаете, оно мне очень понравилось.",
     "You know, I liked it very much.",
     [(159, "оно мне понравилось")], "giving surprising compliment"),
    ("anya", "Да? Это мой старый фирменный рецепт.",
     "Really? This is my old signature recipe.",
     [(160, "Хороший рецепт")], "taking unearned credit"),
    ("anya", "Куропатка оставалась, а выбрасывать было жалко.",
     "Partridge was left over, and it was a shame to throw it out.",
     [(161, "Куропатка оставалась, а выбрасывать жалко")], "bragging nonchalantly"),
    ("elena", "Понятно. Приятно уйти от вас живой.",
     "Understood. It is pleasant to leave your place alive.",
     [(162, "поняла"), (164, "уйти от вас в добром здравии")], "delivering a sarcastic jab"),
    ("anya", "Как? Вы уже уходите из ресторана?",
     "What? Are you already leaving the restaurant?",
     [(165, "Как? Уже уходите")], "acting surprised"),
    ("elena", "Ваше блюдо от шефа готовилось слишком долго.",
     "Your chef's special took far too long to prepare.",
     [(167, "Ваше блюдо от шефа очень долго готовилось")], "complaining about the long delay"),
    ("elena", "До свидания, шеф-повар.",
     "Goodbye, head chef.",
     [(168, "До свидания")], "taking her leave"),
]

OPENER = "Let's replay a few lines to examine key phrases and vocabulary."

WALK = [
    (3, "Чем я могу быть полезен?",
     "'How can I be of service?' Viktor asks courteously as he approaches Elena's table."),
    (6, "Вы знаете, оно мне очень понравилось.",
     "'You know, I liked it very much,' Elena admits graciously, praising the improvised meal."),
    (8, "Куропатка оставалась, а выбрасывать было жалко.",
     "'Partridge was left over, and it was a shame to throw it out,' Barinov brags casually."),
    (11, "Ваше блюдо от шефа готовилось слишком долго.",
     "'Your chef's special took far too long to prepare,' Elena remarks pointedly before leaving."),
]

TRANSITION = "Now listen to the full dining room dialogue once more."

OUTRO = "Elena walks out of the restaurant, leaving Barinov puzzled by the mixed compliments."

CLOSING = ("anya", "Она просто завидует нашему успеху.")
