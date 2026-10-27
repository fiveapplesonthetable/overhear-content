ID = "08-orders"
TITLE = "Эпизод 8: Я не успеваю  (I Can't Keep Up)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "chef": "anja", "lena": "angelina"}
LABELS = {"chef": "Шеф", "lena": "Лена"}
SOURCE_NAME = "Кухня (Kukhnya) S1.05"
SOURCE_FILE = "sources/kukhnya/s01/e05.ru.dual.srt"

INTRO = ("The same kitchen again, now from the fifth episode. It's a very busy day, the orders keep coming in, "
         "and Anya has to learn how to ask for help. As always, the whole story in Russian first, and then "
         "we'll go through it together in English. Don't worry about catching every word.")

STORY = [
 ("chef", "Всем внимание! Сегодня продаём треску.", "Attention, everyone! Today we're selling cod.",
  [(240, "Всем внимание"), (43, "сегодня продаем треску")], ""),
 ("chef", "Аня, две трески!", "Anya, two cod!", [(256, "две трески")], "'Максим' -> 'Аня', short form"),
 ("anya", "Да, шеф!", "Yes, chef!", [(257, "Да, шеф")], ""),
 ("chef", "Где моя треска?", "Where is my cod?", [(272, "Где моя треска")], ""),
 ("anya", "Шеф, я не успеваю. Мне нужна помощь.", "Chef, I can't keep up. I need help.",
  [(274, "Шеф, я не успеваю, мне помощь нужна")], "word order made standard"),
 ("chef", "Помощь? Ну так пойди и попроси.", "Help? Well then, go and ask for some.",
  [(275, "Помощь"), (276, "Ну так пойди и попроси")], ""),
 ("anya", "Лена, помоги мне, пожалуйста, с заказами.", "Lena, please help me with the orders.",
  [(300, "Помоги мне, пожалуйста, с заказами")], "'Федя' -> 'Лена'"),
 ("lena", "Что? Давай ещё разок.", "What? Say it once more.", [(295, "Что?"), (304, "Давай еще разок")], ""),
 ("anya", "Помоги мне, пожалуйста!", "Please help me!", [(300, "Помоги мне, пожалуйста")], ""),
 ("lena", "Ладно. Подвинься. Не переживай.", "Okay. Move over. Don't worry.",
  [(158, "Ладно"), (307, "Подвинься давай"), (8, "Не переживай")], "'давай' dropped from 'Подвинься давай'"),
 ("lena", "Ты, главное, не торопись.", "The main thing is, don't rush.",
  [(284, "Ты, главное, не переживай"), (313, "Не торопись")], "two lines blended"),
 ("anya", "Спасибо, Лена!", "Thank you, Lena!", [(90, "Спасибо")], ""),
 ("chef", "Где моя треска?", "Where is my cod?", [(272, "Где моя треска")], ""),
 ("anya", "Вот она, шеф!", "Here it is, chef!", [], "'Вот она' new"),
 ("chef", "Молодец!", "Well done!", [(171, "Молодец")], ""),
]

OPENER = "Let's go through it line by line. The restaurant has too much cod to sell, and the chef starts the day with an announcement."

WALK = [
 (0, "Всем внимание!",
  "'Attention, everyone!' The first word means 'to everyone'. It's how you start any announcement. Then the plan for the day."),
 (0, "Сегодня продаём треску.",
  "'Today we're selling cod.' 'Today' comes first, as in Russian you often start with the time. The fish is the last word. Then the chef gives Anya her first order."),
 (1, None,
  "'Anya, two cod!' After 'two', the noun takes a special ending, the same one as in 'of cod'. You'll see this after two, three and four. In a kitchen it just means two portions. Anya says yes at once."),
 (2, None,
  "'Yes, chef!' You know this one. A little later, the chef wants his fish."),
 (3, None,
  "'Where is my cod?' Same pattern as 'Where is my knife': 'where', then 'my', then the thing. But 'my' changes to match the fish, which is feminine. Anya is in trouble."),
 (4, None,
  "'Chef, I can't keep up. I need help.' The first verb means 'to manage in time'. And the second sentence is a pattern worth keeping: 'to me, help is needed'. The chef is not sympathetic."),
 (5, None,
  "'Help? Well then, go and ask for some.' Two commands joined by 'and'. It's quite a sensible piece of advice. So Anya turns to a colleague."),
 (6, None,
  "'Lena, please help me with the orders.' She says Lena's name first, to get her attention. The word for 'please' is in the middle. Lena didn't quite hear her."),
 (7, None,
  "'What? Say it once more.' The second phrase literally means 'give once more', a casual way to ask someone to repeat. Anya tries again."),
 (8, None,
  "'Please help me!' Shorter this time, and a little louder. And Lena agrees."),
 (9, None,
  "'Okay. Move over. Don't worry.' Three short sentences, and the last is a command in the negative. Lena is kind, and gives one more piece of advice."),
 (10, None,
  "'The main thing is, don't rush.' The middle word means 'the main thing'. It's how Russians introduce the most important point. Anya is relieved."),
 (11, None,
  "'Thank you, Lena!' She uses Lena's name again. And right away, the chef shouts."),
 (12, None,
  "'Where is my cod?' The same question as before, and this time Anya has the answer."),
 (13, None,
  "'Here it is, chef!' The second word means 'it', and it's feminine again, to match the fish. The chef is satisfied."),
 (14, None,
  "'Well done!' The same word the chef said to Anya last time, when she found his knife. Quite a day."),
]

TRANSITION = "Okay, let's hear it all once more."

OUTRO = ("That's it for today. When you watch the fifth episode, listen out for the chef asking for his cod, "
         "and for Anya's friend telling her not to rush. You'll recognise them now. See you next time.")
CLOSING = ("anya", "Хорошего дня!")
