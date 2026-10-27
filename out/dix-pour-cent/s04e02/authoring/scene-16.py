# Authoring module for dix-pour-cent s04e02 scene 16 (cues 837-843).
# Build: python3 tools/compose.py overhear-content/out/dix-pour-cent/s04e02/authoring/scene-16.py --out overhear-content/out/dix-pour-cent/s04e02/scene-16.json

ID = "dix-pour-cent-s04e02-scene-16"
SHOW = "dix-pour-cent"
SEASON = 4
EPISODE = 2
SCENE = 16
TITLE = "Pardon pour mon agent  (Apology for My Agent)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "dylan": "theo"}
LABELS = {"lea": "Franck", "dylan": "Dylan"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S04E02"
SOURCE_FILE = "sources/dix-pour-cent/s04/e02.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 837-843. Outside the community center, Franck Dubosc apologizes for Gabriel's "
    "clumsy intervention, explaining why he values his agent while gently challenging Dylan "
    "about his secret visit to a speech therapist."
)

INTRO = (
    "Outside the community center, Franck Dubosc apologizes to young Dylan for Gabriel's aggressive meddling. "
    "Explaining why he remains loyal to his clumsy agent, Franck gently questions Dylan about his secret sessions with a speech therapist. "
    "Let's listen to their conversation in French first."
)

OPENER = "Let's examine the conversation line by line and explore the French expressions."
TRANSITION = "Now let's listen to the complete discussion once more to reinforce the vocabulary."

STORY = [
    ("lea", "Je suis désolé pour mon agent.",
     "I am sorry about my agent.",
     [(837, "Je suis désolé pour mon agent")], "Franck apologizes for Gabriel"),
    ("dylan", "Il est encore ton agent officiel?",
     "Is he still your official agent?",
     [(838, "Il est encore ton agent")], "Dylan is surprised"),
    ("lea", "Ouais, il reste toujours mon agent.",
     "Yeah, he still remains my agent.",
     [(839, "Ouais")], "Franck confirms his loyalty"),
    ("lea", "Je crois que je vais le garder.",
     "I think I will keep him.",
     [(840, "Je crois que je vais le garder")], "Franck stands by Gabriel"),
    ("dylan", "Après toutes ses bêtises récentes?",
     "After all his recent blunders?",
     [(838, "ton agent")], "Dylan questions the loyalty"),
    ("lea", "Il a fait une vraie erreur.",
     "He made a real mistake.",
     [(841, "Il a merdé")], "Franck acknowledges the mistake"),
    ("lea", "Mais il est très bien intentionné.",
     "But he means very well.",
     [(841, "il est bien intentionné")], "Franck emphasizes Gabriel's intentions"),
    ("lea", "Et il m'a redonné confiance.",
     "And he restored my confidence.",
     [(841, "il m'a redonné confiance")], "Franck shares his personal feeling"),
    ("dylan", "Comme si tu avais besoin de confiance!",
     "As if you needed confidence!",
     [(842, "Comme si t'avais besoin de confiance")], "Dylan scoffs at the idea"),
    ("dylan", "Tu es un acteur très célèbre.",
     "You are a very famous actor.",
     [(842, "besoin de confiance")], "Dylan notes Franck's stature"),
    ("lea", "Tout le monde doute parfois, Dylan.",
     "Everyone doubts sometimes, Dylan.",
     [(842, "besoin de confiance")], "Franck shares life wisdom"),
    ("lea", "Comme si tu avais besoin d'aide?",
     "As if you needed help?",
     [(843, "Comme si t'avais besoin")], "Franck turns the table"),
    ("lea", "Comme si tu avais besoin d'un orthophoniste?",
     "As if you needed a speech therapist?",
     [(843, "Comme si t'avais besoin d'un orthophoniste")], "Franck addresses Dylan's secret"),
    ("dylan", "Je ne pensais pas que tu savais.",
     "I did not think that you knew.",
     [(843, "un orthophoniste")], "Dylan is taken aback"),
]

WALK = [
    (0, None,
     "'I am sorry about my agent.' Franck apologizes for Gabriel's clumsy and confrontational behavior. "
     "The adjective 'desole' expresses regret."),
    (1, None,
     "'Is he still your official agent?' Dylan is astonished that Franck keeps Gabriel after the incident. "
     "The adverb 'encore' indicates continuity."),
    (2, None,
     "'Yeah, he still remains my agent.' Franck confirms his bond with Gabriel despite the recent drama. "
     "The colloquial affirmative 'ouais' means yeah."),
    (3, None,
     "'I think I will keep him.' Franck explains his decision to stand by Gabriel. "
     "The verb phrase 'vais le garder' uses the near future tense."),
    (4, None,
     "'After all his recent blunders?' Dylan questions the wisdom of keeping such a chaotic agent. "
     "The preposition 'apres' marks temporal succession."),
    (5, None,
     "'He made a real mistake.' Franck honestly admits that Gabriel made an embarrassing error. "
     "The noun 'erreur' designates a mistake or blunder."),
    (6, None,
     "'But he means very well.' Franck defends Gabriel's genuine heart and loyalty. "
     "The compound adjective 'bien intentionne' means well-intentioned."),
    (7, None,
     "'And he restored my confidence.' Franck reveals how much Gabriel supported him in moments of insecurity. "
     "The idiom 'redonner confiance' means to restore morale."),
    (8, None,
     "'As if you needed confidence!' Dylan scoffs at the thought of a major star feeling insecure. "
     "The conjunction 'comme si' introduces a hypothetical comparison."),
    (9, None,
     "'You are a very famous actor.' Dylan points out Franck's massive commercial popularity and success. "
     "The adjective 'celebre' describes public renown."),
    (10, None,
     "'Everyone doubts sometimes, Dylan.' Franck offers a vulnerable truth about the acting profession. "
     "The indefinite pronoun 'tout le monde' functions as singular."),
    (11, None,
     "'As if you needed help?' Franck gently probes whether Dylan also hides private struggles. "
     "The noun 'aide' denotes assistance or support."),
    (12, None,
     "'As if you needed a speech therapist?' Franck brings up the medical care sheet he discovered. "
     "The noun 'orthophoniste' refers to a speech therapist."),
    (13, None,
     "'I did not think that you knew.' Dylan admits his shock at having his private vulnerability uncovered. "
     "The imperfect tense 'pensais' indicates a past belief."),
]

OUTRO = (
    "Franck Dubosc reveals that beneath his popular star persona, he shares the same deep insecurities as young Dylan. "
    "By uncovering Dylan's visits to a speech therapist, Franck builds an unexpected bridge of empathy between two different generations of actors. "
    "Now let's listen to the scene one last time."
)

CLOSING = ("lea", "Ne t'inquiète pas, ton secret reste avec moi.")
