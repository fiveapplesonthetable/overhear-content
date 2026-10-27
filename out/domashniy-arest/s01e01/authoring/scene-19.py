ID = "domashniy-arest-s01e01-scene-19"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 1
SCENE = 19
TITLE = "Список желаний  (The Wish List)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "samson": "anja", "nina": "angelina"}
LABELS = {"anya": "Аркадий", "samson": "Самсон", "nina": "Нина"}
SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.01"
SOURCE_FILE = "sources/domashniy-arest/s01/e01.ru.dual.srt"

INTRO = ("Now we're in the Samsonovs' room. Last time, Arkady refused to fix the leaking toilet pipe and promised "
         "the family everything they want once he's free, and Nina demanded it in writing. "
         "So with a pen and paper on the table, Nina starts the list, and Arkady promises everything. "
         "We'll hear it in Russian first; don't worry about catching every word.")

STORY = [
 ("nina", "Квартира. Три комнаты.", "A flat. Three rooms.",
  [(736, "Квартира"), (745, "три комнаты")], "736 'трёхкомнатная' simplified to 'три комнаты'"),
 ("anya", "Квартира будет отличная. На Симашко есть новый дом.",
  "It'll be an excellent flat. There's a new building on Simashko Street.",
  [(737, "будет отличная"), (738, "на Симашко")], "'квартирка' -> 'квартира'; 'новостроечка' -> 'новый дом'"),
 ("anya", "Хороший район. Там три комнаты и балкон.", "It's a good area. There are three rooms and a balcony.",
  [(740, "хороший район"), (745, "три комнаты")], "746 'балкончик' -> 'балкон'"),
 ("nina", "С мебелью?", "With furniture?",
  [(747, "С мебелью")], ""),
 ("anya", "Конечно, с мебелью.", "Of course, with furniture.",
  [(747, "с мебелью")], "748 'Разумеется' -> the simpler 'Конечно'"),
 ("samson", "Машина. Немецкая.", "A car. A German one.",
  [(749, "Машина")], "749 slang 'Немец' -> 'Немецкая'"),
 ("nina", "Мне ещё работа нужна.", "I need a job too.",
  [(752, "Мне еще работа нужна")], ""),
 ("anya", "Для вас можно открыть салон красоты.", "We could open a beauty salon for you.",
  [(754, "для вас"), (755, "салон красоты")], "754-755 simplified: 'мы можем ... открыть' -> 'можно открыть'"),
 ("anya", "Или ещё лучше: спа!", "Or even better: a spa!",
  [(756, "Или еще лучше"), (757, "Спа")], ""),
 ("nina", "Спа. Давайте!", "A spa. Let's do it!",
  [(758, "Спа"), (759, "Давайте")], ""),
 ("nina", "Юле надо поступить в институт.", "Yulia needs to get into university.",
  [(761, "в институт поступить надо")], "'Юльке' -> 'Юле'; word order made neutral"),
 ("anya", "Это вообще без проблем.", "That's no problem at all.",
  [(764, "Это вообще без проблем")], ""),
 ("samson", "Слушай, обманешь — будут проблемы. Понял?", "Listen, if you cheat us, there'll be trouble. Got it?",
  [(766, "обманешь"), (766, "понял")], "766 retold cleanly: the threat to tear his head off -> 'будут проблемы'"),
 ("anya", "Ваня, расслабься. В этот раз без обмана.", "Vanya, relax. This time there's no trick.",
  [(769, "Ваня, ну расслабься"), (770, "без обмана")], "'ну' and 'вообще' dropped"),
 ("anya", "Почему он меня всё время за горло хватает?", "Why does he keep grabbing me by the throat?",
  [(772, "все время за горло хватает")], "772 'мне' (transcription slip) -> 'меня'"),
 ("samson", "А мне что?", "And what about me?",
  [(774, "А мне что")], ""),
 ("anya", "О, а вот и мой заместитель! Пойдёмте, я вас познакомлю.",
  "Oh, and here's my deputy! Come on, I'll introduce you.",
  [(776, "мой заместитель"), (777, "Пойдемте, я вас")], "'с ним' dropped from 777"),
]

OPENER = "Let's go through the list item by item. Nina knows exactly what she wants, and the flat comes first."

WALK = [
 (0, None,
  "'A flat. Three rooms.' After the number three, the word for 'room' takes a special ending, as it does after two and four. Arkady has just the thing."),
 (1, "Квартира будет отличная.",
  "'It'll be an excellent flat.' The word for 'will be' turns a simple description into a promise. And he knows where."),
 (1, "На Симашко есть новый дом.",
  "'There's a new building on Simashko Street.' The little word in the middle means 'there is', and it's how you say something exists. In the show he admits he kept three of those flats for himself."),
 (2, None,
  "'It's a good area. There are three rooms and a balcony.' The word for 'there' plus a list: simple and useful. Nina has a practical question."),
 (3, None,
  "'With furniture?' The word for 'with' makes the next word change its ending. Arkady doesn't hesitate."),
 (4, None,
  "'Of course, with furniture.' The first word means 'of course', one of the most useful words you can learn. Samson adds his wish."),
 (5, None,
  "'A car. A German one.' The adjective has a feminine ending, because the word for 'car' is feminine. Nina hasn't finished."),
 (6, None,
  "'I need a job too.' Literally 'to me also a job is needed'. The person who needs something comes first, in the 'to me' form. Arkady thinks fast."),
 (7, None,
  "'We could open a beauty salon for you.' The word after 'for you' means 'it's possible', and it's followed by the plain form of a verb. Then he has a better idea."),
 (8, None,
  "'Or even better: a spa!' The last word is the same as in English. Nina loves it."),
 (9, None,
  "'A spa. Let's do it!' The second word is the polite or plural 'let's'. Then she thinks of her daughter."),
 (10, None,
  "'Yulia needs to get into university.' Her name comes first, in the 'to Yulia' form, and then a word that means 'it's necessary'. Same pattern as 'I need' a moment ago. Arkady is generous."),
 (11, None,
  "'That's no problem at all.' The word for 'without' needs a special ending on the next word. Samson wants to make one thing clear."),
 (12, None,
  "'Listen, if you cheat us, there'll be trouble. Got it?' In Russian you don't even need the word 'if': the verb alone sets the condition. In the show his threat is far more colourful. Arkady tries to calm him down."),
 (13, None,
  "'Vanya, relax. This time there's no trick.' He calls Samson by his first name, the short and friendly form of Ivan. Then he complains to Nina."),
 (14, None,
  "'Why does he keep grabbing me by the throat?' The phrase in the middle means 'all the time'. Samson has a complaint of his own."),
 (15, None,
  "'And what about me?' Three little words, and the 'to me' form again. Everyone got something except him. But just then Arkady's deputy arrives, and the question is forgotten."),
 (16, "О, а вот и мой заместитель!",
  "'Oh, and here's my deputy!' The word for 'here' plus 'and' means 'here comes'. Perfect timing."),
 (16, "Пойдёмте, я вас познакомлю.",
  "'Come on, I'll introduce you.' He uses the plural 'come on', because he's taking the whole family to meet the guest."),
]

TRANSITION = "Here's the list scene again, from the top."

OUTRO = ("A flat, a car, a spa and a university place, all on one sheet of paper. "
         "Next time we meet Arkady's guests; see you then.")
CLOSING = ("anya", "Пойдёмте!")
