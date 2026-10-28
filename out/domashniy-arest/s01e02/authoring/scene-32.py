# domashniy-arest/s01e02/scene-32.py
ID = "domashniy-arest-s01e02-scene-32"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 2
SCENE = 32
TITLE = "Никакой приставки  (No Console)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.02"
SOURCE_FILE = "sources/domashniy-arest/s01/e02.ru.dual.srt"
VOICES = {"narrator": "sky", "anya": "alisa", "samson": "anja", "nina": "angelina"}
LABELS = {"anya": "Аркадий", "samson": "Самсон", "nina": "Нина"}
INTRO = "Back in the communal flat, it's evening. Last time, over lunch, the governor laughed at Arkady's phone trick and told him to hand over the money; Arkady refused and walked out. Now Samson comes home with news for Nina, and Arkady comes back in a very bad mood; we'll hear it in Russian first, so don't worry about catching every word."
STORY = [
    ("nina", "Ну что? Работа есть?", "Well? Is there a job?", [], "new: Nina asks how it went with the boss"),
    ("samson", "Короче, нет.", "Long story short, no.", [(1179, 'Короче, нет')], ""),
    ("samson", "С работой не получилось.", "The job didn't work out.", [(1180, 'с работой')], "облом (slang) -> не получилось"),
    ("samson", "И с Крымом тоже.", "And the same with Crimea.", [(1181, 'с Крымом')], "'понятно' left out; 'И' added"),
    ("nina", "А никто и не сомневался.", "Nobody ever doubted it.", [(1182, 'А никто и не сомневался')], ""),
    ("samson", "Нин, ну не начинай.", "Nin, come on, don't start.", [], "new: Samson's reply"),
    ("anya", "Лёша, слушай меня.", "Lyosha, listen to me.", [], "new: Lyosha has come to ask about his console (cue 1183)"),
    ("anya", "Никакой приставки не будет.", "There won't be any console.", [(1186, 'не будет')], "«Нет никакого PSP не будет» -> «Никакой приставки не будет» (Cyrillic word for the console)"),
    ("anya", "Тебя обманули, понял?", "You've been fooled, got it?", [(1187, 'понял')], "«Обманули дурака на четыре кулака» (a mocking rhyme) -> «Тебя обманули»"),
    ("samson", "Аркадий, ты что? Он же ребёнок.", "Arkady, what's got into you? He's just a kid.", [], "new: a reaction to Arkady's cruelty"),
    ("anya", "Славик, дай сюда.", "Slavik, give that here.", [(1189, 'Дай сюда')], "'идиот' dropped; 'Славик' added as address"),
    ("anya", "Это мой айфон.", "That's my iPhone.", [(1190, 'Это мой айфон')], "speaker of cue 1190 not marked; given to Arkady, who takes his iPhone back"),
    ("nina", "Как твой? Вы же поменялись!", "What do you mean, yours? You two swapped!", [], "new: Arkady traded the iPhone to Slavik in scene 15"),
    ("anya", "Мечтай.", "Dream on.", [(1191, 'Мечтай')], ""),
    ("anya", "Всё, иди отсюда!", "That's it, off you go!", [(1192, 'отсюда')], "«Брысь мне отсюда!» -> «Всё, иди отсюда!» (to Slavik)"),
    ("samson", "Что это было?", "What was that?", [], "new: plain stand-in for cue 1194 «Что за ёшкин кот?»"),
    ("nina", "Ну вот. Ни работы, ни Крыма, ни айфона.", "Well, there you go. No job, no Crimea, and no iPhone.", [], "new: Nina's wry summing-up"),
]
OPENER = "Let's go back through it slowly. Nina wants to know how things went with Samson's boss."
WALK = [
    (0, None, "'Well? Is there a job?' The second sentence is only two words, 'work' and 'there is'; the voice going up turns it into a question. Samson doesn't make a long speech of it."),
    (1, None, "'Long story short, no.' The first word is what people say when they want to skip the details, like 'basically'. Then he explains."),
    (2, None, "'The job didn't work out.' Literally, 'with the job it didn't turn out'. This verb is the everyday way to say something did or didn't work. And there's more bad news."),
    (3, None, "'And the same with Crimea.' His boss had given him a holiday by the sea there for two, and that's off as well. Nina is not surprised."),
    (4, None, "'Nobody ever doubted it.' The word for 'nobody' comes with a 'not' before the verb as well: Russian happily uses two negatives in one sentence. Samson isn't in the mood."),
    (5, None, "'Nin, come on, don't start.' Nin is a short, affectionate way of calling Nina. 'Don't' is just 'not' in front of the command. Just then, Arkady comes in, and little Lyosha hurries over to ask about the games console he was promised for his piggy bank."),
    (6, None, "'Lyosha, listen to me.' A simple command to someone you call by their first name. What Arkady says next is hard to hear."),
    (7, None, "'There won't be any console.' Another double negative: 'no console will not be'. After 'there won't be', the missing thing takes the ending for 'of'. And he doesn't soften it."),
    (8, None, "'You've been fooled, got it?' Literally, 'they fooled you'. Russian often uses 'they' with no subject at all when it doesn't matter who did it. Of course, the one who fooled Lyosha is Arkady himself. Samson is shocked."),
    (9, None, "'Arkady, what's got into you? He's just a kid.' The first question is literally 'you what?', a common way to say 'have you lost your mind?'. Lyosha's mother, Marina, leads him away and tells him not to be upset: they'll buy one themselves. But Arkady has already turned to Samson's son."),
    (10, None, "'Slavik, give that here.' Arkady puts 'give' up front and finishes with 'here' to make the point unmistakable."),
    (11, None, "'That's my iPhone.' Arkady swapped it with Slavik for an old phone a few days ago, and now he wants it back. Nina points that out."),
    (12, 'Как твой?', "'What do you mean, yours?' She repeats his word as a question. Then she reminds him of the deal."),
    (12, 'Вы же поменялись!', "'You two swapped!' The little word after 'you' means 'but you know'. Nina uses the plural 'you' because she means both of them. Arkady's answer is one word."),
    (13, None, "'Dream on.' It's a command, 'dream', said with a sneer. And then he sends the boy away."),
    (14, None, "'That's it, off you go!' The first word, 'all', is what Russians say to end a conversation. Samson can only stare."),
    (15, None, "'What was that?' Three short words, and they work exactly like the English. Nina has the last word."),
    (16, None, "'Well, there you go. No job, no Crimea, and no iPhone.' The little word repeated three times means 'neither, nor', and each thing after it takes the ending for 'of'. A grim little list for the Samsonovs."),
]
TRANSITION = "Here's the whole scene again, from the beginning."
OUTRO = "So the Samsonovs lose the job and the trip, and Arkady breaks a promise to a child and takes back a phone. Not a good evening for anyone. See you next time!"
CLOSING = ("nina", "До завтра!")
