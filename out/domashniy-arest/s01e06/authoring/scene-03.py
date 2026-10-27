ID = "domashniy-arest-s01e06-scene-03"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 6
SCENE = 3
TITLE = "Капучино с корицей  (Cappuccino with Cinnamon)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "pasha": "anja", "sizov": "angelina"}
LABELS = {"anya": "Юля", "pasha": "Паша", "sizov": "Сизов"}
SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.06"
SOURCE_FILE = "sources/domashniy-arest/s01/e06.ru.dual.srt"
SOURCE_NOTE = ("Cues 73-96. Slang 'Губер' (84) is restored to 'Губернатор', 'припарковал' (86) is simplified to "
               "'отложил', and garbled 'Самсонов – привод' (90) is adapted to 'Может, Самсонов победит'.")

INTRO = ("Across town at an upscale Sineozersk restaurant, after the debt collectors left Marina's door, "
         "Samson's teenage daughter Yulia is secretly working as a waitress to earn money without her parents knowing. "
         "Listen as Yulia takes a coffee order from acting mayor Pasha Osipenko while Pasha tries to reassure "
         "sceptical local businessman Sizov that his business project is still on track.")

STORY = [
 ("sizov", "Виски, пожалуйста. Спасибо.",
  "Whisky, please. Thank you.",
  [(73, "Виски, пожалуйста"), (74, "Спасибо")], ""),
 ("pasha", "Девушка, принесите мне капучино без корицы.",
  "Miss, bring me a cappuccino without cinnamon.",
  [(75, "Девушка"), (75, "мне капучино без корицы")], "'принесите-ка' -> 'принесите'"),
 ("anya", "Хорошо, сейчас принесу.",
  "All right, I'll bring it right now.",
  [(76, "Хорошо")], "'сейчас принесу' added"),
 ("pasha", "А впрочем, давайте с корицей!",
  "Or rather, make it with cinnamon!",
  [(77, "А впрочем, давайте с корицей")], ""),
 ("pasha", "У многих из вас появились сомнения. Хочу сказать вам.",
  "Many of you have begun to have doubts. I want to tell you.",
  [(78, "у многих из вас появились сомнения"), (79, "хочу сказать вам")], ""),
 ("pasha", "Процесс идёт, всё хорошо. Кластер будет построен!",
  "The process is moving along, everything is fine. The cluster will be built!",
  [(80, "Процесс"), (81, "Кластер будет построен")], "cue 80 simplified to A1"),
 ("pasha", "От вас я по-прежнему жду участия. Всё.",
  "I still expect participation from you. That is all.",
  [(82, "От вас я по-прежнему жду участия"), (83, "Всё")], ""),
 ("sizov", "Паша, скажи лучше. Губернатор с нами?",
  "Pasha, tell us instead. Is the governor with us?",
  [(84, "скажи лучше"), (84, "с нами")], "colloquial 'Паш... Губер' -> 'Паша... Губернатор'"),
 ("pasha", "Конечно, он с нами!",
  "Of course he is with us!",
  [(85, "Естественно")], "'Естественно' -> 'Конечно, он с нами!'"),
 ("sizov", "А я знаю, что он отложил вопрос. Он ждёт результатов выборов.",
  "But I know that he put the question off. He is waiting for the election results.",
  [(86, "А я знаю, что он"), (86, "вопрос"), (87, "Ждёт результатов выборов")],
  "slang 'припарковал' -> 'отложил'"),
 ("pasha", "Смешно! Какие результаты выборов могут быть?",
  "That's funny! What election results could there possibly be?",
  [(88, "смешно. Какие результаты выборов могут быть")], ""),
 ("sizov", "Не знаю. Может, Самсонов победит.",
  "I don't know. Maybe Samsonov will win.",
  [(89, "Не знаю"), (90, "Самсонов")],
  "cue 90 garbled 'Самсонов – привод' -> 'Может, Самсонов победит'"),
 ("pasha", "Спокойно! Здесь у нас сидит председатель избиркома. Сейчас мы у неё всё узнаем.",
  "Stay calm! The chairwoman of the election commission is sitting right here with us. Right now we will find out everything from her.",
  [(91, "Спокойно"), (92, "у нас здесь"), (92, "председатель избиркома"), (93, "Сейчас мы у неё всё узнаем")],
  "'присутствует' -> 'сидит'"),
 ("anya", "Вот ваш капучино.",
  "Here is your cappuccino.",
  [(94, "Ваш капучино")], "'Вот' added"),
 ("pasha", "Милая, я же просил с корицей!",
  "My dear, I asked for it with cinnamon!",
  [(95, "Милая, я"), (95, "просил с корицей")], "'ж' -> 'же'"),
 ("anya", "А, простите! Сейчас сделаю.",
  "Oh, forgive me! I'll do it right now.",
  [(96, "А, простите, сейчас")], "'сделаю' added"),
]

