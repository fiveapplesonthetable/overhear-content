# Authoring module for domashniy-arest-s01e06-scene-15.
ID = 'domashniy-arest-s01e06-scene-15'
SHOW = 'domashniy-arest'
SEASON = 1
EPISODE = 6
SCENE = 15
TITLE = 'Знакомо ли тебе слово педикюр?  (Are You Familiar with the Word Pedicure?)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'arkady': 'Аркадий', 'klavdia': 'Клавдия Викторовна', 'marina': 'Марина'}
SOURCE_NAME = 'Домашний арест (Domashniy Arest) S1.06'
SOURCE_FILE = 'sources/domashniy-arest/s01/e06.ru.dual.srt'
INTRO = "Behind Colonel Mikhail Mikhailovich's back, Major Lavrov and Captain Ovechkin persuade diminutive Lieutenant Lyova Sokolov to dress up as a schoolboy so he can provoke Samsonov on camera. Meanwhile, back at the communal flat, Arkady scrubs Klavdia Viktorovna's mountain of laundry by hand to earn the five thousand roubles she promised him, while Marina prepares a cake in the kitchen. Let's listen in Russian first."
OPENER = "Let's walk through Arkady's chores and the kitchen conversation."
TRANSITION = "Now let's listen to the whole scene again from start to finish."
OUTRO = "While Marina leaves the tin of condensed milk boiling on the stove and Arkady is forced to give Klavdia Viktorovna a pedicure, Ivan Samsonov visits the city library. Listen for 'in the washing machine', 'back', and 'condensed milk' when you watch. See you next time!"
CLOSING = ('arkady', 'Пока!')
STORY = [
    ('klavdia', 'Аркашка, ты еле стираешь! Сильнее три!', "Arkashka, you're barely washing! Rub harder!", [(531, 'Еле'), (532, 'три')], "ASR 'жулькаешь / селее' -> 'стираешь / Сильнее'"),
    ('arkady', 'Клавдия Викторовна, нельзя иначе? Давайте это в стиральной машине постираем?', "Klavdia Viktorovna, can't we do it differently? Let's wash all this in the washing machine?", [(534, 'Клавдия Викторовна'), (534, 'в стиральной машине')], 'split 534 into two short sentences'),
    ('klavdia', 'Ты что, Аркашка? Это же югославские вещи! Их аккуратно руками надо стирать.', 'Are you crazy, Arkashka? These are Yugoslavian things! They have to be washed carefully by hand.', [(535, 'Ты что, Аркашка?'), (536, 'Это же югославские'), (537, 'Их аккуратно'), (537, 'надо')], ''),
    ('klavdia', 'Хватит болтать, столько дел впереди. Ты хочешь получить деньги или нет?', "And anyway stop chatting, there's so much work ahead. Do you want to get the money or not?", [(538, 'хватит болтать'), (539, 'Столько дел впереди'), (540, 'или нет?')], 'cleaned up cues 540-551'),
    ('arkady', 'Клавдия Викторовна, вы со всей квартиры бельё принесли! У меня спина болит.', 'Klavdia Viktorovna, you brought laundry from the whole flat! My back is hurting already.', [(541, 'Клавдия Викторовна, вы со всей квартиры белье')], "colloquial 'притащили' -> 'принесли'"),
    ('arkady', 'Ой, спина не разгибается! Какая вы строгая, Клавдия Викторовна.', "Ow, my back won't straighten! How strict you are, Klavdia Viktorovna.", [(555, 'Какая вы'), (556, 'Клавдия Викторовна')], "simplified 'неуемная' to 'строгая'"),
    ('arkady', 'Марина, зря вы стараетесь. Он никогда не уйдёт от своей Аллы Евгеньевны.', "Marina, you're trying in vain. He will never leave his Alla Evgenyevna.", [(561, 'он никогда не уйдет от своей Аллы Евгеньевны')], 'omitted crude cue 560'),
    ('marina', 'Он уже ушёл.', 'He has already left.', [(562, 'Уже ушел')], ''),
    ('arkady', 'Это он вам так сказал? И вы поверили?', 'Did he tell you that? And you believed him?', [(563, 'Это он вам так сказал? И вы поверили?')], ''),
    ('marina', 'Поверила. Он же не вы.', "I believed him. He isn't like you.", [(564, 'Поверила. Он же не вы')], ''),
    ('klavdia', 'Марина, опять ты со сгущёнкой! В прошлый раз я думала, война началась.', 'Marina, there you go again with your condensed milk! Last time I thought a war had started.', [(565, 'сгущенкой'), (566, 'В прошлый раз'), (566, 'я думала война началась')], ''),
    ('marina', 'Я сейчас таймер поставлю.', "I'll set a timer right now.", [(567, 'Я таймер поставлю')], ''),
    ('arkady', 'Клавдия Викторовна, я всё закончил! Давайте мои пять тысяч.', "Klavdia Viktorovna, I've finished everything! Hand over my five thousand.", [(568, 'я закончил'), (569, 'пять тысяч')], "colloquial 'Гоните' -> 'Давайте мои'"),
    ('klavdia', 'Ничего ты ещё не закончил!', "You haven't finished anything yet!", [(570, 'Ничего'), (570, 'не закончил')], "ASR 'тысяча' -> 'ты ещё'"),
    ('arkady', 'В смысле не закончил?', "What do you mean I haven't finished?", [(571, 'В смысле?')], ''),
    ('klavdia', 'А знакомо ли тебе, Аркашка, слово педикюр?', 'And are you familiar, Arkashka, with the word pedicure?', [(572, 'ли тебе, Аркашка, слово педикюр?')], "ASR 'знакома' -> 'знакомо'"),
]
WALK = [
    (0, None, "Standing over Arkady as he scrubs laundry in a basin, Klavdia Viktorovna scolds him: 'Arkashka, you're barely washing! Rub harder!'"),
    (1, 'Клавдия Викторовна, нельзя иначе?', "Exhausted, Arkady begs for mercy: 'Klavdia Viktorovna, can't we do it differently?'"),
    (1, 'Давайте это в стиральной машине постираем?', "'Let's wash this in the washing machine?' Notice the location endings on 'in the washing machine'."),
    (2, 'Ты что, Аркашка? Это же югославские вещи!', "'Are you crazy, Arkashka? These are Yugoslavian things!' In Soviet times, Yugoslavian clothes were prized imports."),
    (2, 'Их аккуратно руками надо стирать.', "'They have to be washed carefully by hand.' Literally 'with the hands', using the 'with'-form plural."),
    (3, 'Хватит болтать, столько дел впереди.', "'Stop chatting, there's so much work ahead.' The line opens with 'and' and lands on 'ahead' at the end for emphasis."),
    (3, 'Ты хочешь получить деньги или нет?', "'Do you want to get the money or not?' Remember, Arkady desperately needs the five thousand roubles."),
    (4, 'Клавдия Викторовна, вы со всей квартиры бельё принесли!', "'Klavdia Viktorovna, you brought laundry from the whole flat!' Arkady puts 'flat' up front and finishes with 'brought' to make the point unmistakable."),
    (4, 'У меня спина болит.', "'My back is hurting.' After washing the clothes and moving her heavy furniture, Arkady stumbles into the kitchen."),
    (5, None, "Holding his lower back, he groans: 'Ow, my back won't straighten! How strict you are, Klavdia Viktorovna.' At the stove, he sees Marina boiling a can of condensed milk for her dean Eduard Vladimirovich."),
    (6, 'Марина, зря вы стараетесь.', "'Marina, you're trying in vain.' Arkady uses the polite plural 'you' alongside 'are trying', keeping a formal or respectful register."),
    (6, 'Он никогда не уйдёт от своей Аллы Евгеньевны.', "'He will never leave his Alla Evgenyevna.' Remember that the dean's wife is the university rector."),
    (7, None, "Marina answers proudly: 'He has already left.'"),
    (8, None, "Arkady is sceptical: 'Did he tell you that? And you believed him?'"),
    (9, None, "'I believed him. He isn't like you.' Notice the feminine past-tense ending '-la' when Marina says 'I believed'. Just then Klavdia Viktorovna walks in and spots the saucepan on the stove."),
    (10, 'Марина, опять ты со сгущёнкой!', "'Marina, there you go again with the condensed milk!' If a sealed tin of condensed milk boils dry, it explodes across the kitchen."),
    (10, 'В прошлый раз я думала, война началась.', "'Last time I thought a war had started.' The key word here means 'last', anchored at the close by 'started'."),
    (11, None, "Marina reassures her: 'I'll set a timer right now.'"),
    (12, 'Клавдия Викторовна, я всё закончил!', "Arkady proudly announces: 'Klavdia Viktorovna, I've finished everything!'"),
    (12, 'Давайте мои пять тысяч.', "'Hand over my five thousand.' The line opens with 'give' and lands on 'thousand' at the end for emphasis."),
    (13, None, "Klavdia Viktorovna shakes her head: 'You haven't finished anything yet!' Notice the double negation with 'nothing' and 'not'."),
    (14, None, "'What do you mean I haven't finished?' The verb for 'finished' is in the masculine past tense, marked by that 'l' sound at the end."),
    (15, None, "Pointing down at her slippers, the old neighbour smiles wickedly: 'And are you familiar, Arkashka, with the word pedicure?'"),
]
