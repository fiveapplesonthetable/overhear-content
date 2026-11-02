# Hand-crafted German A1 scene: Die Discounter S01E01 Scene 18
ID = 'die-discounter-s01e01-scene-18'
SHOW, SEASON, EPISODE, SCENE = 'die-discounter', 1, 1, 18
TITLE = 'Du hast den Plan  (You Have a Plan)'
LEVEL, PAIR = 'A1 — beginner', 'de-en'
LABELS = {'beyza': 'Beyza', 'pina': 'Pina', 'thorsten': 'Thorsten'}
SOURCE_NAME = 'Die Discounter S01E01 — Der Anfang vom Ende'
SOURCE_FILE = 'sources/die-discounter/s01/e01.de.srt'
SOURCE_NOTE = 'Auto-caption Bestesses restored to Bestes; captures Beyza quietly praising Pina before Thorsten\'s delusional interview aside.'

INTRO = (
    "On her way out of the supermarket, Beyza pulls Pina aside in the aisle to tell her quietly that she is the only person in the branch who actually knows what she is doing. "
    "Watching from a distance, Thorsten convinces himself that Beyza was simply too shy to admit she has a crush on him. "
    "Listen to the German scene first."
)
OPENER = "Let's unpack Beyza's compliment, how to say 'give me a call', and Thorsten's wishful thinking."
TRANSITION = "Now let's hear the whole aisle farewell and interview aside again."
OUTRO = (
    "Beyza puts her trust firmly in Pina while Thorsten lives in a romantic daydream of his own invention. "
    "You have practised praising a colleague, saying 'I do my best', inviting someone to call if anything comes up, and talking about having a crush on someone. "
    "See you next time!"
)
CLOSING = ('pina', 'Bis bald!')

STORY = [
    ('beyza', 'Hallo Pina, hast du noch kurz einen Moment?', 'Hello Pina, do you have a quick moment?', [(592, 'Pina')], ''),
    ('pina', 'Ja, natürlich!', 'Yes, of course!', [(593, 'Ja')], ''),
    ('beyza', 'Ich wollte dir nur noch mal sagen: Du hast hier echt den Plan.', 'I just wanted to tell you once more: you really know what you are doing here.', [(595, 'ich wollte dir nur noch mal sagen'), (597, 'echt, du bist'), (599, 'dem Plan hier')], 'Simplify diejenige mit dem Plan into idiomatic A1 Du hast hier echt den Plan.'),
    ('pina', 'Danke! Ich gebe hier jeden Tag mein Bestes.', 'Thank you! I give it my best here every day.', [(601, 'Ich geb mein')], 'Restore gebe mein Bestes from auto-caption geb mein Bestesses.'),
    ('beyza', 'Super. Wenn noch irgendwas ist, ruf mich einfach an.', 'Great. If anything else comes up, just call me.', [(605, 'Wenn noch irgendwas ist, ruf mich an')], ''),
    ('beyza', 'Du hast ja meine Nummer, oder?', 'You do have my number, right?', [(607, 'meine Nummer')], ''),
    ('pina', 'Ja, die habe ich. Gute Fahrt, Beyza!', 'Yes, I have it. Safe travels, Beyza!', [], 'Replaces cue 610 Ciao/Tschüss so the closing farewell remains fresh.'),
    ('thorsten', 'Ich glaube, sie traut sich einfach noch nicht so richtig.', "I think she just doesn't quite dare yet.", [(611, 'Ich glaube'), (613, 'sie traut sich nicht so richtig')], ''),
    ('thorsten', 'Sie will noch nicht zeigen, dass sie auf mich steht.', "She doesn't want to show yet that she's into me.", [(615, 'zu zeigen, dass sie auf mich steht')], '')
]

WALK = [
    (2, None, "'I just wanted to tell you once more: you really know what you are doing here.' Opening with 'I wanted to tell you' sounds gentler and more thoughtful than 'I want'. In casual German, 'having the plan' is a lively idiom meaning you are on top of things."),
    (3, None, "'Thank you! I give it my best here every day.' Saying 'I give my best' works almost word for word like English, with 'every day' tucked neatly into the middle."),
    (4, None, "'Great. If anything else comes up, just call me.' Notice two everyday gems: literally 'if still anything is' covers 'if anything comes up', and 'call me' splits its prefix 'at' to the very end — 'ring me at'."),
    (5, None, "'You do have my number, right?' Slipping that tiny word in after 'you have' signals shared knowledge — 'as we both know' — and 'or?' at the end checks for confirmation."),
    (6, None, "'Yes, I have it. Safe travels, Beyza!' Wishing someone a 'good journey' or 'good drive' is a warm two-word send-off you can use whenever a visitor heads home by car, train, or bus."),
    (7, None, "'I think she just doesn't quite dare yet.' Here is the same 'dare oneself' expression Flora used with Titus at the till, softened by 'not so rightly' to mean 'not quite yet'."),
    (8, None, "'She doesn't want to show yet that she's into me.' Literally, Thorsten says 'that she stands on me' — the everyday colloquial idiom across Germany for having a crush on someone.")
]
