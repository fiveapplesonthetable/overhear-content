# Authoring module for kukhnya-s06e04-scene-19.
ID = 'kukhnya-s06e04-scene-19'
SHOW = 'kukhnya'
SEASON = 6
EPISODE = 4
SCENE = 19
TITLE = 'Обвинение в краже  (Accusation of Theft)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'guest': 'Гость', 'gulya': 'Гуля'}
SOURCE_NAME = 'Кухня (Kukhnya) S6.04'
SOURCE_FILE = 'sources/kukhnya/s06/e04.ru.srt'
INTRO = "After the kitchen brigade visits Barinov in the hospital, Lyova's mother and her friend block Gulya at the apartment door and demand that she open her handbag to prove she did not steal the five thousand rubles."
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = "Right as the two women wrestle for Gulya's purse in the hallway, Lyova opens the front door and freezes at the sight. Until next time!"
CLOSING = ('guest', 'До встречи!')
STORY = [
    ('guest', 'Здравствуйте, шеф, вам лучше уже?', 'Hello, Chef, are you feeling better already?', [(298, 'Здрасте'), (299, 'Ну что, шеф, вам лучше уже?')], 'adapted'),
    ('barinov', 'Да, спасибо, ребята, уже лучше.', 'Yes, thank you, guys, already better.', [(299, 'Да, спасибо'), (302, 'Да, ребят, уже лучше')], 'adapted'),
    ('guest', 'А когда мне десять тысяч вернете?', 'And when will you pay me back my ten thousand?', [(300, 'А когда мне'), (300, 'тысяч вернете')], 'adapted'),
    ('barinov', 'Пошел вон отсюда, все понял?', 'Get out of here, understood?', [(301, 'Пошел вон. Все понял?')], 'adapted'),
    ('guest', 'А ты куда собралась?', 'And where are you going?', [(303, 'а ты куда')], 'adapted'),
    ('gulya', 'Я к чаю хочу чего-нибудь купить.', 'I want to buy something to go with tea.', [(304, 'Я к чаю хочу чего-нибудь купить')], 'exact'),
    ('guest', 'Ты нам сумочку свою сначала покажи.', 'Show us your handbag first.', [(305, 'Ты нам сумочку свою покажи')], 'adapted'),
    ('gulya', 'Что вы говорите?', 'What are you saying?', [(307, 'Что?')], 'adapted'),
    ('guest', 'Гуля, мы тебя ни в чем не обвиняем.', 'Gulya, we are not accusing you of anything.', [(307, 'мы тебя ни в чем не обвиняем')], 'adapted'),
    ('guest', 'Взяла пять тысяч, думаешь, никто не заметил?', 'You took five thousand, do you think nobody noticed?', [(308, 'пять тысяч, думаешь, никто не заметил?')], 'adapted'),
    ('guest', 'Ну, дай сюда, покажи сумку!', 'Come on, give it here, show the bag!', [(309, 'Ну, дай сюда, покажи сумку')], 'exact'),
    ('gulya', 'Что вы такое делаете, пустите!', 'What are you doing, let go!', [(311, 'Что вы такое делаете?')], 'adapted'),
]
WALK = [
    (0, None, "'Hello, Chef, are you feeling better already?' Here asking whether Barinov feeling better already shows the guest looking for the real truth."),
    (1, None, "'Yes, thank you, guys, already better.' With the hospital and shift in play, Barinov keeps this short reply brisk and direct."),
    (2, None, '\'And when will you pay me back my ten thousand?\' Asking when Barinov pays him back his ten thousand will cuts straight through the tension between the guest and Barinov. In Russian, he does not need helper words like "do" or "did"—rising pitch alone turns it into a question.'),
    (3, None, "'Get out of here, understood?' Wondering if get out of here understood shows Barinov caught off guard."),
    (4, None, '\'And where are you going?\' Here wondering where Barinov going is shows the guest looking for the real truth. Speaking with the close, informal "you" strips away any polite distance between them.'),
    (5, None, "'I want to buy something to go with tea.' Saying that she wants to buy something to go with tea is how Gulya sets the tone with Barinov."),
    (6, None, "'Show us your handbag first.' Once Barinov should show them Barinov's handbag first, the guest can finally tell Barinov what he means."),
    (7, None, '\'What are you saying?\' Asking what Barinov saying is is how Gulya puts Barinov on the spot. Even in the middle of the drama, she keeps the polite plural "you" that workplace Russian expects.'),
    (8, None, '\'Gulya, we are not accusing you of anything.\' Explaining that they are not accusing Barinov of anything lays the cards on the table for Barinov. Speaking with the close, informal "you" strips away any polite distance between them.'),
    (9, None, "'You took five thousand, do you think nobody noticed?' Questioning whether Barinov took five thousand do Barinov thinks nobody noticed is how the guest tests Barinov's story."),
    (10, None, "'Come on, give it here, show the bag!' Because Barinov should come on give it here show the bag, the guest does not bother softening the blow for Barinov. Russian puts the key word right up front so his emotion lands on the first beat."),
    (11, None, '\'What are you doing, let go!\' Because what are Barinov doing let go, Gulya does not bother softening the blow for Barinov. Even in the middle of the drama, she keeps the polite plural "you" that workplace Russian expects.'),
]
