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
    "Welcome to episode one of The Naked Director, or Zenra Kantoku in Japanese. "
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
    (0, None, "'I believe there is a problem with current attitudes in Japan.' Kuroki refers to herself as \"watakushi\", a dressed-up cousin of everyday \"watashi\". Inside her sentence, \"mondai\" means problem, followed by \"ga aru\", there is."),
    (1, None, "'In Japan, there is a culture of shyness.' Starting with \"Nihon ni wa\" sets Japan up as the place we are talking about. At the end, \"gozaimasu\" is the extra-polite twin of \"arimasu\", meaning something exists."),
    (2, None, "'There is no need to be bound by that.' Listen for \"hitsuyou\", need, paired with \"gozaimasen\", the negative form that says none exists. Put any action before \"hitsuyou wa nai\" or \"hitsuyou wa arimasen\" to say you do not need to do it."),
    (3, None, "'Still, I do not feel embarrassed at all.' Opening with \"demo\" pivots straight into 'but'. \"Hazukashii\" means embarrassed or shy, and ending on \"omoidasen\"—here \"omoimasen yo\"—adds a confident \"yo\" to press the point home."),
    (4, None, "'Living just as you are is what makes us human.' \"Arugamama\" paints the picture of things exactly as they are, built around \"aru\", to be, and \"ikiru\" means to live. Adding \"rashisa\" onto \"ningen\", human being, turns 'human' into 'human-ness'."),
    (5, None, "'My theme is love.' Borrowed from German, \"teema\" is the everyday word for theme. After \"wa\", she names \"ai\", love, and wraps up with \"de gozaimasu\", a grander, stage-worthy way to say \"desu\"."),
    (7, None, "'Thank you very much.' You will hear \"arigatou gozaimasu\" everywhere in daily life, from shops to television sets. Dropping \"gozaimasu\" leaves casual \"arigatou\" for friends and family."),
    (8, None, "'I will show everyone the moment a miracle happens.' \"Minasan\" addresses everyone in the room respectfully, built from \"mina\", all, plus polite \"san\". \"Shunkan\" is an instant or split second, and \"omise shimasu\" humbles the speaker while promising to show something."),
    (9, None, "'Please do not close your eyes.' \"Me\" is eye or eyes—Japanese leaves out any separate word for 'your' when body parts are obvious. Attach \"nai de kudasai\" to \"tojiru\", to shut, whenever you want to say 'please do not'."),
    (10, 'いいですね？', "'Are you ready?' Literally \"ii desu ne\" asks 'is it good, right?', checking that everyone is following along. A rising tone turns that short check into 'ready?' or 'got it?'."),
    (11, None, "'Ready, action!' Directors on Japanese sets stretch out \"yooi\", meaning preparation or 'get set', right before calling borrowed English \"akushon\"."),
]

TRANSITION = "Now let's listen to the whole studio opening again from start to finish."

OUTRO = (
    "Notice how \"watakushi\" and \"gozaimasu\" instantly give Japanese speech a formal, public polish, "
    "while \"nai de kudasai\" gives you a clean, polite way to ask someone not to do something. "
    "Until next scene—see you again."
)

CLOSING = ('muranishi', 'また会いましょう。')
