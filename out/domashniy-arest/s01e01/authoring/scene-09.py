ID = "domashniy-arest-s01e01-scene-09"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 1
SCENE = 9
TITLE = "Я хочу на море!  (I Want to Go to the Sea!)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "samson": "anja", "yulia": "angelina"}
LABELS = {"anya": "Нина", "samson": "Самсон", "yulia": "Юля"}
SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.01"
SOURCE_FILE = "sources/domashniy-arest/s01/e01.ru.dual.srt"
SOURCE_NOTE = ("Cues 373-428. Arkady is absent, so Nina is the viewpoint character (`anya`, label Нина). The crude "
               "talk about the 'kiss' (cues 395-399, 408-411) is folded into Samson's 'it's shameful'; slang "
               "(пучком, врубилась, коммуналка kept as the show's key word) simplified.")

INTRO = ("Now we're in the communal flat, in the Samsonovs' small room. Last time, over his morning coffee, Arkady "
         "turned down Pasha's big factory deal. Meanwhile Samson, who quit his job yesterday on Arkady's word, is on "
         "the phone to his old boss, trying to get it back, while his wife Nina listens. We'll hear it in Russian "
         "first; don't worry about catching every word.")

STORY = [
 ("samson", "Николай Филиппович, простите меня, пожалуйста. Я сам не знаю, как это произошло.",
  "Nikolai Filippovich, please forgive me. I don't know myself how it happened.",
  [(374, "простите меня"), (375, "я сам не знаю, как это произошло")], "'ради бога' -> 'пожалуйста'"),
 ("samson", "Я вчера ел маринованные грибы. Может, один гриб был плохой.",
  "Yesterday I ate pickled mushrooms. Maybe one mushroom was bad.",
  [(376, "Я вчера")], "adapted from cues 376-377 ('грибов маринованных хватанул', 'какой-то галлюциногенный попался')"),
 ("anya", "Тише!", "Quiet!", [(378, "Тише")], ""),
 ("samson", "А что вы так грубо разговариваете?", "Why are you talking so rudely?",
  [(380, "так грубо разговариваете")], "'чего ... сразу' -> 'что'"),
 ("anya", "Самсонов, ну я же просила!", "Samsonov, I asked you not to!", [(381, "Самсонов, ну я же просила")], ""),
 ("samson", "Ну что, довольна? Теперь новую работу искать.", "Well, happy now? Now I have to look for a new job.",
  [(384, "Ну что, довольна"), (388, "Теперь новую работу искать")], ""),
 ("anya", "Тебе же предложили работу. Что, плохая работа?", "But you were offered a job. What, is it a bad job?",
  [(391, "тебе же предложили работу"), (393, "Что, плохая работа")], "'что ли' dropped"),
 ("samson", "Подожди, Нин, ты не поняла. Это же стыдно!", "Wait, Nina, you don't get it. It's shameful!",
  [(394, "Подожди, Нин, ты не")], "slang 'врубилась' -> 'поняла'; 'Это же стыдно!' new, replacing the crude cue 395"),
 ("anya", "Ну и что такого?", "So what?", [(396, "Ну и что такого")], ""),
 ("anya", "Юле бы дублёнку купили, Славику бы ноутбук.",
  "We could have bought Yulia a sheepskin coat, and Slavik a laptop.",
  [(402, "бы дубленку купили"), (403, "Славику бы ноутбук")], "'Юльке' -> 'Юле'"),
 ("samson", "Нин, ты что?", "Nina, what's got into you?", [(405, "Нин, ты")], "'чего гонишься' (slang) -> 'что'"),
 ("anya", "Меня уже тошнит от этой коммуналки! У нас труба уже неделю течёт.",
  "I'm sick of this communal flat! Our pipe has been leaking for a week now.",
  [(415, "меня уже"), (415, "тошнит от этой коммуналки"), (416, "уже неделю течет")],
  "'вот' dropped; 'стояк' (riser pipe) -> 'труба'"),
 ("samson", "Я купил герметик. Всё будет нормально.", "I've bought sealant. Everything will be fine.",
  [(417, "я купил герметик"), (417, "все будет")], "slang 'пучком' -> 'нормально'"),
 ("anya", "Нормально? Она через неделю снова потечёт!", "Fine? It'll be leaking again in a week!",
  [(418, "через неделю снова потечет")], "'Пучком!' -> 'Нормально?'; 'он' (стояк) -> 'она' (труба)"),
 ("anya", "Я уже не могу готовить, стирать, убирать. Я хочу на море!",
  "I can't take the cooking, washing and cleaning any more. I want to go to the sea!",
  [(419, "я уже не могу"), (420, "готовить"), (421, "стирать, убирать"), (422, "А я хочу на море")],
  "cues 419-422 joined, 'вот это вот' dropped; 'А' dropped from 'А я хочу на море'"),
 ("anya", "Я хочу нормально жить! Я хочу биде, понимаешь?",
  "I want to live like a normal person! I want a bidet, do you understand?",
  [(423, "Я хочу нормально жить"), (424, "хочу, понимаешь")], "cue 424 'Беде' (misheard) -> 'биде'"),
 ("yulia", "Мам, а что такое биде?", "Mum, what's a bidet?", [(426, "Мам"), (427, "Что такое")],
  "'а' added; cue 427 'беде' -> 'биде'"),
 ("anya", "В интернете посмотри.", "Look it up on the internet.", [],
  "after cue 428 ('Google it')"),
]

