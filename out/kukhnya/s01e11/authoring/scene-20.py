"""s01e11 scene 20: Отказ от салата (Rejecting the Salad)."""

ID = "kukhnya-s01e11-scene-20"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 11
SCENE = 20
TITLE = "Отказ от салата  (Rejecting the Salad)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {
    "narrator": "sky",
    "anya": "alisa",
    "vika": "anja",
}
LABELS = {
    "anya": "Шеф",
    "vika": "Вика",
}
SOURCE_NAME = "Кухня (Kukhnya) S1.11"
SOURCE_FILE = "sources/kukhnya/s01/e11.ru.dual.srt"

INTRO = (
    "In the kitchen of Claude Monet, Victoria rushes to Chef Viktor with alarming news: "
    "the restaurant critic has rejected his fresh salad and is demanding hot soup immediately. "
    "Victoria urges Viktor to give the critic a soup meant for another guest, but the proud chef adamantly refuses to break the rules. "
    "Listen to their conversation in Russian first, then we will break down each line in English."
)

STORY = [
    ("vika", "Виктор Петрович, у нас срочная проблема!",
     "Viktor Petrovich, we have an urgent problem!",
     [], "sounding alarm"),
    ("anya", "Вика, не кричи на кухне.",
     "Vika, do not shout in the kitchen.",
     [], "demanding composure"),
    ("vika", "Критик за столиком отказался от салата.",
     "The critic at the table refused the salad.",
     [(273, "Критик отказался от блюда.")], "reporting refusal"),
    ("anya", "Почему? Мой салат был свежий.",
     "Why? My salad was fresh.",
     [], "defending dish"),
    ("vika", "Он говорит, что не ест траву.",
     "He says that he does not eat grass.",
     [(266, "Настенька, я траву не ем.")], "quoting critic"),
    ("vika", "Он требует горячий суп прямо сейчас.",
     "He demands hot soup right now.",
     [(276, "но он хочет супа побыстрее.")], "stating demand"),
    ("anya", "Пусть сначала сделает нормальный заказ.",
     "Let him make a normal order first.",
     [(278, "Пробивайте чек, и только после этого мы будем готовить.")], "insisting on protocol"),
    ("vika", "Отдайте ему суп с первого стола!",
     "Give him the soup from table one!",
     [(279, "Отдай ему этот суп.")], "suggesting shortcut"),
    ("anya", "Ты в своём уме, Вика?",
     "Are you out of your mind, Vika?",
     [(279, "Ты в своем уме?")], "rebuking suggestion"),
    ("anya", "Этот суп ждёт другой человек.",
     "Another person is waiting for this soup.",
     [(280, "Нет. Этот суп для другого гостя.")], "standing firm"),
    ("vika", "Но критик напишет ужасный отзыв!",
     "But the critic will write a terrible review!",
     [], "fearing bad press"),
    ("anya", "С меня хватит этих капризов.",
     "I have had enough of these whims.",
     [(277, "Все, с меня хватит. Пусть ждет.")], "dismissing panic"),
    ("anya", "Пусть ждёт суп по очереди.",
     "Let him wait for soup in turn.",
     [(277, "Пусть ждет.")], "imposing order"),
]

OPENER = "Let us practice the key lines together."

WALK = [
    (0, "Виктор Петрович, у нас срочная проблема!",
     "'Viktor Petrovich, we have an urgent problem!' — formal vocative name and patronymic followed by an exclamatory phrase."),
    (1, "Вика, не кричи на кухне.",
     "'Vika, do not shout in the kitchen.' — negative imperative verb governing a prepositional place phrase."),
    (2, "Критик за столиком отказался от салата.",
     "'The critic at the table refused the salad.' — past reflexive verb governing a genitive prepositional object."),
    (4, "Он говорит, что не ест траву.",
     "'He says that he does not eat grass.' — reporting verb introducing a subordinate clause with negation."),
    (5, "Он требует горячий суп прямо сейчас.",
     "'He demands hot soup right now.' — transitive verb governing an accusative direct object phrase."),
    (7, "Отдайте ему суп с первого стола!",
     "'Give him the soup from table one!' — plural imperative verb governing dative and prepositional objects."),
    (8, "Ты в своём уме, Вика?",
     "'Are you out of your mind, Vika?' — rhetorical prepositional idiom questioning common sense."),
    (9, "Этот суп ждёт другой человек.",
     "'Another person is waiting for this soup.' — inverted word order emphasizing the legitimate customer."),
    (10, "Но критик напишет ужасный отзыв!",
     "'But the critic will write a terrible review!' — future perfective verb describing an impending consequence."),
    (12, "Пусть ждёт суп по очереди.",
     "'Let him wait for soup in turn.' — third person permissive particle with an accusative and prepositional phrase."),
]

TRANSITION = "Now listen to the full conversation once more."
OUTRO = "Great job! Keep practicing these lively dialogues with us to master everyday Russian."
CLOSING = ("anya", "Пусть ждёт суп по очереди.")
