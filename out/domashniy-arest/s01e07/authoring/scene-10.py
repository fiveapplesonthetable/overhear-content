ID = "domashniy-arest-s01e07-scene-10"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 7
SCENE = 10
TITLE = "Лунтик две тысячи восемнадцать  (Luntik Twenty Eighteen)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "lavrov": "anja", "tech": "angelina"}
LABELS = {"anya": "Михаил Михайлович", "lavrov": "Лавров", "tech": "Денис"}
SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.07"
SOURCE_FILE = "sources/domashniy-arest/s01/e07.ru.dual.srt"

INTRO = ("Last time, a jealous Samsonov chased lawyer Danya out of his flat and argued with Nina about Danya's cheese "
         "fondue. Meanwhile, at the Sineozersk security service office, IT technician Denis is fixing Colonel Mikhail "
         "Mikhailovich's computer when Major Lavrov comes in to ask for archive access. Let's listen in Russian first.")

STORY = [
 ("anya", "Это смешно! Я начальник управления, а компьютер не работает.",
  "It's ridiculous! I'm the head of the department, and my computer doesn't work.",
  [(406, "Это смешно. Начальник управления, а компьютер не работает")], ""),
 ("tech", "Сейчас сделаем, Михаил Михайлович. А пароль у вас какой?",
  "We'll fix it right now, Mikhail Mikhailovich. And what is your password?",
  [(407, "Сейчас сделаем, Михаил Михайлович"), (414, "А пароль"), (414, "какой")], ""),
 ("anya", "Лунтик две тысячи восемнадцать. Что смотрите? Внук приходил, играл!",
  "Luntik twenty eighteen. What are you looking at? My grandson came over and played!",
  [(415, "Лунтик"), (416, "смотрите? Внук приходил")],
  "'2018' written out in words; 'баловался' -> 'играл'"),
 ("anya", "А вы чего опять хотели?",
  "And what did you want again?",
  [(408, "Вы чего опять хотели")], ""),
 ("lavrov", "Нужна ваша помощь. Нужно отправить запросы во все архивы.",
  "We need your help. We need to send requests to all the archives.",
  [(409, "Нужна ваша помощь"), (411, "Нужно"), (411, "запросы во все архивы")],
  "'разослать' -> 'отправить'"),
 ("lavrov", "Может, мы всё-таки найдём компромат на Самсонова.",
  "Maybe we'll still find some dirt on Samsonov.",
  [(412, "Может"), (412, "все-таки"), (412, "компромат на Самсонова")], ""),
 ("anya", "Да нет на него ничего! Вы же уже всё проверили.",
  "There is nothing on him! You already checked everything.",
  [(413, "Да нет на него ничего")],
  "Ovechkin's cue 418 folded in cleanly"),
 ("lavrov", "Значит, надо глубже копать! Дальние родственники, дедушки и бабушки.",
  "Then we have to dig deeper! Distant relatives, grandfathers and grandmothers.",
  [(419, "Значит, надо глубже копать"), (420, "Дальние родственники")],
  "'деды с бабками' -> 'дедушки и бабушки'"),
 ("lavrov", "Вдруг там что-то есть? Мы хотим зайти с другой стороны.",
  "What if there is something there? We want to come at it from another angle.",
  [(421, "Вдруг"), (421, "что-то есть"), (427, "Мы хотим зайти с другой стороны")],
  "cues 424-426 about planting drugs omitted"),
 ("anya", "Какие деликатные! Ладно, вот лейтенант Соколов, он вам поможет.",
  "How delicate of you! Fine, here is Lieutenant Sokolov, he will help you.",
  [(428, "Какие деликатные"), (429, "Ладно, вот Соколов"), (429, "он вам поможет")],
  "idiom 'собаку съел' explained in WALK"),
 ("anya", "Только не впутывайте его ни во что!",
  "Just don't drag him into anything!",
  [(430, "Только не впутывайте его ни во что")], ""),
 ("lavrov", "Да поняли мы уже!",
  "Yes, we got it already!",
  [(431, "Да поняли мы уже")], ""),
 ("tech", "Михаил Михайлович, я посмотрел ваш компьютер. У вас видеокарта слабая.",
  "Mikhail Mikhailovich, I checked your computer. Your graphics card is weak.",
  [(433, "Михаил Михайлович, я посмотрел, у вас видеокарта")],
  "'бюджетная' -> 'слабая'"),
 ("tech", "А вы что, в компьютерные игры играете? За плохих парней?",
  "Wait, do you play computer games? As the bad guys?",
  [(437, "А вы что, в")],
  "cues 437 & 439 'в контрстрайк рубитесь / за террористов' -> clean A1"),
 ("anya", "Это расслабляет! И я должен понимать их психологию! Всё, идите!",
  "It's relaxing! And I must understand their psychology! That's it, go!",
  [(438, "Расслабляет"), (441, "Я должен понимать их психологию"), (442, "Все, идите")], ""),
]

