ID = "kukhnya-s02e02-scene-10"
SHOW = "kukhnya"
SEASON = 2
EPISODE = 2
SCENE = 10
TITLE = "Отец Насти  (Nastya's Father)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "anton": "anja", "max": "angelina"}
LABELS = {"anya": "Аня", "anton": "Антон", "max": "Макс"}
SOURCE_NAME = "Кухня (Kukhnya) S2.02"
SOURCE_FILE = "sources/kukhnya/s02/e02.ru.dual.srt"

INTRO = "An angry man comes looking for Kostya. Max opens the door and a case of mistaken identity leads to threats. Let's listen closely to their exchange in Russian first, and then walk through each line together."

STORY = [
 ("max", "Здравствуйте.", "Hello.", [(163, "Здравствуйте")], ''),
 ("anton", "Константин Анисимов?", "Konstantin Anisimov?", [(163, "Константин Анисимов")], ''),
 ("anya", "Да, это я.", "Yes, that is me.", [(164, "Да, это я")], 'Max claims to be Kostya because he ordered internet repair'),
 ("anya", "А вы интернет чинить?", "Are you here to fix the internet?", [(164, "А вы интернат чинить")], ''),
 ("anton", "Я отец Насти.", "I am Nastya's father.", [], 'new'),
 ("anton", "Обидишь Настю, я из тебя колбасу сделаю.", "If you hurt Nastya, I will turn you into sausage.", [(172, "Обидишь Настю, я из тебя колбасу сделаю")], ''),
 ("anya", "Подождите.", "Wait.", [(174, "Подождите")], ''),
 ("anya", "Вы неправильно поняли.", "You understood incorrectly.", [(174, "вы неправильно поняли")], ''),
 ("anya", "Я не Костя.", "I am not Kostya.", [(174, "Я не Костя")], ''),
 ("anya", "Я Макс.", "I am Max.", [(174, "я Макс")], ''),
 ("max", "А я интернет чинить.", "And I am here to fix the internet.", [(179, "я интернет чинить")], 'The real repairman arrives'),
 ("max", "Кто из вас Константин?", "Which one of you is Konstantin?", [(180, "А кто из вас Константин")], ''),
 ("anton", "Я.", "Me.", [(181, "Я")], 'Kostya finally admits it'),
]

OPENER = "Let's hear this intense encounter."

WALK = [
 (0, "Здравствуйте.", "'Hello.' A polite start to a hostile conversation."),
 (1, "Константин Анисимов?", "'Konstantin Anisimov?' Checking the name."),
 (2, "Да, это я.", "'Yes, that is me.' Max makes a huge mistake by lying."),
 (3, None, "'Are you here to fix the internet?' Max was expecting a technician."),
 (4, None, "'I am Nastya's father.' The worst possible answer for Kostya's roommate."),
 (5, "Обидишь Настю, я из тебя колбасу сделаю.", "'If you hurt Nastya, I will turn you into sausage.' A very creative threat."),
 (6, "Подождите.", "'Wait.' Max tries to backpedal quickly."),
 (7, "Вы неправильно поняли.", "'You understood incorrectly.' Trying to clear up the confusion."),
 (8, "Я не Костя.", "'I am not Kostya.' He confesses the lie."),
 (9, "Я Макс.", "'I am Max.' Offering his real name for safety."),
 (10, None, "'And I am here to fix the internet.' The real technician finally shows up."),
 (11, "Кто из вас Константин?", "'Which one of you is Konstantin?' Now the technician is confused."),
 (12, "Я.", "'Me.' The real Kostya speaks up at last."),
]

TRANSITION = "Now let's hear the whole thing once more."

OUTRO = "And that's it for this scene. When you watch the episode, listen out for the exchange around nastya's father, and for the words meaning 'Anisimov' and 'internet'. You'll catch them now. See you next time."
CLOSING = ("anya", "До свидания!")
