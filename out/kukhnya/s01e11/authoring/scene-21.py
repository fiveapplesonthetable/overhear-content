"""s01e11 scene 21: Все равны (Everyone Is Equal)."""

ID = "kukhnya-s01e11-scene-21"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 11
SCENE = 21
TITLE = "Все равны  (Everyone Is Equal)"
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
    "In the dining room of Claude Monet, Chef Viktor personally carries a bowl of hot soup to an ordinary guest. "
    "Victoria hurries over in a panic, horrified that the influential food critic was made to wait, "
    "but Viktor proudly declares that everyone is equal in his kitchen. "
    "Listen to their conversation in Russian first, then we will break down each line in English."
)

STORY = [
    ("anya", "Твой суп, дружище, приятного аппетита.",
     "Your soup, buddy, enjoy your meal.",
     [(282, "Твой суп, дружище, приятного аппетита.")], "serving guest"),
    ("vika", "Виктор Петрович, что вы делаете?",
     "Viktor Petrovich, what are you doing?",
     [(283, "Ты что делаешь?")], "panicking"),
    ("anya", "Я делаю то, что должен делать.",
     "I am doing what I must do.",
     [(284, "То, что должен.")], "answering firmly"),
    ("vika", "Но там же сидит важный критик!",
     "But an important critic is sitting right there!",
     [(284, "Там же критик.")], "pointing out VIP"),
    ("anya", "Мне всё равно, кто там сидит.",
     "I do not care who is sitting there.",
     [(285, "Мне что, это только одно и надо?")], "dismissing status"),
    ("anya", "Этот гость заказал суп раньше.",
     "This guest ordered soup earlier.",
     [(287, "Этот человек раньше заказал суп, он его получил.")], "explaining principle"),
    ("vika", "Критик очень зол, он уйдёт!",
     "The critic is very angry, he will leave!",
     [], "warning of loss"),
    ("anya", "Пусть уходит, если не умеет ждать.",
     "Let him leave if he does not know how to wait.",
     [], "shrugging off threat"),
    ("vika", "Вы рискуете репутацией нашего ресторана.",
     "You are risking our restaurant's reputation.",
     [], "appealing to business"),
    ("anya", "Да будь он хоть трижды критик!",
     "Even if he were three times a critic!",
     [(285, "Да будь он хоть трижды критик,")], "declaring pride"),
    ("anya", "Я всем гостям подаю по очереди.",
     "I serve all guests in turn.",
     [(286, "я всем подаю по очереди.")], "stating rule"),
    ("anya", "У меня на кухне все равны!",
     "In my kitchen everyone is equal!",
     [(289, "У меня на кухне все равны.")], "proclaiming kitchen code"),
]

OPENER = "Let us practice the key lines together."

WALK = [
    (0, "Твой суп, дружище, приятного аппетита.",
     "'Your soup, buddy, enjoy your meal.' — friendly informal address paired with the standard Russian dining wish."),
    (1, "Виктор Петрович, что вы делаете?",
     "'Viktor Petrovich, what are you doing?' — polite second person plural question with formal patronymic."),
    (2, "Я делаю то, что должен делать.",
     "'I am doing what I must do.' — demonstrative pronoun antecedent with a relative clause of obligation."),
    (3, "Но там же сидит важный критик!",
     "'But an important critic is sitting right there!' — exclamatory clause with an emphatic modal particle."),
    (4, "Мне всё равно, кто там сидит.",
     "'I do not care who is sitting there.' — impersonal dative idiom expressing indifference to status."),
    (5, "Этот гость заказал суп раньше.",
     "'This guest ordered soup earlier.' — past perfective verb with a comparative temporal adverb."),
    (7, "Пусть уходит, если не умеет ждать.",
     "'Let him leave if he does not know how to wait.' — third person hortative with a conditional clause."),
    (8, "Вы рискуете репутацией нашего ресторана.",
     "'You are risking our restaurant's reputation.' — verb governing an instrumental noun phrase."),
    (9, "Да будь он хоть трижды критик!",
     "'Even if he were three times a critic!' — idiomatic imperative conditional of defiant dismissal."),
    (11, "У меня на кухне все равны!",
     "'In my kitchen everyone is equal!' — possessive location phrase with short form plural adjective."),
]

TRANSITION = "Now listen to the full conversation once more."
OUTRO = "And that's it for this scene. When you watch the episode, listen out for the exchange around everyone is equal, and for the words meaning 'soup' and 'buddy'. You'll catch them now. See you next time."
CLOSING = ("anya", "У меня на кухне все равны!")
