# Hand-crafted German A1 scene: Die Discounter S01E01 Scene 09
ID = 'die-discounter-s01e01-scene-09'
SHOW, SEASON, EPISODE, SCENE = 'die-discounter', 1, 1, 9
TITLE = 'Beyza ist da  (Beyza Is Here)'
LEVEL, PAIR = 'A1 — beginner', 'de-en'
LABELS = {'thorsten': 'Thorsten', 'beyza': 'Beyza'}
SOURCE_NAME = 'Die Discounter S01E01 — Der Anfang vom Ende'
SOURCE_FILE = 'sources/die-discounter/s01/e01.de.srt'
SOURCE_NOTE = 'Auto-caption mishears Beyza, die Assistentin as Bes, die Assistente; blank-first-line rolling cues 287 and 293 restored and bridged cleanly.'

INTRO = (
    "Near the entrance, Thorsten spots a familiar visitor and breathes a huge sigh of relief: boss Sabine stayed away and sent her assistant Beyza instead. "
    "Thorsten immediately vows to the camera that today is the day he asks Beyza out, though Beyza is strictly here on business. "
    "Listen to the German exchange first."
)
OPENER = "Let's unpack Thorsten's relieved reaction, how he introduces Beyza, and how they head into the meeting."
TRANSITION = "Now let's hear the whole arrival scene once more."
OUTRO = (
    "Beyza skips the small talk and leads a nervous Thorsten straight toward the office to inspect the numbers. "
    "You have heard how to say 'thank goodness', introduce an assistant, say you don't have much time, and suggest heading into the office. "
    "See you next time!"
)
CLOSING = ('beyza', 'Bis später!')

STORY = [
    ('thorsten', 'Gott sei Dank ist Sabine heute nicht da!', 'Thank goodness Sabine is not here today!', [], 'Restored from raw rolling cue 287 (Gott sei Dank ist Sabine...) skipped by blank-line SRT block split.'),
    ('thorsten', 'Das ist Beyza, die Assistentin von Sabine.', 'That is Beyza, Sabine\'s assistant.', [(290, 'Das ist'), (290, 'die'), (290, 'von Sabine')], 'Correct auto-caption Bes, die Assistente to Beyza, die Assistentin.'),
    ('thorsten', 'Heute frage ich sie nach einem Abendessen.', 'Today I am going to ask her to dinner.', [(291, 'Heute frage ich sie')], 'Clarify what Thorsten plans to ask her (anticipating his dinner invitation in Scene 16).'),
    ('thorsten', 'Hallo Beyza! Schön, dass du hier bist.', "Hello Beyza! Nice that you're here.", [], 'Restored from raw rolling cue 293 (Hallo Bisa) with warm A1 welcome.'),
    ('beyza', 'Hallo Thorsten! Sabine kommt heute leider nicht.', 'Hello Thorsten! Unfortunately, Sabine is not coming today.', [], 'Natural conversational reply establishing why Beyza came in Sabine\'s place.'),
    ('thorsten', 'Kein Problem! Möchtest du zuerst einen Kaffee trinken?', 'No problem! Would you like to drink a coffee first?', [], 'Bridges Thorsten\'s attempt to charm Beyza before the inspection.'),
    ('beyza', 'Nein danke, ich habe heute leider nicht viel Zeit.', "No thank you, unfortunately I don't have much time today.", [], 'Keep Beyza\'s brisk, businesslike tone at A1 level.'),
    ('beyza', 'Und, wollen wir direkt ins Büro gehen?', 'So, shall we go straight to the office?', [(296, 'Und wollen wir')], 'Expand elliptical Und, wollen wir? with direkt ins Büro gehen for beginner clarity.')
]

WALK = [
    (0, None, "'Thank goodness Sabine is not here today!' Word for word, the opening exclamation says 'to God be thanks', the everyday German twin of 'thank goodness!' Because that whole exclamation fills the first slot, 'is' steps straight into second position right behind it."),
    (1, None, "'That is Beyza, Sabine's assistant.' Rather than adding an apostrophe-'s' to a name the way English does, everyday spoken German links people with the word for 'of' or 'from' — literally 'the assistant of Sabine', complete with the feminine job ending."),
    (2, None, "'Today I am going to ask her to dinner.' Notice how German needs no special future helper when a time word like 'today' already makes the plan clear: 'today ask I her' does the whole job, ending with the compound word for 'evening meal'."),
    (3, None, "'Hello Beyza! Nice that you're here.' This warm greeting — literally 'nice that you here are' — is one of the friendliest ways to welcome a guest or coworker. Notice how the word for 'that' sends 'are' right to the end of the clause."),
    (4, None, "'Hello Thorsten! Unfortunately, Sabine is not coming today.' Slipping the single word for 'unfortunately' into the middle of a sentence softens bad news or a change of plans without needing a whole extra clause."),
    (5, None, "'No problem! Would you like to drink a coffee first?' Pairing 'no' with 'problem' works just like in English, followed by a polite phrase for 'would you like to...?' that sends the word for 'drink' cleanly to the end."),
    (7, None, "'So, shall we go straight to the office?' Beyza uses the contraction for 'into the office' — squeezing two little words into one neat syllable — and rounds off with 'shall we?' to get straight down to work.")
]
