ID = 'porta-dos-fundos-s01e01-scene-01'
SHOW, SEASON, EPISODE, SCENE = 'porta-dos-fundos', 1, 1, 1
TITLE = 'Bora pra reunião  (Come to the Meeting)'
LEVEL, PAIR = 'A1 — beginner', 'pt-en'
LABELS = {'colega': 'Colega', 'financeiro': 'Funcionário'}
SOURCE_NAME = 'Porta dos Fundos — Vem pra reunião (2026-01-05)'
SOURCE_FILE = 'sources/porta-dos-fundos/s01/e01.pt.srt'

INTRO = (
    'In this office sketch from Porta dos Fundos, a colleague walks up to a finance employee at his desk and tries to pull him into a marketing meeting. '
    'What starts as a polite refusal quickly turns personal. '
    'Listen to the whole exchange in Brazilian Portuguese first, and do not worry about catching every word.'
)
OPENER = "Now let's go back through the exchange one line at a time."
TRANSITION = "Now let's hear the whole conversation once more from start to finish."
OUTRO = (
    'All the employee did was mention his department, and suddenly his colleague acted betrayed. '
    'Next, we will hear the real reason behind the invitation. See you next time!'
)
CLOSING = ('financeiro', 'Até logo!')

STORY = [
    ('colega', 'Bora pra reunião.', "Let's go to the meeting.", [(7, 'bora pra reunião')], ''),
    ('financeiro', 'Não vou estar nessa reunião, não. Mas valeu.', "I'm not going to be at that meeting. But thanks.", [(15, 'não vou estar nessa reunião'), (15, 'não. Mas valeu')], 'Shortened from cue 13-15.'),
    ('colega', 'Você não vai pra reunião?', "Aren't you going to the meeting?", [(19, 'Você não vai pra reunião')], 'Shortened confirmation question.'),
    ('financeiro', 'É reunião de marketing. Eu sou do financeiro.', "It's a marketing meeting. I'm in finance.", [(19, 'é reunião'), (21, 'de marketing'), (21, 'Eu sou do financeiro')], 'Simplified planejamento de marketing to marketing.'),
    ('colega', 'Ué, eu perguntei qual é o seu cargo?', 'Wait, did I ask what your job title is?', [(25, 'Ué'), (27, 'perguntei qual'), (27, 'seu cargo')], 'Cleaned coarse intensifiers from cues 25-27.'),
    ('financeiro', 'Que isso, cara? Calma!', 'What is this, man? Calm down!', [(29, 'Que isso, cara'), (33, 'Calma')], ''),
    ('colega', 'Você acha que você é melhor que a gente?', 'Do you think you are better than us?', [(35, 'Você acha que você é melhor'), (37, 'que a gente')], ''),
    ('colega', 'Você acha que seu tempo vale mais que o meu?', 'Do you think your time is worth more than mine?', [(39, 'Você acha que seu tempo vale mais que o'), (41, 'meu')], ''),
    ('colega', 'Eu tenho que entrar lá dentro por uma hora!', 'I have to go inside there for an hour!', [(43, 'entrar lá dentro'), (45, 'uma hora')], 'Adapted eu ter que entrar lá dentro... durante uma hora.'),
    ('financeiro', 'Calma aí! Eu só quero saber o motivo disso.', 'Hang on! I just want to know the reason for this.', [(51, 'calma aí'), (53, 'Eu só quero saber o motivo'), (55, 'disso')], ''),
]

WALK = [
    (0, None, ["'Let's go to the meeting.' ", ('colega', 'Bora'), ' is short for the full word and is one of Brazil\'s favourite casual ways to say "let\'s go", followed by ', ('colega', 'pra'), ', the everyday spoken squeezing of the preposition.']),
    (1, None, ["'I'm not going to be at that meeting. But thanks.' Brazilians often sandwich a refusal between two ", ('financeiro', 'Não'), ' words, one at the start and one at the end, then soften it with ', ('financeiro', 'valeu.'), ', which literally means "it was worth it".']),
    (2, None, ['\'Aren\'t you going to the meeting?\' Portuguese needs no helper word like "are" or "do" to make a question: rising pitch turns ', ('colega', 'Você não vai'), ' straight into "aren\'t you going?".']),
    (3, None, ["'It's a marketing meeting. I'm in finance.' To name his department, the employee says ", ('financeiro', 'Eu sou do financeiro.'), ', literally "I am from the finance", blending ', ('financeiro', 'de'), ' and ', ('financeiro', 'o'), ' into ', ('financeiro', 'do'), '.']),
    (4, None, ["'Wait, did I ask what your job title is?' That puzzled little ", ('colega', 'Ué,'), ' at the front is pure Brazilian reaction whenever something makes no sense, and ', ('colega', 'cargo?'), ' means your post or role at work.']),
    (5, None, ["'What is this, man? Calm down!' ", ('financeiro', 'Que isso,'), ' is what you blurt out when someone comes at you way too hard, paired with ', ('financeiro', 'cara?'), ', literally "face", which works just like "man" or "dude".']),
    (6, None, ['\'Do you think you are better than us?\' Instead of the textbook word for "us", everyday speech reaches for ', ('colega', 'a gente?'), ', literally "the people".']),
    (7, None, ["'Do you think your time is worth more than mine?' Notice ", ('colega', 'vale'), ' here: it comes from a similar root as the previous word, only now it carries its literal sense of "is worth".']),
    (8, None, ["'I have to go inside there for an hour!' Portuguese loves doubling up direction for emphasis, so ", ('colega', 'lá dentro'), ' says "over there inside" rather than just "in there".']),
    (9, None, ["'Hang on! I just want to know the reason for this.' Adding ", ('financeiro', 'aí!'), ' after ', ('financeiro', 'Calma'), ' turns "calm" into a conversational "hold on right there", and ', ('financeiro', 'disso.'), ' fuses the word for "of" with ', ('financeiro', 'isso'), ' to mean "of this".']),
]
