ID = "kukhnya-s01e07-scene-06"
TITLE = "Покупка ножа  (Buying a Knife)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "seller": "angelina", "chef": "anja"}
LABELS = {"anya": "Макс", "seller": "Продавец", "chef": "Шеф"}
SOURCE_NAME = "Кухня (Kukhnya) S1.07"
SOURCE_FILE = "sources/kukhnya/s01/e07.ru.dual.srt"

INTRO = ("In this scene at the food market, Chef Viktor Barinov visits a specialty cutlery stall "
         "to inspect professional kitchen knives. A persuasive vendor tries to sell him an ordinary blade, "
         "but Barinov uses his expert culinary eye to test the steel and negotiate a fair deal for a genuine Japanese knife. "
         "Listen to their dialogue in Russian first, and then we will examine every line.")

STORY = [
 ("seller", "Уважаемый шеф, подходите и выбирайте ножи!", "Respected chef, step right up and choose knives!",
  [(56, "Подходим, выбираем")], ""),
 ("seller", "Посмотрите, какое острое и тонкое лезвие!", "Look what a sharp and thin blade!",
  [(56, "Острый")], ""),
 ("chef", "Осторожно, этот клинок острый, как кинжал.", "Careful, this blade is sharp as a dagger.",
  [(57, "Ой, как кинзал"), (58, "Осторожно")], ""),
 ("chef", "Но здесь металл слишком мягкий.", "But here the metal is too soft.",
  [(59, "Что-то не то")], ""),
 ("seller", "Это лучшая прочная сталь для кухни!", "This is the best strong steel for the kitchen!",
  [(56, "выбираем")], "new line"),
 ("chef", "Не обманывай меня, я опытный повар.", "Don't deceive me, I am an experienced chef.",
  [(59, "Что-то не то")], "new line"),
 ("chef", "Таким ножом мясо резать нельзя.", "One cannot cut meat with such a knife.",
  [(59, "Что-то не то")], "new line"),
 ("seller", "Тогда посмотрите вот этот японский нож.", "Then look at this Japanese knife.",
  [(56, "выбираем")], "new line"),
 ("seller", "Его сделали мастера из твёрдой стали.", "Craftsmen made it from hard steel.",
  [(56, "выбираем")], "new line"),
 ("chef", "Да, этот нож лежит в руке идеально.", "Yes, this knife rests in the hand perfectly.",
  [(58, "Осторожно")], "new line"),
 ("chef", "Сколько стоит такой отличный инструмент?", "How much does such an excellent tool cost?",
  [(56, "Подходим")], "new line"),
 ("seller", "Для вас отдам всего за три тысячи.", "For you I will give it for only three thousand.",
  [(56, "Подходим")], "new line"),
 ("chef", "Хорошо, я забираю этот нож.", "Fine, I am taking this knife.",
  [(56, "выбираем")], "new line"),
 ("chef", "На моей кухне нужен острый порядок!", "In my kitchen sharp order is needed!",
  [(56, "Острый")], "new line"),
]

OPENER = "Let's examine this cutlery negotiation line by line."

WALK = [
 (0, None,
  "'Respected chef, step right up and choose knives!' The vendor calls out to market shoppers."),
 (1, None,
  "'Look what a sharp and thin blade!' Praising the cutting edge of a display knife."),
 (2, None,
  "'Careful, this blade is sharp as a dagger.' Viktor tests the fine point with his thumb."),
 (3, None,
  "'But here the metal is too soft.' Spotting poor material quality immediately."),
 (4, None,
  "'This is the best strong steel for the kitchen!' Defending the durability of the merchandise."),
 (5, None,
  "'Don't deceive me, I am an experienced chef.' Reminding the merchant of his culinary expertise."),
 (6, None,
  "'One cannot cut meat with such a knife.' Explaining why soft steel fails for butchering."),
 (7, None,
  "'Then look at this Japanese knife.' Offering a premium alternative from beneath the counter."),
 (8, None,
  "'Craftsmen made it from hard steel.' Describing the authentic craftsmanship of the forged blade."),
 (9, None,
  "'Yes, this knife rests in the hand perfectly.' Feeling the balanced weight and grip in his hand."),
 (10, None,
  "'How much does such an excellent tool cost?' Asking for the price of the superior blade."),
 (11, None,
  "'For you I will give it for only three thousand.' Quoting a discounted rate for a head chef."),
 (12, None,
  "'Fine, I am taking this knife.' Agreeing to purchase the professional knife."),
 (13, None,
  "'In my kitchen sharp order is needed!' Viktor prepares to bring his new purchase to the restaurant."),
]

TRANSITION = "Now let's listen to the entire dialogue once again."

OUTRO = ("That concludes our sixth scene. In Kukhnya, a master chef never compromises on the quality "
         "of his primary kitchen tool. See you next time!")

CLOSING = ("anya", "До встречи!")
