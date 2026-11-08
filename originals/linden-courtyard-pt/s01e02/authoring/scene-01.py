# Authoring module for linden-courtyard-pt-s01e02-scene-01.
ID = 'linden-courtyard-pt-s01e02-scene-01'
SHOW = 'linden-courtyard-pt'
SEASON = 1
EPISODE = 2
SCENE = 1
TITLE = 'The Red Ribbon  (A fita vermelha)'
LEVEL = 'A1 — iniciante'
PAIR = 'en-pt'
LABELS = {'hannah': 'Hannah', 'evelyn': 'Evelyn', 'graham': 'Graham'}
INTRO = 'A manhã de terça-feira chega clara e iluminada na pousada Linden Courtyard Inn. Evelyn desce apressada até a recepção, onde Hannah e Graham estão esperando com a mala recuperada dela. Ouça toda a cena primeiro.'
OPENER = 'Agora vamos repassar a conversa passo a passo.'
TRANSITION = 'Vamos ouvir toda a cena seguida novamente.'
OUTRO = 'Evelyn recuperou sua xícara e suas roupas, e uma lembrança de vinte e cinco anos atrás começa a despertar. Daqui a pouco surge confusão na cozinha do café da manhã. Até a próxima.'
CLOSING = ('evelyn', 'See you soon!')
STORY = [
    ('hannah', 'Good morning, Miss Evelyn! Look what arrived at our gate last night.', 'Bom dia, dona Evelyn! Veja o que chegou ao nosso portão ontem à noite.'),
    ('evelyn', 'My suitcase! Let me open the top pocket... yes, my red ribbon!', 'Minha mala! Deixe-me abrir o bolso de cima... sim, minha fita vermelha!'),
    ('graham', 'And your teacup inside? Is it still in one piece?', 'E a sua xícara de chá lá dentro? Ainda está inteira?'),
    ('evelyn', 'Not a single crack! Who brought it back?', 'Nem um único trincado! Quem trouxe de volta?'),
    ('hannah', 'We do not know. Someone left it on the step and rang the bell.', 'Não sabemos. Alguém deixou no degrau e tocou a campainha.'),
    ('evelyn', 'And he did not ask for his own suitcase with the wooden train?', 'E ele não pediu a própria mala com o trem de madeira?'),
    ('graham', 'He left a short note asking us to keep it until Friday.', 'Deixou um bilhete curto pedindo que a gente guardasse até sexta-feira.'),
    ('evelyn', 'How curious! The handwriting on that tag felt oddly familiar to me.', 'Que curioso! A letra naquela etiqueta pareceu estranhamente familiar para mim.'),
    ('hannah', 'Really? Do you know someone in Portland?', 'Sério? A senhora conhece alguém em Portland?'),
    ('evelyn', 'Twenty-five years ago I taught piano near here, though memories fade.', 'Vinte e cinco anos atrás eu dei aulas de piano perto daqui, embora as lembranças se apaguem.'),
    ('graham', 'For now, his bag stays safe under lock and key.', 'Por enquanto, a mala dele fica guardada a sete chaves.'),
    ('evelyn', 'Wonderful! Now I am ready for a big breakfast.', 'Maravilha! Agora estou pronta para um belo café da manhã.'),
]
WALK = [
    (0, None, ["'Bom dia, dona Evelyn! Veja o que chegou ao nosso portão ontem à noite.' Onde falamos 'ontem à noite', o inglês resolve com duas palavras:", (None, 'last night'), 'a noite passada.']),
    (1, None, ["'Minha mala! Deixe-me abrir o bolso de cima... sim, minha fita vermelha!' A abertura", (None, 'Let me open'), 'anuncia o que você vai fazer na hora e traz o verbo seguinte direto, sem partícula.']),
    (2, None, ["'E a sua xícara de chá lá dentro? Ainda está inteira?' Para perguntar se algo frágil sobreviveu sem quebrar, o inglês pergunta se está", (None, 'in one piece'), 'em um pedaço só.']),
    (3, None, ["'Nem um único trincado! Quem trouxe de volta?' Quando 'quem' é o sujeito da frase, não entra auxiliar na pergunta:", (None, 'Who brought it back'), 'quem a trouxe de volta.']),
    (4, None, ["'Não sabemos. Alguém deixou no degrau e tocou a campainha.' Para negar no presente usamos o auxiliar em", (None, 'We do not know'), 'nós não sabemos.']),
    (5, None, ["'E ele não pediu a própria mala com o trem de madeira?' Pedir um objeto em inglês pede sempre a preposição no final do verbo:", (None, 'ask for'), 'pedir ou procurar por algo.']),
    (6, None, ["'Deixou um bilhete curto pedindo que a gente guardasse até sexta-feira.' Veja a construção enxuta em", (None, 'asking us to keep'), 'pedindo a nós para guardar.']),
    (7, None, ["'Que curioso! A letra naquela etiqueta pareceu estranhamente familiar para mim.' Caligrafia ou letra escrita à mão ganha uma palavra composta própria:", (None, 'handwriting'), 'escrita de mão.']),
    (8, None, ["'Sério? A senhora conhece alguém em Portland?' Com o verbo conhecer, a pergunta no presente começa com auxiliar:", (None, 'Do you know someone'), 'sem preposição antes da pessoa.']),
    (9, None, ["'Vinte e cinco anos atrás eu dei aulas de piano perto daqui, embora as lembranças se apaguem.' Igual ao nosso 'atrás', o inglês posiciona a marca de tempo passado no fim da expressão:", (None, 'Twenty-five years ago'), 'vinte e cinco anos atrás.']),
    (10, None, ["'Por enquanto, a mala dele fica guardada a sete chaves.' O equivalente inglês ao nosso 'a sete chaves' junta cadeado e chave:", (None, 'under lock and key'), 'bem trancada.']),
    (11, None, ["'Maravilha! Agora estou pronta para um belo café da manhã.' Estar pronto para alguma coisa se liga sempre com", (None, 'ready for'), 'pronta para um café reforçado.']),
]