OPENER = ("Let's go back through the scene step by step. Wearing a waitress apron, teenage Yulia stands beside a "
          "long restaurant table where Pasha Osipenko is meeting with Sineozersk businessmen.")

WALK = [
 (0, None,
  "'Whisky, please. Thank you.' The businessman Sizov orders a drink, and then Pasha turns to Yulia."),
 (1, None,
  "'Miss, bring me a cappuccino without cinnamon.' In Russian restaurants, 'young woman' is the polite way to "
  "call a waitress. Notice that 'without' takes the genitive case."),
 (2, None,
  "'All right, I'll bring it right now.' Yulia turns to leave, and Pasha immediately changes his mind."),
 (3, None,
  "'Or rather, make it with cinnamon!' Now 'with' takes the instrumental case of 'cinnamon'. Pasha then stands up "
  "to address the businessmen."),
 (4, "У многих из вас появились сомнения.",
  "'Many of you have begun to have doubts.' Literally 'by many out of you doubts have appeared'."),
 (4, "Хочу сказать вам.",
  "'I want to tell you.' He puts on his most confident smile."),
 (5, "Процесс идёт, всё хорошо.",
  "'The process is moving along, everything is fine.' Literally 'the process goes'."),
 (5, "Кластер будет построен!",
  "'The cluster will be built!' He uses the future tense of 'to be' with the short passive participle 'built'."),
 (6, None,
  "'I still expect participation from you. That is all.' The verb 'to wait for' or 'to expect' takes the genitive "
  "case of 'participation'."),
 (7, None,
  "'Pasha, tell us instead. Is the governor with us?' Sizov cuts straight to the point."),
 (8, None,
  "'Of course he is with us!' Pasha doesn't hesitate, but Sizov knows better."),
 (9, "А я знаю, что он отложил вопрос.",
  "'But I know that he put the question off.' The perfective verb means 'laid aside' or 'postponed'."),
 (9, "Он ждёт результатов выборов.",
  "'He is waiting for the election results.' After 'waits for', 'results' is in the genitive plural."),
 (10, None,
  "'That's funny! What election results could there possibly be?' Pasha scoffs at the idea that he could lose."),
 (11, None,
  "'I don't know. Maybe Samsonov will win.' After the television scandal over the Society for the Blind, everyone "
  "in town is talking about Samsonov."),
 (12, "Спокойно! Здесь у нас сидит председатель избиркома.",
  "'Stay calm! The chairwoman of the election commission is sitting right here with us.' The compound word for "
  "'election commission' is a classic Russian abbreviation."),
 (12, "Сейчас мы у неё всё узнаем.",
  "'Right now we will find out everything from her.' Just then, Yulia sets Pasha's cup down on the table."),
 (13, None,
  "'Here is your cappuccino.' Notice that 'cappuccino' is an indeclinable masculine noun in Russian, so it takes "
  "the masculine possessive 'your'."),
 (14, None,
  "'My dear, I asked for it with cinnamon!' Pasha looks at the cup in annoyance."),
 (15, None,
  "'Oh, forgive me! I'll do it right now.' Yulia apologizes and hurries back toward the bar."),
]

TRANSITION = "Now let's hear the whole restaurant scene again from the start."
OUTRO = ("So Yulia is waiting tables for her father's rival, and the businessmen are nervous about the election. "
         "Next we'll hear what the chairwoman of the election commission tells Pasha at the table; see you there.")
CLOSING = ("pasha", "Милая, я же просил с корицей!")
