# Authoring module for linden-courtyard-pt-s01e04-scene-08.
ID = 'linden-courtyard-pt-s01e04-scene-08'
SHOW = 'linden-courtyard-pt'
SEASON = 1
EPISODE = 4
SCENE = 8
TITLE = 'The Boy on the Stairs  (O menino na escada)'
LEVEL = 'A1 — iniciante'
PAIR = 'en-pt'
LABELS = {'evelyn': 'Evelyn', 'hannah': 'Hannah', 'caleb': 'Caleb'}
INTRO = 'Saindo para o pátio iluminado pelo sol, a senhorita Evelyn conta mais a Hannah sobre os dois irmãos do número doze, sem perceber que Caleb acabou de descer a escada externa atrás delas. Vamos ouvir.'
OPENER = 'Vamos repassar com calma esta cena emocionante.'
TRANSITION = 'Escute mais uma vez toda a conversa do começo ao fim.'
OUTRO = 'Que encontro no pátio: o pequeno Caleb do terceiro degrau está diante de sua professora de piano da infância, e ele é o dono da mala azul! Episodio quatro concluído; até o episódio cinco.'
CLOSING = ('caleb', 'Goodbye!')
STORY = [
    ('hannah', 'Tell me more about the two boys on Linden Street, Miss Evelyn!', 'Me conte mais sobre os dois meninos da rua Linden, senhorita Evelyn!'),
    ('evelyn', 'The older brother was bold and loud, always rushing through his music scales.', 'O irmão mais velho era destemido e barulhento, sempre correndo pelas escalas musicais.'),
    ('hannah', 'And the younger brother with the wooden train?', 'E o irmão mais novo, o do trenzinho de madeira?'),
    ('evelyn', 'Quiet as a mouse! He sat on the third stair listening to every single note.', 'Quieto feito um ratinho! Ele ficava sentado no terceiro degrau ouvindo cada nota.'),
    ('hannah', 'Listening to the sound of the room... wait a second!', 'Ouvindo o som do ambiente... espere um segundo!'),
    ('evelyn', 'Whenever I finished playing, he asked why the piano sounded warmer when it rained.', 'Sempre que eu terminava de tocar, ele perguntava por que o piano soava mais acolhedor quando chovia.'),
    ('caleb', 'Because wet wooden shutters soften the echo from the stone street...', 'Porque as venezianas de madeira molhadas suavizam o eco da rua de pedra...'),
    ('hannah', 'Caleb! Were you standing right there?!', 'Caleb! Você estava parado bem aí?!'),
    ('evelyn', 'Good heavens... look at your eyes! Little Caleb from the third stair?!', 'Minha nossa... olhe para os seus olhos! O pequeno Caleb do terceiro degrau?!'),
    ('caleb', "Miss Evelyn?! My brother's Friday piano teacher?!", 'Senhorita Evelyn?! A professora de piano das sextas-feiras do meu irmão?!'),
    ('hannah', 'Wait, then Monday night on our step... the second blue suitcase...', 'Espere, então na segunda-feira à noite no nosso degrau... a segunda mala azul...'),
    ('caleb', 'Yes, Hannah. That blue suitcase is mine, and I owe you both the whole truth.', 'Sim, Hannah. Aquela mala azul é minha, e eu devo a vocês duas toda a verdade.'),
]
WALK = [
    (0, None, ["'Me conte mais sobre os dois meninos da rua Linden, senhorita Evelyn!' Com nomes de ruas o inglês americano usa 'on':", (None, 'on Linden Street'), 'na rua Linden.']),
    (1, None, ["'O irmão mais velho era destemido e barulhento, sempre correndo pelas escalas musicais.' A combinação", (None, 'rushing through'), 'mostra fazer uma lição às pressas para terminar logo.']),
    (2, None, ["'E o irmão mais novo, o do trenzinho de madeira?' Guarde o par de família:", (None, 'younger brother'), "irmão mais novo, fazendo par com 'older brother'."]),
    (3, None, ["'Quieto feito um ratinho! Ele ficava sentado no terceiro degrau ouvindo cada nota.' A expressão tradicional", (None, 'Quiet as a mouse'), 'descreve uma criança silenciosa e observadora.']),
    (4, None, ["'Ouvindo o som do ambiente... espere um segundo!' Quando uma ficha cai de repente na conversa, diga", (None, 'wait a second'), 'espere um segundo!']),
    (5, None, ["'Sempre que eu terminava de tocar, ele perguntava por que o piano soava mais acolhedor quando chovia.' Duas estruturas ótimas:", (None, 'Whenever'), "para 'sempre que', e '-ing' após 'finish' em", (None, 'finished playing'), 'terminava de tocar.']),
    (6, None, ["'Porque as venezianas de madeira molhadas suavizam o eco da rua de pedra...' O sufixo '-en' transforma o adjetivo 'soft' no verbo", (None, 'soften the echo'), 'suavizar o eco.']),
    (7, None, ["'Caleb! Você estava parado bem aí?!' Na pergunta no passado contínuo invertemos o verbo para", (None, 'Were you standing'), 'você estava parado?']),
    (8, None, ["'Minha nossa... olhe para os seus olhos! O pequeno Caleb do terceiro degrau?!' A exclamação gentil", (None, 'Good heavens'), 'demonstra grande surpresa de forma carinhosa.']),
    (9, None, ["'Senhorita Evelyn?! A professora de piano das sextas-feiras do meu irmão?!' Veja como o apóstrofo com esse liga o dono ao restante em", (None, "My brother's Friday piano teacher"), 'a professora do meu irmão.']),
    (10, None, ["'Espere, então na segunda-feira à noite no nosso degrau... a segunda mala azul...' Para juntar dia da semana e período, basta falar direto:", (None, 'Monday night'), 'segunda à noite.']),
    (11, None, ["'Sim, Hannah. Aquela mala azul é minha, e eu devo a vocês duas toda a verdade.' Quando o substantivo não se repete no final, entra o possessivo autônomo:", (None, 'is mine'), 'é minha.']),
]
