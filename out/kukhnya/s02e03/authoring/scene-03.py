ID = "kukhnya-s02e03-scene-03"
SHOW = "kukhnya"
SEASON = 2
EPISODE = 3
SCENE = 3
TITLE = "Будильник  (The Alarm Clock)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "max": "anja"}
LABELS = {"anya": "Саша", "max": "Макс"}
SOURCE_NAME = "Кухня (Kukhnya) S2.03"
SOURCE_FILE = "sources/kukhnya/s02/e03.ru.dual.srt"

INTRO = "Max and Sasha are in bed when the alarm goes off. They are both exhausted and want to keep sleeping. Let's listen closely to their exchange in Russian first, and then walk through each line together."

STORY = [
 ("max", "Давай еще на десять минут переведем.", "Let's snooze it for another ten minutes.", [(14, "Давай еще на 10 минут переведем, а?")], ''),
 ("anya", "Опять?", "Again?", [(15, "Опять?")], ''),
 ("max", "Ага.", "Yeah.", [(15, "Ага.")], ''),
 ("anya", "Давай вообще на работу не пойдем.", "Let's just skip work altogether.", [(16, "Давай вообще на работу не пойдем.")], ''),
 ("max", "Давай.", "Let's.", [(17, "Давай.")], ''),
 ("max", "Я так хочу спать.", "I want to sleep so much.", [], 'new'),
 ("anya", "Я тоже.", "Me too.", [], 'new'),
 ("max", "Можно просто остаться дома.", "We can just stay home.", [], 'new'),
 ("anya", "Это плохая идея.", "That is a bad idea.", [], 'new'),
 ("anya", "Нас уволят.", "They will fire us.", [], 'new'),
 ("max", "Тогда надо вставать.", "Then we need to get up.", [], 'new'),
 ("anya", "Доброе утро.", "Good morning.", [], 'new'),
]

OPENER = "Let's listen to their conversation."

WALK = [
 (0, "Давай еще на десять минут переведем.", "'Let's snooze it for another ten minutes.' ENG He wants to sleep a little longer."),
 (1, "Опять?", "'Again?' ENG She asks if he really wants to hit snooze again."),
 (2, None, "'Yeah.' ENG He confirms he is still tired."),
 (3, "Давай вообще на работу не пойдем.", "'Let's just skip work altogether.' ENG She jokes about not working."),
 (4, "Давай.", "'Let's.' ENG He enthusiastically agrees."),
 (5, "Я так хочу спать.", "'I want to sleep so much.' ENG He expresses his exhaustion."),
 (6, None, "'Me too.' ENG She shares his feeling."),
 (7, "Можно просто остаться дома.", "'We can just stay home.' ENG He proposes a lazy day."),
 (8, "Это плохая идея.", "'That is a bad idea.' ENG She brings them back to reality."),
 (9, None, "'They will fire us.' ENG The consequence of skipping work."),
 (10, "Тогда надо вставать.", "'Then we need to get up.' ENG He accepts the sad truth."),
 (11, None, "'Good morning.' ENG They finally start their day."),
]

TRANSITION = "Now let's hear the whole thing once more."

OUTRO = "That wraps up this scene."
CLOSING = ("max", "Тогда надо вставать.")
