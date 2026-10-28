# Authoring module for kukhnya-s05e01-scene-20.
ID = 'kukhnya-s05e01-scene-20'
SHOW = 'kukhnya'
SEASON = 5
EPISODE = 1
SCENE = 20
TITLE = 'Разрыв с Катей и итоги открытия  (Breakup with Katya and Opening Fallout)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'denis': 'Денис', 'katya': 'Катя', 'mikhail': 'Михаил'}
SOURCE_NAME = 'Кухня (Kukhnya) S5.01'
SOURCE_FILE = 'sources/kukhnya/s05/e01.ru.srt'
INTRO = 'In the final scene of the episode, guests flee the lobby in panic while Mikhail apologizes to the Prefect, and Katya tells Denis that love requires trust and they should take a break. Listen to the closing exchange.'
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = "And that brings the Season 5 premiere to a close. Notice Katya's key takeaway that love means trust, expressed with the neuter noun 'doveriye'. See you in the next episode. See you next time!"
CLOSING = ('katya', 'Пока!')
STORY = [
    ('mikhail', 'Я сам ничего не понял.', 'I did not understand anything myself.', [(300, 'Я не понял')], 'adapted'),
    ('denis', 'Катя, ну прости меня.', 'Katya, please forgive me.', [(301, 'Катя, ну прости')], 'adapted'),
    ('denis', 'Откуда взялись все эти тараканы?', 'Where did all these cockroaches come from?', [(302, 'Все эти тараканы')], 'adapted'),
    ('denis', 'Я хотел как лучше, пойми.', 'I meant well, understand.', [(303, 'Я хотел как лучше'), (303, 'ну пойми')], 'adapted'),
    ('katya', 'Дело совсем не в тараканах.', 'It is not about the cockroaches at all.', [(303, 'в тараканах')], 'adapted'),
    ('katya', 'Любовь — это не просто красивые слова.', 'Love is not just beautiful words.', [(304, 'Любовь – это не просто красивые слова')], 'verbatim'),
    ('katya', 'Любовь — это настоящее доверие.', 'Love is genuine trust.', [(305, 'Любовь – это доверие')], 'adapted'),
    ('denis', 'Катя, я тебе доверяю честно.', 'Katya, I honestly trust you.', [(306, 'я тебе доверяю честно')], 'adapted'),
    ('katya', 'А дело уже не в тебе.', 'And it is no longer about you.', [(307, 'А дело уже не в тебе')], 'verbatim'),
    ('katya', 'Я теперь сама сомневаюсь.', 'Now I have doubts myself.', [(308, 'Я сомневаюсь')], 'adapted'),
    ('katya', 'Нам лучше пока не встречаться.', 'It is better for us not to date for now.', [(309, 'нам лучше пока не встречаться')], 'verbatim'),
    ('katya', 'Прости меня, Денис.', 'Forgive me, Denis.', [(310, 'Прости')], 'adapted'),
    ('mikhail', 'Мы всех обязательно накажем.', 'We will definitely punish everyone.', [(312, 'мы всех накажем')], 'adapted'),
    ('mikhail', 'Это от отеля за неудобства.', 'This is from the hotel for the inconvenience.', [(313, 'Это от отеля за неудобства')], 'verbatim'),
    ('denis', 'И вернуться назад уже невозможно.', 'And it is already impossible to go back.', [(320, 'И вернуться уже невозможно')], 'adapted'),
]
WALK = [
    (0, None, '\'I did not understand anything myself.\' Claiming that he did not understand anything himself sounds confident, even if Denis has doubts. Russian stacks "never" or "nothing" together with "not", doubling the refusal for extra weight.'),
    (1, None, "'Katya, please forgive me.' Adding that Katya should forgive him fills in the missing piece for Katya."),
    (2, None, "'Where did all these cockroaches come from?' Here asking where all these cockroaches come shows Denis looking for the real truth."),
    (3, None, "'I meant well, understand.' Realizing that he meant well understand changes how Denis handles the situation."),
    (4, None, "'It is not about the cockroaches at all.' Noting that it is not about the cockroaches at all keeps Katya's side of the story simple and clear."),
    (5, None, "'Love is not just beautiful words.' Here telling Denis to love is not just beautiful words sets up the next turn in their exchange."),
    (6, None, '\'Love is genuine trust.\' Since Denis should love is genuine trust, Katya does not waste words on excuses. Russian drops "is" in the present, setting the two halves of the thought side by side.'),
    (7, None, '\'Katya, I honestly trust you.\' With the shift and breakup in play, Denis keeps this short reply brisk and direct. Speaking with the close, informal "you" strips away any polite distance between them.'),
    (8, None, "'And it is no longer about you.' Once it is no longer about Denis, Katya can finally tell Denis what she means."),
    (9, None, "'Now I have doubts myself.' Saying that she has doubts herself is how Katya sets the tone with Denis."),
    (10, None, "'It is better for us not to date for now.' Saying that it is better for them not to date for now is how Katya sets the tone with Denis."),
    (11, None, "'Forgive me, Denis.' With the moment and breakup in play, Katya keeps this short reply brisk and direct."),
    (12, None, "'We will definitely punish everyone.' Mentioning that they will definitely punish everyone moves the talk in a new direction."),
    (13, None, '\'This is from the hotel for the inconvenience.\' Saying that this is from the hotel for the inconvenience is how Mikhail sets the tone with Denis. Russian drops "is" in the present, setting the two halves of the thought side by side.'),
    (14, None, "'And it is already impossible to go back.' Because it is already impossible to go back, Denis treats the matter as settled."),
]
