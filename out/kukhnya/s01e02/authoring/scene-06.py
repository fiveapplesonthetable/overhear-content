ID = "kukhnya-s01e02-scene-06"
TITLE = "Новый бармен  (The New Bartender)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "max": "anja"}
LABELS = {"max": "Макс"}
SOURCE_NAME = "Кухня (Kukhnya) S1.02"
SOURCE_FILE = "sources/kukhnya/s01/e02.ru.dual.srt"

INTRO = ("In this scene, Max agrees to help behind the restaurant bar and marvels at the computerized cash register. "
         "When Anya comes in to order two espressos, she is surprised to see a cook posing as the new bartender. "
         "Listen to their playful exchange in Russian first, and then we will review it in English.")

STORY = [
 ("max", "Так вот как выглядит эта система.", "So this is what this system looks like.",
  [], "new line"),
 ("max", "Я думал, это просто касса.", "I thought it was just a cash register.",
  [(100, "Я думал, это касса")], ""),
 ("anya", "Сделай два эспрессо, пожалуйста.", "Make two espressos, please.",
  [(101, "два эспрессо сделай, пожалуйста")], ""),
 ("anya", "Что ты тут делаешь?", "What are you doing here?",
  [(102, "что ты тут делаешь")], ""),
 ("max", "А я теперь новый бармен.", "And I am now the new bartender.",
  [(102, "А я новый бармен")], ""),
 ("anya", "Да ладно тебе выдумывать.", "Oh, stop making things up.",
  [(104, "Да ладно")], "adapted"),
 ("anya", "Я тебя на кухне видела.", "I saw you in the kitchen.",
  [(104, "Я тебя на кухне видела")], ""),
 ("anya", "Ты же повар.", "You are a cook after all.",
  [(105, "Ты повар")], ""),
 ("max", "У меня очень много талантов.", "I have very many talents.",
  [(105, "А у меня много талантов")], ""),
 ("max", "А в душе я бармен.", "And at heart I am a bartender.",
  [(105, "в душе я бармен")], ""),
 ("anya", "Костя уже починил аппарат?", "Did Kostya already fix the machine?",
  [], "new line"),
 ("max", "Конечно, всё прекрасно работает.", "Of course, everything works wonderfully.",
  [], "new line"),
 ("anya", "Тогда быстрее вари кофе.", "Then make coffee faster.",
  [(107, "сделай два эспрессо, пожалуйста")], "adapted"),
 ("max", "Сию секунду. Всё будет готово.", "Right away. Everything will be ready.",
  [], "new line"),
]

OPENER = "Let's review this funny encounter behind the bar line by line."

WALK = [
 (0, None,
  "'So this is what this system looks like.' Max inspects the computerized cash register at the bar."),
 (1, None,
  "'I thought it was just a cash register.' Admitting he expected something much simpler."),
 (2, None,
  "'Make two espressos, please.' Anya arrives at the bar with a beverage order."),
 (3, None,
  "'What are you doing here?' Surprised to find a kitchen helper standing behind the bar counter."),
 (4, None,
  "'And I am now the new bartender.' Max confidently invents a new position for himself."),
 (5, None,
  "'Oh, stop making things up.' Dismissing his boastful claim."),
 (6, None,
  "'I saw you in the kitchen.' Pointing out that she already recognized him from earlier."),
 (7, None,
  "'You are a cook after all.' Reminding him of his actual job title."),
 (8, None,
  "'I have very many talents.' Boasting about his versatility."),
 (9, None,
  "'And at heart I am a bartender.' A poetic Russian idiom meaning deep down inside his soul."),
 (10, None,
  "'Did Kostya already fix the machine?' Checking if the broken bar equipment is functioning."),
 (11, None,
  "'Of course, everything works wonderfully.' Reassuring her that the order can be completed without delay."),
 (12, None,
  "'Then make coffee faster.' Giving a direct order to hurry up with the drinks."),
 (13, "Сию секунду.",
  "'Right away.' An idiom literally meaning 'this very second'."),
 (13, "Всё будет готово.",
  "'Everything will be ready.' Promising swift service."),
]

TRANSITION = "Alright, let's hear the whole conversation once again."

OUTRO = ("That concludes our sixth scene. In Kukhnya, Max's endless self-confidence and quick wit "
         "get him into and out of all kinds of trouble. See you next time!")

CLOSING = ("anya", "До встречи!")
