"""s01e06 scene 19: Заказ на трюфели (The Truffle Order)."""

ID = "kukhnya-s01e06-scene-19"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 6
SCENE = 19
TITLE = "Заказ на трюфели  (The Truffle Order)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {
    "narrator": "sky",
    "anya": "alisa",
    "chef": "anja",
    "nastya": "angelina",
}
LABELS = {
    "anya": "Макс",
    "chef": "Шеф",
    "nastya": "Настя",
}
SOURCE_NAME = "Кухня (Kukhnya) S1.06"
SOURCE_FILE = "sources/kukhnya/s01/e06.ru.dual.srt"

INTRO = (
    "In the Claude Monet kitchen, Chef Viktor Barinov urgently demands a fresh truffle for a VIP table. "
    "Having lost the precious ingredients earlier, Max frantically intercepts waitress Nastya in hopes of changing the guest's order. "
    "Listen to their conversation in Russian first, then we will break down each line in English."
)

STORY = [
    ("chef", "Огузок, тащи сюда скорее один трюфель!",
     "Rump, bring one truffle here quickly!",
     [(238, "Агузок, тащи сюда один трюфель")], "urgent demand"),
    ("chef", "Седьмой столик заказал салат с трюфелями.",
     "Table seven ordered a salad with truffles.",
     [(237, "салат с трюфелями за седьмой столик")], "specifying ticket"),
    ("anya", "Шеф, я сейчас всё быстро принесу.",
     "Chef, I will bring everything quickly now.",
     [], "stalling for time"),
    ("anya", "Настя, стой, мне срочно нужна помощь!",
     "Nastya, stop, I urgently need help!",
     [(239, "Слушай, Настя")], "frantic appeal"),
    ("nastya", "Что случилось, Макс? Что такое?",
     "What happened, Max? What is it?",
     [], "surprised reaction"),
    ("anya", "Скажи гостю, что трюфели сегодня плохие.",
     "Tell the guest that the truffles are bad today.",
     [(239, "трюфеля сегодня не очень")], "pleading sabotage"),
    ("anya", "Пусть он закажет любое другое блюдо!",
     "Let him order any other dish!",
     [(240, "что-нибудь другое заказали")], "suggesting change"),
    ("nastya", "Нет, я не могу так сказать.",
     "No, I cannot say that.",
     [(241, "Не, не могу")], "firm refusal"),
    ("nastya", "Гость пришёл специально ради этого салата.",
     "The guest came especially for this salad.",
     [(241, "пришел сюда специально ради этого блюда")], "explaining importance"),
    ("anya", "Но у меня нет этого трюфеля!",
     "But I do not have this truffle!",
     [], "terrified admission"),
    ("nastya", "Он очень строгий и важный человек.",
     "He is a very strict and important person.",
     [], "warning gravity"),
    ("nastya", "Кстати, он просил передать тебе записку.",
     "By the way, he asked to give you a note.",
     [(242, "просил тебе вот это передать")], "passing message"),
    ("anya", "О нет, это катастрофа для кухни!",
     "Oh no, this is a disaster for the kitchen!",
     [], "panicked dread"),
    ("nastya", "Торопись, шеф уже очень сильно злится.",
     "Hurry, the chef is already getting very angry.",
     [], "urging action"),
]

OPENER = "Now let us go through each phrase to see how it works in Russian."

WALK = [
    (0, "Огузок, тащи сюда скорее один трюфель!",
     "'Rump, bring one truffle here quickly!' The head chef urgently barks an order across the line."),
    (1, "Седьмой столик заказал салат с трюфелями.",
     "'Table seven ordered a salad with truffles.' Barinov specifies the high-priority luxury dish."),
    (2, "Шеф, я сейчас всё быстро принесу.",
     "'Chef, I will bring everything quickly now.' Max stalls for time while panicking internally."),
    (3, "Настя, стой, мне срочно нужна помощь!",
     "'Nastya, stop, I urgently need help!' The desperate cook rushes to intercept the waitress."),
    (4, "Что случилось, Макс? Что такое?",
     "'What happened, Max? What is it?' Nastya asks in surprise at his sudden anxiety."),
    (5, "Скажи гостю, что трюфели сегодня плохие.",
     "'Tell the guest that the truffles are bad today.' Max begs her to sabotage the delicate order."),
    (6, "Пусть он закажет любое другое блюдо!",
     "'Let him order any other dish!' A frantic attempt to redirect the customer away from truffles."),
    (7, "Нет, я не могу так сказать.",
     "'No, I cannot say that.' Nastya firmly refuses to lie to a dining room guest."),
    (8, "Гость пришёл специально ради этого салата.",
     "'The guest came especially for this salad.' The customer specifically requested the delicacy."),
    (9, "Но у меня нет этого трюфеля!",
     "'But I do not have this truffle!' Max confesses his terrifying culinary dilemma."),
    (10, "Он очень строгий и важный человек.",
     "'He is a very strict and important person.' Nastya emphasizes the high stakes at the table."),
    (11, "Кстати, он просил передать тебе записку.",
     "'By the way, he asked to give you a note.' The waitress delivers an unexpected message."),
    (12, "О нет, это катастрофа для кухни!",
     "'Oh no, this is a disaster for the kitchen!' Max dreads the escalating crisis at work."),
    (13, "Торопись, шеф уже очень сильно злится.",
     "'Hurry, the chef is already getting very angry.' Nastya warns him of Barinov's fiery temper."),
]

TRANSITION = "Alright, let's hear the whole thing once more."

OUTRO = (
    "Faced with a VIP guest demanding truffles, Max realizes he cannot avoid the missing ingredients crisis. "
    "Next time, we will see how Barinov reacts to the delay and whether Max finds a way out. Until then!"
)

CLOSING = ("anya", "Макс понял, что попал в беду.")
