# domashniy-arest/s01e06/scene-26.py
ID = "domashniy-arest-s01e06-scene-26"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 6
SCENE = 26
TITLE = "Ты же говорила, что он погиб!  (You Said He Died!)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.06"
SOURCE_FILE = "sources/domashniy-arest/s01/e06.ru.dual.srt"
VOICES = {"narrator": "sky", "yulia": "angelina", "ignatyev": "anja"}
LABELS = {"yulia": "Юля", "ignatyev": "Игнатьев"}
INTRO = "At Ignatyev's meatpacking plant. Last time, during Marina's candlelit dinner with Eduard, his wife phoned from the airport with food poisoning, exposing that Eduard had lied about leaving her. Meanwhile, having run away from home after her mother found Ignatyev's money, teenage Yulya comes to Ignatyev's office in tears with a new story. We'll hear it in Russian first; don't worry about catching every word."
STORY = [
    ("yulia", "Здравствуйте! Вы можете мне помочь очень срочно?", "Hello! Can you help me very urgently?", [(929, 'Здравствуйте'), (929, 'вы можете мне помочь очень срочно')], ""),
    ("ignatyev", "А что случилось?", "And what happened?", [(930, 'А что случилось')], ""),
    ("yulia", "Врачи сказали, что бабушке нужна операция в Москве.", "The doctors said that Grandma needs an operation in Moscow.", [(931, 'Врачи сказали, что бабушке'), (931, 'нужна операция в Москве')], "'срочно' dropped for A1 length limit"),
    ("yulia", "Мне нужно сто пятьдесят семь тысяч шестьсот рублей!", "I need one hundred and fifty-seven thousand six hundred roubles!", [(932, 'мне'), (933, 'рублей')], "'157 600 рублей' written out in Russian words"),
    ("yulia", "Я всё верну вам! Правда, я буду работать.", "I will return everything to you! Honestly, I will work.", [(934, 'Я все верну вам'), (934, 'Правда, я')], "'до копейки ... отработаю' -> 'буду работать' (A1)"),
    ("ignatyev", "Подожди. Да, кто там внизу? Мужчина пришёл?", "Hold on. Yes, who is downstairs? A man came?", [(935, 'Подожди'), (938, 'Да')], "gate guard's phone call in cues 938-940 folded into Ignatyev's reply"),
    ("yulia", "Не пускайте его, пожалуйста! Это мой бывший парень.", "Don't let him in, please! That is my ex-boyfriend.", [(942, 'Не пускайте его, пожалуйста'), (944, 'Это мой бывший')], "'парень' added for clarity"),
    ("yulia", "Он много пил и меня обижал! Пожалуйста, помогите!", "He drank a lot and hurt me! Please, help!", [(950, 'Пожалуйста, помогите')], "cues 947-948 ('алкашом оказался. Он меня бил, я вообще от него беременна') cleaned to A1"),
    ("ignatyev", "Что же ты мне сразу не сказала?", "Why didn't you tell me right away?", [(951, 'ты мне'), (951, 'не сказала')], "'Что ж ... сразу-то' -> 'Что же ... сразу'"),
    ("ignatyev", "Сиди здесь, сейчас я к нему выйду!", "Sit here, I will go out to him right now!", [(953, 'здесь, сейчас я')], "'побудь ... пойду' -> 'Сиди ... к нему выйду' (A1)"),
    ("ignatyev", "Ты здесь главный, да? Ну, держи, старый дурак!", "You're the boss here, right? Well, take that, you old fool!", [(955, 'ты здесь главный, да'), (957, 'Ну, держи')], "'педофил' (957) cleaned to 'старый дурак'"),
    ("yulia", "Папа, стой! Не надо!", "Dad, stop! Don't!", [], "Yulya running out with Nina in cues 958-962"),
    ("ignatyev", "Что?! Это твой отец? Ты же говорила, что он погиб!", "What?! Is this your father? You said that he died!", [(958, 'Это твой отец'), (960, 'Ты же говорила, что он погиб')], ""),
    ("ignatyev", "А эта женщина — твоя мама? Значит, она тоже живая?!", "And this woman is your mum? So she is alive too?!", [(962, 'Мама'), (964, 'Это кто')], "Ignatyev realising both of Yulya's parents are alive in cues 959-964"),
    ("yulia", "Простите меня, пожалуйста! Я потом всё объясню.", "Forgive me, please! I will explain everything later.", [(961, 'Я потом все объясню'), (970, 'Простите меня, пожалуйста')], ""),
]
OPENER = "Let's go through the scene line by line. Tearful Yulya walks into Ignatyev's office at the meatpacking plant."
WALK = [
    (0, None, "'Hello! Can you help me very urgently?' Yulya uses the polite plural form 'you can' followed by the 'to'-form 'to me' and the basic verb form 'to help'."),
    (1, None, "'And what happened?' Kind-hearted Ignatyev immediately stops his work to listen."),
    (2, None, "'The doctors said that Grandma needs an operation in Moscow.' Remember that earlier Yulya had told Ignatyev she was an orphan living only with her sick grandmother. Here 'to Grandma' is 'to'-form and 'operation' is the feminine subject of 'is needed'."),
    (3, None, "'I need one hundred and fifty-seven thousand six hundred roubles!' In fact, she wants the exact sum for her first year of paid university tuition in Moscow."),
    (4, None, "'I will return everything to you! Honestly, I will work.' Before Ignatyev can open his safe, the security phone on his desk rings."),
    (5, None, "'Hold on. Yes, who is downstairs? A man came?' The guard at the front gate reports that an angry man named Samsonov is demanding to come through. Hearing her father's name, Yulya panics."),
    (6, None, "'Don't let him in, please! That is my ex-boyfriend.' The adjective for 'former' is used as a noun meaning 'ex'."),
    (7, None, "'He drank a lot and hurt me! Please, help!' To stop Ignatyev from letting her father inside, Yulya invents another wild story on the spot."),
    (8, None, "'Why didn't you tell me right away?' Outraged on the poor girl's behalf, Ignatyev stands up from his desk."),
    (9, None, "'Sit here, I will go out to him right now!' He marches down to the plant courtyard to chase the 'ex-boyfriend' away. Outside, Samson is waiting, convinced by school gossip that the wealthy plant owner is his teenage daughter's older lover."),
    (10, None, "'You're the boss here, right? Well, take that, you old fool!' The adjective 'main, chief' means 'the boss', and 'hold this!' is what Russians say when throwing a punch. Samson knocks Ignatyev to the ground just as Yulya, Nina, and Ilona rush into the yard."),
    (11, None, "'Dad, stop! Don't!' Hearing Yulya call the man 'Dad', Ignatyev rubs his bruised jaw in utter disbelief."),
    (12, 'Что?! Это твой отец?', "'What?! Is this your father?' Russian omits the present-tense verb 'to be', connecting 'what?!' directly with 'father'."),
    (12, 'Ты же говорила, что он погиб!', "'You said that he died!' Earlier at the orphanage, Yulya had told Ignatyev that both her parents had been crushed flat in a factory accident!"),
    (13, None, "'And this woman is your mum? So she is alive too?!' As Nina shouts at Samson too, every single one of Yulya's stories falls apart at once."),
    (14, None, "'Forgive me, please! I will explain everything later.' Ashamed, Yulya clasps her hands and begs everyone's forgiveness."),
]
TRANSITION = "Now let's hear the whole scene again, from start to finish."
OUTRO = "So Samson's jealous rescue mission collided head-on with Yulya's web of lies at the meatpacking plant, leaving poor Ignatyev stunned to discover that the orphan's dead parents are both very much alive. See you next time!"
CLOSING = ("ignatyev", "Пока!")
