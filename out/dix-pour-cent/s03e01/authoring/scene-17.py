# Authoring module for dix-pour-cent s03e01 scene 17 (cues 574-603).
# Build: python3 tools/compose.py out/dix-pour-cent/s03e01/authoring/scene-17.py --out out/dix-pour-cent/s03e01/scene-17.json

ID = "dix-pour-cent-s03e01-scene-17"
SHOW = "dix-pour-cent"
SEASON = 3
EPISODE = 1
SCENE = 17
TITLE = "Une salade de quinoa  (A Quinoa Salad)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "annick": "emilie"}
LABELS = {"lea": "Camille", "annick": "Annick"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S03E01"
SOURCE_FILE = "sources/dix-pour-cent/s03/e01.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 574-603. Late at night in their apartment, Annick worries about Camille working long hours, "
    "eating quinoa salad, and taking micro-naps on bathroom floors instead of resting properly."
)

INTRO = (
    "Late at night in their Paris apartment, Annick observes her daughter Camille working tirelessly. "
    "Camille reads scripts while eating a quick meal, trying to prove herself as a junior agent. "
    "Listen to their conversation in French first."
)

STORY = [
    ("lea", "C'est normal que ça prenne du temps.",
     "It is normal that it takes time.",
     [(576, "Non, mais c'est normal que ça prenne un peu de temps.")], ""),
    ("annick", "Personne ne se précipite dans ton bureau?",
     "Nobody is rushing to your office?",
     [(577, "Tout le monde se précipite pas encore dans mon bureau.")], ""),
    ("lea", "Je n'ai pas encore de bureau!",
     "I do not have an office yet!",
     [(578, "Peut-être parce que j'ai pas de bureau.")], ""),
    ("annick", "Tu es trop gentille pour ce milieu.",
     "You are too kind for this environment.",
     [(581, "tu es quelqu'un de bien dans ce milieu de fauves, là.")], ""),
    ("annick", "Et qu'est-ce que tu manges là?",
     "And what are you eating there?",
     [(583, "Qu'est-ce que tu manges ?")], ""),
    ("lea", "Je mange une salade de quinoa.",
     "I am eating a quinoa salad.",
     [(584, "Une taboulette quinoa.")], ""),
    ("annick", "Ils t'ont contaminée avec ce régime!",
     "They contaminated you with this diet!",
     [(585, "Ah, ben voilà, ça y est, ils t'ont contaminée.")], ""),
    ("annick", "Tu ressembles à un petit haricot sec.",
     "You look like a little dried bean.",
     [(591, "On dirait un petit haricot blanc tout sec.")], ""),
    ("lea", "J'ai encore deux scénarios à lire.",
     "I still have two scripts to read.",
     [(593, "J'ai encore deux scénarios à lire.")], ""),
    ("annick", "Va te coucher tout de suite!",
     "Go to bed right now!",
     [(589, "Allez, va te coucher, va.")], ""),
    ("lea", "Je fais des siestes dans la journée.",
     "I take naps during the day.",
     [(594, "Mais t'inquiète pas, je fais des micro-siestes dans la journée.")], ""),
    ("annick", "Où fais-tu ces siestes rapides?",
     "Where do you take these quick naps?",
     [(595, "Je vais me planquer dans les toilettes.")], ""),
    ("lea", "Je dors dix minutes aux toilettes.",
     "I sleep ten minutes in the bathroom.",
     [(597, "10 minutes, ça me suffit pour me reposer, après, ça va mieux.")], ""),
    ("annick", "Il faut garder ta dignité, ma fille!",
     "You must keep your dignity, my daughter!",
     [(601, "Il faut retrouver une dignité, ma fille, là.")], "")
]

OPENER = "Let us examine the way Annick worries about Camille's exhausting work routine."

WALK = [
    (0, None,
     "'It is normal that it takes time.' Camille explains that building an agent career requires patience. "
     "The conjunction que introduces the subjunctive clause."),
    (1, None,
     "'Nobody is rushing to your office?' Annick asks about the pace of clients. "
     "The negative structure personne ne means nobody."),
    (2, None,
     "'I do not have an office yet!' Camille points out her junior reality. "
     "The adverb encore indicates not yet when used with negation."),
    (3, None,
     "'You are too kind for this environment.' Annick worries about fierce competition. "
     "The noun milieu refers here to the professional film circle."),
    (4, None,
     "'And what are you eating there?' Annick questions her daughter's late meal. "
     "The question phrase qu'est-ce que asks what."),
    (5, None,
     "'I am eating a quinoa salad.' Camille names her healthy quick dinner. "
     "The noun salade is feminine."),
    (6, None,
     "'They contaminated you with this diet!' Annick teases her about Parisian habits. "
     "The verb contaminer is used figuratively here."),
    (7, None,
     "'You look like a little dried bean.' Annick uses an affectionate comparison. "
     "The verb phrase ressembler à means to look like."),
    (8, None,
     "'I still have two scripts to read.' Camille defends her late work schedule. "
     "The preposition à precedes the infinitive lire."),
    (9, None,
     "'Go to bed right now!' Annick insists on immediate rest. "
     "The imperative phrase va te coucher is addressed to family."),
    (10, None,
     "'I take naps during the day.' Camille shares her survival trick. "
     "The noun sieste is feminine."),
    (11, None,
     "'Where do you take these quick naps?' Annick asks for more practical details. "
     "The interrogative adverb où asks where."),
    (12, None,
     "'I sleep ten minutes in the bathroom.' Camille reveals her hidden resting spot. "
     "The plural noun toilettes refers to the restroom."),
    (13, None,
     "'You must keep your dignity, my daughter!' Annick reminds her of self-respect. "
     "The impersonal verb phrase il faut expresses necessity.")
]

TRANSITION = "Now let us listen to the dialogue once more at normal conversational speed."

OUTRO = (
    "Late at night, Annick tries to protect Camille from overworking in the competitive world of talent agencies. "
    "Listen to the conversation once more in French."
)

CLOSING = ("annick", "Il faut garder ta dignité, ma fille!")
