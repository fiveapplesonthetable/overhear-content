# Authoring module for dix-pour-cent s03e01 scene 12 (cues 293-305).
# Build: python3 tools/compose.py out/dix-pour-cent/s03e01/authoring/scene-12.py --out out/dix-pour-cent/s03e01/scene-12.json

ID = "dix-pour-cent-s03e01-scene-12"
SHOW = "dix-pour-cent"
SEASON = 3
EPISODE = 1
SCENE = 12
TITLE = "L'homme des bois  (The Wild Man)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "theo": "theo"}
LABELS = {"lea": "Andréa", "theo": "Jean"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S03E01"
SOURCE_FILE = "sources/dix-pour-cent/s03/e01.fr.dual.srt"
SOURCE_NOTE = ("Cues 293-305. In the garden of his country estate, Andréa finds client Jean Dujardin living wild, "
               "refusing modern hygiene, and observing circling birds of prey. Adapted for A1 French.")

INTRO = ("Andrea visits the estate of star client Jean Dujardin after his family raises urgent concerns. "
         "Still deeply immersed in his wilderness movie role, Jean is camping outside in the woods and refusing all modern comforts. "
         "Let's listen to their conversation in French first.")

STORY = [
 ("lea", "Jean? Tu es là?",
  "Jean? Are you there?",
  [(293, "Jean ?")], "Adapted query"),
 ("theo", "Hein? Eh, Andréa!",
  "Huh? Hey, Andrea!",
  [(294, "Hein ?"), (295, "Eh, Andréa !")], ""),
 ("theo", "Il ne fallait pas te déplacer.",
  "You should not have traveled out here.",
  [(296, "Fallait pas te déplacer,")], "Adapted formal negative"),
 ("lea", "Mais il y a une vraie urgence pour toi!",
  "But there is a real emergency for you!",
  [(297, "il y a urgence, là,")], ""),
 ("lea", "Tu as besoin d'une douche immédiatement.",
  "You need a shower immediately.",
  [(297, "douche, pressing,")], "Adapted direct request"),
 ("theo", "Oui, c'est ce que me dit ma femme aussi.",
  "Yes, that is what my wife tells me too.",
  [(298, "c'est ce que me dit ma femme, aussi,")], ""),
 ("theo", "Ne t'inquiète pas, ce n'est pas grave.",
  "Do not worry, it is not serious.",
  [(299, "T'inquiète pas, c'est pas grave.")], "Adapted negative"),
 ("theo", "C'est l'odeur naturelle de la terre.",
  "It is the natural smell of the earth.",
  [(300, "C'est l'odeur de la terre,")], "Adapted explanation"),
 ("lea", "Non, c'est plutôt une odeur de putréfaction.",
  "No, it is rather a smell of putrefaction.",
  [(301, "De la putréfaction.")], "Adapted response"),
 ("theo", "Vous vivez dans un monde tellement aseptisé!",
  "You live in such a sanitized world!",
  [(302, "Vous vivez dans un monde qui est tellement aseptisé,")], ""),
 ("theo", "Regarde là-haut, c'est une buse.",
  "Look up there, that is a buzzard.",
  [(303, "Ça, c'est une buse,")], "Adapted sighting"),
 ("theo", "Tu vois comme elle tourne en rond?",
  "Do you see how it circles around?",
  [(304, "Tu vois, elle tourne autour.")], "Adapted observation"),
 ("theo", "Elle vient pour me voler quelque chose.",
  "It is coming to steal something from me.",
  [(305, "Elle vient me chourer,")], "Adapted explanation"),
 ("lea", "Jean, tu as un rendez-vous important demain.",
  "Jean, you have an important meeting tomorrow.",
  [(297, "il y a urgence, là,")], "Adapted reminder"),
 ("theo", "Ici, je me sens libre et vivant.",
  "Here, I feel free and alive.",
  [(300, "C'est l'odeur de la terre,")], "Adapted philosophy"),
 ("lea", "Tu dois redevenir un acteur maintenant.",
  "You must become an actor again now.",
  [(296, "je suis passé à l'agence.")], "Adapted closing"),
]

OPENER = "Let's explore the conversation line by line and unpack the French phrases."

WALK = [
 (0, None,
  "'Jean? Are you there?' Andrea calls out into the dense garden foliage. "
  "The brief question 'tu es la' checks for physical presence."),
 (1, None,
  "'Huh? Hey, Andrea!' Jean emerges abruptly from the undergrowth. "
  "The colloquial interjection 'hein' indicates sudden surprise."),
 (2, None,
  "'You should not have traveled out here.' Jean minimizes the necessity of her visit. "
  "The imperfect 'fallait pas' frames an unnecessary effort."),
 (3, None,
  "'But there is a real emergency for you!' Andrea highlights the critical situation. "
  "The noun phrase 'une vraie urgence' signals immediate crisis."),
 (4, None,
  "'You need a shower immediately.' Andrea points bluntly to his neglected hygiene. "
  "The idiom 'avoir besoin de' expresses pressing personal necessity."),
 (5, None,
  "'Yes, that is what my wife tells me too.' Jean concedes his family's complaints. "
  "The relative clause 'ce que me dit' reports third-party opinions."),
 (6, None,
  "'Do not worry, it is not serious.' Jean brushes aside her sanitary concerns. "
  "The negative phrase 'c'est pas grave' downplays the issue."),
 (7, None,
  "'It is the natural smell of the earth.' Jean romanticizes his outdoor grime. "
  "The noun 'odeur' refers to sensory atmospheric scent."),
 (8, None,
  "'No, it is rather a smell of putrefaction.' Andrea counters with brutal honesty. "
  "The visceral noun 'putrefaction' describes organic decay."),
 (9, None,
  "'You live in such a sanitized world!' Jean criticizes artificial modern comfort. "
  "The past participle 'aseptise' describes an excessively clean environment."),
 (10, None,
  "'Look up there, that is a buzzard.' Jean spots a bird of prey overhead. "
  "The feminine noun 'buse' denotes a wild predatory hawk."),
 (11, None,
  "'Do you see how it circles around?' Jean interprets the raptor's flight path. "
  "The phrase 'tourne en rond' describes circular hovering."),
 (12, None,
  "'It is coming to steal something from me.' Jean projects paranoia onto the bird. "
  "The motion structure 'vient pour voler' expresses intended action."),
 (13, None,
  "'Jean, you have an important meeting tomorrow.' Andrea tries to anchor him in reality. "
  "The noun phrase 'rendez-vous important' reminds him of work duties."),
 (14, None,
  "'Here, I feel free and alive.' Jean defends his primitive outdoor lifestyle. "
  "The adjective pair 'libre et vivant' celebrates emotional liberation."),
 (15, None,
  "'You must become an actor again now.' Andrea delivers her firm managerial verdict. "
  "The modal verb 'dois redevenir' demands a return to civilized professional life."),
]

TRANSITION = "Now let's listen to the entire dialogue once more to lock in what you have learned."

OUTRO = ("Andrea tracks down Jean Dujardin camping outside in his garden. "
         "Totally absorbed in his wilderness persona, Jean resists returning to civilized life until Andrea insists on his career.")
CLOSING = ("lea", "Tu dois redevenir un acteur maintenant.")
