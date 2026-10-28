# Authoring module for domashniy-arest-s01e06-scene-18.
ID = 'domashniy-arest-s01e06-scene-18'
SHOW = 'domashniy-arest'
SEASON = 1
EPISODE = 6
SCENE = 18
TITLE = 'Привяжи ты к швабре веник  (Tie a Broom to a Mop)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'arkady': 'Аркадий', 'klavdia': 'Клавдия Викторовна', 'nina': 'Нина'}
SOURCE_NAME = 'Домашний арест (Domashniy Arest) S1.06'
SOURCE_FILE = 'sources/domashniy-arest/s01/e06.ru.dual.srt'
INTRO = "Back in the communal flat, exhausted Arkady has just finished giving old Klavdia Viktorovna a pedicure to earn five thousand roubles. Now Klavdia adds one final task before she will pay Arkady, while next door a soaking-wet Samson and Nina confront young Slavik about his sister Yulia. Let's listen in Russian first."
OPENER = "Let's go through it line by line. Sitting in the kitchen with freshly scrubbed feet, Klavdia Viktorovna boasts to Marina about Arkady's pedicure skills."
TRANSITION = "Now let's listen to the whole scene in the communal flat again."
OUTRO = "So Nina dragged Samson off to search for Yulia, while Arkady still could not reach the tree branch outside the kitchen window. Next time we'll join Ilona at the Sineozersk ballet studio as she checks out Ignatyev's ballerina daughter. See you next time!"
CLOSING = ('arkady', 'Пока!')
STORY = [
    ('klavdia', 'Ой, Маринка, я как заново родилась! Пяточки как у младенца.', "Oh, Marinka, I feel as if I've been born again! Heels like a baby's.", [(666, 'Ой, Маринка, я как заново родилась'), (667, 'Пяточки, как у младенца')], ''),
    ('klavdia', 'Он ещё пемзочкой прошёлся.', 'He even went over them with a pumice stone.', [(668, 'Он еще'), (668, 'прошелся')], "ASR 'пензочкой' -> 'пемзочкой'"),
    ('arkady', 'Так, гоните деньги, хозяйка.', 'Right, hand over the money, landlady.', [(669, 'Так, гоните')], "slang 'кэш, рабовладелица' -> 'деньги, хозяйка'"),
    ('klavdia', 'Пакет с ветки снимешь — и отдам.', "Take the bag off the branch and I'll give it to you.", [(670, 'снимешь и отдам')], "crude noun in 670 replaced with 'Пакет с ветки'"),
    ('arkady', 'Чего? Какой ещё пакет?', 'What? What bag?', [(671, 'Чего, какой еще')], "'пакет' added"),
    ('klavdia', 'А он тут, соседи сверху бросили. Уже месяц висит на улице!', "It's right here, the upstairs neighbours threw it. It's been hanging outside for a month already!", [(672, 'А он тут, соседи сверху'), (674, 'Уже месяц висит'), (676, 'на улице')], "'забавляются' -> 'бросили'"),
    ('klavdia', 'Я к печке подхожу. А он маячит перед глазами!', 'I walk up to the stove. And it dangles right before my eyes!', [(673, 'к печке подхожу'), (673, 'он маячит перед глазами')], 'split into two short sentences'),
    ('arkady', 'Он не в квартире, он на улице! Так вы и Луну видите.', "But it's not in the flat, it's outside! Well, you can see the Moon too.", [(676, 'не в квартире, он на улице'), (679, 'Так вы и Луну видите')], ''),
    ('klavdia', 'Я же его вижу! Ну не хочешь — как хочешь.', "But I can see it! Well, if you don't want to, suit yourself.", [(678, 'Я же его вижу'), (680, 'Ну не хочешь, как хочешь')], ''),
    ('nina', 'Дочь две недели в школу не ходит! Это тоже нормально?', "Our daughter hasn't been going to school for two weeks! Is that normal too?", [(688, 'дочь две недели в школу не ходит, это тоже нормально')], ''),
    ('nina', 'Славик, ты почему не сказал про сестру?', "Slavik, why didn't you tell us about your sister?", [(690, 'не сказал')], 'simplified from 690'),
    ('nina', 'Мы не знаем, что с нашей дочерью происходит!', "We don't know what is happening with our daughter!", [(695, 'мы не знаем, что с нашей дочерью происходит')], ''),
    ('nina', 'Если тебе плевать на дочь, то мне нет! Ты водишь.', "If you don't care about our daughter, I do! You're driving.", [(699, 'Если тебе плевать на дочь, то мне нет'), (700, 'Ты водишь')], ''),
    ('arkady', 'Когда нет в кармане денег. Привяжи ты к швабре веник!', 'When there is no money in your pocket. Tie a broom to a mop!', [(702, 'Когда нет в кармане денег'), (703, 'привяжи ты к швабре веник')], ''),
    ('arkady', 'Не получается. Ну, на нет и денег нет.', "It's not working. Well, where there's nothing, there's no money either.", [(704, 'Не получается'), (705, 'Ну, на нет и'), (705, 'нет')], "crude noun in 705 replaced with 'денег'"),
]
WALK = [
    (0, 'Ой, Маринка, я как заново родилась!', "'Oh, Marinka, I feel as if I've been born again!' Because Klavdia is a woman, the past-tense verb ends in '-las'."),
    (0, 'Пяточки как у младенца.', "'Heels like a baby's.' She uses a tender diminutive for 'heels'."),
    (1, None, "'He even went over them with a pumice stone.' The 'with'-form diminutive means 'with a little pumice stone'. Rubbing his aching back, Arkady holds out his hand for the promised five thousand roubles."),
    (2, None, "'Right, hand over the money, landlady.' Meanwhile, Klavdia points out the kitchen window at a bare tree branch."),
    (3, None, "'Take the bag off the branch and I'll give it to you.' Both verbs are in the future-tense form: 'you will take it off, and I will give it'."),
    (4, 'Чего?', "'What?' Arkady stares at her in disbelief."),
    (4, 'Какой ещё пакет?', "'What bag?' He walks over to the window."),
    (5, 'А он тут, соседи сверху бросили.', "'It's right here, the upstairs neighbours threw it.' Klavdia Viktorovna puts 'right here' up front and finishes with 'threw' to make the point unmistakable."),
    (5, 'Уже месяц висит на улице!', "'It's been hanging outside for a month already!' Russian uses the present tense for an action that started in the past and is still going on."),
    (6, 'Я к печке подхожу.', "'I walk up to the stove.' Klavdia describes walking up to the kitchen stove expecting a hot meal."),
    (6, 'А он маячит перед глазами!', "'And it dangles right before my eyes!' After 'in front of', 'eyes' takes the 'with'-form plural."),
    (7, 'Он не в квартире, он на улице!', "'It's not in the flat, it's outside!' Russian leaves out 'am', 'is', or 'are' in the present tense, linking 'it' straight to 'outside'."),
    (7, 'Так вы и Луну видите.', "'Well, you can see the Moon too.' Arkady points out the flaw in her logic, but Klavdia will not budge."),
    (8, 'Я же его вижу!', "'But I can see it!' She points right at it, protesting that she can see it with her own eyes!"),
    (8, 'Ну не хочешь — как хочешь.', "'Well, if you don't want to, suit yourself.' Literally 'you don't want, as you want'. Meanwhile, in the Samsonovs' room, soaking-wet Samson and Nina are scolding Slavik over the collage he made at school."),
    (9, 'Дочь две недели в школу не ходит!', "'Our daughter hasn't been going to school for two weeks!' Nina explodes with the news from the teacher: their daughter hasn't been going to school for two weeks!"),
    (9, 'Это тоже нормально?', "'Is that normal too?' Nina turns on young Slavik."),
    (10, None, "'Slavik, why didn't you tell us about your sister?' At this point, Slavik mutters proudly that he is not a snitch, and Samson agrees that a real boy never rats anyone out."),
    (11, None, "'We don't know what is happening with our daughter!' After 'with', both 'our' and 'daughter' take the 'with/as' form."),
    (12, 'Если тебе плевать на дочь, то мне нет!', "'If you don't care about our daughter, I do!' Russian omits the present-tense verb 'to be', connecting 'if' directly with 'not!'."),
    (12, 'Ты водишь.', "'You're driving.' Nina marches Samson out the door to look for Yulia. Back in the kitchen, Arkady ties a short broom to the end of a wooden mop and makes up a little rhyme."),
    (13, 'Когда нет в кармане денег.', "'When there is no money in your pocket.' He mutters bitterly about how life feels when you don't have a single kopek in your pocket."),
    (13, 'Привяжи ты к швабре веник!', "'Tie a broom to a mop!' Leaning out the open window, he pokes at the tree branch with his contraption."),
    (14, 'Не получается.', "'It's not working.' The branch is still just out of reach."),
    (14, 'Ну, на нет и денег нет.', "'Well, where there's nothing, there's no money either.' He plays on a famous Russian proverb that means 'where there is nothing, there is no trial either'."),
]
