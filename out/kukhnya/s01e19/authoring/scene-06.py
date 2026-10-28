# Authoring module for kukhnya-s01e19-scene-06.
ID = 'kukhnya-s01e19-scene-06'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 19
SCENE = 6
TITLE = "Вопрос гостя  (The Guest's Question)"
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'igor': 'Игорь', 'vika': 'Вика', 'max': 'Макс'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.19'
SOURCE_FILE = 'sources/kukhnya/s01/e19.ru.dual.srt'
INTRO = "Igor turns back before he leaves, with a very personal question for Vika, and Max is near enough to hear it. Here's the Russian; follow the feelings rather than every word."
OPENER = "Now Igor's question and what follows, line by line."
TRANSITION = "And now the whole exchange again, Igor's question and all."
OUTRO = 'Max asked for an open relationship and now dislikes how open it is, and you heard him admit it in Russian. See you next time!'
CLOSING = ('vika', 'Ладно, пока!')
STORY = [
    ('igor', 'Виктория Сергеевна, подождите минуту.', 'Victoria Sergeyevna, wait a minute.', [(119, 'Виктория Сергеевна, подождите')], ''),
    ('igor', 'Я никогда не прощу себе этого.', 'I will never forgive myself for this.', [(120, 'Я никогда не прощу себе')], ''),
    ('igor', 'Если не задам вам вопрос прямо сейчас.', 'If I do not ask you a question right now.', [(120, 'если не задам вам'), (120, 'прямо сейчас')], ''),
    ('igor', 'У вас есть муж или молодой человек?', 'Do you have a husband or a boyfriend?', [(121, 'У вас есть муж или молодой человек?')], ''),
    ('vika', 'Ни мужа, ни парня у меня нет.', 'I have neither a husband nor a boyfriend.', [(123, 'Ни мужа, ни парня у меня нет')], ''),
    ('igor', 'Тогда я буду ждать нашей следующей встречи.', 'Then I will look forward to our next meeting.', [(124, 'буду ждать нашей следующей встречи')], ''),
    ('max', 'Вика, я не понял, что это было?', 'Vika, I did not understand, what was that?', [(126, 'Вика, я не понял, что это было?')], ''),
    ('vika', 'А ты что, ревнуешь меня?', 'Why, are you jealous of me?', [(127, 'А ты что, ревнуешь?')], ''),
    ('max', 'Нет, почему ты про меня не сказала?', 'No, why did you not mention me?', [(128, 'почему ты про меня не сказала')], ''),
    ('vika', 'Потому что он про тебя не спрашивал.', 'Because he did not ask about you.', [(129, 'Потому что он про тебя не спрашивал')], ''),
    ('vika', 'У нас ведь с тобой свободные отношения.', 'After all, you and I have an open relationship.', [(130, 'свободное отношение')], ''),
    ('max', 'Да, но мне это совсем не нравится.', 'Yes, but I do not like this at all.', [], ''),
]
WALK = [
    (0, None, "'Victoria Sergeyevna, wait a minute.' \"Podozhdite\" is the polite 'wait', for someone you call vy; to a friend it's \"podozhdi\". \"Minuta\" becomes \"minutu\": 'wait for a minute'."),
    (1, None, "'I will never forgive myself for this.' \"Proshchu\", 'I'll forgive', already points to the future, so \"ne proshchu\" is 'I won't forgive'. Russian needs both \"nikogda\" and ne: 'never not forgive'."),
    (2, None, "'If I do not ask you a question right now.' \"Zadat' vopros\", literally 'to set a question', is how Russians say 'to ask a question'. \"Pryamo seychas\" is 'right now', with \"pryamo\" meaning 'straight'."),
    (3, None, "'Do you have a husband or a boyfriend?' \"Molodoy\" chelovek, 'young man', is the respectful way to ask about a boyfriend; it's also how you call a waiter over. \"U vas est'\" asks 'do you have'."),
    (4, None, "'I have neither a husband nor a boyfriend.' After \"ni\" ... \"ni, muzh\" becomes \"muzha\" and \"paren'\" becomes \"parnya\". \"Paren'\", 'guy', is the casual word, where Igor used the polite one."),
    (5, None, "'Then I will look forward to our next meeting.' After \"zhdat'\", a thing you hope for takes the 'of' ending, so \"vstrecha\" becomes \"vstrechi\". \"Budu zhdat'\" is 'I'll be waiting'."),
    (6, None, "'Vika, I did not understand, what was that?' Ya ne ponyal, 'I didn't get it', is what Russians say for 'what just happened?'. \"Chto eto bylo\" is literally 'what this was'."),
    (7, None, "'Why, are you jealous of me?' A \"ty chto\" is a teasing 'what, you ...?'. \"Revnuesh'\", 'you're jealous', comes from \"revnovat'\", where -ova- turns into -u-."),
    (8, None, "'No, why did you not mention me?' \"Pro menya\" is the chatty 'about me'; the textbook version is \"obo mne\". \"Skazala\", 'said', has the -a of a woman doing the saying: Max is talking about Vika."),
    (9, None, "'Because he did not ask about you.' \"Potomu chto\", 'because', always comes as this pair. \"Ne sprashival\", 'didn't ask', means the question never came up at all."),
    (10, None, "'After all, you and I have an open relationship.' \"U nas s toboy\", literally 'at us with you', means 'you and I have'. \"Ved'\", 'after all', points back to something Max already agreed to."),
    (11, None, "'Yes, but I do not like this at all.' \"Mne ne nravitsya\" is 'it doesn't please me', the Russian 'I don't like it'. \"Sovsem\", 'completely', with ne makes 'not at all'."),
]
