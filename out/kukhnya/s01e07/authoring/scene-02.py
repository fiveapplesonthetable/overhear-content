# Authoring module for kukhnya-s01e07-scene-02.
ID = 'kukhnya-s01e07-scene-02'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 7
SCENE = 2
TITLE = 'Секретный жилец  (The Secret Resident)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'kostya': 'Костя', 'max': 'Макс'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.07'
SOURCE_FILE = 'sources/kukhnya/s01/e07.ru.dual.srt'
INTRO = "It's early morning at Claude Monet. Kostya, the bartender, comes in and finds Max, the new cook, wandering about in ordinary clothes long before his shift. When Kostya asks why, Max has to admit what he has been doing at night. Here's the Russian, with a few times of day to listen for."
OPENER = "Let's go back through it. Kostya asks the questions, and Max does his best to avoid the answers."
TRANSITION = 'Now the whole scene again, straight through.'
OUTRO = "Max's secret comes out in four words: 'I live right here'. Kostya's answer is the sort of thing that anybody would say. See you next time."
CLOSING = ('max', 'Пока!')
STORY = [
    ('max', 'Костя, почему ты пришёл так рано?', 'Kostya, why did you arrive so early?', [(5, 'ты как так рано приперся')], ''),
    ('kostya', 'Сейчас уже восемь часов утра, Макс.', "It is already eight o'clock in the morning, Max.", [(6, 'Не рано')], ''),
    ('max', 'Я думал, что ресторан ещё закрыт.', 'I thought that the restaurant was still closed.', [], ''),
    ('kostya', 'Почему ты ещё не надел форму?', "Why haven't you put on your uniform yet?", [(6, 'Че не переоделся')], ''),
    ('max', 'Мой ключ от шкафа лежит здесь.', 'My locker key is lying here.', [(7, 'А у меня ключ здесь')], ''),
    ('kostya', 'Тогда иди быстрее в раздевалку персонала.', 'Then go faster to the staff locker room.', [(8, 'Ну и вали переодеваться')], ''),
    ('max', 'Не командуй мной, я всё успею.', 'Do not boss me around, I will manage everything in time.', [(9, 'Погоди, че ты меня строишь')], ''),
    ('kostya', 'Что ты вообще делал здесь ночью?', 'What were you doing here at night at all?', [(9, 'Че ты здесь делаешь')], ''),
    ('max', 'Честно говоря, я живу прямо здесь.', 'Honestly speaking, I live right here.', [(10, 'Живу я здесь')], ''),
    ('kostya', 'Ты ночуешь в ресторане шефа Баринова?!', "You spend the night in Chef Barinov's restaurant?!", [(10, 'Как так')], ''),
    ('max', 'Да, я сплю на диване в зале.', 'Yes, I sleep on the sofa in the dining room.', [(11, 'Так, так')], ''),
    ('kostya', 'Если шеф узнает, он тебя убьёт!', 'If the chef finds out, he will kill you!', [], ''),
    ('max', 'Пожалуйста, не рассказывай никому мой секрет.', 'Please do not tell anyone my secret.', [], ''),
]
WALK = [
    (0, None, '\'Kostya, why did you arrive so early?\' "Prishyol", \'came\', is for arriving on foot, with pri- meaning arrival. "Tak rano" is \'so early\'.'),
    (1, None, '\'It is already eight o\'clock in the morning, Max.\' Russian counts the clock in hours: vosem\' chasov, \'eight of hours\'. "Utra", \'of the morning\', is how you say a.m.'),
    (2, None, '\'I thought that the restaurant was still closed.\' "Dumal" ends in -l, the past tense for a man; a woman would say dumala. "Yeshchyo" means \'still\' here.'),
    (3, None, '\'Why haven\'t you put on your uniform yet?\' "Yeshchyo ne", \'still not\', is how Russian says \'not yet\'. "Nadet\'" is the verb for putting on clothes, and forma becomes formu as the thing being put on.'),
    (4, None, "'My locker key is lying here.' A key in Russian 'lies', lezhit, when it is flat on a surface. And it's a key ot shkafa, 'from the locker', where English says 'to' or 'of'."),
    (5, None, '\'Then go faster to the staff locker room.\' "Idi" is the command \'go\', and bystreye, \'faster\', is how you tell someone to hurry. "Razdevalka", the changing room, comes from razdevat\'sya, to get undressed.'),
    (6, None, '\'Do not boss me around, I will manage everything in time.\' "Komandovat\'", to command, takes mnoy, the \'by me\' form of \'me\'. "Uspeyu" is the future of uspet\', to make it in time, and you\'ll hear it whenever someone is running late.'),
    (7, None, '\'What were you doing here at night at all?\' "Vobshche", \'at all\', gives the question a suspicious edge. "Noch\'yu", \'at night\', is the word for night with an ending that turns it into a time.'),
    (8, None, '\'Honestly speaking, I live right here.\' "Chestno govorya" is a fixed phrase, like \'to be honest\'. "Pryamo zdes\'" is \'straight here\', meaning right here.'),
    (9, None, '\'You spend the night in Chef Barinov\'s restaurant?!\' "Nochevat\'", to spend the night, is built on noch\', night. "Shefa Barinova", \'of Chef Barinov\', puts an -a on both words to show whose restaurant it is.'),
    (10, None, '\'Yes, I sleep on the sofa in the dining room.\' "Splyu", \'I sleep\', has an extra l that only the I form gets; \'you sleep\' is spish. "Divan" and zal both take -e after na and v: na divane, v zale.'),
    (11, None, '\'If the chef finds out, he will kill you!\' Russian puts uznayet, \'will find out\', in the future, where English says \'finds out\'. "Ub\'yot", \'will kill\', is the future too.'),
    (12, None, '\'Please do not tell anyone my secret.\' "Nikomu" means \'to nobody\', and the ne in front of rasskazyvay stays: \'don\'t tell to nobody\'. Ne rasskazyvay is the usual way to ask someone to keep quiet.'),
]
