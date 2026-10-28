ID = "kukhnya-s04e20-scene-09"
SHOW = "kukhnya"
SEASON = 4
EPISODE = 20
SCENE = 9
TITLE = "Запись со скрытой камеры  (The Hidden Camera Recording)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "vika": "angelina", "nagiyev": "anja"}
LABELS = {"anya": "Денис", "vika": "Вика", "nagiyev": "Нагиев"}
SOURCE_NAME = "Кухня (Kukhnya) S4.20"
SOURCE_FILE = "sources/kukhnya/s04/e20.ru.srt"
SOURCE_NOTE = "After the elimination tournament montage on stage, Vika and Denis search yesterday's security footage in the office and copy the video proving Denis jumped out the window alone."

INTRO = "Out on stage, the elimination round heats up as restaurant critic Mikhail Kochetkov suffers a fiery accident with a flambé dish. Meanwhile, inside the office, Vika and Denis scroll through yesterday's security camera archive—and briefly spot a scandalous clip of Nagiyev with finalist Oksana before finding Denis's jump. Let's listen to the scene in Russian."

STORY = [
    ("nagiyev", "Добрый вечер, это лучшее шоу страны!", "Good evening, this is the best show in the country!", [], "new"),
    ("nagiyev", "Прямо сейчас мы начинаем новый тур.", "Right now we are starting a new round.", [], "new"),
    ("nagiyev", "Не переживай, Миша, шрамы украшают мужчину.", "Do not worry, Misha, scars adorn a man.", [(141, 'не переживай, Миша, шрамы, они украшают мужчину')], "adapted"),
    ("vika", "Так, нам надо найти вчерашний день.", "All right, we need to find yesterday's date.", [(144, 'Так, надо найти вчерашний день')], "adapted"),
    ("anya", "Подожди, Вика, а это что такое?", "Wait, Vika, what is that right there?", [(145, 'Подожди, это что такое')], "adapted"),
    ("vika", "Кажется, это Нагиев и участница Оксана.", "It seems that is Nagiyev and the contestant Oksana.", [], "new"),
    ("anya", "Смотри, вот я захожу к тебе!", "Look, here I am walking in to see you!", [], "new"),
    ("vika", "Ну, скажи, как твои ночные кошмары?", "Well, tell me, how are your nightmares?", [(148, 'Как'), (149, 'твои кошмары')], "adapted"),
    ("anya", "Всё хорошо, не подходи, я прыгну!", "Everything is fine, do not come closer, I will jump!", [(150, 'Хорошо'), (151, 'Не подходи, я прыгну')], "adapted"),
    ("vika", "Ты тогда правда очень странно выглядел.", "You really did look very strange back then.", [], "new"),
    ("vika", "Вот, я сделаю копию для Кати.", "Here, I will make a copy for Katya.", [(152, 'Вот, сделаю копию для Кати')], "adapted"),
    ("anya", "Спасибо тебе огромное за помощь, Вика!", "Thank you so very much for your help, Vika!", [(153, 'Спасибо')], "adapted"),
]

OPENER = "Now let's examine the tournament broadcast and the office video search line by line."

WALK = [
    (0, None, "'Good evening, this is the best show in the country!' On set, Nagiyev launches the elimination round with his booming television voice."),
    (1, None, "'Right now we are starting a new round.' A first-person plural present verb takes the inanimate accusative singular of new round."),
    (2, None, "'Do not worry, Misha, scars adorn a man.' After a contestant accidentally singes critic Kochetkov, Nagiyev quotes a famous Russian proverb."),
    (3, None, "'All right, we need to find yesterday's date.' In the office, Vika searches the computer archive using a temporal adjective meaning yesterday's."),
    (4, None, "'Wait, Vika, what is that right there?' Scrolling through the video, Denis spots Nagiyev and contestant Oksana kissing in the office."),
    (5, None, "'It seems that is Nagiyev and the contestant Oksana.' Vika raises her eyebrows as they fast-forward past Nagiyev's secret rendezvous."),
    (6, None, "'Look, here I am walking in to see you!' They reach the timestamp from yesterday afternoon when Denis entered the office."),
    (7, None, "'Well, tell me, how are your nightmares?' On the computer screen, recorded Vika asks Denis how his nightmares are going."),
    (8, None, "'Everything is fine, do not come closer, I will jump!' The recording clearly shows Denis backing away by himself and leaping out the window."),
    (9, None, "'You really did look very strange back then.' Vika shakes her head watching Denis jump out the window for no apparent reason."),
    (10, None, "'Here, I will make a copy for Katya.' She transfers the video file onto Denis's tablet using the accusative singular of copy."),
    (11, None, "'Thank you so very much for your help, Vika!' Clutching the tablet with his good hand, Denis thanks Vika and rushes out."),
]

TRANSITION = "Let's hear the broadcast and office scene again from beginning to end."
OUTRO = "With the video file copied onto his tablet, Denis hurries off to find Katya and prove that he never cheated on her. Listen for the nouns meaning tournament, day, and copy. See you in the next scene."
CLOSING = ("vika", "Вот, я сделаю копию для Кати.")
CLOSING_TRANS = "Here, I will make a copy for Katya."
