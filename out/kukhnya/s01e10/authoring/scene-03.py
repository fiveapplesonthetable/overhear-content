# Authoring module for kukhnya-s01e10-scene-03.
ID = 'kukhnya-s01e10-scene-03'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 10
SCENE = 3
TITLE = 'Незнакомая гостья  (An Unknown Guest)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'kostya': 'Костя'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.10'
SOURCE_FILE = 'sources/kukhnya/s01/e10.ru.dual.srt'
INTRO = "In the corridor outside the bustling kitchen of Claude Monet, bartender Kostya approaches Chef Viktor Barinov with a message. An unfamiliar young woman has arrived at the restaurant specifically asking for the head chef, claiming to have an important proposal. Let's listen to their brief exchange in Russian first."
OPENER = "Now let's examine Kostya and Barinov's corridor conversation line by line."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = "Curious despite his lingering hangover, Chef Barinov heads toward the entrance to discover what the television representative wants, while Kostya hurries to brew his tea. Next time you watch the episode, listen for the Russian expressions for 'important' and 'time' — you will catch every word right away. See you next time!"
CLOSING = ('kostya', 'Пока!')
STORY = [
    ('kostya', 'Шеф, вас там какая-то девушка зовёт.', 'Chef, some young woman is calling for you over there.', [(6, 'Вас там какая-то девушка зовет.')], ''),
    ('barinov', 'Кто она такая и что ей нужно?', 'Who is she and what does she need?', [], ''),
    ('kostya', 'Она сказала, что пришла с телевидения.', 'She said that she came from television.', [], ''),
    ('barinov', 'Я не хочу ни с кем говорить.', 'I do not want to talk to anyone.', [], ''),
    ('kostya', 'Она говорит, что дело очень важное.', 'She says that the matter is very important.', [], ''),
    ('barinov', 'У меня сейчас совершенно нет времени.', 'I currently have absolutely no time.', [], ''),
    ('kostya', 'Она ждёт вас возле главного входа.', 'She is waiting for you near the main entrance.', [], ''),
    ('barinov', 'Пусть зайдёт ко мне в кабинет.', 'Let her come into my office.', [], ''),
    ('kostya', 'Она просила выйти на одну минуту.', 'She asked you to come out for one minute.', [], ''),
    ('barinov', 'Ладно, Костя, я сейчас подойду сам.', 'Fine, Kostya, I will come over myself now.', [], ''),
    ('kostya', 'Спасибо, шеф, я передам ваши слова.', 'Thank you, chef, I will convey your words.', [], ''),
    ('barinov', 'И налей мне крепкого чёрного чая.', 'And pour me some strong black tea.', [], ''),
    ('kostya', 'Конечно, шеф, сделаю прямо сейчас.', 'Of course, chef, I will do it right now.', [], ''),
]
WALK = [
    (0, None, "'Chef, some young woman is calling for you over there.' Catching Barinov in the corridor, Kostya lets him know that some young woman is asking for him."),
    (1, None, "'Who is she and what does she need?' Still irritable from his hangover, Barinov demands to know who she is and what she wants."),
    (2, None, "'She said that she came from television.' Kostya explains that the visitor claims to have come from a television studio."),
    (3, None, "'I do not want to talk to anyone.' Russian stacks negatives here — literally 'I do not want with no one to speak' — as Barinov refuses to see anyone."),
    (4, None, "'She says that the matter is very important.' Kostya adds that the young woman insists her business with the chef is very important."),
    (5, None, "'I currently have absolutely no time.' Russian expresses 'I have no time' as 'at me there is no time', with 'completely' adding extra finality."),
    (6, None, "'She is waiting for you near the main entrance.' Kostya points out that she is standing right by the main entrance waiting for him."),
    (7, None, "'Let her come into my office.' Giving in a little, Barinov tells Kostya to send her into his office."),
    (8, None, "'She asked you to come out for one minute.' Kostya relays her polite request to step outside for just sixty seconds."),
    (9, None, "'Fine, Kostya, I will come over myself now.' Curious despite his grumpy mood, Barinov relents and says he will walk out to meet her himself."),
    (10, None, "'Thank you, chef, I will convey your words.' Kostya thanks the chef and heads back to let the visitor know he is coming."),
    (11, None, "'And pour me some strong black tea.' Before Kostya leaves, Barinov asks him to pour a cup of strong black tea for his headache."),
    (12, None, "'Of course, chef, I will do it right now.' Kostya cheerfully agrees to brew the fresh tea right away."),
]