OPENER = ("Let's break it down. Colonel Mikhail Mikhailovich is grumbling at his desk while young technician Denis "
          "inspects his sluggish computer.")

WALK = [
 (0, "Это смешно! Я начальник управления, а компьютер не работает.",
  "'It's ridiculous! I'm the head of the department, and my computer doesn't work.' Denis sits down at the keyboard."),
 (1, "Сейчас сделаем, Михаил Михайлович. А пароль у вас какой?",
  "'We'll fix it right now, Mikhail Mikhailovich. And what is your password?' The stern Colonel mutters the name of a "
  "purple cartoon moon-creature for toddlers."),
 (2, "Лунтик две тысячи восемнадцать. Что смотрите? Внук приходил, играл!",
  "'Luntik twenty eighteen. What are you looking at? My grandson came over and played!' Lavrov and Ovechkin exchange a "
  "grin, and the Colonel barks at them."),
 (3, "А вы чего опять хотели?",
  "'And what did you want again?' Lavrov steps forward."),
 (4, "Нужна ваша помощь. Нужно отправить запросы во все архивы.",
  "'We need your help. We need to send requests to all the archives.' Notice how 'your help is needed' uses the short "
  "feminine adjective to agree with 'help'."),
 (5, "Может, мы всё-таки найдём компромат на Самсонова.",
  "'Maybe we'll still find some dirt on Samsonov.' The Colonel scoffs."),
 (6, "Да нет на него ничего! Вы же уже всё проверили.",
  "'There is nothing on him! You already checked everything.' Parents, brothers, sisters — all clean. Lavrov wants to "
  "go further back."),
 (7, "Значит, надо глубже копать! Дальние родственники, дедушки и бабушки.",
  "'Then we have to dig deeper! Distant relatives, grandfathers and grandmothers.' And he explains why."),
 (8, "Вдруг там что-то есть? Мы хотим зайти с другой стороны.",
  "'What if there is something there? We want to come at it from another angle.' The Colonel agrees to give them his "
  "nephew, who knows the archive inside out."),
 (9, "Какие деликатные! Ладно, вот лейтенант Соколов, он вам поможет.",
  "'How delicate of you! Fine, here is Lieutenant Sokolov, he will help you.' Still stinging from yesterday's bridge "
  "fiasco, he adds a strict warning."),
 (10, "Только не впутывайте его ни во что!",
  "'Just don't drag him into anything!' Lavrov nods to him in agreement."),
 (11, "Да поняли мы уже!",
  "'Yes, we got it already!' As Lavrov leaves, technician Denis finishes checking the Colonel's computer."),
 (12, "Михаил Михайлович, я посмотрел ваш компьютер. У вас видеокарта слабая.",
  "'Mikhail Mikhailovich, I checked your computer. Your graphics card is weak.' Denis notices what game is installed "
  "and what team the Colonel plays on."),
 (13, "А вы что, в компьютерные игры играете? За плохих парней?",
  "'Wait, do you play computer games? As the bad guys?' Caught red-handed, the Colonel comes up with a professional "
  "excuse."),
 (14, "Это расслабляет! И я должен понимать их психологию! Всё, идите!",
  "'It's relaxing! And I must understand their psychology! That's it, go!' And he shoos Denis out of the office."),
]

TRANSITION = "Now let's listen to the whole scene in Colonel Mikhail Mikhailovich's office again."

OUTRO = ("So while the Colonel upgrades his computer's graphics card, Lavrov heads down to the basement archive to "
         "put Lieutenant Lyova Sokolov to work digging into Samsonov's family tree. See you next time.")
CLOSING = ("anya", "Я должен понимать их психологию!")
