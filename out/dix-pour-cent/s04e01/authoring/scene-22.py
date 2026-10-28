# Authoring module for dix-pour-cent s04e01 scene 22 (cues 940-978).
# Build: python3 tools/compose.py out/dix-pour-cent/s04e01/authoring/scene-22.py --out out/dix-pour-cent/s04e01/scene-22.json

ID = "dix-pour-cent-s04e01-scene-22"
SHOW = "dix-pour-cent"
SEASON = 4
EPISODE = 1
SCENE = 22
TITLE = "Une vraie actrice  (A True Actress)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "gabriel": "theo", "charlotte": "emilie"}
LABELS = {"lea": "Sofia", "gabriel": "Gabriel", "charlotte": "Charlotte"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S04E01"
SOURCE_FILE = "sources/dix-pour-cent/s04/e01.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 940-978. In the quiet backstage hallway, Sofia tells Gabriel that she wants to give up, but Gabriel insists "
    "that she quit her desk job at ASK to focus entirely on acting. When Charlotte Gainsbourg asks for her autograph "
    "on her cast, Sofia realizes she is recognized as a true actress."
)

INTRO = (
    "In the quiet backstage hallway, Sofia tells Gabriel that she wants to give up, but Gabriel insists that she quit her desk job at ASK to focus entirely on acting. "
    "When a fan and Charlotte Gainsbourg both ask for her autograph on their casts, Sofia realizes she is truly an actress. "
    "Let's listen to the scene in French first."
)

STORY = [
    ("lea", "Il est temps que j'arrête tout.",
     "It is time that I stop everything.",
     [(941, "Il est temps que j'arrête")], "Declared her desire to quit acting"),
    ("gabriel", "Tu as raison d'arrêter l'accueil.",
     "You are right to stop the front desk.",
     [(942, "Tu as raison"), (944, "l'accueil")], "Clarified that she should only leave reception"),
    ("lea", "Comment je paye mon loyer maintenant?",
     "How do I pay my rent now?",
     [(947, "Comment je paye mon loyer ?")], "Worried about paying her living expenses"),
    ("gabriel", "Tu joues, c'est ton métier désormais.",
     "You act, it is your job from now on.",
     [(948, "Tu joues"), (955, "c'est")], "Emphasized her true calling as an actress"),
    ("lea", "J'ai raté ma dernière audition importante.",
     "I blew my last important audition.",
     [(952, "J'ai raté mon audition")], "Doubted her talent after a tough audition"),
    ("gabriel", "Tu dois avoir confiance en ton talent.",
     "You must have confidence in your talent.",
     [(949, "tu dois me faire confiance")], "Encouraged her to believe in herself"),
    ("charlotte", "Excusez-moi, pourriez-vous baisser la voix?",
     "Excuse me, could you lower your voices?",
     [(963, "Excusez-moi. Pourriez-vous baisser la voix ?")], "Politely asked them to speak more quietly"),
    ("gabriel", "Bonsoir mademoiselle Charlotte Gainsbourg.",
     "Good evening Miss Charlotte Gainsbourg.",
     [(964, "Bonjour, Mademoiselle Gainsbourg")], "Greeted the renowned actress with respect"),
    ("charlotte", "La cérémonie était beaucoup trop longue.",
     "The ceremony was much too long.",
     [(966, "La cérémonie est trop longue")], "Confided her fatigue with the event"),
    ("lea", "Vous avez un plâtre à la jambe?",
     "You have a cast on your leg?",
     [(966, "Avec mon plâtre et tout")], "Noticed Charlotte's bulky medical cast"),
    ("charlotte", "Vous avez un stylo pour signer?",
     "Do you have a pen to sign?",
     [(968, "Vous avez un stylo ?")], "Requested a pen for an autograph"),
    ("lea", "Vous voulez vraiment ma signature ici?",
     "You really want my signature here?",
     [(959, "Moi ? Signer ton plâtre ?")], "Felt shocked and honored to sign"),
    ("charlotte", "C'est super, merci beaucoup et bravo!",
     "It is great, thank you very much and congratulations!",
     [(972, "C'est super. Merci beaucoup")], "Thanked Sofia warmly for the autograph"),
    ("gabriel", "Tu vois, le public t'admire déjà.",
     "You see, the public already admires you.",
     [(951, "Les gens veulent te voir")], "Affirmed that she is recognized as a star")
]

OPENER = "Let's break down the dialogue line by line."

WALK = [
    (0, None,
     "'It is time that I stop everything.' Sofia sighs deeply in the backstage hallway. "
     "The subjunctive clause expresses her sudden decision."),
    (1, None,
     "'You are right to stop the front desk.' Gabriel clarifies his meaning at once. "
     "The preposition de with infinitive focuses on the desk job."),
    (2, None,
     "'How do I pay my rent now?' Sofia asks anxiously about her daily finances. "
     "The interrogative adverb introduces her practical worry."),
    (3, None,
     "'You act, it is your job from now on.' Gabriel insists on her real vocation. "
     "The decisive adverb marks a major career shift."),
    (4, None,
     "'I blew my last important audition.' Sofia laments her missed chance for the film. "
     "The compound past recalls the difficult trial."),
    (5, None,
     "'You must have confidence in your talent.' Gabriel counters her persistent doubts. "
     "The modal verb construction urges self-assurance."),
    (6, None,
     "'Excuse me, could you lower your voices?' Charlotte Gainsbourg steps out on crutches. "
     "The polite conditional softens her gentle request."),
    (7, None,
     "'Good evening Miss Charlotte Gainsbourg.' Gabriel greets her with deference. "
     "The formal title honors the distinguished guest star."),
    (8, None,
     "'The ceremony was much too long.' Charlotte shares her weariness with the gala. "
     "The comparative adverb highlights the exhausting pace."),
    (9, None,
     "'You have a cast on your leg?' Sofia looks down with genuine sympathy. "
     "The prepositional phrase describes the bulky medical cast."),
    (10, None,
     "'Do you have a pen to sign?' Charlotte asks with a conspiratorial smile. "
     "The preposition pour with infinitive states her purpose."),
    (11, None,
     "'You really want my signature here?' Sofia asks in disbelieving wonder. "
     "The adverb expresses her delightful surprise."),
    (12, None,
     "'It is great, thank you very much and congratulations!' Charlotte signs off with charm. "
     "The enthusiastic interjections praise Sofia warmly."),
    (13, None,
     "'You see, the public already admires you.' Gabriel smiles proudly at his client. "
     "The direct object pronoun emphasizes public respect.")
]

TRANSITION = "Now, listen to the complete dialogue again at normal conversational pace."
OUTRO = "Meeting Charlotte Gainsbourg gives Sofia newfound pride and purpose in her acting career. When you watch the episode, listen out for the expressions meaning 'time' and 'stop'. You'll catch them now. See you next time."
CLOSING = ("gabriel", "Tu vois, le public t'admire déjà.")
