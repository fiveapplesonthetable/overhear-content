# Authoring module for kukhnya-s06e12-scene-12.
ID = 'kukhnya-s06e12-scene-12'
SHOW = 'kukhnya'
SEASON = 6
EPISODE = 12
SCENE = 12
TITLE = 'Подмена сыворотки  (Swapping the Serum)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'mikhail': 'Михаил', 'nikita': 'Никита'}
SOURCE_NAME = 'Кухня (Kukhnya) S6.12'
SOURCE_FILE = 'sources/kukhnya/s06/e12.ru.srt'
INTRO = "When Nikita reports that the bookmaker guest has arrived claiming he won a free lunch from the chef, Barinov prepares a special dish for him. While Barinov yells at the chefs over a ruined roast, Mikhail dumps the truth serum into the staff's pasta pot and fills the vial with water."
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = 'Unaware that his vial now holds plain water while the staff pasta is loaded with belladonna, Barinov plates his soup for the bookmaker. See you next time!'
CLOSING = ('barinov', 'До встречи!')
STORY = [
    ('mikhail', 'Виктор, а как эта сыворотка попадёт к букмекеру?', 'Viktor, and how will this serum get to the bookmaker?', [(192, 'А как сыворотка попадет')], 'adapted'),
    ('nikita', 'Шеф, там пришёл гость на бесплатный обед от шефа.', 'Chef, a guest arrived there for a free lunch from the chef.', [(193, 'Шеф, там пришел гость и сказал, что выиграл бесплатный обед от шефа')], 'adapted'),
    ('barinov', 'Спасибо, Никита, считай, что сыворотка уже попала!', 'Thank you, Nikita, consider the serum already delivered!', [(194, 'Спасибо, Никита')], 'adapted'),
    ('barinov', 'Ну что, Миша, ты сегодня ставишь со мной?', 'Well what, Misha, are you betting with me today?', [(195, 'Ну что, ставишь')], 'adapted'),
    ('mikhail', 'Да нет, я пас, у меня сейчас нет денег.', 'No, I pass, I have no money right now.', [(195, 'Да нет, я пас')], 'adapted'),
    ('barinov', 'Повара, скажите, кто поставил такой сильный режим в печи?', 'Chefs, tell me, who set such a strong mode on the oven?', [(198, 'кто ж такой режим поставил')], 'adapted'),
    ('barinov', 'Сеня, признавайся, это ты сегодня ставил мясо в печь?', 'Senya, admit it, was it you who put the meat in the oven today?', [(199, 'Сеня'), (200, 'Ты ставил')], 'adapted'),
    ('nikita', 'Нет, шеф, я сегодня вообще к печи не подходил.', 'No, chef, I did not even go near the oven today.', [(201, 'Нет')], 'adapted'),
    ('barinov', 'Тогда скажите мне немедленно, кто это сегодня сделал?', 'Then tell me immediately, who did this today?', [(202, 'Кто это сделал')], 'adapted'),
    ('barinov', 'Где Лёва, неужели он опять всё блюдо испортил?', 'Where is Lyova, did he really ruin the whole dish again?', [(203, 'Где этот Лёва')], 'adapted'),
    ('mikhail', 'Ладно, Виктор, я тогда пойду по своим делам.', 'Alright, Viktor, then I will go about my business.', [(206, 'Ну, пойду я')], 'adapted'),
    ('barinov', 'Давай, иди, а я пока приготовлю суп для гостя!', 'Go ahead, go, and meanwhile I will prepare soup for the guest!', [(207, 'Давай-давай')], 'adapted'),
]
WALK = [
    (0, None, '\'Viktor, and how will this serum get to the bookmaker?\' Wondering how this serum get to the bookmaker will is how Mikhail puts Barinov on the spot. In Russian, he does not need helper words like "do" or "did"—rising pitch alone turns it into a question.'),
    (1, None, "'Chef, a guest arrived there for a free lunch from the chef.' With the kitchen and guest in play, Nikita keeps this short reply brisk and direct."),
    (2, None, "'Thank you, Nikita, consider the serum already delivered!' With the moment and guest at stake, Barinov reacts without holding back. Russian puts the key word right up front so his emotion lands on the first beat."),
    (3, None, '\'Well what, Misha, are you betting with me today?\' Asking whether what Misha are Mikhail betting with him today puts Mikhail right on the defensive. Speaking with the close, informal "you" strips away any polite distance between them.'),
    (4, None, "'No, I pass, I have no money right now.' Because he passes he has no money right now, Mikhail treats the matter as settled."),
    (5, None, '\'Chefs, tell me, who set such a strong mode on the oven?\' Questioning whether chefs tell him who set such a strong mode on the oven is how Barinov tests Mikhail\'s story. In Russian, he does not need helper words like "do" or "did"—rising pitch alone turns it into a question.'),
    (6, None, '\'Senya, admit it, was it you who put the meat in the oven today?\' Barinov asks whether admit it was it Mikhail who put the meat in the oven today, refusing to let the point slide. Using the informal "you" shows how direct and unfiltered their kitchen relationship is.'),
    (7, None, "'No, chef, I did not even go near the oven today.' Saying that he did not even go near the oven today is how Nikita sets the tone with Barinov."),
    (8, None, '\'Then tell me immediately, who did this today?\' Asking whether tell him immediately who did this today puts Mikhail right on the defensive. Russian drops "is" in the present, setting the two halves of the thought side by side.'),
    (9, None, '\'Where is Lyova, did he really ruin the whole dish again?\' Here wondering where Lyova did he really ruin the whole dish again is shows Barinov looking for the real truth. In Russian, he does not need helper words like "do" or "did"—rising pitch alone turns it into a question.'),
    (10, None, "'Alright, Viktor, then I will go about my business.' Even though Alright Viktor then he will go about his business, Mikhail keeps a steady face in front of Barinov."),
    (11, None, '\'Go ahead, go, and meanwhile I will prepare soup for the guest!\' Here going ahead go and meanwhile he will prepare soup for the guest lets Barinov\'s real feelings break through. Starting with "davay" is the everyday Russian way to say "come on, let us do this".'),
]
