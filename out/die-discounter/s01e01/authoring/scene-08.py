# Hand-crafted German A1 scene: Die Discounter S01E01 Scene 08
ID = 'die-discounter-s01e01-scene-08'
SHOW, SEASON, EPISODE, SCENE = 'die-discounter', 1, 1, 8
TITLE = 'Ein Foto mit dem Star  (A Photo with the Star)'
LEVEL, PAIR = 'A1 — beginner', 'de-en'
LABELS = {'jonas': 'Jonas', 'fahri': 'Fahri'}
SOURCE_NAME = 'Die Discounter S01E01 — Der Anfang vom Ende'
SOURCE_FILE = 'sources/die-discounter/s01/e01.de.srt'
SOURCE_NOTE = 'Security guard Jonas mistakes actor Fahri Yardim for Elyas M\'Barek; auto-caption Elias mein Warik clarified to Elyas.'

INTRO = (
    "At the supermarket entrance, earnest security guard Jonas explains how seriously he watches everyone walking in and out. "
    "When actor Fahri arrives needing a plastic token for a shopping trolley, starstruck Jonas begs for a photo — while mistaking him for another German actor entirely. "
    "Listen to the German scene first."
)
OPENER = "Let's walk through Jonas's job description, trolley-token small talk, and polite request for a photo."
TRANSITION = "Now let's listen to the whole entrance scene again."
OUTRO = (
    "Jonas proudly poses for a selfie, blissfully unaware that he has the wrong movie star. "
    "You have practised saying what you are responsible for, saying you liked a film, asking if someone has a spare item with them, and politely requesting a photo. "
    "Until next time!"
)
CLOSING = ('jonas', 'Schönen Tag noch!')

STORY = [
    ('jonas', 'Ja, ich bin Jonas, und ich bin hier für die Sicherheit zuständig.', "Yes, I'm Jonas, and I'm in charge of security here.", [(233, 'Ja, ich bin Jonas. Ich bin hier für die'), (235, 'zuständig')], 'Replace English loan Security with standard German Sicherheit.'),
    ('jonas', 'Da kriege ich natürlich mit, wer hier rein und raus geht.', 'So of course I notice who goes in and out here.', [(235, 'da kriege ich'), (237, 'natürlich mit, wer'), (237, 'hier rein')], 'Write rein und raus geht cleanly for A1 tokenization.'),
    ('jonas', 'Ich bin ein großer Fan von dem Film, wo er den Lehrer spielt.', "I'm a big fan of the film where he plays the teacher.", [(239, 'großer Fan von'), (245, 'wo er den Lehrer'), (247, 'spielt')], ''),
    ('jonas', 'Der Film hat mir sehr gut gefallen.', 'I really liked that film.', [(249, 'hat mir'), (251, 'gut gefallen')], ''),
    ('fahri', 'Hallo! Hast du einen Chip? Ich habe meinen Chip vergessen.', 'Hello! Do you have a trolley token? I forgot my token.', [(261, 'Hallo'), (265, 'Hast du'), (265, 'Chip? Ich habe'), (265, 'Chip vergessen')], 'Restore accusative einen Chip / meinen Chip.'),
    ('jonas', 'Ja, den habe ich immer dabei für den Notfall. Bitte!', 'Yes, I always have one on me for emergencies. Here you go!', [(269, 'Ja, habe ich immer dabei'), (271, 'Notfall'), (271, 'Bitte')], 'Restore article den Notfall.'),
    ('jonas', 'Entschuldigung, dürfte ich vielleicht ein Foto mit Ihnen machen?', 'Excuse me, could I perhaps take a photo with you?', [(277, 'Entschuldigung'), (277, 'Dürfte ich'), (279, 'vielleicht ein Foto mit Ihnen machen')], ''),
    ('fahri', 'Ja, komm, mach schnell, bitte.', 'Yeah, come on, make it quick, please.', [(281, 'Ja, komm, mach schnell'), (281, 'bitte')], ''),
    ('jonas', 'Danke! Das sind ich und Elyas!', "Thanks! That's me and Elyas!", [(283, 'Danke'), (285, 'ich und')], 'Auto-caption writes Elias mein Warik for Elyas M\'Barek.')
]

WALK = [
    (0, None, "'Yes, I'm Jonas, and I'm in charge of security here.' The key workplace word at the very end means 'responsible' or 'in charge', and it always pairs with the preposition for 'for'. Swap in your own department and you can describe almost any job role."),
    (1, None, "'So of course I notice who goes in and out here.' Everyday spoken German loves this split-apart expression for 'catch on' or 'notice': 'get' stands near the front and 'with' lands after 'of course'. Later, the short pair for 'in and out' captures people coming and going."),
    (3, None, "'I really liked that film.' Where English says 'I liked the film', German flips the perspective: 'the film has pleased to me very well'. That makes the movie the doer and 'to me' the person enjoying it."),
    (4, None, "'Hello! Do you have a trolley token? I forgot my token.' German supermarkets lock their shopping trolleys until you slot in a coin or a plastic token — called by the borrowed word 'chip'. Notice the '-en' ending showing the token is the thing he needs and forgot."),
    (5, None, "'Yes, I always have one on me for emergencies. Here you go!' That handy little word near the middle means 'with me' or 'on me' — what you say for keys, cash, or a phone in your pocket. The compound for emergency literally joins 'need' and 'case'."),
    (6, None, "'Excuse me, could I perhaps take a photo with you?' Jonas switches to ultra-polite mode for his idol: softening 'may I' into 'might I', adding the word for 'perhaps', and addressing him with the formal 'you'. Notice too that German 'makes' a photo rather than 'taking' one."),
    (7, None, "'Yeah, come on, make it quick, please.' Fahri answers in brisk casual style, literally saying 'make fast, please' — a reusable everyday phrase whenever someone needs to hurry up.")
]
