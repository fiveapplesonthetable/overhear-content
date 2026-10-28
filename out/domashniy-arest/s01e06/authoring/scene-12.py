ID = "domashniy-arest-s01e06-scene-12"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 6
SCENE = 12
TITLE = "Слабое место Игнатьева  (Ignatyev's Weak Spot)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "ilona": "angelina", "ignatyev": "anja"}
LABELS = {"anya": "Юля", "ilona": "Илона", "ignatyev": "Игнатьев"}
SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.06"
SOURCE_FILE = "sources/domashniy-arest/s01/e06.ru.dual.srt"

INTRO = ("Last time, after Marina turned down Arkady's request for five thousand roubles, neighbour Klavdia "
         "Viktorovna offered to pay him the money if he worked it off by washing her laundry. Meanwhile, inside "
         "his office at the meatpacking plant, owner Veniamin Ignatyev treats Ilona to slices of his prized cured "
         "meat, thinking she is a wholesale buyer. We'll hear it in Russian first; don't worry about catching "
         "every word.")

STORY = [
 ("ignatyev", "Ну что, как?",
  "Well then, how is it?",
  [(438, "Ну что, как")], ""),
 ("ilona", "Потрясающе! Испанский?",
  "Incredible! Is it Spanish?",
  [(439, "Потрясающе"), (440, "Испанские")],
  "ASR plural 'Испанские' -> 'Испанский' (for хамон)"),
 ("ignatyev", "Здесь делаем, в Ложкино. И лучше, чем там!",
  "We make it right here, in Lozhkino. And better than over there!",
  [(441, "Здесь делаем"), (442, "И лучше, чем там")],
  "ASR 'к Лоджицам' in 445 restored to 'в Ложкино'"),
 ("ignatyev", "Если бы меня не душили люди из мэрии! Я бы тут развернулся.",
  "If only the people from City Hall weren't strangling me! I would really expand here.",
  [(451, "Если бы меня не душили"), (451, "из мэрии"), (452, "Я бы тут развернулся")],
  "crude 'твари' in 451 -> 'люди'"),
 ("ignatyev", "Илоночка, вы мне понравились. Сделаю вам скидку пятнадцать процентов.",
  "Ilonochka, I like you. I'll give you a fifteen percent discount.",
  [(453, "Илоночка, вы мне понравились"), (454, "сделаю скидку"), (454, "процентов")],
  "digits '15' written out as 'пятнадцать'"),
 ("ilona", "Понимаете, я не совсем оптовик.",
  "You see, I'm not quite a wholesaler.",
  [(456, "Понимаете"), (458, "я не совсем оптовик")], ""),
 ("ignatyev", "А кто?",
  "Then who are you?",
  [(459, "А кто")], ""),
 ("ilona", "Я возглавляю предвыборный штаб Ивана Самсонова.",
  "I head the election campaign of Ivan Samsonov.",
  [(461, "Я возглавляю предвыборный штаб Ивана Самсонова")], ""),
 ("anya", "Не дал? Подождите, есть у него одно слабое место.",
  "He didn't give any? Wait, he does have one weak spot.",
  [(463, "Не дал"), (464, "Подождите. Есть у него одно"), (464, "слабое")], ""),
 ("ilona", "Так что за слабое место?",
  "So what kind of weak spot?",
  [(464, "слабое"), (465, "Так что за")],
  "'пунктик' -> 'слабое место'"),
 ("anya", "А вы родителям про меня не расскажете?",
  "And you won't tell my parents about me?",
  [(466, "А вы родителям про меня не расскажете")], ""),
 ("ilona", "Не расскажу.",
  "I won't tell.",
  [(467, "Не расскажу")], ""),
 ("anya", "Дочку свою он безумно любит. А она его видеть не хочет.",
  "He loves his daughter madly. And she doesn't want to see him.",
  [(468, "дочку свою он безумно любит. Она его видеть не хочет")], ""),
 ("anya", "Он хотел, чтобы она его дело продолжила.",
  "He wanted her to continue his business.",
  [(470, "Он хотел, чтобы она его дело продолжила")], ""),
 ("anya", "А она балерина, да ещё и вегетарианка!",
  "And she's a ballerina, and a vegetarian on top of that!",
  [(471, "Она балерина. Да еще и вегетарианка")], ""),
 ("anya", "Они уже год не общаются. Она из дома ушла.",
  "They haven't spoken for a year already. She left home.",
  [(473, "Они уже год"), (473, "не общаются. Она из дома ушла")],
  "ASR 'год три' -> 'год'"),
 ("anya", "А он с девочками разговаривать не научился.",
  "And he never learned how to talk to girls.",
  [(474, "А он"), (474, "с девочками разговаривать"), (474, "не научился")],
  "garbled 'у него хорошее' dropped"),
]

