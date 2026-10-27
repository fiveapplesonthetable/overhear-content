ID = "kukhnya-s02e03-scene-04"
SHOW = "kukhnya"
SEASON = 2
EPISODE = 3
SCENE = 4
TITLE = "Надрыв связок  (A Torn Ligament)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "chef": "anja"}
LABELS = {"anya": "Врач", "chef": "Шеф"}
SOURCE_NAME = "Кухня (Kukhnya) S2.03"
SOURCE_FILE = "sources/kukhnya/s02/e03.ru.dual.srt"

INTRO = "Chef Viktor is at the hospital after being hit by a car. The doctor examines his leg, but Viktor makes up a story to protect the person who hit him."

STORY = [
 ("anya", "У вас надрыв связок.", "You have a partial ligament tear.", [(42, "Надрыв связок.")], ''),
 ("anya", "Это не очень страшно.", "It's not too serious.", [(43, "Это не очень страшно.")], ''),
 ("anya", "Не нагружайте ногу.", "Keep your weight off that leg.", [(44, "Не нагружайте ногу.")], ''),
 ("chef", "Спасибо.", "Thank you.", [(46, "Спасибо.")], ''),
 ("anya", "Какая причина вашей травмы?", "What is the cause of your injury?", [(46, "Мы должны записать причину вашей травмы.")], ''),
 ("chef", "Я попал под машину.", "I got hit by a car.", [(48, "попал под машину.")], ''),
 ("anya", "Будете заявлять в полицию?", "Will you report to the police?", [(50, "Будете заявлять в полицию?")], ''),
 ("chef", "Нет.", "No.", [(50, "Нет.")], ''),
 ("chef", "Я забыл поставить машину на ручник.", "I forgot to put the car on handbrake.", [(51, "Я забыл поставить на ручник свою машину.")], ''),
 ("chef", "И она на меня наехала.", "And it ran over me.", [(52, "И она на меня наехала.")], ''),
 ("anya", "Понятно.", "I see.", [], 'new'),
 ("chef", "Заявлять не буду.", "I will not report it.", [(53, "Заявлять не будет.")], ''),
]

OPENER = "Let's listen to their conversation."

WALK = [
 (0, "У вас надрыв связок.", "'You have a partial ligament tear.' ENG The doctor delivers the diagnosis."),
 (1, "Это не очень страшно.", "'It's not too serious.' ENG She reassures him it will heal."),
 (2, None, "'Keep your weight off that leg.' ENG Medical advice to rest."),
 (3, "Спасибо.", "'Thank you.' ENG He appreciates the help."),
 (4, "Какая причина вашей травмы?", "'What is the cause of your injury?' ENG The hospital needs it for their records."),
 (5, "Я попал под машину.", "'I got hit by a car.' ENG He explains what happened."),
 (6, None, "'Will you report to the police?' ENG She asks if he wants to file a report."),
 (7, "Нет.", "'No.' ENG He quickly declines."),
 (8, "Я забыл поставить машину на ручник.", "'I forgot to put the car on handbrake.' ENG He lies to cover for Elena."),
 (9, "И она на меня наехала.", "'And it ran over me.' ENG He claims his own car hit him."),
 (10, "Понятно.", "'I see.' ENG The doctor writes it down."),
 (11, None, "'I will not report it.' ENG He confirms the case is closed."),
]

TRANSITION = "Now let's hear the whole thing once more."

OUTRO = "That wraps up this scene."
CLOSING = ("chef", "Спасибо.")
