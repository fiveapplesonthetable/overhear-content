ID = 'porta-dos-fundos-s01e01-scene-05'
SHOW, SEASON, EPISODE, SCENE = 'porta-dos-fundos', 1, 1, 5
TITLE = 'Isso aqui é um gráfico  (This Here Is a Chart)'
LEVEL, PAIR = 'A1 — beginner', 'pt-en'
LABELS = {'apresentador': 'Apresentador'}
SOURCE_NAME = 'Porta dos Fundos — Vem pra reunião (2026-01-05)'
SOURCE_FILE = 'sources/porta-dos-fundos/s01/e01.pt.srt'

INTRO = (
    "In the sketch's closing tag, we finally step inside one of the office's endless meetings. "
    'A presenter clicks through charts full of numbers he barely explains, far prouder of how he made the slides. '
    'Listen in Brazilian Portuguese first, and do not worry about catching every word.'
)
OPENER = "Let's go back through the presentation one line at a time."
TRANSITION = "Now let's hear the whole presentation once more."
OUTRO = (
    'So much for an urgent meeting: good numbers, bad numbers, and plenty of pride in Canva. '
    'That wraps up this Brazilian Portuguese sketch — see you next time!'
)
CLOSING = ('apresentador', 'Boa tarde!')

STORY = [
    ('apresentador', 'Bom, pessoal, isso aqui é um gráfico, né?', 'Well, folks, this here is a chart, right?', [(240, 'Bom, pessoal, isso aqui é um gráfico'), (241, 'né')], ''),
    ('apresentador', 'Se vocês olharem bem, tem alguns números.', 'If you look closely, there are some numbers.', [(241, 'Se vocês'), (241, 'bem, tem alguns'), (243, 'números')], 'Simplified repararem to A1 olharem.'),
    ('apresentador', 'Alguns são bons, outros são ruins.', 'Some are good, others are bad.', [(243, 'Alguns são bons, outros'), (243, 'ruins')], 'Repeated são for balanced A1 clause.'),
    ('apresentador', 'Tem que ver. Vamos seguir.', "We have to look into it. Let's move on.", [(245, 'Tem que ver'), (247, 'Vamos seguir')], ''),
    ('apresentador', 'Aqui tem outro gráfico, é a mesma coisa.', "Here's another chart, it's the same thing.", [(250, 'Outro gráfico, a mesma coisa')], 'Expanded fragment into a complete A1 sentence.'),
    ('apresentador', 'Tem uns números bons e outros ruins.', 'There are some good numbers and other bad ones.', [(250, 'tem uns'), (251, 'números bons, ruins')], ''),
    ('apresentador', 'Mas esse slide aqui eu fiz no Canva.', 'But this slide here I made in Canva.', [(251, 'mas esse slide aqui'), (253, 'eu fiz no Canva')], 'Omitted unclear caption tail.'),
    ('apresentador', 'Desculpa, pessoal.', 'Sorry, folks.', [(258, 'Desculpa, pessoal')], ''),
    ('apresentador', 'Eu que fiz também. No Canva também!', 'I am the one who made it too. In Canva too!', [(263, 'Eu que fiz também'), (263, 'Canva também')], ''),
]

WALK = [
    (0, None, ["'Well, folks, this here is a chart, right?' Addressing a group as ", ('apresentador', 'pessoal,'), ' works just like "folks" or "everyone", and tiny ', ('apresentador', 'né?'), ' at the end squeezes the full negative question into one syllable.']),
    (1, None, ["'If you look closely, there are some numbers.' Spoken Brazilian Portuguese uses ", ('apresentador', 'tem'), ', literally "has", where English says "there is" or "there are".']),
    (2, None, ["'Some are good, others are bad.' Both ", ('apresentador', 'bons,'), ' and ', ('apresentador', 'ruins.'), ' change their endings when talking about more than one number, and together they deliver zero real insight.']),
    (3, None, ["'We have to look into it. Let's move on.' ", ('apresentador', 'Tem que ver.'), ' is a classic vague office dodge meaning "someone ought to check on that", right before ', ('apresentador', 'Vamos seguir.'), ' rushes everyone to the next slide.']),
    (4, None, ['\'Here\'s another chart, it\'s the same thing.\' Unlike English "an" plus "other", ', ('apresentador', 'outro'), ' stands all by itself for "another", with no extra word needed in front.']),
    (5, None, ["'There are some good numbers and other bad ones.' Swapping a more formal word for ", ('apresentador', 'uns'), ' makes "some" feel looser and more casual, like waving a hand at the screen.']),
    (6, None, ["'But this slide here I made in Canva.' Placing ", ('apresentador', 'esse slide aqui'), ' ahead of ', ('apresentador', 'eu fiz'), ' puts pride of place on the slide itself, and ', ('apresentador', 'fiz'), ' is the completed past of the verb "to make".']),
    (7, None, ["'Sorry, folks.' ", ('apresentador', 'Desculpa,'), ' is the everyday all-purpose "sorry" or "excuse me" in Brazil, whether you bump into someone or lose track of your talk.']),
    (8, None, ["'I am the one who made it too. In Canva too!' Slipping ", ('apresentador', 'que'), ' between ', ('apresentador', 'Eu'), ' and ', ('apresentador', 'fiz'), ' — literally "I that made" — is how Brazilians stress "I\'m the one who made it".']),
]
