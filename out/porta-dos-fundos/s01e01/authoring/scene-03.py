ID = 'porta-dos-fundos-s01e01-scene-03'
SHOW, SEASON, EPISODE, SCENE = 'porta-dos-fundos', 1, 1, 3
TITLE = 'Olha a Cíntia  (Look at Cintia)'
LEVEL, PAIR = 'A1 — beginner', 'pt-en'
LABELS = {'colega': 'Colega', 'financeiro': 'Funcionário'}
SOURCE_NAME = 'Porta dos Fundos — Vem pra reunião (2026-01-05)'
SOURCE_FILE = 'sources/porta-dos-fundos/s01/e01.pt.srt'

INTRO = (
    'Still standing by the desks, the colleague refuses to let the finance employee get back to his tasks. '
    'Now he points to another coworker, Cintia, as a cautionary tale about skipping meetings. '
    'Hear the whole exchange in Brazilian Portuguese first, and do not worry about catching every word.'
)
OPENER = "Let's walk through the colleague's dramatic story one line at a time."
TRANSITION = "Now let's hear the whole conversation once more."
OUTRO = (
    'According to the colleague, skipping one meeting leads straight to staring at a phone in despair — and shouting about it counts as generosity. '
    'Next, we see whether the employee finally gives in. See you next time!'
)
CLOSING = ('financeiro', 'Tchau!')

STORY = [
    ('colega', 'Olha a Cíntia, por exemplo. Olha pra ela.', 'Look at Cintia, for example. Look at her.', [(111, 'Olha a Cíntia, por exemplo, olha pra'), (113, 'ela')], ''),
    ('financeiro', 'Que que tem a Cíntia?', "What's up with Cintia?", [(115, 'Que que tem a Cíntia')], ''),
    ('colega', 'Ela faltou a uma reunião e adiantou o trabalho dela.', 'She missed a meeting and got ahead on her work.', [(115, 'Faltou'), (117, 'adiantou o trabalho'), (119, 'dela')], 'Added standard preposition a; shortened reunião de alinhamento.'),
    ('colega', 'Só que agora ela precisa da ajuda do Carlos.', "Except now she needs Carlos's help.", [(121, 'Só que agora'), (123, 'ela precisa da ajuda do'), (125, 'Carlos')], ''),
    ('colega', 'E o Carlos tá na reunião do marketing.', 'And Carlos is in the marketing meeting.', [(125, 'Carlos'), (125, 'tá na reunião'), (127, 'do marketing')], 'Shortened com seu Milton do marketing.'),
    ('colega', 'Agora ela não tem o que fazer e fica no celular.', 'Now she has nothing to do and stays on her phone.', [(127, 'Agora ela não tem o que'), (129, 'fazer'), (135, 'no celular')], 'Simplified pega o celular e fica jogando joguinho.'),
    ('colega', 'É isso que você quer pra sua vida? Perder o foco?', 'Is that what you want for your life? To lose focus?', [(131, 'É isso que você quer pra sua'), (133, 'vida perder o foco')], ''),
    ('financeiro', 'Eu acho que você tá exagerando.', "I think you're exaggerating.", [(137, 'Eu acho que você tá')], 'Completed truncated caption exag. to exagerando.'),
    ('financeiro', 'Você precisava gritar comigo na frente dos outros?', 'Did you need to shout at me in front of everyone else?', [(145, 'Você precisava gritar comigo na frente'), (147, 'dos outros')], ''),
    ('colega', 'Tô sendo generoso, amigo.', "I'm being generous, my friend.", [(147, 'Tô sendo generoso, amigo')], ''),
]

WALK = [
    (0, None, ["'Look at Cintia, for example. Look at her.' Brazilians regularly put ", ('colega', 'a'), ' or ', ('colega', 'o'), ' right before first names, so ', ('colega', 'a Cíntia,'), ' sounds warm and familiar rather than stiff.']),
    (1, None, ["'What's up with Cintia?' ", ('colega', 'Que que tem?'), ' literally asks "what is it that she has?", and it is a super handy everyday chunk for "what\'s wrong with...?" or "what about...?". ']),
    (2, None, ["'She missed a meeting and got ahead on her work.' The word ", ('colega', 'adiantou o trabalho'), ' comes from a root meaning "ahead" or "forward", so it means she knocked her work out early.']),
    (3, None, ["'Except now she needs Carlos's help.' ", ('colega', 'Só que'), ' literally says "only that", and in conversation it works just like "except" or "the catch is" when a plan hits a snag.']),
    (4, None, ["'And Carlos is in the marketing meeting.' Here ", ('colega', 'na'), ' fuses the preposition with ', ('colega', 'a'), ' for "in the" before feminine ', ('colega', 'reunião'), ', matching ', ('colega', 'do'), ' before masculine ', ('colega', 'marketing.'), '.']),
    (5, None, ["'Now she has nothing to do and stays on her phone.' Using ", ('colega', 'fica'), ' — literally "stays" — captures sitting around stuck in a habit, and Brazil\'s word for a mobile phone is ', ('colega', 'celular.'), '.']),
    (6, None, ["'Is that what you want for your life? To lose focus?' Framing a question with ", ('colega', 'É isso que'), ' — "is that what..." — puts theatrical spotlight on ', ('colega', 'isso'), ', turning a small delay into a life crisis.']),
    (7, None, ['\'I think you\'re exaggerating.\' Where English can drop "that", Portuguese keeps ', ('financeiro', 'que'), ' in ', ('financeiro', 'eu acho que'), ', a gentle opener you can reuse before any opinion.']),
    (8, None, ['\'Did you need to shout at me in front of everyone else?\' Instead of saying the separate words for "with me", Portuguese joins them into one special word, ', ('financeiro', 'comigo'), ', and here you shout "with" someone rather than "at" them.']),
    (9, None, ["'I'm being generous, my friend.' Just as the full verb shrinks in everyday speech, ", ('colega', 'Tô sendo'), ' rolls off the tongue for "I\'m being".']),
]
