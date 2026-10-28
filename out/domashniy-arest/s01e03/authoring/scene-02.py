# Authoring module for domashniy-arest-s01e03-scene-02.
ID = 'domashniy-arest-s01e03-scene-02'
SHOW = 'domashniy-arest'
SEASON = 1
EPISODE = 3
SCENE = 2
TITLE = 'Плохой кофе и Лёля  (Bad Coffee and Lyolya)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'arkady': 'Аркадий', 'slavik': 'Славик', 'yulia': 'Юля'}
SOURCE_NAME = 'Домашний арест (Domashniy Arest) S1.03'
SOURCE_FILE = 'sources/domashniy-arest/s01/e03.ru.dual.srt'
INTRO = "Back in the communal flat, a little later that morning. Now Arkady walks into the shared kitchen, where Samson's children, Yulia and ten-year-old Slavik, are having breakfast, and shows Slavik a photo on his phone of his glamorous girlfriend Lyolya. We'll hear the conversation in Russian first; don't worry about catching every word."
OPENER = "Let's walk through it slowly. Arkady comes into the kitchen in his dressing gown and spots Slavik and Lyosha at the table."
TRANSITION = "Now let's hear the whole kitchen conversation once more from the start."
OUTRO = "So Slavik has seen the photo of glamorous Lyolya and heard Arkady's shark story, which will soon get the boy into big trouble at school. Next we cross the street to see who is listening in on the flat; see you then. See you next time!"
CLOSING = ('arkady', 'Пока!')
STORY = [
    ('arkady', 'Привет, молодёжь! Почему вы не в школе?', "Hi, kids! Why aren't you at school?", [(83, 'молодежь')], "'прогуливаем?' (skipping class?) simplified to 'Почему вы не в школе?'"),
    ('slavik', 'А у нас сегодня вторая смена.', "We're on the afternoon shift today.", [(85, 'у нас вторая смена')], "'Ну, вообще-то' -> 'А'; 'сегодня' added"),
    ('arkady', 'Очень плохой кофе. Девочка, дай сахар, пожалуйста.', 'Very bad coffee. Girl, pass me the sugar, please.', [(86, 'Очень плохой кофе'), (87, 'Девочка, дай сахар, пожалуйста')], ''),
    ('yulia', 'Меня вообще-то Юля зовут. Вот сахар.', "My name is actually Yulia. Here's the sugar.", [(88, 'Меня вообще-то Юля зовут')], "'Вот сахар' added"),
    ('arkady', 'Спасибо, девочка.', 'Thank you, girl.', [(89, 'Спасибо, девочка')], ''),
    ('slavik', 'Кто это у вас в телефоне? Это же мой телефон был!', 'Who is that on your phone? Hey, that used to be my phone!', [(90, 'Кто это'), (91, 'телефона'), (92, 'это вообще мой телефон был')], "slang 'фотки попер' and 'отжали' (91, 93) left out"),
    ('arkady', 'Ладно, не плачь. Это Лёля. Нравится?', "All right, don't cry. That's Lyolya. Do you like her?", [(94, 'Ладно, не'), (96, 'Нравится')], "'не ной' -> 'не плачь'; cue 95 garbles 'Лёля' as 'Юля'"),
    ('slavik', 'Красивая. Но это же не ваша жена! Я вашу жену видел.', "She's pretty. But that's not your wife! I've seen your wife.", [(98, 'это же не ваша жена'), (99, 'Я вашу жену видел')], "'Ну, ничего такая' -> 'Красивая'"),
    ('arkady', 'У мужчины, мальчик, бывает не только жена. Это моя девушка.', "A man, my boy, can have more than just a wife. She's my girlfriend.", [(100, 'У мужчины, мальчик, бывает не только')], "cue 100 'жены' normalised to singular 'жена'; 'любовница' (101) -> 'Это моя девушка'"),
    ('slavik', 'А как вы с ней познакомились?', 'And how did you meet her?', [(102, 'А как вы с ней познакомились')], ''),
    ('arkady', 'Это она со мной познакомилась! Ходила вокруг меня, как акула.', 'She was the one who met me! She circled around me like a shark.', [(103, 'Это она со мной познакомилась'), (104, 'вокруг меня'), (104, 'как акула')], "'Нарезала ... круги' -> 'Ходила'"),
    ('arkady', 'Очень плохая сосиска.', 'Very bad sausage.', [(105, 'Очень плохая сосиска')], ''),
    ('slavik', 'Вот мне бы так!', 'I wish I had a girl like that!', [(106, 'Вот мне бы так')], ''),
    ('arkady', 'Малыш, какие твои годы? Будет и у тебя такая.', "Kid, you've got plenty of time! You'll have one like her too.", [(107, 'малыш, какие твои годы'), (108, 'Будет и у тебя такая')], ''),
    ('arkady', 'Ладно, сиди, ешь и молчи.', 'All right, sit there, eat and be quiet.', [(114, 'ешь'), (115, 'Молчи')], 'clean ending from cues 114-115'),
]
WALK = [
    (0, None, "'Hi, kids! Why aren't you at school?' The word he uses for 'kids' literally means 'youth', 'young people'. Slavik has a simple answer."),
    (1, None, "'We're on the afternoon shift today.' Literally 'at us today is the second shift': in many Russian schools, some classes go in the morning and others in the afternoon. Arkady takes a sip from his mug and makes a face."),
    (2, 'Очень плохой кофе.', "'Very bad coffee.' Notice that the describing word has the masculine ending: in Russian, coffee is masculine."),
    (2, 'Девочка, дай сахар, пожалуйста.', "'Girl, pass me the sugar, please.' Literally 'give sugar, please'. He doesn't even bother to use Yulia's name, and Yulia doesn't like that at all."),
    (3, None, "'My name is actually Yulia. Here's the sugar.' Literally 'they call me Yulia'. And Arkady ignores the correction completely."),
    (4, None, "'Thank you, girl.' Then he looks at his phone, and Slavik peeks over his arm."),
    (5, None, "'Who is that on your phone? Hey, that used to be my phone!' Literally 'in the phone'. In the previous episode, Arkady gave Slavik that phone as a present and then took it back when he needed one himself. Arkady waves that away and shows off the photo."),
    (6, None, "'All right, don't cry. That's Lyolya. Do you like her?' The last word is one action word: 'does she please you?'. Slavik looks closely."),
    (7, 'Красивая. Но это же не ваша жена!', "'She's pretty. But that's not your wife!' The little little word after 'this' adds 'after all, wait a minute'."),
    (7, 'Я вашу жену видел.', "'I've seen your wife.' Because 'wife' is the object here, both 'your' and 'wife' take the feminine object ending. Arkady answers with a smug little lecture."),
    (8, None, "'A man, my boy, can have more than just a wife. She's my girlfriend.' The word for 'girlfriend' literally means 'young woman'. Slavik is curious."),
    (9, None, "'And how did you meet her?' In Russian you don't just 'meet' someone, you 'get acquainted with her', using the little word 'with' and the 'with/as' form. Arkady brags shamelessly."),
    (10, 'Это она со мной познакомилась!', "'She was the one who met me!' Putting 'it is she' at the start puts all the emphasis on her."),
    (10, 'Ходила вокруг меня, как акула.', "'She circled around me like a shark.' Literally 'walked around me like a shark'. Keep that shark line in mind, because Slavik is going to repeat it at school later. Then Arkady takes a bite of his breakfast."),
    (11, None, "'Very bad sausage.' First the coffee was masculine, now the sausage is feminine, so the describing word changes its ending to match. Slavik is still staring at the photo of Lyolya."),
    (12, None, "'I wish I had a girl like that!' Literally 'here to me would be so': a short, wistful phrase for 'I wish I had it like that'. Arkady pats him on the shoulder."),
    (13, None, "'Kid, you've got plenty of time! You'll have one like her too.' The first sentence is a fixed idiom, literally 'what are your years?', meaning 'you're still young'. And then he finishes his breakfast."),
    (14, None, "'All right, sit there, eat and be quiet.' Three blunt commands in a row: sit, eat, and keep quiet."),
]
