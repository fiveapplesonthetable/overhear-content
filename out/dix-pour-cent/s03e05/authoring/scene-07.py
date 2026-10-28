# Authoring module for dix-pour-cent s03e05 scene 07 (cues 182-224).
# Build: python3 tools/compose.py out/dix-pour-cent/s03e05/authoring/scene-07.py --out out/dix-pour-cent/s03e05/scene-07.json

ID = "dix-pour-cent-s03e05-scene-07"
SHOW = "dix-pour-cent"
SEASON = 3
EPISODE = 5
SCENE = 7
TITLE = "Béatrice sur le plateau  (Béatrice on Set)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "beatrice": "emilie", "realisateur": "theo"}
LABELS = {"lea": "Andréa", "beatrice": "Béatrice", "realisateur": "Le Réalisateur"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S03E05"
SOURCE_FILE = "sources/dix-pour-cent/s03/e05.fr.dual.srt"
SOURCE_NOTE = ("Cues 182-224. On a film set, Beatrice Dalle refuses to shoot an unexpected nude corpse scene. "
               "Andrea arrives just in time to confront the demanding director and enforce the written contract. Adapted for A1 French.")

INTRO = ("On a tense movie set, director and star clash over an unexpected artistic demand. "
         "When the director insists that Beatrice Dalle appear completely naked in a morgue scene, Andrea Martel steps in to protect her client. "
         "Let's listen to the argument in French first.")

STORY = [
    ("realisateur", "Je te demande d'être nue ici.",
     "I am asking you to be naked here.",
     [(197, "je te demande d'être nue")], "The director pushes for nudity"),
    ("beatrice", "Non, je ne peux pas faire ça!",
     "No, I cannot do that!",
     [(198, "Non, je peux pas, non")], "Beatrice sets a firm boundary"),
    ("realisateur", "Tu seras magnifique, fais-moi confiance!",
     "You will be magnificent, trust me!",
     [(199, "Tu seras magnifique, fais-moi confiance")], "The director tries flattery"),
    ("beatrice", "Je refuse d'être un tas de viande!",
     "I refuse to be a slab of meat!",
     [(200, "pas envie d'être comme un tas de viande")], "Beatrice denounces the setup"),
    ("lea", "Cette scène lui semble un peu gratuite.",
     "This scene seems a little gratuitous to her.",
     [(202, "ça lui semble un petit peu gratuit")], "Andrea articulates the objection"),
    ("realisateur", "Rien n'est gratuit dans mon travail!",
     "Nothing is gratuitous in my work!",
     [(203, "rien n'est gratuit dans mon travail")], "The director defends his vision"),
    ("beatrice", "Trouve une autre idée sans me déshabiller!",
     "Find another idea without undressing me!",
     [(206, "ce soit troublant")], "Beatrice challenges his creativity"),
    ("lea", "Regardons ce qui est écrit dans le scénario.",
     "Let's look at what is written in the script.",
     [(212, "qu'est-ce qu'il y a dans le scénario ?")], "Andrea turns to the text"),
    ("lea", "Le personnage découvre seulement son visage.",
     "The character only discovers her face.",
     [(214, "il découvre son visage")], "Andrea reads the stage directions"),
    ("lea", "C'est écrit ici, seulement son visage!",
     "It is written here, only her face!",
     [(215, "C'est écrit, là, son visage !")], "Andrea underlines the wording"),
    ("realisateur", "Un scénario est fait pour être détruit!",
     "A script is made to be destroyed!",
     [(217, "Un scénario, c'est fait pour être détruit")], "The director dismisses the page"),
    ("lea", "Un contrat se signe sur un scénario!",
     "A contract is signed based on a script!",
     [(219, "un contrat, ça se signe sur un scénario")], "Andrea enforces contractual law"),
    ("beatrice", "Tu es la meilleure, mon agente préférée!",
     "You are the best, my favorite agent!",
     [(224, "T'es la meilleure, ma chérie")], "Beatrice thanks Andrea warmly"),
]

OPENER = "Let's explore how Andrea defends Beatrice against an aggressive director line by line."

WALK = [
    (0, None,
     "'I am asking you to be naked here.' The director insists on shooting a full frontal nudity scene. Notice how the short vowel drops before a vowel sound around 'ask', making the phrase flow smoothly as one unit."),
    (1, None,
     "'No, I cannot do that!' Beatrice firmly refuses to strip down for the scene. Dropping the subject pronoun turns the verb for 'can' into a direct, punchy command."),
    (2, None,
     "'You will be magnificent, trust me!' The director attempts to flatter the actress into complying. the director uses the casual singular 'you' with 'will be', showing close familiarity."),
    (3, None,
     "'I refuse to be a slab of meat!' Beatrice compares the proposed autopsy scene to cheap exploitation. Notice how the short vowel drops before a vowel sound around 'refuse', making the phrase flow smoothly as one unit."),
    (4, None,
     "'This scene seems a little gratuitous to her.' Andrea steps in diplomatically to defend her client's dignity. Notice how 'seems' leads directly into the noun meaning 'scene'."),
    (5, None,
     "'Nothing is gratuitous in my work!' The director aggressively defends his artistic choices. In spoken French, the little word before 'work!' drops its final vowel and attaches with an apostrophe."),
    (6, None,
     "'Find another idea without undressing me!' Beatrice demands creative visual solutions that preserve her boundaries. The verb meaning 'find' pairs naturally with the noun for 'idea' in everyday conversation."),
    (7, None,
     "'Let's look at what is written in the script.' Andrea checks the official written screenplay for guidance. Notice how 'let's look' leads directly into the noun meaning 'script.'."),
    (8, None,
     "'The character only discovers her face.' Andrea points out that the text mentions only facial framing. Notice how 'discovers' leads directly into the noun meaning 'character'."),
    (9, None,
     "'It is written here, only her face!' Andrea underlines the exact scripted instructions to the director. The verb meaning 'it is' pairs naturally with the noun for 'face!' in everyday conversation."),
    (10, None,
     "'A script is made to be destroyed!' The director claims artistic license to change agreed terms. Dropping the subject pronoun turns the verb for 'made' into a direct, punchy command."),
    (11, None,
     "'A contract is signed based on a script!' Andrea counters with firm legal and contractual reality. The reflexive pronoun sits right in front of the verb for 'is signed', turning the action back onto the subject."),
    (12, None,
     "'You are the best, my favorite agent!' Beatrice expresses deep gratitude to Andrea for protecting her. The key noun here means 'agent', anchored by its matching French article."),
]

TRANSITION = "Now let's listen to the on-set showdown once more from beginning to end."

OUTRO = ("Andrea steps up to defend Beatrice Dalle's artistic autonomy and enforce contractual agreements on set. "
         "Let's review the key cinema and negotiation vocabulary from this scene.")

CLOSING = ("beatrice", "Tu es la meilleure, mon agente préférée!")
