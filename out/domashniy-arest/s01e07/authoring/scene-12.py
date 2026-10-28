# domashniy-arest/s01e07/scene-12.py
ID = "domashniy-arest-s01e07-scene-12"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 7
SCENE = 12
TITLE = "Он тебя очаровал  (He Charmed You)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
SOURCE_NAME = "Домашний арест, Сезон 1, Эпизод 7"
SOURCE_FILE = "sources/domashniy-arest/s01/e07.ru.dual.srt"
VOICES = {"narrator": "sky", "dean": "anja", "marina": "angelina"}
LABELS = {"dean": "Эдуард Владимирович", "marina": "Марина"}
INTRO = "Previously, inside the trauma doctor's office, Arkady dropped to his knees and begged for a fake cast in the name of love until the embarrassed doctor finally sent him into the dressing room. Meanwhile, waiting out in the hospital corridor, Marina's older boyfriend Eduard grows jealous and asks why she cares so much about Arkady."
STORY = [
    ("marina", "Не надо, Эдик.", "Don't, Edik.", [(483, 'Не надо'), (488, 'Эдик')], "added Эдик from cue 488"),
    ("dean", "Мне кажется, я догадываюсь, почему мы здесь.", "I think I can guess why we are here.", [(485, 'Мне кажется, я догадываюсь, почему мы здесь')], ""),
    ("dean", "Ты к нему что-то чувствуешь?", "Do you feel something for him?", [(486, 'Ты к нему что-то чувствуешь?')], ""),
    ("marina", "Что за глупость? Эдик, мне его просто жалко.", "What nonsense is that? Edik, I just feel sorry for him.", [(487, 'Что за глупость?'), (488, 'Эдик, мне его просто жалко')], "combined cues 487-488"),
    ("dean", "Нет, всё правильно. Он тебя очаровал.", "No, it all makes sense. He charmed you.", [(489, 'Нет'), (489, 'всё правильно'), (491, 'Он тебя очаровал')], "combined cues 489 and 491"),
    ("marina", "Конечно!", "Of course!", [(492, 'Конечно')], ""),
    ("dean", "Зачем тебе старик, когда рядом такой шустрый молодой сосед?", "Why do you need an old man when there's such a lively young neighbor nearby?", [(493, 'Зачем тебе старик'), (494, 'когда рядом такой шустрый молодой')], "replaced archaic повес with сосед"),
    ("marina", "Перестань! Никто меня не очаровал.", "Stop it! Nobody charmed me.", [(495, 'Перестань'), (496, 'Никто меня не очаровал')], "combined cues 495-496"),
    ("dean", "Никто? Даже я?", "Nobody? Not even me?", [(497, 'Никто? Даже я?')], ""),
    ("marina", "Хватит, Эдик! Это я должна обижаться.", "Enough, Edik! I'm the one who should be offended.", [(498, 'Хватит, Эдик'), (500, 'это я должна обижаться')], "combined cues 498 and 500"),
    ("dean", "Прости меня, я виноват.", "Forgive me, it's my fault.", [(501, 'Прости меня, я виноват')], ""),
    ("dean", "Прости, я исправлю свою вину.", "Forgive me, I will make up for my fault.", [(502, 'Прости'), (502, 'вино')], "simplified заглажу and fixed ASR свое вино to свою вину"),
    ("marina", "Мы уже поедем домой?", "Are we going home now?", [(503, 'Уже поедем домой?')], "added Мы"),
    ("dean", "Да, там летнее кафе ещё работает.", "Yes, the summer cafe there is still open.", [(504, 'Там'), (504, 'еще')], "simplified colloquial леточка еще действует to летнее кафе ещё работает"),
]
OPENER = "Let's walk through Eduard and Marina's jealous conversation in the hospital hallway."
WALK = [
    (1, None, "'I think I can guess why we are here.' Eduard starts connecting the dots while they wait."),
    (2, None, "'Do you feel something for him?' Literally, toward him do you feel something."),
    (3, 'Что за глупость?', "'What kind of nonsense is that?' Marina dismisses his suspicion right away."),
    (3, 'Эдик, мне его просто жалко.', "'Edik, I just feel sorry for him.' Impersonal 'to'-form with the object-form of the person pitied."),
    (4, 'Он тебя очаровал.', "'He charmed you!' A single-action form verb meaning to enchant or charm someone."),
    (6, None, "'Why do you need an old man when there's such a lively young neighbor nearby?' Russian omits the present-tense verb 'to be', connecting 'why' directly with 'neighbor'."),
    (7, None, "'Stop it! Nobody charmed me.' Remember that Russian uses double negation with nobody."),
    (8, None, "'Nobody? Not even me?' Eduard teases her with a wounded smile."),
    (9, 'Это я должна обижаться.', "'I am the one who should be offended!' Marina turns the tables on him."),
    (10, None, "'Forgive me, I am at fault.' Eduard immediately backs down and apologizes."),
    (11, None, "'Forgive me, I will make up for my fault.' He promises to make things right."),
    (12, None, "'Are we going home already?' Marina asks just as Arkady walks out with both arms in casts."),
]
TRANSITION = "Now listen to the hallway conversation once more."
OUTRO = "Just as Eduard apologizes to Marina, Arkady emerges from the dressing room with both arms wrapped in plaster casts. See you next time!"
CLOSING = ("dean", "Пока!")
