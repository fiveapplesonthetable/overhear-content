# domashniy-arest/s01e07/scene-15.py
ID = "domashniy-arest-s01e07-scene-15"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 7
SCENE = 15
TITLE = "Я Сунь-цзы  (I Am Sun Tzu)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.07"
SOURCE_FILE = "sources/domashniy-arest/s01/e07.ru.dual.srt"
VOICES = {"narrator": "sky", "suntzu": "angelina", "samson": "anja"}
LABELS = {"suntzu": "Сунь-цзы", "samson": "Самсон"}
INTRO = "Meanwhile, Samsonov falls asleep over his book on the art of war and dreams that the ancient Chinese strategist himself has come to give him battle advice against polite lawyer Danya. Listen to the Russian conversation first, and don't worry about catching every word."
STORY = [
    ("suntzu", "Ну, привет, Самсонов!", "Well, hello, Samsonov!", [(564, 'Ну, привет, Самсонов')], ""),
    ("samson", "Привет! А ты кто?", "Hello! And who are you?", [(565, 'Привет'), (566, 'А ты кто')], ""),
    ("suntzu", "Как кто? Я Сунь-цзы.", "What do you mean, who? I am Sun Tzu.", [(567, 'Как кто')], "ASR 'Суньзы' -> 'Сунь-цзы'"),
    ("suntzu", "Самсонов, у тебя большие проблемы.", "Samsonov, you have big problems.", [(569, 'Самсонов, у тебя большие проблемы')], ""),
    ("suntzu", "Этот Даня зашёл на твою территорию.", "This Danya has stepped onto your territory.", [(570, 'Этот Даня'), (570, 'на твою территорию')], ""),
    ("suntzu", "А любовь, Самсонов, — как война. Адвокат — твой враг.", "And love, Samsonov, is like war. The lawyer is your enemy.", [(572, 'А любовь, Самсонов, как война'), (573, 'Адвокат твой враг')], ""),
    ("samson", "А как мне победить его?", "And how can I defeat him?", [(577, 'А как')], "slang 'Гасить его надо' (575-576) -> 'победить его'"),
    ("suntzu", "Ты плохо читал мою книгу!", "You did not read my book carefully!", [(580, 'Ты плохо читал мою книгу')], ""),
    ("suntzu", "Удар нужно наносить там, где противник слаб.", "You must strike where the enemy is weak.", [(583, 'Удар нужно наносить там, где противник слаб')], ""),
    ("suntzu", "Надо заманить его на свою территорию. Там, где ты сильный.", "You need to lure him onto your territory. Right where you are strong.", [(588, 'заманить его на свою территорию'), (589, 'Там, где ты сильный')], ""),
    ("samson", "А где я сильный?", "And where am I strong?", [(590, 'А где я сильный')], ""),
    ("suntzu", "Ну ты где служил?", "Well, where did you serve?", [(591, 'Ну ты где служил')], ""),
    ("samson", "В десанте, конечно!", "In the airborne troops, of course!", [(594, 'Конечно')], "ASR 592 'В ДВ' (В ВДВ) + 593 'Десантура?' -> 'В десанте, конечно!'"),
    ("suntzu", "Значит, у тебя есть навыки выживания. А у него их нет!", "That means you have survival skills. And he does not have them!", [(595, 'Значит, у тебя есть навыки выживания')], ""),
    ("samson", "Понял, Сунь-цзы, понял! Что делать?", "Got it, Sun Tzu, got it! What should I do?", [(596, 'Понял')], "crude 599 'не ссы' omitted"),
    ("suntzu", "Беги, Самсонов! Ты должен драться за свою любовь.", "Run, Samsonov! You must fight for your love.", [(602, 'Беги, Самсонов'), (606, 'Ты должен драться за свою любовь')], ""),
    ("suntzu", "Не мешай! Опять ты в туалете с книгой заснул!", "Get out of the way! You fell asleep in the toilet with your book again!", [(610, 'Не мешай')], "ASR 615-616 'из артерии заснешь' (в сортире заснёшь) cleaned to 'в туалете с книгой заснул'"),
]
OPENER = "Did you catch the Chinese general's battle plan for Samsonov? Let's walk through the dream step by step."
WALK = [
    (0, None, "In Samsonov's dream, a wise Chinese general in silk robes greets him warmly: 'Well, hello, Samsonov!'"),
    (1, None, "'Hello! And who are you?' Samsonov asks in surprise."),
    (2, None, "'What do you mean, who? I am Sun Tzu,' the general replies."),
    (3, None, "Sun Tzu gets straight to business: 'Samsonov, you have big problems.' Notice the construction for 'you have' followed by the plural noun."),
    (4, None, "'This Danya has stepped onto your territory,' he warns."),
    (5, 'А любовь, Самсонов, — как война.', "'And love, Samsonov, is like war,' the strategist declares."),
    (5, 'Адвокат — твой враг.', "'The lawyer is your enemy.' Listen for the word meaning 'lawyer', which leads straight into 'enemy'."),
    (6, None, "'And how can I defeat him?' Samsonov asks."),
    (7, None, "'You read my book badly!' Sun Tzu scolds him."),
    (8, None, "'You must strike where the enemy is weak,' he quotes from his treatise."),
    (9, 'Надо заманить его на свою территорию.', "'You need to lure him onto your own territory,' Sun Tzu explains."),
    (9, 'Там, где ты сильный.', "'Right where you are strong.' Sun Tzu puts 'there' up front and finishes with 'strong' to make the point unmistakable."),
    (10, None, "'And where am I strong?' Samsonov wonders."),
    (11, None, "'Well, where did you serve in the army?' Sun Tzu asks."),
    (12, None, "'In the airborne troops, of course!' Samsonov answers proudly."),
    (13, 'Значит, у тебя есть навыки выживания.', "'That means you have survival skills,' Sun Tzu points out."),
    (13, 'А у него их нет!', "'And he does not have them!' Notice the negative existential form."),
    (14, None, "'Got it, Sun Tzu, got it! What should I do?' Samsonov asks eagerly."),
    (15, 'Беги, Самсонов!', "Suddenly Nina bursts into the dream, and Sun Tzu shouts: 'Run, Samsonov!'"),
    (15, 'Ты должен драться за свою любовь.', "'You must fight for your love!' he calls out as Nina throws him out the window."),
    (16, 'Не мешай!', "In reality, Nina is banging on the bathroom door: 'Don't block the way!'"),
    (16, 'Опять ты в туалете с книгой заснул!', "'You fell asleep in the toilet with your book again!' she yells, waking him up."),
]
TRANSITION = "Now let's hear the whole dream sequence again from start to finish."
OUTRO = "Waking up on the toilet with his military treatise in hand, Samsonov now has a wild plan: lure polite city lawyer Danya out into the wild where airborne survival skills rule. See you next time!"
CLOSING = ("suntzu", "Пока!")
