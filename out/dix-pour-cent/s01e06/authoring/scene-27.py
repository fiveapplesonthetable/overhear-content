# Authoring module for dix-pour-cent s01e06 scene 27 (cues 692-719).
# Build: python3 tools/compose.py out/dix-pour-cent/s01e06/authoring/scene-27.py --out out/dix-pour-cent/s01e06/scene-27.json

ID = "dix-pour-cent-s01e06-scene-27"
SHOW = "dix-pour-cent"
SEASON = 1
EPISODE = 6
SCENE = 27
TITLE = "Le verdict du contrôle fiscal  (The Tax Audit Verdict)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "mathias": "theo", "gabriel": "marcel"}
LABELS = {"lea": "Colette", "mathias": "Mathias", "gabriel": "Gabriel"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S01E06"
SOURCE_FILE = "sources/dix-pour-cent/s01/e06.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 692-719. Colette Brancillon delivers the conclusions of her tax audit to the ASK "
    "partners in the conference room. Long legal clauses in cues 696-706 and 715-717 are simplified for A1."
)

INTRO = (
    "After three days of silence following her breakup with Andrea, tax inspector Colette Brancillon "
    "has returned to ASK, walking straight past Andrea into the conference room. Now Colette stands "
    "before Mathias, Andrea, Gabriel, Arlette, and Helene Kerr to announce the verdict of her tax audit. "
    "Listen to the French first, without worrying about catching every word."
)

STORY = [
    ("lea", "Bonjour à tous.",
     "Hello, everyone.",
     [(692, "Bonjour à tous")], ""),
    ("mathias", "Bonjour.",
     "Hello.",
     [(693, "Bonjour")], ""),
    ("lea", "Quand je suis arrivée, vous veniez de perdre votre patron. Je suis désolée.",
     "When I arrived, you had just lost your boss. I'm sorry.",
     [(694, "Quand je suis arrivée"), (695, "vous veniez de perdre votre patron. Je suis désolée")], ""),
    ("lea", "Mais la loi est la loi.",
     "But the law is the law.",
     [(696, "Mais la loi est la loi")], "'Elle ne connaît ni le deuil ni la peine' omitted for A1"),
    ("lea", "Une entreprise n'est pas une famille. Il y a des lois.",
     "A company is not a family. There are laws.",
     [(697, "Une entreprise n'est pas une famille"), (698, "Il y a des lois")], "'où l'on invente ses propres règles' omitted for A1"),
    ("lea", "Vous confondez vie privée et vie professionnelle.",
     "You confuse private life and professional life.",
     [(700, "Vous confondez vie privée et vie professionnelle")], ""),
    ("lea", "Il y aura une amende à payer, et vous irez au tribunal de commerce.",
     "There will be a fine to pay, and you will go to commercial court.",
     [(703, "Il y aura une amende à payer"), (704, "tribunal de commerce")], "'serez également convoqués au' -> 'irez au' for A1"),
    ("mathias", "Pourquoi le tribunal?",
     "Why the court?",
     [(708, "Pourquoi le tribunal")], ""),
    ("lea", "L'entreprise a payé une chambre d'hôtel privée pendant dix ans.",
     "The company paid for a private hotel room for ten years.",
     [(709, "L'entreprise a payé une chambre d'hôtel privée pendant dix ans")], ""),
    ("lea", "Les femmes de ménage et les vacances étaient payées avec l'argent de l'agence.",
     "The cleaners and the vacations were paid for with the agency's money.",
     [(710, "Les femmes de ménage et les vacances étaient payées avec l'argent de l'agence")], ""),
    ("lea", "Certains ont même acheté des chaussettes avec l'argent de la société!",
     "Some people even bought socks with the company's money!",
     [(713, "Certains ont même acheté des chaussettes avec l'argent de la société")], ""),
    ("gabriel", "C'est différent. C'était un festival dans les Alpes, j'avais les pieds gelés!",
     "That's different. It was a festival in the Alps, my feet were freezing!",
     [(714, "C'est différent"), (715, "C'était un festival dans les Alpes, j'avais les pieds gelés")], "credit-card PIN clause in cue 716 omitted for A1"),
    ("lea", "C'est un délit. Désolée. Au revoir.",
     "It's an offense. Sorry. Goodbye.",
     [(718, "C'est un délit. Désolée"), (719, "Au revoir")], "legal term 'abus de biens sociaux' in cue 717 omitted for A1"),
]

OPENER = "Let's walk through the scene line by line. Colette greets the partners in the conference room."

WALK = [
    (0, None,
     "'Hello, everyone.' Literally 'Good day to all.'"),
    (1, None,
     "'Hello.' Mathias answers politely, bracing for the report."),
    (2, None,
     "'When I arrived, you had just lost your boss. I'm sorry.' Because Colette is a woman, the past participle 'arrived' takes an extra silent 'e'."),
    (3, None,
     "'But the law is the law.' Colette makes it clear that grief does not excuse breaking tax rules."),
    (4, None,
     "'A company is not a family. There are laws.' The fixed expression 'there is' or 'there are' is used for both singular and plural nouns."),
    (5, None,
     "'You confuse private life and professional life.' Notice how both adjectives come after the feminine noun 'life'."),
    (6, None,
     "'There will be a fine to pay, and you will go to commercial court.' The future form 'there will be' introduces the penalty."),
    (7, None,
     "'Why the court?' Mathias is stunned that the audit is going beyond a simple tax bill."),
    (8, None,
     "'The company paid for a private hotel room for ten years.' Samuel Kerr lived in a luxury hotel at the agency's expense."),
    (9, None,
     "'The cleaners and the vacations were paid for with the agency's money.' The partners treated the company bank account like their personal wallet."),
    (10, None,
     "'Some people even bought socks with the company's money!' The word for 'even' sits between the helper verb and the past participle."),
    (11, None,
     "'That's different. It was a festival in the Alps, my feet were freezing!' Gabriel tries to defend his ski-festival socks."),
    (12, None,
     "'It's an offense. Sorry. Goodbye.' Colette closes her file and walks out without looking at Andrea."),
]

TRANSITION = "Now let's listen to the whole scene again from start to finish."

OUTRO = (
    "Colette leaves the partners reeling from the news of a heavy fine and a commercial court summons. "
    "Next, Helene Kerr demands to know how ASK will survive the audit. See you there."
)
CLOSING = ("lea", "Mais la loi est la loi.")
