# Authoring module for kukhnya-s01e08-scene-30.
ID = 'kukhnya-s01e08-scene-30'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 8
SCENE = 30
TITLE = 'Иллюзия контроля  (The Illusion of Control)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'max': 'Макс'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.08'
SOURCE_FILE = 'sources/kukhnya/s01/e08.ru.dual.srt'
INTRO = "Barinov has won the bet, and he is in his office at Claude Monet enjoying it. Max, the young cook, comes in with a few thoughts about people and their mistakes, and the chef takes them personally. Here it is in Russian first."
OPENER = "Let's go through it slowly. Max reflects, and Barinov answers every thought with his own victory."
TRANSITION = "Now the conversation in one go."
OUTRO = "Russian has two everyday ways to talk about mistakes: the two-word phrase 'to make mistakes' and a single verb meaning 'to be mistaken'. You heard both in Max's speech here. See you next time."
CLOSING = ('barinov', 'Пока!')
STORY = [
    ('max', 'Шеф, люди очень не любят делать ошибки.', 'Chef, people really do not like making mistakes.', [(357, 'Люди не любят делать ошибки')], ''),
    ('max', 'Но тем не менее постоянно их совершают.', 'Yet nevertheless constantly make them.', [(357, 'но тем не менее постоянно их совершают.')], ''),
    ('barinov', 'Макс, умные повара вообще не ошибаются.', 'Max, smart cooks do not make mistakes at all.', [], ''),
    ('max', 'Вы думаете, что контролируете абсолютно всё?', 'You think that you control absolutely everything?', [], ''),
    ('barinov', 'Конечно, на моей кухне всегда идеальный порядок!', 'Of course, in my kitchen there is always perfect order!', [], ''),
    ('max', 'Одни заблуждаются, что могут всё контролировать.', 'Some fool themselves into thinking they can control everything.', [(358, 'Одни заблуждаются, что могут все контролировать.')], ''),
    ('barinov', 'Я выиграл пари и доказал свою правоту.', 'I won the bet and proved I was right.', [], ''),
    ('max', 'Но повара сегодня устроили настоящий кошмар.', 'But the cooks caused a real nightmare today.', [], ''),
    ('barinov', 'Они точно выполнили мой секретный план!', 'They accurately carried out my secret plan!', [], ''),
    ('max', 'Иногда наши победы бывают слишком странными.', 'Sometimes our victories turn out too strange.', [], ''),
    ('barinov', 'Главное, что победа осталась за мной!', 'The main thing is that victory remained mine!', [], ''),
    ('max', 'Самоуверенность часто приводит к неожиданным проблемам.', 'Overconfidence often leads to unexpected problems.', [], ''),
    ('barinov', 'Иди работай и не умничай здесь!', 'Go work and do not be a smart-aleck here!', [], ''),
]
WALK = [
    (0, None, ["'Chef, people really do not like making mistakes.' He tells the boss people really dislike making mistakes, using the everyday word ", ('max', 'ошибки'), ' to describe those errors.']),
    (1, None, ["'Yet nevertheless constantly make them.' Max adds that they constantly make them anyway, picking the more formal action word ", ('max', 'совершают'), ' for committing those acts.']),
    (2, None, ["'Max, smart cooks do not make mistakes at all.' The chef quickly fires back that smart cooks do not make errors at all, wrapping the whole idea into the single action ", ('barinov', 'ошибаются'), ' instead of making mistakes.']),
    (3, None, ["'You think that you control absolutely everything?' Questioning his boss about whether he controls absolutely everything, the young cook respectfully uses the word ", ('max', 'контролируете'), ' to ask about his control.']),
    (4, None, ["'Of course, in my kitchen there is always perfect order!' Of course there is always perfect order in his domain, the chef replies, calling his kitchen ", ('barinov', 'кухне'), ' while talking about being in that place.']),
    (5, None, ["'Some fool themselves into thinking they can control everything.' Some people fool themselves into thinking they can control everything, Max says, choosing a word for wandering off the path, ", ('max', 'заблуждаются'), ', to mean being deluded.']),
    (6, None, ["'I won the bet and proved I was right.' Reminding everyone that he won the bet and proved he was right, Barinov builds the word for winning, ", ('barinov', 'выиграл'), ', from the ideas of out and played.']),
    (7, None, ["'But the cooks caused a real nightmare today.' Pointing out the cooks caused a real nightmare today, the young man calls the disaster a ", ('max', 'кошмар'), ', a word locals use for terrible scenes.']),
    (8, None, ["'They accurately carried out my secret plan!' Insisting they accurately carried out his secret plan, the boss selects the specific word ", ('barinov', 'выполнили'), ' which describes completing a task exactly.']),
    (9, None, ["'Sometimes our victories turn out too strange.' Sometimes our victories turn out to be too weird, Max suggests, letting the strange aspect be captured by ", ('max', 'странными'), ' at the end of his thought.']),
    (10, None, ["'The main thing is that victory remained mine!' Winning the bet is the main thing for Barinov, who declares the victory stayed on his side using ", ('barinov', 'осталась'), ' to describe how it remained behind him.']),
    (11, None, ["'Overconfidence often leads to unexpected problems.' Warning that too much self assurance causes unexpected issues, Max builds the long word ", ('max', 'Самоуверенность'), ' from the ideas of self and confidence.']),
    (12, None, ["'Go work and do not be a smart-aleck here!' Finally ending the conversation by telling Max to go work, the chef uses a form of the word clever, ", ('barinov', 'умничай'), ', to demand he stop showing off.']),
]
