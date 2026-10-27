ID = "kukhnya-s01e01-scene-05"
TITLE = "Мечта о кухне  (Dream of the Kitchen)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "dmitry": "anja"}
LABELS = {"dmitry": "Нагиев"}
SOURCE_NAME = "Кухня (Kukhnya) S1.01"
SOURCE_FILE = "sources/kukhnya/s01/e01.ru.dual.srt"

INTRO = ("In this scene, we learn about the passion for cooking that started in childhood and led to military kitchen duty. "
         "Celebrity restaurant owner Dmitry Nagiyev visits the mess hall, tastes the soup, and offers an incredible opportunity. "
         "Listen to the story in Russian first, and then we will examine every line together.")

STORY = [
 ("anya", "Я всегда знала, что буду поваром.", "I always knew I would be a chef.",
  [(35, "что буду поваром")], "знал -> знала"),
 ("anya", "Не пожарным и не космонавтом.", "Not a firefighter and not an astronaut.",
  [(36, "не пожарным, не космонавтом")], "shortened for A1"),
 ("anya", "Даже не президентом. А именно поваром.", "Not even president. Exactly a chef.",
  [(37, "Даже не президентом"), (37, "А именно поваром")], ""),
 ("dmitry", "Вот он, наш герой!", "Here he is, our hero!",
  [(46, "Вот он наш герой")], ""),
 ("dmitry", "Мне очень понравилась ваша солянка.", "I really liked your solyanka.",
  [(47, "Мне очень понравилась ваша солянка")], ""),
 ("anya", "Спасибо! Я очень старалась.", "Thank you! I tried very hard.",
  [(44, "мои старания")], "старания -> старалась"),
 ("dmitry", "Молодец. Из ничего практически шедевр.", "Well done. Practically a masterpiece out of nothing.",
  [(48, "Молодец"), (48, "Из ничего практически шедевр")], ""),
 ("dmitry", "Хотите поработать в хорошем ресторане?", "Would you like to work in a good restaurant?",
  [(49, "поработать в хорошем ресторане")], "framed as direct question"),
 ("anya", "Конечно! Это моя мечта.", "Of course! That is my dream.",
  [], "new line"),
 ("dmitry", "Милости просим. Буду рад.", "You are welcome. I will be glad.",
  [(50, "милости просим, буду рад")], ""),
 ("dmitry", "Я говорю совершенно серьёзно.", "I am speaking completely seriously.",
  [(50, "Я серьезно")], "adapted"),
 ("anya", "В каком ресторане?", "In which restaurant?",
  [], "new line"),
 ("dmitry", "Ресторан Клод Моне в Москве.", "Restaurant Claude Monet in Moscow.",
  [(51, "Ресторан Клод Мане"), (51, "в Москве")], ""),
 ("anya", "Спасибо огромное! Я обязательно приду.", "Thank you very much! I will definitely come.",
  [], "new line"),
]

OPENER = "Let's examine how a simple army soup opened the door to Moscow's culinary elite."

WALK = [
 (0, None,
  "'I always knew I would be a chef.' The first words mean 'I always knew', followed by 'that I will be a chef' using the instrumental case."),
 (1, None,
  "'Not a firefighter and not an astronaut.' Negative particles are repeated before each profession in the instrumental case."),
 (2, "Даже не президентом.",
  "'Not even president.' The word at the start means 'even', adding emphasis."),
 (2, "А именно поваром.",
  "'Exactly a chef.' The contrastive conjunction is paired with an adverb meaning 'namely' or 'precisely'."),
 (3, None,
  "'Here he is, our hero!' A proud exclamation introducing the talented cook."),
 (4, None,
  "'I really liked your solyanka.' The past-tense verb agrees with the feminine noun for the traditional sour soup."),
 (5, "Спасибо! Я очень старалась.",
  "'Thank you! I tried very hard.' A grateful reply using the past tense feminine form of the verb 'to try'."),
 (6, "Молодец.",
  "'Well done.' The quintessential Russian word of praise."),
 (6, "Из ничего практически шедевр.",
  "'Practically a masterpiece out of nothing.' High praise from the celebrity guest, noting how great food can be made from basic ingredients."),
 (7, None,
  "'Would you like to work in a good restaurant?' An invitation framed politely as a question about what the cook wants to do."),
 (8, None,
  "'Of course! That is my dream.' A passionate response using the common word for 'dream'."),
 (9, "Милости просим. Буду рад.",
  "'You are welcome. I will be glad.' A warm traditional Russian formula of hospitality followed by a promise of being delighted to see them."),
 (10, None,
  "'I am speaking completely seriously.' Reassuring the young cook that this is a genuine professional job offer."),
 (12, "Ресторан Клод Моне в Москве.",
  "'Restaurant Claude Monet in Moscow.' Naming the top French fine-dining venue in the capital."),
 (13, "Спасибо огромное! Я обязательно приду.",
  "'Thank you very much! I will definitely come.' An enthusiastic promise using the adverb for 'definitely'."),
]

TRANSITION = "Now let's listen to the whole conversation once again."

OUTRO = ("That is our fifth scene. In Kukhnya, this fateful meeting sets the entire story in motion, "
         "leading our cook straight to the prestigious kitchen of Claude Monet. See you next time!")

CLOSING = ("anya", "До встречи!")
