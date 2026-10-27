# Authoring module for dix-pour-cent s03e02 scene 12 (cues 678-734).
# Build: python3 tools/compose.py overhear-content/out/dix-pour-cent/s03e02/authoring/scene-12.py --out overhear-content/out/dix-pour-cent/s03e02/scene-12.json

ID = "dix-pour-cent-s03e02-scene-12"
SHOW = "dix-pour-cent"
SEASON = 3
EPISODE = 2
SCENE = 12
TITLE = "Le dîner de coparentalité  (The Coparenting Dinner)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "hicham": "marcel", "colette": "emilie"}
LABELS = {"lea": "Andréa", "hicham": "Hicham", "colette": "Colette"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S03E02"
SOURCE_FILE = "sources/dix-pour-cent/s03/e02.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 678-734. Over a gastronomic dinner, Hicham announces to Andrea and Colette that he intends "
    "to officially recognize their unborn baby, destroying Colette's legal adoption hopes."
)

INTRO = (
    "At a luxury restaurant dinner, Hicham drops an emotional bombshell on Andrea and Colette by announcing that he wants to be named as the legal father on the birth certificate. "
    "The sudden demand threatens Colette's future parental rights. "
    "Listen to the scene in French first."
)

STORY = [
    ("hicham", "J'aimerais que cette fille connaisse son histoire.",
     "I would like this girl to know her history.",
     [(711, "connaisse son histoire")], ""),
    ("lea", "Oui, bien sûr, nous sommes d'accord.",
     "Yes, of course, we agree.",
     [(712, "Oui, bien sûr"), (714, "On est d'accord")], ""),
    ("hicham", "L'histoire, c'est que je suis son père.",
     "The story is that I am her father.",
     [(714, "je suis son père")], ""),
    ("lea", "C'est une petite partie de l'histoire.",
     "That is a small part of the story.",
     [(715, "petite partie de l'histoire")], ""),
    ("hicham", "Sans moi, il n'y a pas d'histoire.",
     "Without me, there is no story.",
     [(716, "Sans moi")], ""),
    ("hicham", "Donc, je voudrais la reconnaître officiellement.",
     "So, I would like to officially recognize her.",
     [(717, "reconnaître officiellement")], ""),
    ("lea", "Ce n'est pas ce qu'on avait décidé!",
     "That is not what we had decided!",
     [(718, "ce qu'on avait décidé")], ""),
    ("hicham", "Peut-être, mais c'est mon droit légal.",
     "Maybe, but it is my legal right.",
     [(719, "c'est mon droit")], ""),
    ("colette", "Si tu deviens officiellement le père du bébé,",
     "If you officially become the baby's father,",
     [(720, "officiellement le père de ce bébé")], ""),
    ("colette", "je ne serai jamais vraiment sa mère.",
     "I will never really be her mother.",
     [(721, "jamais vraiment sa mère")], ""),
    ("colette", "L'adoption plénière ne sera plus possible.",
     "Full adoption will no longer be possible.",
     [(722, "l'adoption plénière sera plus jamais possible")], ""),
    ("hicham", "Tu pourras faire une adoption simple.",
     "You can still do a simple adoption.",
     [(723, "faire une adoption simple")], ""),
    ("colette", "Mais ce sera révocable avec ton consentement!",
     "But that would be revocable with your consent!",
     [(724, "avec ton consentement")], ""),
    ("lea", "Sans Colette, je n'aurais jamais gardé l'enfant.",
     "Without Colette, I would never have kept the child.",
     [(726, "Sans Colette")], ""),
    ("colette", "Parce que moi, je ne peux pas en avoir.",
     "Because I cannot have children myself.",
     [(733, "Pourquoi t'en fais pas un"), (734, "je peux pas en avoir")], "")
]

OPENER = "Let's walk through the conversation step by step."

WALK = [
    (0, None,
     "'I would like this girl to know her history.' Hicham explains his paternal perspective. "
     "The conditional verb expresses personal yearning."),
    (1, None,
     "'Yes, of course, we agree.' Andrea politely acknowledges biological reality. "
     "The idiomatic phrase indicates shared baseline understanding."),
    (2, None,
     "'The story is that I am her father.' Hicham firmly asserts his biological parenthood. "
     "The copular clause identifies his central role."),
    (3, None,
     "'That is a small part of the story.' Andrea downplays his role in daily parenting. "
     "The noun phrase qualifies the scope of his involvement."),
    (4, None,
     "'Without me, there is no story.' Hicham claims ultimate credit for the conception. "
     "The prepositional phrase stresses his indispensability."),
    (5, None,
     "'So, I would like to officially recognize her.' He declares his intent to claim paternity. "
     "The adverb highlights formal civil registration."),
    (6, None,
     "'That is not what we had decided!' Andrea reacts with shock at his broken promise. "
     "The relative clause recalls their original verbal pact."),
    (7, None,
     "'Maybe, but it is my legal right.' Hicham stands firm on statutory paternity entitlements. "
     "The possessive noun phrase emphasizes legal standing."),
    (8, None,
     "'If you officially become the baby's father,' Colette begins her emotional counterargument. "
     "The conditional clause sets up the legal consequence."),
    (9, None,
     "'I will never really be her mother.' Colette fears losing all maternal recognition. "
     "The negative future verb underscores total exclusion."),
    (10, None,
     "'Full adoption will no longer be possible.' She points out the strict legal obstacle. "
     "The legal terminology defines irrevocable parentage."),
    (11, None,
     "'You can still do a simple adoption.' Hicham suggests a lesser legal compromise. "
     "The modal future verb offers an alternative procedure."),
    (12, None,
     "'But that would be revocable with your consent!' Colette rejects second-rate maternal status. "
     "The conditional clause exposes precarious dependency."),
    (13, None,
     "'Without Colette, I would never have kept the child.' Andrea defends her partner unconditionally. "
     "The past conditional construction expresses profound loyalty."),
    (14, None,
     "'Because I cannot have children myself.' Colette reveals her painful biological infertility. "
     "The negative modal verb silences the table in grief.")
]

TRANSITION = "Now listen to the whole scene again at normal speed, and see how much more you catch."

OUTRO = (
    "A tense dinner turns into an emotional crisis as Hicham's paternity ambitions clash with Colette and Andrea's family plans. "
    "Listen to the conversation once more in French."
)

CLOSING = ("lea", "Ce dîner est un désastre complet.")
