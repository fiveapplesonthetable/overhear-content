ID = "kukhnya-s01e10-scene-28"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 10
SCENE = 28
TITLE = "Тайная доставка  (A Secret Delivery)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "chef": "anja"}
LABELS = {"anya": "Сеня", "chef": "Шеф"}
SOURCE_NAME = "Кухня (Kukhnya) S1.10"
SOURCE_FILE = "sources/kukhnya/s01/e10.ru.dual.srt"
SOURCE_NOTE = (
    "Cues 202-203. In the back of the kitchen, Senya discreetly brings Chef Viktor "
    "a heavy secret shipment that was urgently ordered to save dinner service."
)

INTRO = (
    "In the quiet storage area behind the kitchen, Senya meets Chef Viktor Petrovich "
    "with a secretive package. Desperate to replace the missing luxury ingredients without "
    "alerting management, Viktor nervously inspects the arrival. "
    "Let us listen to their hushed exchange in Russian first."
)

STORY = [
    ("anya", "Шеф, я принёс вам секретный заказ.",
     "Chef, I brought you the secret order.",
     [(202, "Ну что? Принёс")], "adapted"),
    ("chef", "Ты проверил, никто не видел тебя?",
     "Did you check that no one saw you?",
     [], "new"),
    ("anya", "В коридоре было совершенно пусто.",
     "In the corridor it was completely empty.",
     [], "new"),
    ("chef", "Отлично, ставь эту коробку на стол.",
     "Excellent, put this box on the table.",
     [], "new"),
    ("anya", "Коробка оказалась очень тяжёлой.",
     "The box turned out to be very heavy.",
     [], "new"),
    ("chef", "Главное, чтобы товар был свежим.",
     "The main thing is that the goods are fresh.",
     [], "new"),
    ("anya", "Я выбрал самый лучший свежий товар.",
     "I chose the very best fresh goods.",
     [], "new"),
    ("chef", "Наш ресторан не может ждать долго.",
     "Our restaurant cannot wait long.",
     [], "new"),
    ("anya", "Я выполнил всё быстро и вовремя.",
     "I completed everything quickly and on time.",
     [], "new"),
    ("chef", "Надеюсь, этот секрет останется между нами.",
     "I hope this secret remains between us.",
     [], "new"),
    ("anya", "Конечно, шеф, я умею молчать.",
     "Of course, chef, I know how to keep silent.",
     [], "new"),
    ("chef", "Сейчас мы откроем и проверим товар.",
     "Now we will open and inspect the goods.",
     [], "new"),
    ("anya", "Вы будете очень довольны покупкой.",
     "You will be very pleased with the purchase.",
     [], "new"),
]

OPENER = "Now let us examine Senya and Viktor's secretive kitchen interaction line by line."

WALK = [
    (0, None,
     "'Chef, I brought you the secret order.' -- Senya announces that he has brought the requested delivery."),
    (1, None,
     "'Did you check that no one saw you?' -- The chef asks whether Senya arrived unnoticed."),
    (2, None,
     "'In the corridor it was completely empty.' -- Senya assures him that no one was around."),
    (3, None,
     "'Excellent, put this box on the table.' -- The chef directs him to place the container down."),
    (4, None,
     "'The box turned out to be very heavy.' -- The cook notes the surprising weight of the package."),
    (5, None,
     "'The main thing is that the goods are fresh.' -- Viktor stresses the supreme importance of freshness."),
    (6, None,
     "'I chose the very best fresh goods.' -- Senya boasts of selecting high quality items."),
    (7, None,
     "'Our restaurant cannot wait long.' -- The chef reminds him that timing is critical in the kitchen."),
    (8, None,
     "'I completed everything quickly and on time.' -- Senya takes pride in his punctual delivery."),
    (9, None,
     "'I hope this secret remains between us.' -- Viktor warns him to keep the transaction strictly private."),
    (10, None,
     "'Of course, chef, I know how to keep silent.' -- Senya promises that he will not tell anyone."),
    (11, None,
     "'Now we will open and inspect the goods.' -- The chef prepares to inspect the contents immediately."),
    (12, None,
     "'You will be very pleased with the purchase.' -- The cook assures Viktor of complete satisfaction."),
]

TRANSITION = "Now let us listen to the discreet conversation again without pause."
OUTRO = (
    "With the heavy box securely on the table and secrecy promised, Viktor Petrovich "
    "prepares to unveil the mysterious ingredients that Senya has procured."
)
CLOSING = ("anya", "Вы будете очень довольны покупкой.")
