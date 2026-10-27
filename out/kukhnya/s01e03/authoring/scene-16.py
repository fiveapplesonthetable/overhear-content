"""s01e03 scene 16: Комплимент от шефа (A Compliment from the Chef)."""

ID = "kukhnya-s01e03-scene-16"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 3
SCENE = 16
TITLE = "Комплимент от шефа  (A Compliment from the Chef)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {
    "narrator": "sky",
    "anya": "alisa",
    "guest": "anja",
}
LABELS = {
    "anya": "Шеф",
    "guest": "Вадим",
}
SOURCE_NAME = "Кухня (Kukhnya) S1.03"
SOURCE_FILE = "sources/kukhnya/s01/e03.ru.dual.srt"

INTRO = (
    "Chef Viktor Barinov personally brings a complimentary birthday course to a table of influential guests. "
    "The guest of honor is delighted and hints at useful connections, but the chef's perfectionism takes over upon tasting. "
    "Listen to their polite conversation in Russian first, then we will break down each line in English."
)

STORY = [
    ("anya", "Добрый вечер, дорогие гости нашего ресторана!",
     "Good evening, dear guests of our restaurant!",
     [(280, "Добрый вечер")], "gracious greeting"),
    ("guest", "Добрый вечер, шеф-повар!",
     "Good evening, head chef!",
     [(280, "Добрый вечер")], "polite reply"),
    ("anya", "Я принёс вам особенный сюрприз.",
     "I brought you a special surprise.",
     [(283, "маленький сюрприз")], "announcing treat"),
    ("anya", "Это комплимент в честь дня рождения.",
     "This is a compliment in honor of the birthday.",
     [(284, "Это комплимент от шефа"), (284, "дня рождения")], "verbatim phrase"),
    ("guest", "Спасибо большое, всё выглядит очень вкусно!",
     "Thank you very much, everything looks very delicious!",
     [(285, "Все так вкусно")], "warm appreciation"),
    ("guest", "Я вижу, что вы отличный повар.",
     "I see that you are an excellent cook.",
     [(286, "я вижу")], "verbatim praise"),
    ("guest", "Я могу вам помочь в городе.",
     "I can help you in the city.",
     [(287, "могу вам кое-чем помочь")], "offering patronage"),
    ("guest", "Позвоните мне завтра в любое время.",
     "Call me tomorrow at any time.",
     [(288, "Позвоните мне завтра")], "verbatim invitation"),
    ("anya", "Спасибо, для меня это большая честь!",
     "Thank you, this is a great honor for me!",
     [], "polite gratitude"),
    ("anya", "Подождите, я сначала сам попробую блюдо.",
     "Wait, I will taste the dish myself first.",
     [(289, "я сначала попробую")], "verbatim inspection"),
    ("anya", "Ой, повар слишком сильно переперчил соус!",
     "Oh, the cook put way too much pepper in the sauce!",
     [(290, "Переперчел")], "verbatim disaster"),
    ("guest", "А по-моему, получилось довольно вкусно.",
     "And in my opinion, it turned out quite delicious.",
     [(293, "По-моему, вкусно")], "verbatim polite remark"),
    ("anya", "Нет, я немедленно всё переделаю!",
     "No, I will immediately redo everything!",
     [(292, "Я переделаю и принесу")], "verbatim determination"),
    ("anya", "Я лично принесу вам идеальное блюдо.",
     "I will personally bring you an ideal dish.",
     [(292, "Я переделаю и принесу")], "culinary promise"),
]

OPENER = "Now let us go through each phrase to see how it works in Russian."

WALK = [
    (0, "Добрый вечер, дорогие гости нашего ресторана!",
     "'Good evening, dear guests of our restaurant!' A courteous welcome greeting from the head chef."),
    (1, "Добрый вечер, шеф-повар!",
     "'Good evening, head chef!' The guest replies politely using Barinov's professional title."),
    (2, "Я принёс вам особенный сюрприз.",
     "'I brought you a special surprise.' The past verb indicates a delivered personal treat."),
    (3, "Это комплимент в честь дня рождения.",
     "'This is a compliment in honor of the birthday.' A formal culinary term for a gift on the house."),
    (4, "Спасибо большое, всё выглядит очень вкусно!",
     "'Thank you very much, everything looks very delicious!' The guest compliments the visual presentation."),
    (5, "Я вижу, что вы отличный повар.",
     "'I see that you are an excellent cook.' The subordinate clause conveys praise from an official."),
    (6, "Я могу вам помочь в городе.",
     "'I can help you in the city.' A hint of political influence and useful administrative connections."),
    (7, "Позвоните мне завтра в любое время.",
     "'Call me tomorrow at any time.' An open invitation offering direct contact."),
    (8, "Спасибо, для меня это большая честь!",
     "'Thank you, this is a great honor for me!' An expression of deep professional gratitude."),
    (9, "Подождите, я сначала сам попробую блюдо.",
     "'Wait, I will taste the dish myself first.' The chef insists on testing the quality."),
    (10, "Ой, повар слишком сильно переперчил соус!",
     "'Oh, the cook put way too much pepper in the sauce!' A culinary disaster detected upon tasting."),
    (11, "А по-моему, получилось довольно вкусно.",
     "'And in my opinion, it turned out quite delicious.' The guest tries to be polite about the spicy food."),
    (12, "Нет, я немедленно всё переделаю!",
     "'No, I will immediately redo everything!' A perfectionist refusal to serve subpar cooking."),
    (13, "Я лично принесу вам идеальное блюдо.",
     "'I will personally bring you an ideal dish.' A solemn culinary promise delivered by the master."),
]

TRANSITION = "Alright, let's hear the whole thing once more."

OUTRO = (
    "Chef Barinov refuses to let an over-peppered sauce ruin his reputation, whisking the plate away to be remade. "
    "Next time, we will see whether his perfectionism impresses the VIP guest or causes an awkward scene. Until then!"
)

CLOSING = ("anya", "Всё должно быть идеально вкусно.")
