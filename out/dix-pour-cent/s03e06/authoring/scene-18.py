# Authoring module for dix-pour-cent s03e06 scene 18 (cues 915-977).
# Build: python3 tools/compose.py overhear-content/out/dix-pour-cent/s03e06/authoring/scene-18.py --out overhear-content/out/dix-pour-cent/s03e06/scene-18.json

ID = "dix-pour-cent-s03e06-scene-18"
SHOW = "dix-pour-cent"
SEASON = 3
EPISODE = 6
SCENE = 18
TITLE = "L'amie d'Hervé  (Hervé's Friend)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "herve": "theo", "corinne": "emilie"}
LABELS = {"lea": "Camille", "herve": "Hervé", "corinne": "Corinne"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S03E06"
SOURCE_FILE = "sources/dix-pour-cent/s03/e06.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 915-977. At the ASK anniversary party, Camille notices an eccentric woman in red speaking "
    "with all the stars. Hervé defends his friend Corinne, before panic breaks out when Isabelle Huppert goes missing."
)

INTRO = (
    "At ASK's thirtieth anniversary party, Camille spots an eccentric woman in a bright red dress chatting up all the agency's famous clients. "
    "Herve explains that the guest is his dear former friend Corinne, before news arrives that star client Isabelle Huppert has vanished. "
    "Listen to the scene in French first."
)

STORY = [
    ("lea", "Qui est cette femme en robe rouge?",
     "Who is that woman in a red dress?",
     [(915, "c'est qui la folle"), (917, "La dame en rouge")], ""),
    ("herve", "C'est une grande amie, Corinne.",
     "She is a great friend, Corinne.",
     [(918, "amie comédienne, Corinne")], ""),
    ("lea", "Pourquoi parle-t-elle à tous nos acteurs?",
     "Why is she talking to all our actors?",
     [(915, "parle à tous nos talents"), (919, "pourquoi elle est là")], ""),
    ("herve", "Elle a beaucoup compté pour moi.",
     "She meant a lot to me.",
     [(927, "beaucoup compté pour moi")], ""),
    ("herve", "Elle ne va pas très bien actuellement.",
     "She is not doing very well right now.",
     [(929, "elle va pas très fort")], ""),
    ("herve", "Je voulais lui présenter des invités sympathiques.",
     "I wanted to introduce her to nice guests.",
     [(930, "présenter des invités")], ""),
    ("lea", "D'accord, laisse-la profiter de la soirée.",
     "Alright, let her enjoy the party.",
     [(931, "tu la laisses tranquille")], ""),
    ("corinne", "Vous avez les yeux de Bella Darvy!",
     "You have the eyes of Bella Darvy!",
     [(938, "les yeux de Bella Darvy")], ""),
    ("lea", "Hervé, où est passée Isabelle Huppert?",
     "Hervé, where did Isabelle Huppert go?",
     [(950, "Elle est où, Isabelle")], ""),
    ("herve", "Je ne sais pas du tout où!",
     "I do not know at all where!",
     [(954, "je sais pas")], ""),
    ("lea", "Les producteurs américains sont déjà en bas.",
     "The American producers are already downstairs.",
     [(958, "Les Américains sont en bas")], ""),
    ("lea", "Et nous avons perdu notre grande star!",
     "And we have lost our big star!",
     [(959, "on a perdu Isabelle")], ""),
    ("herve", "Allons vite regarder sur la terrasse.",
     "Let us go check on the terrace quickly.",
     [(967, "sur la terrasse")], ""),
    ("lea", "Dépêchons-nous avant une catastrophe!",
     "Let us hurry before a disaster!",
     [(968, "Dépêche-toi")], "")
]

OPENER = "Let's walk through the conversation step by step."

WALK = [
    (0, None,
     "'Who is that woman in a red dress?' Camille notices an unfamiliar guest mingling boldly. "
     "The interrogative sentence points out her vibrant outfit."),
    (1, None,
     "'She is a great friend, Corinne.' Herve introduces his guest with fond loyalty. "
     "The warm noun phrase defends her presence."),
    (2, None,
     "'Why is she talking to all our actors?' Camille questions why the stranger is cornering VIP talent. "
     "The question displays professional anxiety."),
    (3, None,
     "'She meant a lot to me.' Herve explains her vital importance during his youth. "
     "The past tense expresses gratitude."),
    (4, None,
     "'She is not doing very well right now.' He admits his friend needs moral support. "
     "The negative sentence explains her vulnerability."),
    (5, None,
     "'I wanted to introduce her to nice guests.' He shares his kind intention for bringing her along. "
     "The imperfect tense softens his explanation."),
    (6, None,
     "'Alright, let her enjoy the party.' Camille softens and allows the guest to stay. "
     "The imperative verb grants permission."),
    (7, None,
     "'You have the eyes of Bella Darvy!' Corinne pays an eccentric compliment to a party guest. "
     "The dramatic reference creates humorous awkwardness."),
    (8, None,
     "'Hervé, where did Isabelle Huppert go?' Panic strikes as the guest of honor disappears. "
     "The direct question alerts her colleague."),
    (9, None,
     "'I do not know at all where!' Herve throws up his hands in confusion. "
     "The negative adverb underscores his cluelessness."),
    (10, None,
     "'The American producers are already downstairs.' Camille warns that important guests have arrived. "
     "The temporal adverb heightens the urgency."),
    (11, None,
     "'And we have lost our big star!' She laments the untimely disappearance of their leading lady. "
     "The past participle emphasizes the crisis."),
    (12, None,
     "'Let us go check on the terrace quickly.' Herve suggests a logical search location. "
     "The imperative verb initiates a search party."),
    (13, None,
     "'Let us hurry before a disaster!' Camille urges immediate action before chaos ensues. "
     "The prepositional phrase underlines the high stakes.")
]

TRANSITION = "Now listen to the whole scene again at normal speed, and see how much more you catch."

OUTRO = (
    "Between eccentric friends and missing film stars, ASK's anniversary party spirals into high-stakes comedic chaos. "
    "Listen to the conversation once more in French."
)

CLOSING = ("herve", "Cette fête est complètement folle.")
