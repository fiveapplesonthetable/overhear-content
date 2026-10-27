ID = "domashniy-arest-s01e01-scene-08"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 1
SCENE = 8
TITLE = "Кофе и кластер  (Coffee and the Cluster)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "pasha": "anja", "secretary": "angelina"}
LABELS = {"anya": "Аркадий", "pasha": "Паша", "secretary": "Лидия Алексеевна"}
SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.01"
SOURCE_FILE = "sources/domashniy-arest/s01/e01.ru.dual.srt"
SOURCE_NOTE = ("Cues 323-372. The subtitles garble the businessman's name (Саракелян); the script uses the standard "
               "form Аракелян. Arkady's crude teasing of Pasha about his private life (cues 363-371) is left out; "
               "the narrator only says that he teases Pasha and sends him off.")

INTRO = ("The next morning, back in the mayor's office. Last time, Arkady named a humiliating condition for the "
         "job, a silly kiss, to pay Samson back for his childhood, and Samson stormed out. Now Arkady is in a fine "
         "mood: he orders coffee, and his deputy Pasha comes in with news and a big money idea. We'll hear it in "
         "Russian first; don't worry about catching every word.")

STORY = [
 ("anya", "Какое хорошее утро! Лидия Алексеевна, чашку кофе, пожалуйста.",
  "What a lovely morning! Lidia Alekseyevna, a cup of coffee, please.",
  [(323, "Какое хорошее утро"), (324, "Лидия Алексеевна"), (324, "пожалуйста")],
  "'чашечку Американо' -> 'чашку кофе'"),
 ("secretary", "Хорошо, Аркадий Борисович.", "Of course, Arkady Borisovich.",
  [(325, "Хорошо, Аркадий Борисович")], ""),
 ("pasha", "Аркаш, можно?", "Arkasha, may I come in?", [(326, "Аркаш, можно")], ""),
 ("anya", "Заходи.", "Come in.", [(327, "Заходи")], ""),
 ("pasha", "Реакция положительная. Людям нравится.", "The reaction is positive. People like it.",
  [(328, "Реакция"), (328, "положительная")],
  "'на вступление' dropped; 'Людям нравится' new, after cue 329 (the voters are in a good mood)"),
 ("anya", "Хорошо. А что с торговым центром?", "Good. And what about the shopping centre?",
  [(330, "с торговым центром что")], "word order made standard, 'у нас' dropped, 'Хорошо' added"),
 ("pasha", "Аракелян просит время. Сумма очень большая.", "Arakelyan is asking for more time. The sum is very large.",
  [(331, "просит"), (331, "сумма очень большая")], "name normalised (Саракелян -> Аракелян); 'отсрочек' -> 'время'"),
 ("anya", "Три дня ему даём. Всё.", "We give him three days. That's it.",
  [(332, "три дня ему даем"), (333, "Все")], ""),
 ("pasha", "Аркаш, мне москвичи звонят каждый день. Может, всё-таки передумаем?",
  "Arkasha, the people from Moscow call me every day. Maybe we should reconsider after all?",
  [(337, "мне москвичи звонят каждый день"), (339, "все-таки передумаем")], "'слушай' and 'мы' dropped"),
 ("anya", "Я же сказал: нет.", "I told you: no.", [(341, "сказал нет")], "'чётко' (clearly) dropped"),
 ("pasha", "Там такие деньги! Деньги рекой потекут.", "There's so much money in it! Money will flow like a river.",
  [(342, "там такие"), (344, "рекой потекут")], "'суммы' -> 'деньги', slang 'бабки' -> 'деньги'"),
 ("anya", "А потом отходы потекут.", "And then waste will flow.", [(345, "А потом отходы потекут")], ""),
 ("pasha", "Мы же бизнесом здесь занимаемся.", "But we're in business here.",
  [(346, "бизнесом здесь занимаемся")], "'вроде как' dropped, 'же' added"),
 ("anya", "Жадность, Паша, должна быть умеренная. Комнатной температуры.",
  "Greed, Pasha, should be moderate. Room temperature.",
  [(359, "Жадность, Паша, должна быть умеренная"), (360, "Комнатной температуры")], ""),
 ("anya", "Посмотри, какой у нас город прекрасный. Озёра, луга.",
  "Look what a beautiful town we have. Lakes, meadows.",
  [(349, "посмотри, какой у нас"), (349, "прекрасный"), (350, "Озера, луга")], "'городок' -> 'город'"),
 ("anya", "Мы же здесь выросли. И о людях тоже надо думать.",
  "After all, we grew up here. And you have to think about people too.",
  [(352, "здесь выросли"), (354, "И о людях тоже")], "'все-таки' -> 'же'; 'думать надо' -> 'надо думать', 'Паш' dropped"),
 ("pasha", "Я бы на твоём месте подумал.", "If I were you, I'd think about it.",
  [(361, "я бы на твоем месте подумал")], ""),
 ("anya", "Вот поэтому ты и не на моём месте.", "And that's exactly why you're not in my place.",
  [(362, "Вот поэтому"), (362, "ты и не на моём месте")], "'Паш' dropped"),
]

