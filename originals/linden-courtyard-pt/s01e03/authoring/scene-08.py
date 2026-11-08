# Authoring module for linden-courtyard-pt-s01e03-scene-08.
ID = 'linden-courtyard-pt-s01e03-scene-08'
SHOW = 'linden-courtyard-pt'
SEASON = 1
EPISODE = 3
SCENE = 8
TITLE = 'Ice-Cold Pipes  (Canos gelados)'
LEVEL = 'A1 — iniciante'
PAIR = 'en-pt'
LABELS = {'graham': 'Graham', 'hannah': 'Hannah', 'arthur': 'Arthur'}
INTRO = 'Lá embaixo na recepção, Hannah e Arthur esperam apreensivos perto da porta do porão até Graham subir limpando as mãos num pano e balançando a cabeça. Vamos ouvir primeiro.'
OPENER = 'Agora vamos conferir cada frase com calma.'
TRANSITION = 'Vamos escutar toda a cena mais uma vez sem pausas.'
OUTRO = 'Um suposto inspetor de guia de viagens no terceiro andar, uma válvula quebrada no porão e uma corrida às sete da manhã pelo outro lado da ponte! Fim do episódio três; nos vemos no episódio quatro.'
CLOSING = ('graham', 'See you tomorrow!')
STORY = [
    ('arthur', 'Tell me it was just a tiny air bubble, Graham! Please!', 'Me diga que era só uma bolhinha de ar, Graham! Por favor!'),
    ('graham', 'Bad news. The brass pressure valve on the old boiler just gave up.', 'Más notícias. A válvula de pressão de latão da caldeira velha acabou de pifar.'),
    ('hannah', 'Does that mean no radiators tonight, or no hot water too?', 'Isso quer dizer sem aquecedores hoje à noite, ou sem água quente também?'),
    ('graham', 'The rooms will stay warm until morning, Hannah, because the brick walls hold heat.', 'Os quartos vão continuar quentes até de manhã, Hannah, porque as paredes de tijolo seguram o calor.'),
    ('arthur', 'Thank heavens! And the morning showers?', 'Graças aos céus! E os banhos da manhã?'),
    ('graham', 'At seven tomorrow morning, the shower water will be ice cold.', 'Amanhã às sete da manhã, a água do chuveiro vai estar gelada.'),
    ('arthur', 'Ice cold showers?! With the Portland Travel Guide inspector on the third floor?!', 'Banhos gelados?! Com o inspetor do Guia de Viagens de Portland no terceiro andar?!'),
    ('hannah', 'Do you have a spare brass valve in your toolbox?', 'Você tem uma válvula de latão reserva na sua caixa de ferramentas?'),
    ('graham', 'Used my last one in winter. Only the old hardware shop past the bridge sells this size.', 'Usei a última no inverno. Só a velha loja de ferragens depois da ponte vende deste tamanho.'),
    ('hannah', 'What time does that hardware shop open?', 'A que horas abre essa loja de ferragens?'),
    ('graham', 'Seven sharp, half an hour before breakfast.', 'Às sete em ponto, meia hora antes do café da manhã.'),
    ('hannah', 'Set your alarm, Graham. Tomorrow morning we beat the cold showers!', 'Coloque seu despertador, Graham. Amanhã cedo nós vencemos os banhos frios!'),
]
WALK = [
    (0, None, ["'Me diga que era só uma bolhinha de ar, Graham! Por favor!' Logo depois de", (None, 'Tell me'), "o inglês costuma dispensar o equivalente ao nosso 'que' e seguir direto."]),
    (1, None, ["'Más notícias. A válvula de pressão de latão da caldeira velha acabou de pifar.' Repare no verbo com partícula", (None, 'gave up'), "que literalmente é 'desistiu', ótimo para máquinas que param de funcionar."]),
    (2, None, ["'Isso quer dizer sem aquecedores hoje à noite, ou sem água quente também?' No fim da frase,", (None, 'too'), "acrescenta 'também' de forma leve e natural."]),
    (3, None, ["'Os quartos vão continuar quentes até de manhã, Hannah, porque as paredes de tijolo seguram o calor.' O par", (None, 'stay warm'), "une 'continuar' ao adjetivo para mostrar que o calor se mantém."]),
    (4, None, ["'Graças aos céus! E os banhos da manhã?' A exclamação", (None, 'Thank heavens'), "expressa alívio imediato, igual ao nosso 'ainda bem!' ou 'graças aos céus!'."]),
    (5, None, ["'Amanhã às sete da manhã, a água do chuveiro vai estar gelada.' A combinação", (None, 'ice cold'), 'pinta a cena na hora: fria como gelo.']),
    (6, None, ["'Banhos gelados?! Com o inspetor do Guia de Viagens de Portland no terceiro andar?!' Para andares de prédios o inglês usa sempre a preposição de superfície:", (None, 'on the third floor'), 'no terceiro andar.']),
    (7, None, ["'Você tem uma válvula de latão reserva na sua caixa de ferramentas?' Antes de qualquer peça ou chave,", (None, 'spare'), 'indica algo sobressalente ou reserva.']),
    (8, None, ["'Usei a última no inverno. Só a velha loja de ferragens depois da ponte vende deste tamanho.' Loja de ferragens em inglês é", (None, 'hardware shop'), 'e', (None, 'past the bridge'), "indica 'passando da ponte'."]),
    (9, None, ["'A que horas abre essa loja de ferragens?' Para perguntar horários não usamos preposição na frente:", (None, 'What time does'), "já vale por 'a que horas?'."]),
    (10, None, ["'Às sete em ponto, meia hora antes do café da manhã.' Depois de um horário,", (None, 'Seven sharp'), 'garante pontualidade total: sete em ponto.']),
    (11, None, ["'Coloque seu despertador, Graham. Amanhã cedo nós vencemos os banhos frios!' Para programar o alarme do relógio ou celular, diga sempre", (None, 'Set your alarm'), 'ajustar o despertador.']),
]
