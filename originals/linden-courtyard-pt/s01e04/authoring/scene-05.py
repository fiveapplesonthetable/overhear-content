# Authoring module for linden-courtyard-pt-s01e04-scene-05.
ID = 'linden-courtyard-pt-s01e04-scene-05'
SHOW = 'linden-courtyard-pt'
SEASON = 1
EPISODE = 4
SCENE = 5
TITLE = 'Five-Star Showers  (Banhos cinco estrelas)'
LEVEL = 'A1 — iniciante'
PAIR = 'en-pt'
LABELS = {'arthur': 'Arthur', 'caleb': 'Caleb', 'hannah': 'Hannah'}
INTRO = 'Vinte minutos depois, no cantinho ensolarado do café, Caleb desce renovado enquanto Hannah serve café e Arthur ronda a mesa ansioso. Ouça primeiro.'
OPENER = 'Vamos conferir cada fala passo a passo.'
TRANSITION = 'Agora vamos ouvir toda a conversa novamente.'
OUTRO = 'Arthur entregou o segredo em tempo recorde e, em vez de ficar sério, Caleb convidou todos até o pátio para mostrar seu verdadeiro trabalho! Até logo.'
CLOSING = ('caleb', 'Take care!')
STORY = [
    ('caleb', 'Good morning, Hannah! Good morning, sir! What a bright morning after the rain.', 'Bom dia, Hannah! Bom dia, senhor! Que manhã iluminada depois da chuva.'),
    ('hannah', 'Good morning, Caleb! Did you sleep well under the roof beams?', 'Bom dia, Caleb! O senhor dormiu bem sob as vigas do telhado?'),
    ('caleb', 'Best sleep I have had all month, and the shower water was wonderfully hot!', 'A melhor noite de sono que tive o mês inteiro, e a água do chuveiro estava maravilhosamente quente!'),
    ('arthur', 'Hot! Hear that, Hannah? Reliable, modern, five-star hot water!', 'Quente! Ouviu isso, Hannah? Água quente confiável, moderna e cinco estrelas!'),
    ('caleb', 'Old brick buildings usually take ages to warm up on the top floor.', 'Prédios antigos de tijolo costumam demorar uma eternidade para esquentar no último andar.'),
    ('arthur', "Please write that down! 'Hot water on the third floor: ten out of ten!'", "Por favor, anote isso! 'Água quente no terceiro andar: dez de dez!'"),
    ('caleb', 'Excuse me? Ten out of ten?', 'Como assim? Dez de dez?'),
    ('hannah', 'What Arthur means is... we hope every guest feels ten out of ten here!', 'O que o Arthur quer dizer é... esperamos que todo hóspede se sinta nota dez aqui!'),
    ('arthur', 'No, Hannah, let us be honest professionals! Sir, we respect the Portland Travel Guide!', 'Não, Hannah, sejamos profissionais sinceros! Senhor, nós respeitamos o Guia de Viagens de Portland!'),
    ('caleb', 'The Portland Travel Guide? Wait, do you think I am a hotel inspector?', 'O Guia de Viagens de Portland? Esperem, vocês acham que eu sou um inspetor de hotéis?'),
    ('hannah', "When your notebook fell open on the counter last night, we saw 'nine out of ten'...", "Quando o seu caderno caiu aberto no balcão ontem à noite, nós vimos 'nove de dez'..."),
    ('caleb', 'Oh! Come outside to the courtyard for a minute. Let me show you what I really do!', 'Ah! Venham lá fora no pátio por um minuto. Deixem eu mostrar o que realmente faço!'),
]
WALK = [
    (0, None, ["'Bom dia, Hannah! Bom dia, senhor! Que manhã iluminada depois da chuva.' Para exclamar 'que manhã iluminada!', lembre do artigo em", (None, 'What a bright morning'), 'antes do adjetivo.']),
    (1, None, ["'Bom dia, Caleb! O senhor dormiu bem sob as vigas do telhado?' Na pergunta no passado com auxiliar,", (None, 'Did you sleep well'), "mantém 'sleep' na forma básica."]),
    (2, None, ["'A melhor noite de sono que tive o mês inteiro, e a água do chuveiro estava maravilhosamente quente!' Como o mês ainda não acabou, entra o tempo perfeito em", (None, 'I have had all month'), 'que tive no mês todo.']),
    (3, None, ["'Quente! Ouviu isso, Hannah? Água quente confiável, moderna e cinco estrelas!' Na fala coloquial,", (None, 'Hear that'), "encurta 'did you hear that?' sem perder clareza."]),
    (4, None, ["'Prédios antigos de tijolo costumam demorar uma eternidade para esquentar no último andar.' A expressão informal", (None, 'take ages'), 'quer dizer demorar um tempão.']),
    (5, None, ["'Por favor, anote isso! Água quente no terceiro andar: dez de dez!' Com o pronome no meio,", (None, 'write that down'), 'significa colocar no papel para registrar.']),
    (6, None, ["'Como assim? Dez de dez?' Dito em tom de pergunta,", (None, 'Excuse me'), 'pede esclarecimento quando alguém diz algo inesperado.']),
    (7, None, ["'O que o Arthur quer dizer é... esperamos que todo hóspede se sinta nota dez aqui!' Para explicar com jeito o que outra pessoa falou, comece com", (None, 'What Arthur means is'), 'o que ele quer dizer é.']),
    (8, None, ["'Não, Hannah, sejamos profissionais sinceros! Senhor, nós respeitamos o Guia de Viagens de Portland!' A estrutura", (None, 'let us be'), 'convida o grupo a agir de determinada maneira.']),
    (9, None, ["'O Guia de Viagens de Portland? Esperem, vocês acham que eu sou um inspetor de hotéis?' Com profissões no singular o inglês sempre pede artigo indefinido:", (None, 'a hotel inspector'), 'um inspetor.']),
    (10, None, ["'Quando o seu caderno caiu aberto no balcão ontem à noite, nós vimos nove de dez...' Para dizer 'ontem à noite', use sempre", (None, 'last night'), 'sem nenhuma preposição antes.']),
    (11, None, ["'Ah! Venham lá fora no pátio por um minuto. Deixem eu mostrar o que realmente faço!' A oferta simpática", (None, 'Let me show you'), 'abre qualquer demonstração prática.']),
]
