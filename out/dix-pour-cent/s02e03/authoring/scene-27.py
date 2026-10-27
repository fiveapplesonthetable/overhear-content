# Authoring module for dix-pour-cent s02e03 scene 27 (cues 683-721).
# Build: python3 tools/compose.py out/dix-pour-cent/s02e03/authoring/scene-27.py --out out/dix-pour-cent/s02e03/scene-27.json

ID = "dix-pour-cent-s02e03-scene-27"
SHOW = "dix-pour-cent"
SEASON = 2
EPISODE = 3
SCENE = 27
TITLE = "Travail tardif au bureau  (Working Late)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "mathias": "theo"}
LABELS = {"lea": "Noémie", "mathias": "Mathias"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S02E03"
SOURCE_FILE = "sources/dix-pour-cent/s02/e03.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 683-721. In Mathias's office late at night, Mathias and Noémie work through complicated "
    "shooting schedules for Tonie Marshall's film. They apologize for past tensions and share a moment "
    "of tender intimacy. Adapted for A1 French."
)

INTRO = (
    "In Mathias's office late at night, Noemie is hard at work solving a complicated shooting schedule. "
    "Mathias joins her, and as they examine the script sequences together, personal feelings resurface. "
    "Let's listen to the scene in French first."
)

STORY = [
    ("mathias", "Il faut s'arrêter, Noémie, il est tard.",
     "We must stop, Noémie, it is late.",
     [(686, "Il faut s'arrêter, Noémie, il est tard.")], ""),
    ("lea", "J'ai pris du retard dans mon travail.",
     "I got behind in my work.",
     [(687, "j'ai pris du retard dans mon travail hier.")], "Shortened line"),
    ("mathias", "Je voulais m'excuser pour hier.",
     "I wanted to apologize for yesterday.",
     [(688, "Je voulais m'excuser pour hier.")], ""),
    ("lea", "Ce n'est pas ta faute, Mathias.",
     "It is not your fault, Mathias.",
     [(689, "C'est pas ta faute.")], "Added Mathias"),
    ("mathias", "La situation est complexe.",
     "The situation is complex.",
     [(690, "La situation... est complexe.")], ""),
    ("lea", "J'avais peur que tu sois fâché contre moi.",
     "I was afraid you were angry with me.",
     [(692, "J'avais tellement peur que tu sois vraiment en colère contre moi.")], "Simplified to fâché"),
    ("mathias", "Désolé de t'avoir mise dans cette situation.",
     "Sorry for having put you in this situation.",
     [(695, "Désolé de t'avoir mis dans cette situation.")], ""),
    ("mathias", "Tu ne peux pas passer la nuit sur ces plannings.",
     "You cannot spend the night on these schedules.",
     [(704, "Tu peux pas passer la nuit sur ces plannings.")], "Formalized negation"),
    ("lea", "Mais je suis sûre que ça peut marcher.",
     "But I am sure that it can work.",
     [(707, "mais je suis sûre que ça peut marcher.")], ""),
    ("lea", "Ils doivent commencer par la fin du tournage.",
     "They must start with the end of the shoot.",
     [(708, "Ils doivent commencer par la fin, le tournage à Paris.")], "Shortened phrase"),
    ("mathias", "Voyons voir, quelle séquence?",
     "Let us see, which sequence?",
     [(709, "Voyons voir."), (713, "Quelle séquence ?")], "Combined short lines"),
    ("lea", "La séquence soixante-neuf.",
     "Sequence sixty-nine.",
     [(713, "69.")], "Spelled out number 69"),
    ("lea", "Voilà le résumé de la scène.",
     "Here is the summary of the scene.",
     [(716, "voilà le résumé... et la voilà.")], "Adapted line"),
    ("mathias", "Oui, ils peuvent commencer par là.",
     "Yes, they can start there.",
     [(718, "Oui, ils peuvent commencer par là.")], ""),
    ("mathias", "Tu as fait un travail formidable, Noémie.",
     "You did a wonderful job, Noémie.",
     [], "Mathias praising Noémie"),
    ("lea", "Merci, Mathias.",
     "Thank you, Mathias.",
     [(720, "Oh, Mathias.")], "Adapted line"),
]

OPENER = "Let's examine how Mathias and Noemie are sharing an intimate moment working late."

WALK = [
    (0, None,
     "'We must stop, Noemie, it is late.' The impersonal expression il faut followed by an infinitive."),
    (1, None,
     "'I got behind in my work.' The idiom prendre du retard meaning to fall behind."),
    (2, None,
     "'I wanted to apologize for yesterday.' The reflexive verb s'excuser expressing regret."),
    (3, None,
     "'It is not your fault, Mathias.' A reassuring phrase using the noun faute."),
    (4, None,
     "'The situation is complex.' An objective assessment using the adjective complexe."),
    (5, None,
     "'I was afraid you were angry with me.' The adjective fache expressing anger."),
    (6, None,
     "'Sorry for having put you in this situation.' A past infinitive introduced by de."),
    (7, None,
     "'You cannot spend the night on these schedules.' A negative warning with passer la nuit."),
    (8, None,
     "'But I am sure that it can work.' An assertive clause expressing confidence."),
    (9, None,
     "'They must start with the end of the shoot.' The verb commencer followed by the preposition par."),
    (10, None,
     "'Let us see, which sequence?' An informal prompt asking for detail."),
    (11, None,
     "'Sequence sixty-nine.' A spelled out cardinal number identifying the script scene."),
    (12, None,
     "'Here is the summary of the scene.' The presentative voila introducing the document."),
    (13, None,
     "'Yes, they can start there.' The spatial adverb la meaning there."),
    (14, None,
     "'You did a wonderful job, Noemie.' Mathias commends her dedication."),
    (15, None,
     "'Thank you, Mathias.' An intimate tender response."),
]

TRANSITION = "Now let's listen to the whole discussion again without stopping."

OUTRO = (
    "Working side by side in the quiet office, Mathias and Noemie find a solution to the schedule crisis. "
    "Their professional collaboration rekindles their deep personal connection."
)

CLOSING = ("mathias", "Bonne nuit, Noémie.")