OPENER = "Let's go through it slowly. It's a sunny morning, and Arkady is very pleased with himself."

WALK = [
 (0, "Какое хорошее утро!",
  "'What a lovely morning!' The word for 'what a' agrees with the neuter word for 'morning'. Then he calls his secretary."),
 (0, "Лидия Алексеевна, чашку кофе, пожалуйста.",
  "'Lidia Alekseyevna, a cup of coffee, please.' First name plus father's name: that's the polite way to address "
  "someone. The cup takes the accusative ending, because it's what he wants."),
 (1, None,
  "'Of course, Arkady Borisovich.' She answers in the same polite style. Then his deputy, Pasha, puts his head round the door."),
 (2, None,
  "'Arkasha, may I come in?' The second word means 'may I', or 'is it allowed'. A handy one-word question."),
 (3, None,
  "'Come in.' Arkady uses the familiar form with Pasha. Pasha starts with the campaign news."),
 (4, None,
  "'The reaction is positive. People like it.' Yesterday Arkady announced that he's running for mayor again, and the "
  "voters seem pleased. Notice the second sentence: literally, 'to people it is pleasing'. Arkady moves on to money."),
 (5, None,
  "'Good. And what about the shopping centre?' A businessman, Arakelyan, has to pay a large sum to get the land for "
  "a new shopping centre."),
 (6, None,
  "'Arakelyan is asking for more time. The sum is very large.' Arkady is not impressed."),
 (7, None,
  "'We give him three days. That's it.' If the money doesn't come, Arkady says, the land goes to someone else. Now "
  "Pasha comes to what he really wants."),
 (8, "Аркаш, мне москвичи звонят каждый день.",
  "'Arkasha, the people from Moscow call me every day.' Literally, 'to me Muscovites call'. Some Moscow investors "
  "want to build a huge industrial complex, a 'cluster', near the town."),
 (8, "Может, всё-таки передумаем?",
  "'Maybe we should reconsider after all?' It's the same verb Arkady used yesterday with Samson, about changing "
  "your mind. Arkady has already said no."),
 (9, None,
  "'I told you: no.' The little word after 'I' adds emphasis, like 'I did tell you'. Pasha tries the money argument."),
 (10, None,
  "'There's so much money in it! Money will flow like a river.' The word for 'river' here is in the instrumental "
  "case: it means 'like a river'. Arkady answers with the same verb."),
 (11, None,
  "'And then waste will flow.' Factory waste, into the lakes. Pasha reminds him who they are."),
 (12, None,
  "'But we're in business here.' He means: we're here to make money. Arkady has a funny answer."),
 (13, None,
  "'Greed, Pasha, should be moderate. Room temperature.' Greed is fine, but not too hot. Then he points out of the window."),
 (14, None,
  "'Look what a beautiful town we have. Lakes, meadows.' The town is called something like 'Blue Lakes', and it's "
  "full of them."),
 (15, None,
  "'After all, we grew up here. And you have to think about people too.' The word for 'have to' has no person in it: "
  "it means 'one must'. In the show he adds, with a smile, 'not often, but you have to'. Pasha doesn't give up."),
 (16, None,
  "'If I were you, I'd think about it.' Literally, 'I would, in your place, think'. The small word meaning 'would' "
  "plus a past-tense verb makes the 'would' form. And Arkady's reply is the punchline."),
 (17, None,
  "'And that's exactly why you're not in my place.' After that he teases Pasha a little about his private life and "
  "sends him back to work."),
]

TRANSITION = "Now let's hear the whole conversation again."

OUTRO = ("And that's the morning meeting: coffee, a quick 'no', and a joke at Pasha's expense. Listen out for "
         "'room temperature' and 'if I were you' when you watch; see you next time.")
CLOSING = ("anya", "Всё, свободен!")
