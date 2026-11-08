# Authoring module for linden-courtyard-pt-s01e02-scene-02.
ID = 'linden-courtyard-pt-s01e02-scene-02'
SHOW = 'linden-courtyard-pt'
SEASON = 1
EPISODE = 2
SCENE = 2
TITLE = 'No Milk in the Fridge  (Sem leite na geladeira)'
LEVEL = 'A1 — iniciante'
PAIR = 'en-pt'
LABELS = {'tessa': 'Tessa', 'hannah': 'Hannah', 'arthur': 'Arthur'}
INTRO = 'De volta à cozinha do café, Tessa abre a geladeira e leva um susto bem na hora em que Hannah e o proprietário Arthur entram. Oito hóspedes estão acordando lá em cima, e o café da manhã começa em vinte minutos. Ouça primeiro.'
OPENER = 'Vamos conferir cada fala dessa correria.'
TRANSITION = 'Vamos escutar toda a cena de novo no ritmo natural.'
OUTRO = 'Munida da lista de compras e de dinheiro do caixa, Hannah dispara rumo ao mercadinho da esquina. Na próxima cena vamos ver o que ela traz de volta.'
CLOSING = ('hannah', 'See you later!')
STORY = [
    ('tessa', 'Oh no! Arthur, Hannah, we have a kitchen emergency!', 'Ah não! Arthur, Hannah, temos uma emergência na cozinha!'),
    ('arthur', 'Please do not say the word emergency before my morning coffee!', 'Por favor, não diga a palavra emergência antes do meu café da manhã!'),
    ('tessa', 'The dairy van has a flat tire outside town. Look in the fridge!', 'A van de laticínios está com um pneu furado fora da cidade. Olhem na geladeira!'),
    ('hannah', 'One tiny splash of milk, two eggs, and no butter at all!', 'Um pinguinho de leite, dois ovos e nada de manteiga!'),
    ('arthur', 'Eight hungry guests will come down the stairs at seven thirty!', 'Oito hóspedes famintos vão descer as escadas às sete e meia!'),
    ('tessa', 'My bread dough is ready in the oven, at least.', 'Minha massa de pão já está pronta no forno, pelo menos.'),
    ('hannah', 'Give me a bag and some cash! The corner market opens at seven.', 'Me dê uma sacola e algum dinheiro vivo! O mercadinho da esquina abre às sete.'),
    ('arthur', 'Can you run there and back in ten minutes?', 'Você consegue ir correndo até lá e voltar em dez minutos?'),
    ('hannah', 'Watch me! Tell me exactly what to buy.', 'Pode apostar! Me diga exatamente o que comprar.'),
    ('tessa', 'Three bottles of milk, twenty eggs, butter, cheese, and red apples!', 'Três garrafas de leite, vinte ovos, manteiga, queijo e maçãs vermelhas!'),
    ('arthur', 'Here is fifty from the cash box. Bring back the receipt!', 'Aqui estão cinquenta do caixa. Traga a nota fiscal de volta!'),
    ('hannah', 'Hold the fort, I am already out the door!', 'Segurem as pontas aí, já estou saindo pela porta!'),
]
WALK = [
    (0, None, ["'Ah não! Arthur, Hannah, temos uma emergência na cozinha!' Em inglês, colocar um substantivo antes de outro qualifica o tipo de situação:", (None, 'kitchen emergency'), 'emergência de cozinha.']),
    (1, None, ["'Por favor, não diga a palavra emergência antes do meu café da manhã!' Um pedido educado na negativa começa sempre muito claro com", (None, 'Please do not say'), 'por favor não diga.']),
    (2, None, ["'A van de laticínios está com um pneu furado fora da cidade. Olhem na geladeira!' Pneu murcho ou furado no inglês americano se chama", (None, 'a flat tire'), 'ao pé da letra, um pneu achatado.']),
    (3, None, ["'Um pinguinho de leite, dois ovos e nada de manteiga!' Para reforçar que não sobrou nadinha mesmo, o inglês fecha com", (None, 'no butter at all'), 'absolutamente nada de manteiga.']),
    (4, None, ["'Oito hóspedes famintos vão descer as escadas às sete e meia!' Em inglês ninguém 'tem fome' com o verbo ter; a pessoa 'está faminta', como em", (None, 'hungry guests'), 'hóspedes com fome.']),
    (5, None, ["'Minha massa de pão já está pronta no forno, pelo menos.' No fim da frase,", (None, 'at least'), "traz aquele alívio parcial do nosso 'pelo menos'."]),
    (6, None, ["'Me dê uma sacola e algum dinheiro vivo! O mercadinho da esquina abre às sete.' Dinheiro em cédulas ou moedas é incontável:", (None, 'some cash'), 'algum dinheiro em espécie.']),
    (7, None, ["'Você consegue ir correndo até lá e voltar em dez minutos?' Veja que jeito rápido de dizer 'ir lá e voltar':", (None, 'there and back'), 'ida e volta.']),
    (8, None, ["'Pode apostar! Me diga exatamente o que comprar.' Quando alguém aceita um desafio na hora,", (None, 'Watch me'), "quer dizer 'fique só olhando!', seguido de", (None, 'what to buy'), 'o que comprar.']),
    (9, None, ["'Três garrafas de leite, vinte ovos, manteiga, queijo e maçãs vermelhas!' Como líquidos são incontáveis, contamos os recipientes em", (None, 'Three bottles of milk'), 'três garrafas de leite.']),
    (10, None, ["'Aqui estão cinquenta do caixa. Traga a nota fiscal de volta!' Trazer algo de retorno combina verbo e partícula em", (None, 'Bring back'), 'traga de volta.']),
    (11, None, ["'Segurem as pontas aí, já estou saindo pela porta!' A expressão coloquial", (None, 'Hold the fort'), "literalmente 'segurem o forte', pede que cuidem de tudo enquanto você sai."]),
]
