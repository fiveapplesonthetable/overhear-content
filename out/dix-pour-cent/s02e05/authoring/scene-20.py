# Authoring module for dix-pour-cent s02e05 scene 20 (cues 596-642).
# Build: python3 tools/compose.py out/dix-pour-cent/s02e05/authoring/scene-20.py --out out/dix-pour-cent/s02e05/scene-20.json

ID = "dix-pour-cent-s02e05-scene-20"
SHOW = "dix-pour-cent"
SEASON = 2
EPISODE = 5
SCENE = 20
TITLE = "La vente de l'appartement  (Showing the Apartment)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "mathias": "theo"}
LABELS = {"lea": "Noémie", "mathias": "Mathias"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S02E05"
SOURCE_FILE = "sources/dix-pour-cent/s02/e05.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 596-642. After prospective buyers complete their visit of Mathias's apartment, Noémie finds Mathias alone, "
    "emotionally drained and haunted by memories of his marriage. Noémie offers gentle comfort and encouragement."
)

INTRO = (
    "Following a visit by prospective buyers and estate agents, Mathias sits alone in his apartment, feeling overwhelmed. "
    "Noémie arrives and finds him drowning in nostalgia, offering him the comfort and strength he needs to carry on. "
    "Listen to the scene in French first."
)

STORY = [
    ("mathias", "La visite de l'appartement vient de se terminer.",
     "The apartment viewing has just finished.",
     [(596, "Monsieur Barneville ?"), (607, "Bon, on ne va pas vous déranger plus longtemps.")], ""),
    ("lea", "Comment s'est passée la visite avec les acheteurs?",
     "How did the visit go with the buyers?",
     [(600, "Madame et monsieur sont enchantés."), (602, "On aime vraiment l'ambiance.")], ""),
    ("mathias", "Ils ont adoré l'endroit et veulent faire une offre.",
     "They loved the place and want to make an offer.",
     [(603, "C'est exactement ce qu'on cherche."), (631, "Je crois qu'ils sont intéressés.")], ""),
    ("lea", "C'est une bonne nouvelle pour régler tes problèmes.",
     "It is good news to settle your problems.",
     [(632, "Tu m'avais dit que ça n'était pas un problème.")], ""),
    ("mathias", "Pourtant, je me sens complètement bouleversé.",
     "Yet, I feel completely overwhelmed.",
     [(624, "Non, c'est rien, c'est juste..."), (626, "Je suis arrivé pendant la visite.")], ""),
    ("lea", "Qu'est-ce qui te fait de la peine, Mathias?",
     "What is hurting you, Mathias?",
     [(621, "Qu'est-ce qui se passe ?"), (625, "Dis-moi, Mathias.")], ""),
    ("mathias", "Ce jeune couple me rappelle Catherine et moi avant.",
     "This young couple reminds me of Catherine and me in the past.",
     [(627, "Ils étaient jeunes et..."), (628, "Ils nous ressemblaient, avant.")], ""),
    ("mathias", "Nous étions tellement heureux dans cet appartement.",
     "We were so happy in this apartment.",
     [(604, "Vous étiez heureux ici ?"), (606, "Beaucoup.")], ""),
    ("lea", "Je comprends ta tristesse face à ce changement.",
     "I understand your sadness about this change.",
     [(633, "Tu es fatigué.")], ""),
    ("mathias", "Je n'en peux plus, tout devient trop difficile.",
     "I cannot take it anymore, everything is becoming too difficult.",
     [(634, "Je n'en peux plus, je n'y arrive plus.")], ""),
    ("lea", "Tu es courageux, tu vas surmonter cette épreuve.",
     "You are brave, you will overcome this trial.",
     [(635, "Si, tu peux.")], ""),
    ("mathias", "Mon père disait que la vie est une longue épreuve.",
     "My father used to say that life is a long trial.",
     [(636, "Mon père disait : « La vie, c'est une longue chierie. »")], ""),
    ("lea", "Ton père avait tort d'être aussi pessimiste.",
     "Your father was wrong to be so pessimistic.",
     [(637, "Excuse-moi, mais ton père était un connard.")], ""),
    ("mathias", "Peut-être, mais j'ai du mal à garder espoir.",
     "Maybe, but I have trouble keeping hope.",
     [(638, "C'est peut-être vrai. Peut-être..."), (640, "C'est trop dur.")], ""),
    ("lea", "Regarde-moi, Mathias. Tu n'es pas tout seul.",
     "Look at me, Mathias. You are not alone.",
     [(641, "Chéri.")], ""),
    ("lea", "Je suis là avec toi, nous réussirons ensemble.",
     "I am here with you, we will succeed together.",
     [(642, "Chéri.")], "")
]

OPENER = "Let's examine how Noémie comforts a grieving and overwhelmed Mathias."

WALK = [
    (0, None,
     "'The apartment viewing has just finished.' Mathias speaks with weary relief. "
     "The construction vient de se terminer expresses recent completion."),
    (1, None,
     "'How did the visit go with the buyers?' Noémie inquires with caring interest. "
     "The masculine plural noun acheteurs refers to property buyers."),
    (2, None,
     "'They loved the place and want to make an offer.' Mathias reports their positive reaction. "
     "The noun phrase faire une offre means to make an offer."),
    (3, None,
     "'It is good news to settle your problems.' Noémie tries to highlight the positive aspect. "
     "The feminine noun locution bonne nouvelle means good news."),
    (4, None,
     "'Yet, I feel completely overwhelmed.' Mathias shares his internal emotional turmoil. "
     "The past participle bouleversé means shaken or overwhelmed."),
    (5, None,
     "'What is hurting you, Mathias?' Noémie gently probes the cause of his sadness. "
     "The idiom faire de la peine means to cause grief or sorrow."),
    (6, None,
     "'This young couple reminds me of Catherine and me in the past.' Mathias is haunted by nostalgia. "
     "The verb rappelle means reminds or recalls."),
    (7, None,
     "'We were so happy in this apartment.' Mathias looks back on happier years. "
     "The imperfect étions expresses a past ongoing state."),
    (8, None,
     "'I understand your sadness about this change.' Noémie shows deep empathy for his pain. "
     "The prepositional locution face à means in the face of."),
    (9, None,
     "'I cannot take it anymore, everything is becoming too difficult.' Mathias admits his exhaustion. "
     "The verbal idiom n'en pouvoir plus means to be at one's limit."),
    (10, None,
     "'You are brave, you will overcome this trial.' Noémie offers steadfast reassurance. "
     "The infinitive surmonter means to overcome."),
    (11, None,
     "'My father used to say that life is a long trial.' Mathias recalls a somber family proverb. "
     "The imperfect disait introduces past speech."),
    (12, None,
     "'Your father was wrong to be so pessimistic.' Noémie rejects the cynical worldview. "
     "The idiom avoir tort de means to be wrong to do something."),
    (13, None,
     "'Maybe, but I have trouble keeping hope.' Mathias struggles against despair. "
     "The expression avoir du mal à means to find it difficult to."),
    (14, None,
     "'Look at me, Mathias. You are not alone.' Noémie reminds him of her loyal presence. "
     "The adjective seul means alone."),
    (15, None,
     "'I am here with you, we will succeed together.' Noémie promises her loving support. "
     "The simple future réussirons conveys determination.")
]

TRANSITION = "Now let's listen to the emotional conversation once more at normal pace."

OUTRO = (
    "In the empty apartment, Noémie gives Mathias the warmth and courage he needs to face the future. "
    "Listen to the poignant conversation once more in French."
)

CLOSING = ("lea", "Je suis là avec toi, nous réussirons ensemble.")
