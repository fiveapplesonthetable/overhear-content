ID = 'the-naked-director-s01e01-scene-01'
SHOW = 'the-naked-director'
SEASON = 1
EPISODE = 1
SCENE = 1
TITLE = 'よーい、アクション  (Lights, Camera, Action)'
LEVEL = 'A1 — beginner'
PAIR = 'ja-en'
LABELS = {'kuroki': '黒木', 'muranishi': '村西'}
SOURCE_NAME = '全裸監督 (The Naked Director) S01E01'
SOURCE_FILE = 'sources/the-naked-director/s01/e01.ja.srt'

INTRO = (
    "Welcome to episode one of The Naked Director. "
    "We open in a bright Tokyo studio before jumping back to where Toru Muranishi started. "
    "Kaoru Kuroki speaks politely about living naturally and about love, while Muranishi gets his camera ready to roll. "
    "Just listen to the rhythm first without worrying about every detail."
)

STORY = [
    ('kuroki', 'わたくしは日本の風潮に問題があると思っております。', 'I believe there is a problem with current attitudes in Japan.', [(1, 'わたくしは日本の風潮に 問題があると思っております')], ''),
    ('kuroki', '日本には恥じらいの文化がございます。', 'In Japan, there is a culture of shyness.', [(2, '日本には恥じらいの文化')], 'Trimmed trailing clause for A1 length.'),
    ('kuroki', 'それに縛られる必要はございません。', 'There is no need to be bound by that.', [(3, 'それに縛られる必要は ございません')], 'Trimmed final explanatory particle.'),
    ('muranishi', 'でも恥ずかしいなんて思いませんよ。', 'Still, I do not feel embarrassed at all.', [(14, 'でも恥ずかしいなんて思いませんよ')], ''),
    ('muranishi', 'あるがままに生きることが人間らしさです。', 'Living just as you are is what makes us human.', [(15, 'あるがままに生きることが 人間らしさ')], 'Simplified rhetorical ending to plain polite statement.'),
    ('kuroki', 'わたくしのテーマは愛でございます。', 'My theme is love.', [(19, 'わたくしのテーマは愛でございます')], ''),
    ('kuroki', 'そして愛とは自然の受容でございます。', 'And love means accepting nature.', [(20, 'そして愛とは 自然の受容でございます')], ''),
    ('kuroki', 'ありがとうございます。', 'Thank you very much.', [(27, 'ありがとうございます')], ''),
    ('muranishi', '皆さんにミラクルが起きる瞬間をお見せします。', 'I will show everyone the moment a miracle happens.', [(29, '皆さんにミラクルが起きる瞬間を')], 'Shortened ending to polite future.'),
    ('muranishi', '目を閉じないでください。', 'Please do not close your eyes.', [(30, '目を閉じないでください')], ''),
    ('muranishi', 'いいですね？それでは参ります。', 'Are you ready? Here we go.', [(31, 'いいですね それでは参ります')], ''),
    ('muranishi', 'よーい、アクション！', 'Ready, action!', [(32, 'アクション')], ''),
]

OPENER = "Kuroki speaks with extra-polished studio manners, while Muranishi addresses the room like a showman. Let's hear their key lines up close."

WALK = [
    (0, None, [
        '"\'I believe there is a problem with current attitudes in Japan.\' Kuroki refers to herself as " We can hear ',
        ("kuroki", "わたくし"), ", a dressed-up cousin of the everyday word for 'I'. Inside her sentence, ",
        ("kuroki", "問題"), " this word means problem, followed by ",
        ("kuroki", "がある"), ", there is."
    ]),
    (1, None, [
        '"\'In Japan, there is a culture of shyness.\' Starting with " Hear how ',
        ("kuroki", "日本には"), " sets Japan up as the place we are talking about. At the end, ",
        ("kuroki", "ございます"), " is an extra-polite way to say something exists."
    ]),
    (2, None, [
        '"\'There is no need to be bound by that.\' Listen for " In this line, ',
        ("kuroki", "必要"), ", and this word this word means need, paired with ",
        ("kuroki", "ございません"), ", the negative form that says none exists. You can use this pattern to say you do not need to do something."
    ]),
    (3, None, [
        '"\'Still, I do not feel embarrassed at all.\' Opening with " The word ',
        ("muranishi", "でも"), " pivots straight into 'but'. ",
        ("muranishi", "恥ずかしい"), " this word means embarrassed or shy, and ending on ",
        ("muranishi", "思いませんよ"), " adds a confident closing particle to press the point home."
    ]),
    (4, None, [
        "'Living just as you are is what makes us human.'  The speaker uses ",
        ("muranishi", "あるがまま"), " paints the picture of things exactly as they are, built around ",
        ("muranishi", "ある"), ", and this word this word means to be, and ",
        ("muranishi", "生きる"), " this word means to live. Adding ",
        ("muranishi", "人間らしさ"), " onto ",
        ("muranishi", "人間"), ", and this word this word means human being, and this word turns 'human' into 'human-ness'."
    ]),
    (5, None, [
        '"\'My theme is love.\' Borrowed from German, " You can catch ',
        ("kuroki", "テーマ"), " this word is the everyday word for theme. After ",
        ("kuroki", "は"), ", she names ",
        ("kuroki", "愛"), ", and this word this word means love, and wraps up with ",
        ("kuroki", "でございます"), ", a grander, stage-worthy way to say 'is'."
    ]),
    (7, None, [
        '"\'Thank you very much.\' You will hear " Here, the word ',
        ("kuroki", "ありがとうございます"), " everywhere in daily life, from shops to television sets. Dropping ",
        ("kuroki", "ございます"), " leaves casual ",
        ("kuroki", "ありがとう"), " for friends and family."
    ]),
    (8, None, [
        "'I will show everyone the moment a miracle happens.'  The character says ",
        ("muranishi", "皆さん"), " addresses everyone in the room respectfully, and this word is built from ",
        ("muranishi", "皆さん"), ", and this word this word means all, plus the polite suffix ",
        ("muranishi", "さん"), ". ",
        ("muranishi", "瞬間"), " is an instant or split second, and ",
        ("muranishi", "お見せします"), " humbles the speaker while promising to show something."
    ]),
    (9, None, [
        "'Please do not close your eyes.'  The phrase contains ",
        ("muranishi", "目"), " is eye or eyes—the language leaves out any separate word for 'your' when body parts are obvious. Attach ",
        ("muranishi", "ないでください"), " to the verb stem ",
        ("muranishi", "閉じ"), ", and this word this word means to shut, whenever you want to say 'please do not'."
    ]),
    (10, 'いいですね？', [
        '"\'Are you ready?\' Literally, " The phrase contains ',
        ("muranishi", "いいですね"), " asks 'is it good, right?', checking that everyone is following along. A rising tone turns that short check into 'ready?' or 'got it?'."
    ]),
    (11, None, [
        '"\'Ready, action!\' Directors on Japanese sets stretch out " Here, the word ',
        ("muranishi", "よーい"), ", and this word this word means preparation or 'get set', right before calling borrowed English ",
        ("muranishi", "アクション")
    ]),
]

TRANSITION = "Now let's listen to the whole studio opening again from start to finish."

OUTRO = (
    "Notice how the formal words for 'I' and 'to be' instantly give Japanese speech a formal, public polish, "
    "while the negative request pattern gives you a clean, polite way to ask someone not to do something. "
    "Until next scene—see you again."
)

CLOSING = ('muranishi', 'また会いましょう。')
