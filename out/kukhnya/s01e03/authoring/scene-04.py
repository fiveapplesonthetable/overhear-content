ID = "kukhnya-s01e03-scene-04"
TITLE = "Опасный разговор  (A Dangerous Conversation)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "vadim": "anja"}
LABELS = {"anya": "Макс", "vadim": "Вадим"}
SOURCE_NAME = "Кухня (Kukhnya) S1.03"
SOURCE_FILE = "sources/kukhnya/s01/e03.ru.dual.srt"

INTRO = ("This scene takes place outside restaurant Claude Monet in the third episode. "
         "A stern prosecutor named Vadim confronts Max and demands to know who Vika is dating. "
         "Listen to their tense conversation in Russian first, and then we will break it down together.")

STORY = [
 ("vadim", "Слышь, малой, есть разговор.", "Listen, kid, I want to talk.",
  [(132, "разговор есть")], "малой kept"),
 ("anya", "Что вам нужно?", "What do you need?",
  [], "new line"),
 ("vadim", "Тут у вас работает Вика.", "Vika works here with you.",
  [(133, "Тут у вас работает Вика")], ""),
 ("vadim", "Виктория Сергеевна.", "Viktoria Sergeyevna.",
  [(133, "Виктория Сергеевна")], ""),
 ("vadim", "С кем она тут встречается?", "Who is she seeing here?",
  [(134, "с кем она у вас тут встречается")], ""),
 ("vadim", "Ну, почему молчим?", "Well, why are we silent?",
  [], "new line"),
 ("anya", "Почему я должен отвечать?", "Why should I answer?",
  [(136, "я тебе должен отвечать")], ""),
 ("vadim", "Не хочешь отвечать здесь?", "Don't want to answer here?",
  [(137, "Не хочешь отвечать здесь")], ""),
 ("vadim", "Ответишь у меня в прокуратуре.", "You'll answer in my prosecutor's office.",
  [(138, "у меня в прокуратуре")], ""),
 ("vadim", "Ты меня понял?", "Did you understand me?",
  [(139, "Понял")], ""),
 ("anya", "Понял, всё понял.", "Understood, understood everything.",
  [(140, "Понял, понял")], ""),
 ("anya", "Она ни с кем не встречается.", "She is not seeing anyone.",
  [(141, "она здесь ни с кем не встречается")], ""),
 ("vadim", "Ну, смотри у меня.", "Well, you watch yourself.",
  [(142, "Ну, смотри")], ""),
 ("anya", "Надо срочно предупредить всех.", "Must urgently warn everyone.",
  [(160, "Надо предупредить")], "simplified"),
]

OPENER = "Let's examine this threatening interrogation step by step."

WALK = [
 (0, None,
  "'Listen, kid, I want to talk.' A gruff stranger corners Max outside the restaurant."),
 (1, None,
  "'What do you need?' Max responds cautiously to the aggressive tone."),
 (2, None,
  "'Vika works here with you.' The stranger names art director Vika."),
 (3, None,
  "'Viktoria Sergeyevna.' Adding her formal patronymic to show authority."),
 (4, None,
  "'Who is she seeing here?' Demanding to know about her romantic life."),
 (5, None,
  "'Well, why are we silent?' Pressuring him to answer immediately."),
 (6, None,
  "'Why should I answer?' Max tries to stand his ground."),
 (7, None,
  "'Don't want to answer here?' The stranger issues an ominous threat."),
 (8, None,
  "'You'll answer in my prosecutor's office.' Revealing his powerful law-enforcement background."),
 (9, None,
  "'Did you understand me?' Making sure the threat landed."),
 (10, None,
  "'Understood, understood everything.' Backing down quickly in the face of serious trouble."),
 (11, None,
  "'She is not seeing anyone.' Max protects Vika and himself with a firm denial."),
 (12, None,
  "'Well, you watch yourself.' A parting warning to keep quiet."),
 (13, None,
  "'Must urgently warn everyone.' Realizing the immense danger of the situation."),
]

TRANSITION = "Alright, let's hear the whole dialogue once more."

OUTRO = ("That is our fourth scene. In Kukhnya, running into an angry prosecutor is the last thing Max needed. "
         "See you next time!")

CLOSING = ("anya", "До встречи!")
