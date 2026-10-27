# Authoring module for dix-pour-cent s02e01 scene 25 (cues 763-780).
# Build: python3 tools/compose.py out/dix-pour-cent/s02e01/authoring/scene-25.py --out out/dix-pour-cent/s02e01/scene-25.json

ID = "dix-pour-cent-s02e01-scene-25"
SHOW = "dix-pour-cent"
SEASON = 2
EPISODE = 1
SCENE = 25
TITLE = "La trahison dévoilée  (The Betrayal Revealed)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "gabriel": "theo"}
LABELS = {"lea": "Virginie", "gabriel": "Gabriel"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S02E01"
SOURCE_FILE = "sources/dix-pour-cent/s02/e01.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 763-780. At a Parisian cafe, Gabriel meets Virginie Efira after their director fails to show up. "
    "Gabriel seizes the moment to expose Mathias's deceit: Mathias created a secret contract that paid Ramzy "
    "far more than Virginie. Adapted for A1 French."
)

INTRO = (
    "At a Parisian cafe terrace, Gabriel meets actress Virginie Efira while waiting for their director. "
    "When the director stands them up, Gabriel decides to reveal an uncomfortable truth about Mathias. "
    "Let's listen to the scene in French first."
)

STORY = [
    ("gabriel", "Il ne vient pas?",
     "Is he not coming?",
     [(763, "Il ne vient pas ?")], ""),
    ("lea", "Il est où, ton réalisateur?",
     "Where is your director?",
     [(764, "Il est où, ton réalisateur ?")], ""),
    ("gabriel", "Il nous a posé un lapin.",
     "He stood us up.",
     [(765, "il nous a posé un lapin.")], ""),
    ("gabriel", "Comment ça se passe avec Mathias?",
     "How are things going with Mathias?",
     [(766, "Comment ça se passe avec Mathias Barneville ?")], "Shortened Mathias Barneville"),
    ("lea", "Si tu veux critiquer mon agent, laisse tomber.",
     "If you want to criticize my agent, drop it.",
     [(767, "Si tu es là pour descendre mon agent, laisse tomber.")], "Replaced descendre with critiquer"),
    ("lea", "De quoi il s'agit?",
     "What is this about?",
     [(768, "De quoi il s'agit ?")], ""),
    ("gabriel", "Tu mérites des gens de ton côté.",
     "You deserve people on your side.",
     [(769, "tu mérites de travailler"), (770, "avec des gens qui sont de ton côté.")], "Shortened line"),
    ("lea", "Bien sûr. Merci pour le café.",
     "Of course. Thanks for the coffee.",
     [(771, "Bien sûr. Merci pour le café.")], ""),
    ("gabriel", "Je vais faire simple. Ramzy te ment.",
     "I will keep it simple. Ramzy is lying to you.",
     [(772, "je vais faire vite et simple. Ramzy te ment.")], "Shortened phrase"),
    ("gabriel", "Mathias aussi. Il te manipule.",
     "Mathias too. He is manipulating you.",
     [(773, "Mathias aussi. En plus, il te manipule.")], "Shortened sentence"),
    ("gabriel", "Vous n'avez pas touché le même salaire.",
     "You did not receive the same fee.",
     [(774, "n'avez pas touché le même cachet.")], "Simplified cachet to salaire"),
    ("gabriel", "Loin de là.",
     "Far from it.",
     [(775, "Loin de là.")], ""),
    ("lea", "C'est pathétique.",
     "This is pathetic.",
     [(776, "C'est pathétique.")], ""),
    ("gabriel", "J'ai lu le contrat de Ramzy.",
     "I read Ramzy's contract.",
     [(777, "J'ai lu le contrat de Ramzy.")], ""),
    ("gabriel", "Il y a un autre contrat secret.",
     "There is another secret contract.",
     [(778, "Il y en a un autre.")], "Clarified secret contract"),
    ("gabriel", "Tu veux le voir?",
     "Do you want to see it?",
     [(780, "Tu veux le voir ?")], ""),
]

OPENER = "Let's examine how Gabriel reveals Mathias's secret betrayal to Virginie."

WALK = [
    (0, None,
     "'Is he not coming?' A negative question using the verb venir."),
    (1, None,
     "'Where is your director?' A familiar question putting the interrogative adverb in final position."),
    (2, None,
     "'He stood us up.' An idiom meaning to stand someone up."),
    (3, None,
     "'How are things going with Mathias?' The reflexive verb se passer asking how things unfold."),
    (4, None,
     "'If you want to criticize my agent, drop it.' An imperative idiom telling someone to let it go."),
    (5, None,
     "'What is this about?' An impersonal phrase asking about the subject matter."),
    (6, None,
     "'You deserve people on your side.' The verb meriter expressing what someone is entitled to."),
    (7, None,
     "'Of course. Thanks for the coffee.' A polite formula before leaving."),
    (8, None,
     "'I will keep it simple. Ramzy is lying to you.' The verb mentir in the present tense."),
    (9, None,
     "'Mathias too. He is manipulating you.' The direct object pronoun placed before the verb."),
    (10, None,
     "'You did not receive the same fee.' The past tense of toucher meaning to receive money."),
    (11, None,
     "'Far from it.' An adverbial phrase expressing a wide difference."),
    (12, None,
     "'This is pathetic.' An evaluative adjective expressing disbelief."),
    (13, None,
     "'I read Ramzy's contract.' The compound past tense of the irregular verb lire."),
    (14, None,
     "'There is another secret contract.' The presentative phrase il y a."),
    (15, None,
     "'Do you want to see it?' The modal verb vouloir followed by the pronoun and infinitive."),
]

TRANSITION = "Now let's listen to the whole discussion again without stopping."

OUTRO = (
    "Gabriel has exposed the secret financial deal behind the film. "
    "Virginie now holds the proof of Mathias's betrayal and Ramzy's complicity."
)

CLOSING = ("lea", "Montre-moi ce contrat.")
