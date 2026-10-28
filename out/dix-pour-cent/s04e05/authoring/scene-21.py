# Authoring module for dix-pour-cent s04e05 scene 21 (cues 807-833).
# Build: python3 tools/compose.py out/dix-pour-cent/s04e05/authoring/scene-21.py --out out/dix-pour-cent/s04e05/scene-21.json

ID = "dix-pour-cent-s04e05-scene-21"
SHOW = "dix-pour-cent"
SEASON = 4
EPISODE = 5
SCENE = 21
TITLE = "Une théorie du complot  (A Conspiracy Theory)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "gabriel": "theo"}
LABELS = {"lea": "Andrea", "gabriel": "Gabriel"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S04E05"
SOURCE_FILE = "sources/dix-pour-cent/s04/e05.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 807-833. Outside ASK, a frantic Gabriel corners Andrea with photographic proof that newly hired "
    "agent Elise Formain was secretly meeting StarMedia boss Brehier on a bridge. Though Andrea initially "
    "mocks his paranoia, Gabriel insists Elise is a double agent seeking to sabotage ASK."
)

INTRO = (
    "Outside the ASK offices, Gabriel frantically waits to pull Andrea aside after spotting her with dancer Rayane Bensetti. "
    "Armed with photos from tailing Elise Formain across Paris, Gabriel tries to convince a skeptical Andrea that their new partner is a traitor. "
    "Let's listen to their conversation in French first."
)

OPENER = "Let's examine the conversation line by line and explore the French expressions."
TRANSITION = "Now let's listen to the complete discussion once more to reinforce the vocabulary."

STORY = [
    ("gabriel", "Andréa, tu as reçu mes messages?",
     "Andréa, did you receive my messages?",
     [(819, "Andréa! Tu as eu mes messages?")], "Approached with urgent news"),
    ("lea", "J'étais avec Rayane Bensetti, Gabriel.",
     "I was with Rayane Bensetti, Gabriel.",
     [(808, "Rayane, ça va?"), (816, "Rayane Bensetti")], "Explained her delayed response"),
    ("gabriel", "On file Élise depuis deux jours.",
     "We have been tailing Élise for two days.",
     [(821, "On file Élise depuis deux jours")], "Revealed their secret surveillance"),
    ("lea", "Tu tombes dans une paranoïa totale!",
     "You are falling into complete paranoia!",
     [(823, "embarquer dans sa paranoïa")], "Dismissed his suspicious claims"),
    ("gabriel", "Elle rencontre toujours le patron Bréhier.",
     "She is still meeting the boss Bréhier.",
     [(825, "Elle voit toujours Bréhier")], "Pointed out her suspicious contact"),
    ("lea", "Ils discutent peut-être de simple paperasse.",
     "They are perhaps discussing simple paperwork.",
     [(826, "ils font de la paperasse")], "Suggested an innocent explanation"),
    ("gabriel", "De la paperasse sur un pont?",
     "Paperwork on a bridge?",
     [(827, "De la paperasse sur un pont?")], "Challenged the unlikely meeting place"),
    ("lea", "C'est ta collègue de travail maintenant.",
     "She is your work colleague now.",
     [(824, "c'est ta collègue")], "Reminded him of workplace solidarity"),
    ("gabriel", "Elle travaille toujours pour StarMédia, Andréa!",
     "She is still working for StarMédia, Andréa!",
     [(828, "n'a jamais rompu avec StarMédia")], "Insisted on her secret corporate loyalty"),
    ("lea", "C'est une belle théorie du complot.",
     "That is a fine conspiracy theory.",
     [(830, "belle petite théorie du complot")], "Mocked his elaborate theory"),
    ("gabriel", "Elle veut nous détruire de l'intérieur.",
     "She wants to destroy us from the inside.",
     [(829, "faire pression sur Bréhier")], "Warned of imminent sabotage"),
    ("lea", "Allons lui poser la question directement.",
     "Let us go ask her the question directly.",
     [(832, "allons lui demander directement")], "Proposed an immediate confrontation"),
    ("gabriel", "Elle ne va rien nous avouer.",
     "She is not going to confess anything to us.",
     [(831, "C'est pas une théorie")], "Doubted the rival agent would tell the truth"),
    ("lea", "Nous allons éclaircir cette affaire ensemble.",
     "We are going to clear up this matter together.",
     [(833, "reprendre le travail")], "Urged a swift end to office suspicions"),
]

WALK = [
    (0, None,
     "'Andrea, did you receive my messages?' Gabriel intercepts his colleague on the street. "
     "The compound past verb phrase 'as recu' opens the dialogue with urgency."),
    (1, None,
     "'I was with Rayane Bensetti, Gabriel.' Andrea justifies her busy afternoon. "
     "The imperfect verb 'etais' sets the background context."),
    (2, None,
     "'We have been tailing Elise for two days.' Gabriel reveals the shadow operation. "
     "The colloquial verb file conveys undercover surveillance."),
    (3, None,
     "'You are falling into complete paranoia!' Andrea scoffs at the cloak-and-dagger talk. "
     "The phrase 'paranoia totale' labels his behavior."),
    (4, None,
     "'She is still meeting the boss Brehier.' Gabriel offers hard proof of collusion. "
     "The adverb toujours highlights persistent disloyalty."),
    (5, None,
     "'They are perhaps discussing simple paperwork.' Andrea looks for a harmless rationale. "
     "The noun paperasse refers to mundane administrative files."),
    (6, None,
     "'Paperwork on a bridge?' Gabriel scoffs at the absurd excuse. "
     "The prepositional phrase sur un pont underlines the clandestine location."),
    (7, None,
     "'She is your work colleague now.' Andrea urges professional etiquette. "
     "The noun 'collegue' reminds him of her official status."),
    (8, None,
     "'She is still working for StarMedia, Andrea!' Gabriel refuses to let his guard down. "
     "The proper noun StarMedia names the rival powerhouse."),
    (9, None,
     "'That is a fine conspiracy theory.' Andrea brushes off his dramatic narrative. "
     "The phrase 'theorie du complot' diagnoses his overactive imagination."),
    (10, None,
     "'She wants to destroy us from the inside.' Gabriel warns of an undercover plot. "
     "The phrase 'de l'interieur' points to internal betrayal."),
    (11, None,
     "'Let us go ask her the question directly.' Andrea chooses a forthright solution. "
     "The imperative verb phrase allons lui poser decides on immediate action."),
    (12, None,
     "'She is not going to confess anything to us.' Gabriel warns that she will lie. "
     "The near future construction ne va rien avouer predicts deception."),
    (13, None,
     "'We are going to clear up this matter together.' Andrea wraps up the debate firmly. "
     "The infinitive 'eclaircir' promises absolute clarity."),
]

OUTRO = "Gabriel and Andrea walk into the agency lobby, determined to uncover the truth behind Elise's secret meetings. When you watch the episode, listen out for the expressions meaning 'received' and 'messages'. You'll catch them now. See you next time."
CLOSING = ("lea", "Nous allons éclaircir cette affaire ensemble.")
