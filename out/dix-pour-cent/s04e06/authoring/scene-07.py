# Authoring module for dix-pour-cent s04e06 scene 07 (cues 317-356).
# Build: python3 tools/compose.py out/dix-pour-cent/s04e06/authoring/scene-07.py --out out/dix-pour-cent/s04e06/scene-07.json

ID = "dix-pour-cent-s04e06-scene-07"
SHOW = "dix-pour-cent"
SEASON = 4
EPISODE = 6
SCENE = 7
TITLE = "L'offre empoisonnée  (The Poisoned Offer)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "gabriel": "theo"}
LABELS = {"lea": "Élise", "gabriel": "Gabriel"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S04E06"
SOURCE_FILE = "sources/dix-pour-cent/s04/e06.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 317-356. In a cafe, Elise Formain tries to recruit Gabriel to join StarMedia, "
    "but Gabriel fiercely rejects her and calls out her obsession with Andrea."
)

INTRO = (
    "At a cafe, traitorous agent Elise Formain invites Gabriel for a talk. "
    "She attempts to entice him into joining StarMedia, but Gabriel sees right through her opportunistic scheme. "
    "Let's listen to their conversation in French first."
)

OPENER = "Let's look at Elise and Gabriel confronting each other step by step."

STORY = [
    ("gabriel", "Tu veux fêter quoi aujourd'hui?",
     "What do you want to celebrate today?",
     [(321, "Fêter quoi")], "Gabriel questions Elise's celebratory mood"),
    ("gabriel", "Tu veux saigner notre agence?",
     "Do you want to bleed our agency dry?",
     [(322, "Saigner ASK")], "Gabriel confronts her about poaching ASK clients"),
    ("lea", "Ce n'était pas difficile du tout.",
     "It was not difficult at all.",
     [(325, "Ce n'était pas difficile")], "Elise boasts about how easily she raided the agency"),
    ("gabriel", "Dis-moi vite ce que tu veux.",
     "Tell me quickly what you want.",
     [(327, "Qu'est-ce que tu veux")], "Gabriel impatiently demands her actual motive"),
    ("lea", "Toi et Andréa formiez un duo.",
     "You and Andrea formed a duo.",
     [(330, "duo d'agents")], "Elise recalls Gabriel and Andrea's successful partnership"),
    ("lea", "Viens chez StarMédia avec tes acteurs.",
     "Come to StarMedia with your actors.",
     [(334, "chez StarMédia")], "Elise extends a job offer to bring his clients over"),
    ("lea", "Formons une nouvelle équipe ensemble.",
     "Let us form a new team together.",
     [(335, "former une équipe")], "Elise proposes they become business partners"),
    ("gabriel", "Tu ne recules devant rien, jamais.",
     "You stop at nothing, ever.",
     [(336, "recules devant rien")], "Gabriel scoffs at her ruthless ambition"),
    ("gabriel", "Ton rêve secret, c'est d'être Andréa.",
     "Your secret dream is to be Andrea.",
     [(338, "d'être Andréa")], "Gabriel identifies her deep psychological obsession"),
    ("gabriel", "Mais tu ne seras jamais elle.",
     "But you will never be her.",
     [(341, "jamais être Andréa")], "Gabriel insists she could never match Andrea's talent"),
    ("lea", "C'est juste une proposition amicale.",
     "It is just a friendly proposal.",
     [(344, "proposition")], "Elise pretends her offer was merely collegial"),
    ("gabriel", "Tu sais où la mettre, non?",
     "You know where to shove it, right?",
     [(345, "te la mettre")], "Gabriel bluntly tells her where to put her offer"),
    ("lea", "Je plante une graine utile.",
     "I am planting a useful seed.",
     [(347, "graine")], "Elise suggests she has introduced a tempting thought"),
    ("lea", "Vois tranquillement si elle germe.",
     "See calmly if it sprouts.",
     [(348, "si elle germe")], "Elise invites him to let the idea grow over time"),
]

WALK = [
    (0, None,
     "'What do you want to celebrate today?' Gabriel asks what victory she thinks she is marking. In spoken French, the little word before 'want' drops its final vowel and attaches with an apostrophe."),
    (1, None,
     "'Do you want to bleed our agency dry?' Gabriel challenges her predatory tactics against ASK. The verb meaning 'want' pairs naturally with the noun for 'agency' in everyday conversation."),
    (2, None,
     "'It was not difficult at all.' Elise casually brushes off the effort required to steal their talent. The clause hinges on the everyday verb meaning 'was'."),
    (3, None,
     "'Tell me quickly what you want.' Gabriel demands that she get straight to the point of the meeting. The informal 'you' form around 'tell' marks a direct, personal relationship."),
    (4, None,
     "'You and Andrea formed a duo.' Elise brings up his historic collaboration with Andrea. Notice how 'formed' leads directly into the noun meaning 'pair'."),
    (5, None,
     "'Come to StarMedia with your actors.' Elise formally invites him to defect with his roster. The verb meaning 'come' pairs naturally with the noun for 'actors' in everyday conversation."),
    (6, None,
     "'Let us form a new team together.' Elise suggests combining forces at her new agency. The verb meaning 'let us form' pairs naturally with the noun for 'team' in everyday conversation."),
    (7, None,
     "'You stop at nothing, ever.' Gabriel condemns her shameless lack of professional ethics. French builds the 'never' negation in two parts wrapped right around 'back down'."),
    (8, None,
     "'Your secret dream is to be Andrea.' Gabriel accuses her of wanting to emulate Andrea in every way. The descriptive adjective for 'secret' agrees in gender and number with its noun."),
    (9, None,
     "'But you will never be her.' Gabriel tells her firmly that she will always fall short of Andrea's stature. The informal 'you' form around 'will be' marks a direct, personal relationship."),
    (10, None,
     "'It is just a friendly proposal.' Elise plays down the tension with an innocent posture. The key noun here means 'proposal', anchored by its matching French article."),
    (11, None,
     "'You know where to shove it, right?' Gabriel uses a colloquial rebuff to reject her overture completely. Gabriel uses the casual singular 'you' with 'know', showing close familiarity."),
    (12, None,
     "'I am planting a useful seed.' Elise uses a metaphor for planting a persuasive idea in his mind. The verb meaning 'plant' pairs naturally with the noun for 'seed' in everyday conversation."),
    (13, None,
     "'See calmly if it sprouts.' Elise suggests that he will reconsider in due time."),
]

TRANSITION = "Now listen to the whole scene again at normal speed, and see how much more you catch."
OUTRO = "Disgusted by Elise's cynical attempt to recruit him to StarMedia, Gabriel fiercely rejects her offer and defends his loyalty to Andrea and ASK. When you watch the episode, listen out for the expressions meaning 'want' and 'to celebrate'. You'll catch them now. See you next time."
CLOSING = ("lea", "Vois tranquillement si elle germe.")
