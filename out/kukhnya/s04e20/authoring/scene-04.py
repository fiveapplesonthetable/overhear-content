ID = 'kukhnya-s04e20-scene-04'
SHOW = 'kukhnya'
SEASON = 4
EPISODE = 20
SCENE = 4
TITLE = "Медвежья услуга Айнуры  (Ainura's Disservice)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = 'ru-en'
VOICES = {"narrator": "sky", "ainura": "angelina", "denis": "anja"}
LABELS = {"ainura": "Айнура", "denis": "Денис"}
SOURCE_NAME = 'Кухня (Kukhnya) S4.20'
SOURCE_FILE = 'sources/kukhnya/s04/e20.ru.srt'

INTRO = "Hoping to clear up the misunderstanding right away, Denis follows Katya into the kitchen and asks Kostya to confirm that the story was just a dream. Unfortunately, Ainura overhears and tries to back up her earlier gossip by swearing she saw Denis and Vika on the office windowsill. Let's listen to the chaos in Russian."

STORY = [
    ('denis', 'Катя, дай я тебе всё объясню.', 'Katya, let me explain everything to you.', [(56, 'Катя, дай я тебе все объясню')], 'adapted'),
    ('ainura', 'Денис, просто отстань сейчас от меня!', 'Denis, just leave me alone right now!', [(56, 'Отвали от меня')], 'adapted'),
    ('denis', 'Катя, мне же всё это приснилось!', 'Katya, I only dreamed all of that!', [(57, 'Катя, мне'), (57, 'это приснилось')], 'adapted'),
    ('denis', 'Я просто рассказывал Косте свой сон.', 'I was just telling Kostya my dream.', [(58, 'Я Косте рассказывал сон')], 'adapted'),
    ('denis', 'Пойдём к нему, он тебе подтвердит.', "Let's go to him, he will confirm it for you.", [(59, 'Пойдем к нему, он тебе подтвердит')], ''),
    ('ainura', 'Да, Костя, это был просто сон?', 'Yes, Kostya, was that really just a dream?', [(61, 'сон')], 'adapted'),
    ('ainura', 'Я никогда в жизни не обманываю!', 'I never lie in my life!', [(63, 'если я обманываю')], 'adapted'),
    ('ainura', 'Я всё видела своими собственными глазами.', 'I saw everything with my own eyes.', [(64, 'Я своими глазами видела')], 'adapted'),
    ('ainura', 'Они были там вдвоём у окна.', 'The two of them were there by the window.', [(64, 'как они на подоконнике')], 'adapted'),
    ('ainura', 'Из-за этого Денис выпал из окна!', 'Because of that Denis fell out of the window!', [(65, 'из-за этого же Денис выпал из окна')], 'adapted'),
    ('denis', 'Катя, подожди, этого правда не было!', 'Katya, wait, that really did not happen!', [(66, 'не было этого. Катя, подожди')], 'adapted'),
    ('ainura', 'Не трогай меня, уйди с дороги!', 'Do not touch me, get out of my way!', [(67, 'Не трогай меня')], 'adapted'),
]

OPENER = "Now let's break down the way Ainura accidentally makes Denis's situation worse line by line."

WALK = [
    (0, None, "'Katya, let me explain everything to you.' Denis pairs 'give' with 'will explain' directly, since spoken Russian skips English filler words like 'the', 'a', and 'is'."),
    (1, None, "'Denis, just leave me alone right now!' Notice how Russian puts 'simply, just' and 'right now' together in a short, direct phrase where word endings show how the ideas connect."),
    (2, None, "'Katya, I only dreamed all of that!' He insists that the entire episode in Vika's office happened only in his sleep."),
    (3, None, "'I was just telling Kostya my dream.' In everyday Russian, 'simply, just' flows straight into 'dream' without extra linking words."),
    (4, None, "'Let's go to him, he will confirm it for you.' Denis pairs 'let's go' with 'to confirm, corroborate' directly, since spoken Russian skips English filler words like 'the', 'a', and 'is'."),
    (5, None, "'Yes, Kostya, was that really just a dream?' Overhearing them, Ainura steps in with heavy sarcasm because nobody believed her gossip earlier."),
    (6, None, "'I never lie in my life!' Ainura swears that she is telling the absolute truth using a negated present verb."),
    (7, None, "'I saw everything with my own eyes.' In everyday Russian, 'saw' flows straight into 'eyes' without extra linking words."),
    (8, None, "'The two of them were there by the window.' Having seen Denis tumble out of Vika's window yesterday, Ainura jumped to the wildest conclusion."),
    (9, None, "'Because of that Denis fell out of the window!' Notice how Russian puts 'fell out' and 'window' together in a short, direct phrase where word endings show how the ideas connect."),
    (10, None, "'Katya, wait, that really did not happen!' Here Denis anchors the thought on 'wait' and finishes on 'really', keeping the spoken rhythm brisk and natural."),
    (11, None, "'Do not touch me, get out of my way!' Putting the short word for 'not' right in front of the action word is all Russian needs to make a sentence negative, with no extra helper words like 'do' or 'did'."),
]

TRANSITION = "Let's hear the kitchen argument again from beginning to end."
OUTRO = "Convinced by Ainura's eyewitness claim, Katya refuses to let Denis touch her and walks out of the kitchen. Listen for the verbs meaning confirm, deceive, and saw. See you next time!"
CLOSING = ("denis", "До встречи!")
