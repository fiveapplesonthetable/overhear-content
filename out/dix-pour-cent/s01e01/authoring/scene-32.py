ID = "dix-pour-cent-s01e01-scene-32"
SHOW = "dix-pour-cent"
SEASON = 1
EPISODE = 1
SCENE = 32
TITLE = "Arlette secoue Gabriel  (Arlette Shakes Gabriel Up)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "gabriel": "theo"}
LABELS = {"lea": "Arlette", "gabriel": "Gabriel"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S01E01"
SOURCE_FILE = "sources/dix-pour-cent/s01/e01.fr.dual.srt"

INTRO = ("While Camille was celebrating her second chance with Andréa, poor Gabriel was hiding from the world. "
         "He has lost Cécile, his favourite client and friend: she left him and signed with Mathias, and now she won't even speak to him. "
         "So he's lying on the sofa in Arlette's office, on a hot afternoon, looking at pictures of a young unknown actress. "
         "Arlette, the oldest and sharpest agent in the building, walks in and is not impressed. "
         "Listen to it in French first. It's fine to understand only bits of it for now.")

STORY = [
 ("lea", "Il fait chaud. Vous faites quoi?", "It's hot. What are you doing?",
  [(823, "Il fait chaud"), (823, "Vous faites quoi")], ""),
 ("gabriel", "Je travaille.", "I'm working.",
  [(823, "Je travaille")], ""),
 ("gabriel", "Alice Tiscalini. Vous la connaissez?", "Alice Tiscalini. Do you know her?",
  [(824, "Alice Tiscalini. Vous la connaissez")], ""),
 ("gabriel", "Elle est vraiment bien.", "She's really good.",
  [(825, "Elle est vraiment bien")], ""),
 ("lea", "Oui. Elle attrape bien la lumière.", "Yes. She catches the light well.",
  [(827, "Elle attrape bien la lumière")], "Arlette's cheeky follow-up about the actress's body left out"),
 ("gabriel", "Elle a fait un peu de théâtre.", "She's done a bit of theatre.",
  [(830, "Elle a fait un peu de théâtre")], "who says 829-833 is inferred: Gabriel is pitching his find"),
 ("gabriel", "Elle est prête pour nous.", "She's ready for us.",
  [(832, "Elle est prête pour nous")], ""),
 ("lea", "Alors, Cécile change d'agent, et vous cherchez une remplaçante?", "So Cécile changes agent, and you look for a replacement?",
  [(834, "Cécile change d'agent"), (834, "remplaçante")], "'vous vous précipitez pour trouver' -> 'vous cherchez'; the dating-app joke left out"),
 ("gabriel", "Arrêtez, Arlette!", "Stop it, Arlette!",
  [(836, "Arrêtez, Arlette")], ""),
 ("lea", "Samuel a oublié de vous apprendre la ténacité.", "Samuel forgot to teach you tenacity.",
  [(837, "Samuel a oublié de vous apprendre")], "'ce qu'est la ténacité' -> 'la ténacité'"),
 ("gabriel", "Je fais quoi, alors?", "So what do I do?",
  [], "simplified from 838 'Qu'est-ce que vous voulez que je fasse ?' (subjunctive, beyond A1)"),
 ("gabriel", "Elle ne veut plus me parler.", "She doesn't want to talk to me anymore.",
  [(839, "elle ne veut plus me parler")], ""),
 ("gabriel", "Elle est partie avec Mathias. C'est son choix.", "She left with Mathias. It's her choice.",
  [(840, "elle est partie avec")], "'il doit lui convenir' (841) -> 'C'est son choix'"),
 ("lea", "Vous croyez? Elle est mieux avec Mathias?", "You think so? She's better off with Mathias?",
  [(844, "est mieux avec Mathias")], "Arlette switches to tu here in the source ('Tu crois ?'); kept in vous for a consistent A1 register"),
 ("lea", "Je connais Cécile. Elle déteste les hommes comme Mathias.", "I know Cécile. She hates men like Mathias.",
  [(845, "Je connais Cécile. Elle déteste les")], "'mecs' (slang) -> 'hommes'"),
 ("lea", "C'est Mathias. Il manipule tout le monde.", "That's Mathias. He manipulates everyone.",
  [], "simplified from 846 'Il a dû l'embobiner'"),
 ("lea", "Allez, Gabriel! Ne restez pas là à ne rien faire!", "Come on, Gabriel! Don't just lie there doing nothing!",
  [(847, "à ne rien faire")], "source is sarcastic ('t'as raison, reste là à ne rien faire'); made a direct push"),
]

OPENER = ("Let's go through it together. Arlette comes in, looks at Gabriel stretched out on her sofa, and asks the obvious question.")

WALK = [
 (0, "Il fait chaud.",
  "'It's hot.' For the weather, French uses the verb 'to make' with 'it': literally 'it makes hot'."),
 (0, "Vous faites quoi?",
  "'What are you doing?' Same verb, 'to make' or 'to do', now with the formal 'you'. Arlette and Gabriel are colleagues, but she's from another generation, so they keep it formal."),
 (1, None,
  "'I'm working.' One verb in the present tense covers both 'I work' and 'I'm working'. From the sofa, that's a bold claim."),
 (2, None,
  "'Alice Tiscalini. Do you know her?' The little word for 'her' comes before the verb, not after it like in English."),
 (3, None,
  "'She's really good.' Gabriel is excited about her. Arlette takes a look."),
 (4, None,
  "'Yes. She catches the light well.' That means she looks great on camera. Arlette adds a cheeky comment in the show, which we'll skip."),
 (5, None,
  "'She's done a bit of theatre.' That's the past tense with 'to have' plus the past form of 'to do'. Gabriel keeps selling."),
 (6, None,
  "'She's ready for us.' He means she's a fresh talent nobody has signed yet. Now Arlette sees what's really going on."),
 (7, None,
  "'So Cécile changes agent, and you look for a replacement?' The last word is the feminine form: a woman who replaces another. Arlette is teasing him for rushing to forget Cécile."),
 (8, None,
  "'Stop it, Arlette!' A formal command. Gabriel is hurt."),
 (9, None,
  "'Samuel forgot to teach you tenacity.' Samuel is the boss who trained him. The 'you' here means 'to you', and again it comes before the verb."),
 (10, None,
  "'So what do I do?' A very natural spoken question, with the question word left at the end."),
 (11, None,
  "'She doesn't want to talk to me anymore.' That's 'not anymore' again: two small words around the verb, the second meaning 'more'."),
 (12, None,
  "'She left with Mathias. It's her choice.' Notice the past tense here uses 'to be' instead of 'to have', because the verb is about leaving, a movement."),
 (13, None,
  "'You think so? She's better off with Mathias?' Arlette doesn't believe it for a second."),
 (14, None,
  "'I know Cécile. She hates men like Mathias.' Arlette sounds completely sure of herself."),
 (15, None,
  "'That's Mathias. He manipulates everyone.' She means Mathias talked Cécile into it with clever words."),
 (16, None,
  "'Come on, Gabriel! Don't just lie there doing nothing!' Two negatives here: first 'don't stay', then 'nothing', both built around the verb. And it works: in the next scene, Gabriel goes off to find Cécile."),
]

TRANSITION = "Now, the whole scene again, a little faster."

OUTRO = ("Well done, that was a quick and witty exchange. Listen for the 'not anymore' and the 'nothing' when you watch, "
         "and I'll see you in the next scene.")
CLOSING = ("lea", "Courage, Gabriel!")
