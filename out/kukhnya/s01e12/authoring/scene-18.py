"""s01e12 scene 18: Полный зал (A Packed House)."""

ID = "kukhnya-s01e12-scene-18"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 12
SCENE = 18
TITLE = "Полный зал  (A Packed House)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {
    "narrator": "sky",
    "anya": "alisa",
    "nagiev": "anja",
}
LABELS = {
    "anya": "Ангелина",
    "nagiev": "Нагиев",
}
SOURCE_NAME = "Кухня (Kukhnya) S1.12"
SOURCE_FILE = "sources/kukhnya/s01/e12.ru.dual.srt"

INTRO = (
    "In the dining room of Claude Monet, restaurant owner Dmitry Nagiyev checks the reservation book with hostess Angelina. "
    "Delighted to hear that all tables are booked solid, Nagiyev proudly declares that their restaurant needs no gimmicks to win over guests. "
    "Listen to their conversation in Russian first, then we will break down each line in English."
)

STORY = [
    ("nagiev", "Ангелина, что у нас с резервами сегодня?",
     "Angelina, how are our reservations today?",
     [(239, "Ангелина, что у нас с резервами на сегодня?")], "checking bookings"),
    ("anya", "Дмитрий Владимирович, все столики уже заняты.",
     "Dmitry Vladimirovich, all tables are already booked.",
     [(240, "Все столики забронированы.")], "reporting full tables"),
    ("nagiev", "Правда? Совсем не осталось мест?",
     "Really? Are there no seats left at all?",
     [], "asking confirmation"),
    ("anya", "Да, свободных столиков больше нет.",
     "Yes, there are no more free tables.",
     [], "confirming status"),
    ("anya", "Гости начнут приходить с минуты на минуту.",
     "The guests will start arriving any minute.",
     [(240, "Гость сейчас будет приезжать.")], "noting arrival"),
    ("nagiev", "Ты смотри! Вышло так, как я говорил.",
     "Look at that! It turned out just like I said.",
     [(241, "Ты смотри, опять вышло так, как я сказал.")], "feeling vindicated"),
    ("anya", "Наш ресторан сейчас очень популярен.",
     "Our restaurant is very popular right now.",
     [], "agreeing happily"),
    ("nagiev", "Люди любят нас именно такими!",
     "People love us just the way we are!",
     [(242, "Нас любят такими, какими мы есть.")], "praising authenticity"),
    ("nagiev", "Иди готовь дополнительные столики.",
     "Go prepare additional tables.",
     [(243, "Иди готовь экстра столики.")], "giving instructions"),
    ("anya", "Мы поставим ещё два стола у окна.",
     "We will place two more tables by the window.",
     [], "suggesting location"),
    ("nagiev", "Отлично, сегодня у нас полный зал!",
     "Great, today we have a full house!",
     [(244, "У нас сегодня биток.")], "celebrating crowd"),
    ("anya", "Я сейчас всё быстро организую.",
     "I will quickly organize everything right now.",
     [], "taking charge"),
    ("nagiev", "Прекрасно, вечер обещает быть удачным!",
     "Wonderful, the evening promises to be successful!",
     [], "concluding warmly"),
]

OPENER = "Let us practice the key lines together."

WALK = [
    (0, "Ангелина, что у нас с резервами сегодня?",
     "'Angelina, how are our reservations today?' — polite vocative inquiry followed by a prepositional phrase."),
    (1, "Дмитрий Владимирович, все столики уже заняты.",
     "'Dmitry Vladimirovich, all tables are already booked.' — formal Russian patronymic with a short passive participle."),
    (3, "Да, свободных столиков больше нет.",
     "'Yes, there are no more free tables.' — negative existential construction governing a genitive plural phrase."),
    (4, "Гости начнут приходить с минуты на минуту.",
     "'The guests will start arriving any minute.' — compound future predicate with a common temporal idiom."),
    (5, "Ты смотри! Вышло так, как я говорил.",
     "'Look at that! It turned out just like I said.' — colloquial imperative followed by a comparative clause."),
    (7, "Люди любят нас именно такими!",
     "'People love us just the way we are!' — transitive verb governing an accusative pronoun with an emphatic modifier."),
    (8, "Иди готовь дополнительные столики.",
     "'Go prepare additional tables.' — double imperative sequence of motion and preparation."),
    (9, "Мы поставим ещё два стола у окна.",
     "'We will place two more tables by the window.' — numerical construction governing a genitive singular noun."),
    (10, "Отлично, сегодня у нас полный зал!",
     "'Great, today we have a full house!' — exclamatory adverb followed by an idiomatic possession phrase."),
    (12, "Прекрасно, вечер обещает быть удачным!",
     "'Wonderful, the evening promises to be successful!' — modal verb governing an infinitive and instrumental adjective."),
]

TRANSITION = "Now listen to the full conversation once more."
OUTRO = "Great job! Keep practicing these lively dialogues with us to master everyday Russian."
CLOSING = ("nagiev", "Прекрасно, вечер обещает быть удачным!")
