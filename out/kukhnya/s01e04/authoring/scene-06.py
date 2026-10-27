ID = "kukhnya-s01e04-scene-06"
TITLE = "Гнев шефа  (The Chef's Wrath)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "chef": "anja", "elena": "angelina"}
LABELS = {"anya": "Макс", "chef": "Шеф", "elena": "Елена"}
SOURCE_NAME = "Кухня (Kukhnya) S1.04"
SOURCE_FILE = "sources/kukhnya/s01/e04.ru.dual.srt"

INTRO = ("In this scene, Chef Viktor Barinov discovers that rival restaurant Arcobaleno is trying to recruit his kitchen staff. "
         "After an angry phone call with rival chef Elena, Barinov confronts his cooks and demands to know who applied for the job. "
         "Listen to the tense scene in Russian first, and then we will examine every line.")

STORY = [
 ("chef", "Я съем свой поварской колпак!", "I will eat my chef's hat!",
  [(52, "Я съем свой колпак")], ""),
 ("chef", "Никто из моих людей не пойдёт к вам!", "None of my people will go to you!",
  [(52, "кто-то из моих ходил к вам")], "negated, пойдёт adapted"),
 ("elena", "Тогда приятного вам аппетита, Виктор!", "Then bon appétit to you, Viktor!",
  [(53, "Тогда приятного аппетита")], "Виктор added"),
 ("chef", "Ах вы, неблагодарные люди!", "Oh you, ungrateful people!",
  [(54, "неблагодарные")], "сволочи replaced for A1"),
 ("chef", "Чьё это резюме лежит на столе?", "Whose résumé is lying on the table?",
  [(55, "Чье это")], "резюме лежит на столе added"),
 ("chef", "Кто ходил на собеседование к конкурентам?", "Who went for an interview to the competitors?",
  [], "new line"),
 ("anya", "Шеф, мы ничего об этом не знаем.", "Chef, we know nothing about this.",
  [], "new line"),
 ("chef", "Почему вы все молчите?", "Why are you all silent?",
  [(56, "Молчите")], "инвалиды replaced for clean A1"),
 ("chef", "Вы думаете, я ничего не узнаю?", "Do you think I won't find out anything?",
  [], "new line"),
 ("anya", "Мы верны нашему ресторану.", "We are loyal to our restaurant.",
  [], "new line"),
 ("chef", "Ну что ж, я сам всё выясню!", "Well then, I will find out everything myself!",
  [(57, "Ничтуж")], "ну что ж adapted from subtitled ничтуж"),
 ("chef", "Предатель будет немедленно уволен!", "The traitor will be immediately fired!",
  [], "new line"),
 ("anya", "Кажется, шеф в настоящей ярости.", "It seems the chef is in a real fury.",
  [], "new line"),
 ("anya", "Надо быть очень осторожным сегодня.", "Must be very careful today.",
  [], "new line"),
]

OPENER = "Let's examine this fiery interrogation line by line."

WALK = [
 (0, None,
  "'I will eat my chef's hat!' Barinov makes an outrageous bet on the phone."),
 (1, None,
  "'None of my people will go to you!' Insisting that his kitchen staff is entirely loyal."),
 (2, None,
  "'Then bon appétit to you, Viktor!' Elena mocks his boast with sweet sarcasm."),
 (3, None,
  "'Oh you, ungrateful people!' Cursing the rival restaurant after slamming down the phone."),
 (4, None,
  "'Whose résumé is lying on the table?' Spotting evidence of job hunting in his kitchen."),
 (5, None,
  "'Who went for an interview to the competitors?' Demanding a confession from his team."),
 (6, None,
  "'Chef, we know nothing about this.' Max tries to deflect the dangerous suspicion."),
 (7, None,
  "'Why are you all silent?' Infuriated by the guilty silence of the cooks."),
 (8, None,
  "'Do you think I won't find out anything?' Promising to uncover the truth."),
 (9, None,
  "'We are loyal to our restaurant.' Reaffirming devotion to Claude Monet."),
 (10, None,
  "'Well then, I will find out everything myself!' Resolving to investigate the betrayal personally."),
 (11, None,
  "'The traitor will be immediately fired!' Warning of ruthless consequences for disloyalty."),
 (12, None,
  "'It seems the chef is in a real fury.' Max observes the escalating storm."),
 (13, None,
  "'Must be very careful today.' Noting the need to keep a low profile."),
]

TRANSITION = "Now let's listen to the whole conversation once again."

OUTRO = ("That concludes our sixth scene. In Kukhnya, betraying Chef Barinov for a rival restaurant "
         "is a dangerous game that nobody wins easily. See you next time!")

CLOSING = ("anya", "До встречи!")
