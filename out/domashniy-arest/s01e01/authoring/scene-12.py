# domashniy-arest/s01e01/scene-12.py
ID = "domashniy-arest-s01e01-scene-12"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 1
SCENE = 12
TITLE = "Звонок в машине  (A Call in the Car)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.01"
SOURCE_FILE = "sources/domashniy-arest/s01/e01.ru.dual.srt"
VOICES = {"narrator": "sky", "anya": "alisa", "arakelyan": "anja"}
LABELS = {"anya": "Аркадий", "arakelyan": "Аракелян"}
INTRO = "Now Arkady is in his official car, and his driver, Vitalik, is taking him through town. Last time, Samson went through with the humiliating deal, and Arkady simply broke his promise and sent him off to the job centre. Now the phone rings: it's Arakelyan, a businessman who owes the mayor a large payment for the new shopping centre. Let's listen in Russian first."
STORY = [
    ("anya", "Виталик, почему мы так медленно едем? Быстрее!", "Vitalik, why are we going so slowly? Faster!", [(492, 'Виталик')], "slang 'ну чего тащимся? Притопи!' -> plain 'почему мы так медленно едем? Быстрее!'"),
    ("anya", "Да, слушаю.", "Yes, I'm listening.", [(493, 'Да')], "'слушаю' added (how Russians answer the phone)"),
    ("arakelyan", "Аркадий Борисович, здравствуйте.", "Arkady Borisovich, hello.", [(494, 'Аркадий Борисович, здравствуйте')], ""),
    ("arakelyan", "Это Аракелян. Я по поводу торгового центра.", "It's Arakelyan. I'm calling about the shopping centre.", [(496, 'Я по поводу торгового центра')], "'Это Аракелян' new: the subtitle garbles his self-introduction in cue 495"),
    ("arakelyan", "У меня всё готово.", "Everything is ready on my side.", [(496, 'У меня все готово')], ""),
    ("anya", "Это хорошо, что готово. А то мы уже начали беспокоиться.", "It's good that it's ready. We were starting to worry.", [(497, 'Это хорошо, что готово'), (497, 'беспокоиться')], "'уж беспокоиться начали' -> 'уже начали беспокоиться'"),
    ("anya", "Позвони мне вечером. Договоримся на завтра.", "Call me this evening. We'll arrange something for tomorrow.", [(498, 'Договоримся')], "slang 'Вечерком меня набери' -> 'Позвони мне вечером'; 'На счет завтра' -> 'на завтра'"),
    ("arakelyan", "Извините, вечером не могу. Я улетаю в Ереван.", "Sorry, I can't this evening. I'm flying to Yerevan.", [(499, 'вечером не могу'), (499, 'улетаю')], "'Я извиняюсь' -> 'Извините'; 'Ереван улетаю' -> 'Я улетаю в Ереван'"),
    ("arakelyan", "Мама болеет.", "My mother is ill.", [(500, 'Мама болеет')], ""),
    ("arakelyan", "Может, встретимся сейчас?", "Maybe we could meet now?", [(500, 'сейчас')], "slang 'Не могли бы сейчас пересекнуться?' -> 'Может, встретимся сейчас?'"),
    ("anya", "Ну как же ты не вовремя! Где ты сейчас?", "Your timing couldn't be worse! Where are you now?", [(501, 'Ну как же ты не вовремя'), (501, 'Где ты сейчас')], "'со своей мамой' dropped"),
    ("arakelyan", "Я в Санта-Фе.", "I'm at the Santa Fe.", [(502, 'Санта-Фе')], "'Я' added"),
    ("anya", "Ладно, будь там. Через десять минут буду.", "All right, stay there. I'll be there in ten minutes.", [(503, 'Ладно, будь там. Через десять минут буду')], ""),
    ("arakelyan", "Хорошо. Жду вас.", "Fine. I'll be waiting for you.", [], "new: closes the call"),
    ("anya", "Виталик, в Санта-Фе едем.", "Vitalik, we're going to the Santa Fe.", [(504, 'Виталик, в Санта-Фе едем')], ""),
]
OPENER = "Let's take it a line at a time. Arkady is in a hurry, as usual, and the first person to hear about it is his driver."
WALK = [
    (0, 'Виталик, почему мы так медленно едем?', "'Vitalik, why are we going so slowly?' The verb means 'we are going' by car or any vehicle. On foot it would be a different verb. Then one impatient word."),
    (0, 'Быстрее!', "'Faster!' It's the word for 'fast' with an ending that means 'more'. Just then, his phone rings."),
    (1, None, "'Yes, I'm listening.' This is a very common way to answer the phone, and it sounds a little official, just right for a mayor. The caller is polite."),
    (2, None, "'Arkady Borisovich, hello.' The long form of 'hello', the one you use with people you don't call by a nickname. Then he says who he is and why he's calling."),
    (3, 'Это Аракелян.', "'It's Arakelyan.' On the phone, you introduce yourself with 'this is', and your name."),
    (3, 'Я по поводу торгового центра.', "'I'm calling about the shopping centre.' The phrase in the middle means 'about' or 'concerning', and the shopping centre takes the ending for 'of'. Now the important news."),
    (4, None, "'Everything is ready on my side.' Literally, 'at me, everything is ready'. He means the money is ready. The mayor gave him three days to pay, in an earlier scene. Arkady is pleased."),
    (5, None, "'It's good that it's ready. We were starting to worry.' Notice Arkady says 'we', as if he were speaking for the whole town hall. Then he proposes a time."),
    (6, None, "'Call me this evening. We'll arrange something for tomorrow.' The first word is a command, 'call', and the last word means 'for tomorrow'. But that doesn't suit Arakelyan."),
    (7, None, "'Sorry, I can't this evening. I'm flying to Yerevan.' The verb for flying has a beginning that means 'away': flying away from here. He gives a reason."),
    (8, None, "'My mother is ill.' Literally, 'Mum is ill.' Russians often say just 'Mum' where English says 'my mother'. And he suggests something else."),
    (9, None, "'Maybe we could meet now?' The first word means 'maybe', and the verb means 'we will meet'. A very natural way to suggest something. Arkady grumbles, but agrees."),
    (10, 'Ну как же ты не вовремя!', "'Your timing couldn't be worse!' Literally, 'how untimely you are!'. Notice that Arkady says the casual 'you' to Arakelyan, while Arakelyan uses the polite one. That tells you who is the boss here."),
    (10, 'Где ты сейчас?', "'Where are you now?' Russian omits the present-tense verb 'to be', connecting 'where' directly with 'now'."),
    (11, None, "'I'm at the Santa Fe.' It's the name of a café in town. Arkady makes up his mind."),
    (12, 'Ладно, будь там.', "'All right, stay there.' Literally 'be there'. It's the command form of the verb 'to be'."),
    (12, 'Через десять минут буду.', "'I'll be there in ten minutes.' The first word means 'in' when you count time forward. The last word is 'I will be'. In the present, Russian has no 'am', but in the future you do need this verb."),
    (13, None, "'Fine. I'll be waiting for you.' Literally 'I'm waiting for you', and again, the polite form. And now new orders for the driver."),
    (14, None, "'Vitalik, we're going to the Santa Fe.' The present tense, 'we are going', is used for a plan that starts right now. The same verb we heard at the very beginning."),
]
TRANSITION = "Let's listen to the whole phone call once more."
OUTRO = "And that's the end of the call. Keep an ear out for the phrase about being there in ten minutes; you'll use it more often than you think. Until next time!"
CLOSING = ("anya", "Пока!")
