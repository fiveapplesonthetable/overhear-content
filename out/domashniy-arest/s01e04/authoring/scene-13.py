# domashniy-arest/s01e04/scene-13.py
ID = "domashniy-arest-s01e04-scene-13"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 4
SCENE = 13
TITLE = "Политтехнолог из Москвы  (The Strategist from Moscow)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.04"
SOURCE_FILE = "sources/domashniy-arest/s01/e04.ru.dual.srt"
VOICES = {"narrator": "sky", "ksyusha": "anja", "ilona": "angelina"}
LABELS = {"ksyusha": "Ксюша", "ilona": "Илона"}
INTRO = "Last time, Arkady and Samson held a press conference in the courtyard and announced that Samson is running for mayor. Meanwhile, at acting mayor Pasha Osipenko's campaign headquarters, young coordinator Ksyusha is presenting a new election poster to the room, where Moscow strategist Ilona Leonidovna is listening quietly. We'll hear it in Russian first; don't worry about catching every word."
STORY = [
    ("ksyusha", "Мы провели опросы. Стихи работают лучше всего!", "We conducted polls. Verses work best of all!", [(431, 'опросов'), (431, 'работает лучше всего')], "cue 431 'По данным наших опросов, стихотворная форма работает лучше всего' simplified to two A1 sentences"),
    ("ksyusha", "Это легко, доступно и хорошо запоминается.", "It is easy, accessible, and easy to remember.", [(435, 'легко, доступно и хорошо запоминается')], ""),
    ("ksyusha", "«Пенсионер, болит твоя коленка? Проголосуй за Павла Осипенко!»", "'Pensioner, does your knee hurt? Vote for Pavel Osipenko!'", [(436, 'Пенсионер, болит твоя коленка, проголосуй за Павла Осипенко')], ""),
    ("ksyusha", "Павлу Юрьевичу это очень нравится!", "Pavel Yuryevich likes this very much!", [(439, 'Павлу Юрьевичу нравится')], "'это очень' added"),
    ("ilona", "Я рада. Только всё это нужно переделать.", "I'm glad. Only all of this needs to be redone.", [(440, 'Я рада'), (441, 'Только все это нужно')], "'перепридумать' -> 'переделать'"),
    ("ksyusha", "А мы считаем, что ничего менять не надо.", "And we think that nothing needs to be changed.", [(442, 'А мы считаем, что ничего'), (442, 'не надо')], "'перепридумывать' -> 'менять'"),
    ("ilona", "Я новый руководитель предвыборного штаба Павла Юрьевича.", "I am the new head of Pavel Yuryevich's campaign headquarters.", [(446, 'руководитель предвыборного штаба Павла Юрьевича')], ""),
    ("ksyusha", "Прошу прощения за опоздание! Сидите, сидите. Уже познакомились?", "I apologise for being late! Sit, sit. Have you met already?", [(455, 'Прошу прощения за опоздание'), (456, 'Сидите, сидите'), (457, 'познакомились')], ""),
    ("ksyusha", "Илона Леонидовна из Москвы будет руководить нашим штабом.", "Ilona Leonidovna from Moscow will lead our headquarters.", [(459, 'Илона Леонидовна'), (459, 'из Москвы'), (460, 'будет руководить нашим'), (460, 'штабом')], ""),
    ("ksyusha", "Ну, начинаем. Что у нас нового?", "Well, let's begin. What's new with us?", [(461, 'Ну'), (462, 'у нас')], "'приступим. Чего у нас там?' -> 'начинаем. Что у нас нового?'"),
    ("ksyusha", "У нас большая проблема! Новый конкурент — Иван Самсонов.", "We have a big problem! A new rival — Ivan Samsonov.", [(464, 'У нас'), (466, 'Новый конкурент. Иван Самсонов')], "'форс-мажор' -> 'большая проблема'"),
    ("ksyusha", "Ну и что? У него ни ума, ни денег, ни образования!", "So what? He has neither brains, nor money, nor education!", [(467, 'Ну и что'), (468, 'У него ни ума, ни денег, ни образования')], "insult 'дебил' in 467 omitted"),
    ("ksyusha", "Павел Юрьевич, а вас много показывают по телевизору?", "Pavel Yuryevich, do they show you a lot on television?", [(469, 'Павел Юрьевич'), (470, 'много')], "cue 470 'У вас было много эфиров на центральном телевизоре?' simplified"),
    ("ksyusha", "Ну, пока ещё не было.", "Well, not yet so far.", [(471, 'Ну, пока не было еще')], ""),
    ("ksyusha", "А его весь день показывают! Он самый известный человек в Синеозерске.", "And they show him all day long! He is the most famous man in Sineozersk.", [(472, 'А его весь день показывают'), (473, 'Он самый известный человек в Синеозерске')], ""),
    ("ksyusha", "Он самый известный клоун в Синеозерске! Я не хочу об этом слышать.", "He is the most famous clown in Sineozersk! I don't want to hear about this.", [(474, 'Он самый известный клоун в Синеозерске'), (475, 'я'), (475, 'не хочу об этом'), (475, 'слышать')], ""),
]
OPENER = "Let's walk through it. Notice that Arkady isn't here, so Ilona Leonidovna takes the main voice as Ksyusha pitches a dreadful campaign rhyme."
WALK = [
    (0, None, "'We conducted polls. Verses work best of all!' 'Best of all' is literally 'better of everything'. Ksyusha explains why."),
    (1, None, "'It is easy, accessible, and easy to remember.' Literally 'is remembered well'. Then she reads the slogan on the poster."),
    (2, '«Пенсионер, болит твоя коленка?', "''Pensioner, does your knee hurt?' There is no question word here — in Russian, rising intonation on 'knee' is enough to make it a question."),
    (2, 'Проголосуй за Павла Осипенко!»', "'Vote for Pavel Osipenko!' In Russian, the word for 'knee' rhymes with the surname 'Osipenko'. Notice that voting 'for' someone uses the preposition 'behind, for' plus the direct-object form. Ksyusha beams proudly."),
    (3, None, "'Pavel Yuryevich likes this very much!' Literally 'to Pavel Yuryevich this is very pleasing'. From the back of the room, Ilona speaks up coolly."),
    (4, 'Я рада.', "'I'm glad.' The short adjective has the feminine ending because Ilona is a woman."),
    (4, 'Только всё это нужно переделать.', "'Only all of this needs to be redone.' The prefix on the verb means 're-, over again'. Ksyusha bristles, thinking Ilona is just a focus-group volunteer."),
    (5, None, "'And we think that nothing needs to be changed.' So Ilona steps up to the board and introduces herself."),
    (6, None, "'I am the new head of Pavel Yuryevich's campaign headquarters.' Just then, Pasha himself hurries into the room."),
    (7, None, "'I apologise for being late! Sit, sit. Have you met already?' And he confirms who Ilona is."),
    (8, None, "'Ilona Leonidovna from Moscow will lead our headquarters.' The verb 'to lead, to head' takes the 'with/as' form: 'our headquarters'. Then Pasha sits down to business."),
    (9, None, "'Well, let's begin. What's new with us?' Ksyusha looks at her tablet with bad news."),
    (10, 'У нас большая проблема!', "'We have a big problem!' Literally 'by us is a big problem'."),
    (10, 'Новый конкурент — Иван Самсонов.', "'A new rival — Ivan Samsonov.' Pasha laughs it off."),
    (11, 'Ну и что?', "'So what?' Three small words to brush off the news."),
    (11, 'У него ни ума, ни денег, ни образования!', "'He has neither brains, nor money, nor education!' Repeated before each noun, that little negative particle means 'neither... nor...', and every noun after it goes into the 'of' form. Ksyusha asks a pointed question."),
    (12, None, "'Pavel Yuryevich, do they show you a lot on television?' Pasha mumbles."),
    (13, None, "'Well, not yet so far.' And Ksyusha delivers the punchline."),
    (14, 'А его весь день показывают!', "'And they show him all day long!' The key word here means 'day', anchored at the close by 'show'."),
    (14, 'Он самый известный человек в Синеозерске.', "'He is the most famous man in Sineozersk.' The exact same words Arkady just used! Pasha loses his temper."),
    (15, 'Он самый известный клоун в Синеозерске!', "'He is the most famous clown in Sineozersk!' The adjective for 'famous' agrees in gender, number, and case with 'clown'."),
    (15, 'Я не хочу об этом слышать.', "'I don't want to hear about this.' Pasha puts 'want' up front and finishes with 'to hear' to make the point unmistakable."),
]
TRANSITION = "Now let's listen to the whole scene at campaign headquarters again."
OUTRO = "So Moscow strategist Ilona Leonidovna takes charge of Pasha's campaign just as Ivan Samsonov enters the race and dominates the television news. Listen for how 'vote for' and 'lead' take their cases. See you next time!"
CLOSING = ("ilona", "Пока!")
