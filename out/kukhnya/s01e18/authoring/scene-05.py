ID = "kukhnya-s01e18-scene-05"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 18
SCENE = 5
TITLE = "Заказ у стойки  (Order at the Bar)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "max": "anja"}
LABELS = {"anya": "Костя", "max": "Макс"}
SOURCE_NAME = "Кухня (Kukhnya) S1.18"
SOURCE_FILE = "sources/kukhnya/s01/e18.ru.dual.srt"
SOURCE_NOTE = (
    "Cue 133. At the bar in Claude Monet, Kostya serves a customer a drink "
    "and discusses customer service and drinks with Max."
)

INTRO = (
    "At the bar of restaurant Claude Monet, Kostya serves a customer a beverage with polite service. "
    "Max stops by the bar to chat about working with customers and serving drinks. "
    "Let us listen to their conversation in Russian first."
)

STORY = [
    ("anya", "Пожалуйста, вот ваш вкусный напиток.",
     "Here you go, here is your delicious drink.",
     [(133, "Пожалуйста.")], "adapted"),
    ("max", "Костя, ты отлично работаешь за этой стойкой.",
     "Kostya, you work excellently behind this bar.",
     [], "new"),
    ("anya", "Спасибо, я стараюсь быть очень вежливым.",
     "Thank you, I try to be very polite.",
     [], "new"),
    ("max", "Гости всегда любят свежие и вкусные напитки.",
     "Guests always love fresh and delicious drinks.",
     [], "new"),
    ("anya", "Наш бар предлагает самые лучшие дорогие напитки.",
     "Our bar offers the very best expensive drinks.",
     [], "new"),
    ("max", "Люди в зале готовы платить любые деньги.",
     "People in the dining room are ready to pay any money.",
     [], "new"),
    ("anya", "Главное — всегда честно делать свою работу.",
     "The main thing is always to do your work honestly.",
     [], "new"),
    ("max", "Но некоторые бармены знают хитрые секреты.",
     "However, some barmen know clever secrets.",
     [], "new"),
    ("anya", "Я не хочу обманывать наших гостей.",
     "I do not want to deceive our guests.",
     [], "new"),
    ("max", "Ты просто слишком честный и добрый парень.",
     "You are simply too honest and kind a guy.",
     [], "new"),
    ("anya", "Зато моя совесть абсолютно чиста сегодня.",
     "On the other hand, my conscience is absolutely clean today.",
     [], "new"),
    ("max", "Ладно, продолжай наливать сок и вино.",
     "All right, keep pouring juice and wine.",
     [], "new"),
    ("anya", "Я с радостью налью гостям сок!",
     "I will gladly pour juice for the guests!",
     [], "new"),
]

OPENER = "Now let us examine Kostya and Max's conversation at the bar line by line."

WALK = [
    (0, None,
     "'Here you go, here is your delicious drink.' -- Kostya hands over a freshly prepared beverage to a diner."),
    (1, None,
     "'Kostya, you work excellently behind this bar.' -- Max compliments his friend on his attentive bartending."),
    (2, None,
     "'Thank you, I try to be very polite.' -- The modest barman explains his dedication to good hospitality."),
    (3, None,
     "'Guests always love fresh and delicious drinks.' -- Max notes that satisfied customers appreciate quality."),
    (4, None,
     "'Our bar offers the very best expensive drinks.' -- Kostya takes pride in the high standards of the restaurant."),
    (5, None,
     "'People in the dining room are ready to pay any money.' -- The cook observes the lavish spending of wealthy patrons."),
    (6, None,
     "'The main thing is always to do your work honestly.' -- Kostya emphasizes his ethical approach to serving diners."),
    (7, None,
     "'However, some barmen know clever secrets.' -- Max hints that other bartenders use questionable tricks for profit."),
    (8, None,
     "'I do not want to deceive our guests.' -- The upright young man rejects any suggestion of cheating the customers."),
    (9, None,
     "'You are simply too honest and kind a guy.' -- Max teases his roommate for being remarkably innocent."),
    (10, None,
     "'On the other hand, my conscience is absolutely clean today.' -- Kostya values peace of mind over shady earnings."),
    (11, None,
     "'All right, keep pouring juice and wine.' -- Max drops the topic and lets Kostya continue his duties."),
    (12, None,
     "'I will gladly pour juice for the guests!' -- The cheerful bartender turns back to serving drinks with enthusiasm."),
]

TRANSITION = "Now let us listen to Kostya and Max once again."
OUTRO = (
    "Dedicated to honest service, Kostya continues mixing and pouring drinks at the bar "
    "while Max prepares to observe the evening crowd."
)
CLOSING = ("anya", "Я с радостью налью гостям сок!")
