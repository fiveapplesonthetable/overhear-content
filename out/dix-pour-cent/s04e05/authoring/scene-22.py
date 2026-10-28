# Authoring module for dix-pour-cent s04e05 scene 22 (cues 834-848).
# Build: python3 tools/compose.py out/dix-pour-cent/s04e05/authoring/scene-22.py --out out/dix-pour-cent/s04e05/scene-22.json

ID = "dix-pour-cent-s04e05-scene-22"
SHOW = "dix-pour-cent"
SEASON = 4
EPISODE = 5
SCENE = 22
TITLE = "Le carnage des talents  (The Talent Carnage)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "gabriel": "theo"}
LABELS = {"lea": "Andrea", "gabriel": "Gabriel"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S04E05"
SOURCE_FILE = "sources/dix-pour-cent/s04/e05.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 834-848. Returning to ASK, Andrea and Gabriel are hit with devastating news: phones are ringing off "
    "the hook as marquee clients fire them. Checking her inbox, Andrea discovers that Elise Formain has orchestrated "
    "a mass defection of ASK's biggest stars to StarMedia, leaving the agency in ruins."
)

INTRO = (
    "Stepping into the agency, Andrea and Gabriel find the floor deserted and phone lines blinking with panic. "
    "Within minutes, devastating emails confirm their worst nightmare: rival agent Elise Formain has poached their most prestigious clients. "
    "Let's listen to their conversation in French first."
)

OPENER = "Let's examine the conversation line by line and explore the French expressions."
TRANSITION = "Now let's listen to the complete discussion once more to reinforce the vocabulary."

STORY = [
    ("gabriel", "Les téléphones sonnent sans arrêt aujourd'hui.",
     "The phones are ringing without stopping today.",
     [(836, "C'est quoi ces conneries")], "Reported the sudden surge of panicked calls"),
    ("lea", "Où sont passés tous nos assistants?",
     "Where have all our assistants gone?",
     [(834, "Les assistants?"), (835, "Je ne les ai pas vus")], "Noticed the eerily quiet reception desks"),
    ("gabriel", "Fabrice Luchini vient de me quitter!",
     "Fabrice Luchini has just left me!",
     [(837, "Luchini dit qu'il me lâche")], "Delivered a devastating personal blow"),
    ("lea", "Pourquoi prend-il une telle décision brutale?",
     "Why does he make such a brutal decision?",
     [(838, "Je ne comprends pas")], "Struggled to understand the sudden departure"),
    ("gabriel", "Il prétend que je le critique.",
     "He claims that I criticize him.",
     [(837, "je dis du mal de lui dans son dos")], "Shared the actor's paranoid complaint"),
    ("lea", "Regarde mes courriels, c'est le carnage.",
     "Look at my emails, it is carnage.",
     [(841, "T'as regardé tes mails?"), (843, "C'est le carnage")], "Scanned through a barrage of cancellation notices"),
    ("gabriel", "Qu'est-ce qui se passe encore?",
     "What is happening now?",
     [(842, "Non. Pourquoi?")], "Feared further bad news"),
    ("lea", "Dujardin et Berléand nous quittent aussi!",
     "Dujardin and Berléand are leaving us too!",
     [(844, "Dujardin, Berléand... Toutes nos stars quittent")], "Announced the collapse of their client list"),
    ("gabriel", "Mais toutes nos stars partent ensemble?",
     "Are all our stars leaving together?",
     [(844, "Toutes nos stars quittent l'agence")], "Reeled from the synchronized exodus"),
    ("lea", "Élise est en train de nous saigner.",
     "Élise is bleeding us dry.",
     [(845, "Elle nous saigne?")], "Identified the mastermind behind the attack"),
    ("gabriel", "Je t'avais prévenue pour cette traîtresse!",
     "I had warned you about that traitor!",
     [(848, "Elle part chez StarMédia?")], "Reminded her of his earlier suspicions"),
    ("lea", "Elle emmène tout le monde chez StarMédia.",
     "She is taking everyone to StarMédia.",
     [(848, "Elle part chez StarMédia")], "Confirmed the mass corporate defection"),
    ("gabriel", "Notre agence est complètement ruinée, Andréa.",
     "Our agency is completely ruined, Andréa.",
     [(846, "Donne-moi au moins une raison")], "Spoke of total professional devastation"),
    ("lea", "Je vais lui faire payer cher.",
     "I am going to make her pay dearly.",
     [(847, "Elle a raccroché")], "Vowed fierce retaliation for the betrayal"),
]

WALK = [
    (0, None,
     "'The phones are ringing without stopping today.' Gabriel rushes across the bustling floor. "
     "The prepositional phrase sans arrêt depicts nonstop disruption."),
    (1, None,
     "'Where have all our assistants gone?' Andrea surveys the empty desks with unease. "
     "The interrogative phrase où sont passés highlights the sudden absence."),
    (2, None,
     "'Fabrice Luchini has just left me!' Gabriel clutches his receiver in disbelief. "
     "The recent past construction vient de quitter reports the loss of a star."),
    (3, None,
     "'Why does he make such a brutal decision?' Andrea questions the actor's motive. "
     "The adjective brutale conveys sudden shock."),
    (4, None,
     "'He claims that I criticize him.' Gabriel recounts the false accusation. "
     "The verb prétend indicates an unfounded rumor."),
    (5, None,
     "'Look at my emails, it is carnage.' Andrea opens her inbox to endless resignation notices. "
     "The dramatic noun carnage captures total destruction."),
    (6, None,
     "'What is happening now?' Gabriel asks in dread. "
     "The adverb encore expresses weary disbelief."),
    (7, None,
     "'Dujardin and Berléand are leaving us too!' Andrea reads the incoming signatures. "
     "The proper nouns cite marquee French cinema icons."),
    (8, None,
     "'Are all our stars leaving together?' Gabriel connects the coordinated strike. "
     "The adverb ensemble underlines the organized sabotage."),
    (9, None,
     "'Elise is bleeding us dry.' Andrea grasps the ruthless strategy. "
     "The progressive structure est en train de saigner evokes lethal damage."),
    (10, None,
     "'I had warned you about that traitor!' Gabriel's earlier warnings prove prophetic. "
     "The past perfect verb t'avais prévenue reminds her of his foresight."),
    (11, None,
     "'She is taking everyone to StarMedia.' Andrea names the rival agency destination. "
     "The present verb emmène describes the massive poaching."),
    (12, None,
     "'Our agency is completely ruined, Andrea.' Gabriel faces financial collapse. "
     "The adjective ruinée spells catastrophe for ASK."),
    (13, None,
     "'I am going to make her pay dearly.' Andrea's shock turns to cold anger. "
     "The idiomatic promise faire payer cher heralds a fierce counterattack."),
]

OUTRO = "Stunned into silence, Andrea and Gabriel realize that ASK has just suffered the deadliest strike in its history. When you watch the episode, listen out for the expressions meaning 'phones' and 'ring'. You'll catch them now. See you next time."
CLOSING = ("lea", "Je vais lui faire payer cher.")