OPENER = "Let's go through it together. Samson is calling his old boss, the man he was so rude to yesterday."

WALK = [
 (0, "Николай Филиппович, простите меня, пожалуйста.",
  "'Nikolai Filippovich, please forgive me.' He uses the boss's first name and father's name, and the polite form "
  "of 'forgive'."),
 (0, "Я сам не знаю, как это произошло.",
  "'I don't know myself how it happened.' The word for 'myself' is masculine here, because Samson is a man. Then "
  "he invents an excuse."),
 (1, None,
  "'Yesterday I ate pickled mushrooms. Maybe one mushroom was bad.' So it was the mushrooms talking, not him. Nina wants "
  "him to keep his voice down."),
 (2, None,
  "'Quiet!' Literally, 'more quietly'. But the boss is not friendly, and Samson starts to lose his temper."),
 (3, None,
  "'Why are you talking so rudely?' He still uses the polite 'you' with his boss, even when he's angry. Nina is in despair."),
 (4, None,
  "'Samsonov, I asked you not to!' She calls her husband by his surname, a sign she is really cross. Notice the "
  "feminine ending on 'asked', because Nina is a woman. The call ends badly."),
 (5, "Ну что, довольна?",
  "'Well, happy now?' Nina was the one who sent him to make peace with his childhood friend, Arkady."),
 (5, "Теперь новую работу искать.",
  "'Now I have to look for a new job.' Literally, 'now a new job to look for'. Nina has a different idea."),
 (6, None,
  "'But you were offered a job. What, is it a bad job?' Literally, 'to you they offered work'. She means "
  "Arkady's offer."),
 (7, None,
  "'Wait, Nina, you don't get it. It's shameful!' He means the humiliating kiss Arkady asked for. Nina is not impressed."),
 (8, None,
  "'So what?' Short and very common. And she starts to dream."),
 (9, None,
  "'We could have bought Yulia a sheepskin coat, and Slavik a laptop.' The little word that means 'would' turns "
  "this into a wish about what could have been. The names have the dative ending: 'for Yulia', 'for Slavik'. "
  "Samson can't believe his wife."),
 (10, None,
  "'Nina, what's got into you?' And now Nina says what she really feels."),
 (11, "Меня уже тошнит от этой коммуналки!",
  "'I'm sick of this communal flat!' Literally, 'this communal flat makes me feel sick'."),
 (11, "У нас труба уже неделю течёт.",
  "'Our pipe has been leaking for a week now.' Russian uses the present tense here, where English says 'has been "
  "leaking'. Samson has a plan."),
 (12, None,
  "'I've bought sealant. Everything will be fine.' Nina throws his word back at him."),
 (13, None,
  "'Fine? It'll be leaking again in a week!' The word for 'it' is feminine, because the word for 'pipe' is feminine."),
 (14, "Я уже не могу готовить, стирать, убирать.",
  "'I can't take the cooking, washing and cleaning any more.' Three verbs in a row, all in the basic form after "
  "'I can't'."),
 (14, "Я хочу на море!",
  "'I want to go to the sea!' There's no verb for 'go': 'I want to the sea' is enough."),
 (15, None,
  "'I want to live like a normal person! I want a bidet, do you understand?' A bidet, the little bathroom basin: "
  "the dream of a proper flat. Their daughter has a question."),
 (16, None,
  "'Mum, what's a bidet?' A handy pattern for asking what any word means. And Nina's answer is very modern."),
 (17, None,
  "'Look it up on the internet.' The verb is a command, 'look', and it comes at the end for emphasis. What every "
  "parent says to a teenager these days."),
]

TRANSITION = "Let's hear the whole family scene once more."

OUTRO = ("That's all for this scene: a lost job, a leaking pipe, and a dream of the sea. Listen out for Nina's "
         "'I want to go to the sea' when you watch; see you next time.")
CLOSING = ("anya", "Всё, пока!")
