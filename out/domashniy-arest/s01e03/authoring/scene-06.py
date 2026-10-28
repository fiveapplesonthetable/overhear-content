# Authoring module for domashniy-arest-s01e03-scene-06.
ID = 'domashniy-arest-s01e03-scene-06'
SHOW = 'domashniy-arest'
SEASON = 1
EPISODE = 3
SCENE = 6
TITLE = "Народные деньги  (The People's Money)"
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'arkady': 'Аркадий', 'samson': 'Самсон'}
SOURCE_NAME = 'Домашний арест (Domashniy Arest) S1.03'
SOURCE_FILE = 'sources/domashniy-arest/s01/e03.ru.dual.srt'
INTRO = "Back in the communal flat, just after Marina received the hidden bug outside. Pushed along the corridor by his wife Nina, Samson walks into Arkady's tiny room to demand the hidden millions so that he and Nina can get their new three-room flat. We'll hear the whole conversation in Russian first; don't worry about catching every word."
OPENER = "Let's go back through the scene slowly. Samson steps into Arkady's room looking awkward, and Arkady greets him casually."
TRANSITION = "Now let's hear the whole scene once more, from start to finish."
OUTRO = "So Arkady calls Samson's bluff, tells him he lost the money on the stock exchange, and dares him to do his worst. Next we head to the park with Pasha and the judge; see you then. See you next time!"
CLOSING = ('samson', 'Пока!')
STORY = [
    ('arkady', 'Привет, Самсон. Что хотел?', 'Hi, Samson. What did you want?', [(219, 'Привет'), (220, 'Что хотел')], "'Здорово' dropped; garbled 'Санцовчик' -> 'Самсон'"),
    ('samson', 'Такое дело. Нам квартиру дадут.', "Here's the thing. They're going to give us a flat.", [(221, 'Такое дело. Нам квартиру дадут')], ''),
    ('arkady', 'Здорово, поздравляю.', 'Great, congratulations.', [(222, 'Здорово, поздравляю')], ''),
    ('samson', 'Только нужно, чтобы ты деньги отдал, Аркаша.', 'We just need you to hand over the money, Arkasha.', [(224, 'Только нужно, чтобы ты'), (225, 'деньги отдал')], "garbled 'замуж ему' in cue 225 dropped; 'Аркаш' -> 'Аркаша'"),
    ('arkady', 'Какие деньги?', 'What money?', [(226, 'Какие деньги')], ''),
    ('samson', 'Твои. Народные.', "Yours. The people's money.", [(227, 'Твои. Народные')], ''),
    ('arkady', 'А, так за народными к народу.', "Ah, well for the people's money, go to the people.", [(229, 'А, так за народными к народу')], ''),
    ('samson', 'Шутишь? Правда, скажи, где деньги? Меня наняли.', "Are you joking? Seriously, tell me, where's the money? They hired me.", [(230, 'Шутишь'), (231, 'правда'), (231, 'скажи, где деньги'), (232, 'меня наняли')], "cue 232 shortened to 'Меня наняли'"),
    ('arkady', 'Осипенко, что ли, тебя нанял?', 'Was it Osipenko who hired you?', [(233, 'что ли, нанял'), (234, 'Тебя')], "cue 233 garbles Pasha's surname 'Осипенко' as 'А Сипенко'"),
    ('arkady', 'А если я не скажу, то что? Ты мне ухо отрежешь?', "And if I don't tell you, then what? Will you cut my ear off?", [(235, 'а если я не скажу, то что'), (236, 'Ты мне ухо отрежешь')], "'Ну' dropped"),
    ('samson', 'Ну, допустим.', 'Well, maybe.', [(237, 'Ну, допустим')], ''),
    ('arkady', 'Самсон, ты же добрый, хороший человек.', "Samson, you're a kind, good person.", [(238, 'Самсон'), (239, 'Ты же добрый, хороший человек')], "'ты посмотри на себя' dropped"),
    ('samson', 'Чего? Я тебе палец сломал. Забыл, что ли?', 'What? I broke your finger. Did you forget?', [(240, 'Чего'), (241, 'Я тебе палец сломал'), (242, 'Забыл, что ли')], ''),
    ('arkady', 'Я тебя обманул, и ты был прав. Теперь всё изменилось, Самсон.', 'I tricked you, and you were right. Now everything has changed, Samson.', [(244, 'Я тебя обманул, и ты был прав'), (245, 'теперь все изменилось, Самсон')], "'Ну' dropped"),
    ('arkady', 'Я тебя полюбил. Ты мой друг.', "I've grown fond of you. You're my friend.", [(246, 'Я тебя полюбил'), (247, 'Ты мой друг')], ''),
    ('arkady', 'Денег нет, Самсон. Я их на бирже проиграл.', 'There is no money, Samson. I lost it on the stock exchange.', [(252, 'Денег нет, Самсон'), (253, 'Я их на бирже проиграл')], ''),
    ('samson', 'Ты что, очкарик, не понимаешь? Мне тебя мучить придётся.', "Don't you get it, four-eyes? I'm going to have to torture you.", [(254, 'Ты что'), (254, 'не понимаешь'), (256, 'мне тебя мучить придется')], "garbled 'очканавт' (255) -> 'очкарик'; 'Блин' (256) and swearing (257) dropped"),
    ('arkady', 'Мучить? Детские слова какие. Ну давай, мучай, Самсон!', 'Torture? What childish words. Go on then, torture me, Samson!', [(259, 'Мучить. Детские'), (260, 'Ну давай, мучай, Самсон')], "cues 258-259 ('Где ты слов таких понабрался? Мучить. Детские такие.') simplified"),
]
WALK = [
    (0, None, "'Hi, Samson. What did you want?' In Russian, asking 'what did you want?' in the past tense is a natural, casual way to ask 'what can I do for you?'. Samson comes straight out with his news."),
    (1, 'Такое дело.', "'Here's the thing.' Literally, 'such a matter', a classic way to open an awkward request."),
    (1, 'Нам квартиру дадут.', "'They're going to give us a flat.' The verb is third person plural with no subject: 'they will give to us a flat'. Arkady pretends to be delighted for him."),
    (2, None, "'Great, congratulations.' Literally, 'great, I congratulate'. Then Samson explains the catch."),
    (3, None, "'We just need you to hand over the money, Arkasha.' After 'in order that', Russian always uses the past-tense form of the verb, so literally 'that you handed over the money'. Arkady plays innocent."),
    (4, None, "'What money?' Because the word for 'money' is always plural in Russian, the question word 'what kind of' is plural too."),
    (5, None, "'Yours. The people's money.' Both words are plural to match 'money'. Samson means the public money Arkady stole from the town. Arkady turns the phrase into a joke."),
    (6, None, "'Ah, well for the people's money, go to the people.' No verb at all: just 'for the people's, to the people'. Samson drops all pretence."),
    (7, 'Правда, скажи, где деньги?', "'Seriously, tell me, where's the money?' After asking if Arkady is joking, he uses the informal command 'tell'."),
    (7, 'Меня наняли.', "'They hired me.' Samson blurts out that someone put him up to this, and Arkady guesses who."),
    (8, None, "'Was it Osipenko who hired you?' Meanwhile, Osipenko is the surname of Pasha, Arkady's treacherous deputy. The two little words in the middle mean 'or what, is it really?'. Then Arkady calls Samson's bluff."),
    (9, 'А если я не скажу, то что?', "'And if I don't tell you, then what?' Again, the single-action form 'I will tell' points to the future."),
    (9, 'Ты мне ухо отрежешь?', "'Will you cut my ear off?' In Russian, body parts take 'to me' instead of 'my': 'will you cut off an ear to me?'. Samson tries to sound menacing."),
    (10, None, "'Well, maybe.' Literally, 'well, let's suppose'. Arkady just smiles and flatters him."),
    (11, None, "'Samson, you're a kind, good person.' The little particle after 'you' means 'after all, as we both know'. Samson is baffled and holds up Arkady's bandaged hand."),
    (12, None, "'What? I broke your finger. Did you forget?' Back in the first episode, Samson slammed the door on Arkady's finger. Arkady waves that away."),
    (13, 'Я тебя обманул, и ты был прав.', "'I tricked you, and you were right.' All masculine forms, because both men are speaking about themselves."),
    (13, 'Теперь всё изменилось, Самсон.', "'Now everything has changed, Samson.' And he lays it on even thicker."),
    (14, None, "'I've grown fond of you. You're my friend.' The prefix on the verb 'loved' turns it into 'came to love, grew fond of'. Then comes Arkady's new lie about the money."),
    (15, 'Денег нет, Самсон.', "'There is no money, Samson.' With 'there is no', the plural word 'money' drops its ending altogether."),
    (15, 'Я их на бирже проиграл.', "'I lost it on the stock exchange.' Because 'money' is plural, he says 'I lost them'. Samson loses his temper."),
    (16, 'Ты что, очкарик, не понимаешь?', "'Don't you get it, four-eyes?' He falls back on his old schoolyard nickname for Arkady."),
    (16, 'Мне тебя мучить придётся.', "'I'm going to have to torture you.' Literally, 'to me it will fall to torture you'. Arkady bursts out laughing."),
    (17, None, "'Torture? What childish words. Go on then, torture me, Samson!' First the basic verb form 'to torture', and then the command 'torture!'. Samson has no idea what to do next and walks out."),
]