OPENER = ("Let's walk through it. Ignatyev watches proudly as Ilona tastes a slice of his local cured ham.")

WALK = [
 (0, None,
  "'Well then, how is it?' Ilona is genuinely impressed."),
 (1, "Потрясающе!",
  "'Incredible!' she exclaims."),
 (1, "Испанский?",
  "'Is it Spanish?' Ignatyev beams with local pride."),
 (2, "Здесь делаем, в Ложкино.",
  "'We make it right here, in Lozhkino.' Listen for the word meaning 'right here' right alongside 'make' in this line."),
 (2, "И лучше, чем там!",
  "'And better than over there!' Then his face darkens as he thinks of the town authorities."),
 (3, "Если бы меня не душили люди из мэрии!",
  "'If only the people from City Hall weren't strangling me!' Notice the conditional particle 'would' with the "
  "past tense for an unreal condition."),
 (3, "Я бы тут развернулся.",
  "'I would really expand here.' Charmed by Ilona's praise, he makes her a generous offer."),
 (4, "Илоночка, вы мне понравились.",
  "'Ilonochka, I like you.' Literally 'you were pleasing to me'."),
 (4, "Сделаю вам скидку пятнадцать процентов.",
  "'I'll give you a fifteen percent discount.' Seeing her opening, Ilona reveals why she really came."),
 (5, None,
  "'You see, I'm not quite a wholesaler.' Ignatyev frowns."),
 (6, None,
  "'Then who are you?' Ilona hands him her card."),
 (7, None,
  "'I head the election campaign of Ivan Samsonov.' Furious at anything connected to politics, Ignatyev throws her "
  "out at once. Outside in the corridor, Yulya catches up with her."),
 (8, "Не дал?",
  "'He didn't give any?' she asks."),
 (8, "Подождите, есть у него одно слабое место.",
  "'Wait, he does have one weak spot.' Ilona stops and turns around."),
 (9, None,
  "'So what kind of weak spot?' That phrase 'what for a...' means 'what kind of...'. First Yulya secures her deal."),
 (10, None,
  "'And you won't tell my parents about me?' Ilona promises."),
 (11, None,
  "'I won't tell.' So Yulya shares the boss's family secret."),
 (12, "Дочку свою он безумно любит.",
  "'He loves his daughter madly.' the speaker starts with 'daughter' and pairs it with 'he' to make the point clear."),
 (12, "А она его видеть не хочет.",
  "'And she doesn't want to see him.' Yulya explains why they fell out."),
 (13, None,
  "'He wanted her to continue his business.' Notice how 'wanted that she continue' uses the past tense after "
  "'in order that'. Instead, his daughter chose the exact opposite path."),
 (14, None,
  "'And she's a ballerina, and a vegetarian on top of that!' Literally 'yes still and a vegetarian!'."),
 (15, "Они уже год не общаются.",
  "'They haven't spoken for a year already.' the speaker starts with 'they' and pairs it with 'already' to make the point clear."),
 (15, "Она из дома ушла.",
  "'She left home.' And Yulya adds one last observation."),
 (16, None,
  "'And he never learned how to talk to girls.' Ilona's eyes light up with a new plan."),
]

TRANSITION = "Now let's hear the whole conversation again from the beginning."

OUTRO = ("So after Ignatyev throws Ilona out of his office, Yulya tips her off about his one weak spot: his "
         "estranged daughter Galina, a ballerina and vegetarian who hasn't spoken to him in a year. Listen for the "
         "conditional particle 'would' in 'if only they weren't strangling me'; see you in the next scene.")
CLOSING = ("anya", "Есть у него одно слабое место.")
