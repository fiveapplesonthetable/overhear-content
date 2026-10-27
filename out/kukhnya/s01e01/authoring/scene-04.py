ID = "kukhnya-s01e01-scene-04"
TITLE = "Утро после клуба  (The Morning After the Club)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "max": "anja"}
LABELS = {"anya": "Вика", "max": "Максим"}
SOURCE_NAME = "Кухня (Kukhnya) S1.01"
SOURCE_FILE = "sources/kukhnya/s01/e01.ru.dual.srt"

INTRO = ("This scene takes place on the morning after a lively night at the club. "
         "Max is quietly trying to leave the apartment, but Vika wakes up and catches him at the door. "
         "As always, listen to the whole conversation in Russian first, "
         "and then we will break it down together in English.")

STORY = [
 ("max", "Мне уже идти надо.", "I need to go now.",
  [(24, "мне идти надо")], "уже added for flow"),
 ("anya", "Ты что, убегаешь?", "What, are you running away?",
  [(25, "Ты что"), (25, "убегаешь")], "типа omitted for A1 clarity"),
 ("max", "Почему убегаю? Нет, просто ухожу.", "Why running away? No, I'm just leaving.",
  [(26, "Почему убегаю"), (26, "Нет, просто ухожу")], ""),
 ("anya", "Вот так? И всё?", "Just like that? And that's all?",
  [(27, "Вот так вот"), (27, "И все")], "вот dropped from Вот так вот"),
 ("anya", "А то, что между нами было?", "What about what was between us?",
  [(28, "то, что между нами было")], ""),
 ("max", "Спасибо. Прикольно было.", "Thank you. It was fun.",
  [(29, "Спасибо"), (29, "прикольно было")], ""),
 ("anya", "Прикольно, и всё?", "Fun, and that's it?",
  [(30, "Прикольно и все")], ""),
 ("max", "А что ещё?", "What else?",
  [(31, "А что ещё")], ""),
 ("anya", "Да ладно тебе.", "Oh, come on.",
  [(32, "Да ладно")], "тебе added for natural dialogue"),
 ("max", "Нет, денег у меня нет.", "No, I have no money.",
  [(33, "Нет, денег у меня нет")], ""),
 ("max", "Мы с тобой так не договаривались.", "You and I didn't agree to that.",
  [(34, "мы с тобой так не договаривались")], ""),
 ("anya", "Мне не нужны твои деньги.", "I don't need your money.",
  [], "new line"),
 ("max", "Тогда я пошёл. У меня дела.", "Then I am off. I have things to do.",
  [], "new line"),
 ("anya", "Уходи. И не возвращайся сюда.", "Leave. And do not come back here.",
  [], "new line"),
]

OPENER = "Let's go through their awkward morning exchange step by step. Max is eager to leave, but Vika has questions."

WALK = [
 (0, "Мне уже идти надо.",
  "'I need to go now.' The first word is the dative form of 'I', meaning 'to me'. Then comes the verb 'to go' paired with 'necessary'. Max wants to slip away quietly."),
 (1, "Ты что, убегаешь?",
  "'What, are you running away?' Vika uses a very common conversational opening asking what he is doing, followed by the verb 'to run away' in the present tense."),
 (2, "Почему убегаю?",
  "'Why running away?' Max repeats her verb with the question word 'why' to buy himself a second. Then he denies it."),
 (2, "Нет, просто ухожу.",
  "'No, I'm just leaving.' The little word in the middle means 'simply' or 'just'. Max makes a distinction between fleeing and simply walking out."),
 (3, "Вот так? И всё?",
  "'Just like that? And that's all?' Two tiny questions expressing disbelief. The first phrase means 'just like that', and the second asks if that is really the end of it."),
 (4, None,
  "'What about what was between us?' The conjunction at the start introduces a contrast, followed by the phrase 'between us' with the instrumental case."),
 (5, "Спасибо. Прикольно было.",
  "'Thank you. It was fun.' A casual thank you followed by a colloquial word meaning 'cool' or 'fun'. Not quite the romantic sentiment Vika hoped for."),
 (6, None,
  "'Fun, and that's it?' Vika repeats his casual adjective with incredulity, pointing out how inadequate that response sounds."),
 (7, None,
  "'What else?' A blunt three-word question. Max genuinely does not see what more needs to be said."),
 (8, None,
  "'Oh, come on.' A friendly or exasperated idiom used to tell someone to stop making silly excuses."),
 (9, None,
  "'No, I have no money.' Max assumes she might be asking for payment. In Russian, stating you lack something uses the genitive case with the negative word."),
 (10, None,
  "'You and I didn't agree to that.' Literally, 'we with you so did not agree'. Russian prefers saying 'we with you' where English says 'you and I'."),
 (11, None,
  "'I don't need your money.' Literally, 'to me are not needed your moneys'. Vika is insulted by the implication."),
 (12, "Тогда я пошёл.",
  "'Then I am off.' In spoken Russian, the past tense of 'to go' is often used to announce an immediate departure, like saying 'I'm out of here'."),
 (13, "Уходи. И не возвращайся сюда.",
  "'Leave. And do not come back here.' Two strong imperatives. The first tells him to walk out, and the second tells him never to return."),
]

TRANSITION = "Alright, let's hear the whole conversation once more."

OUTRO = ("That concludes our fourth scene. When you watch the first episode of Kukhnya, "
         "listen for Max trying to slip away and Vika asking if he is really running away. "
         "You will recognise these lines right away. See you next time!")

CLOSING = ("anya", "До встречи!")
