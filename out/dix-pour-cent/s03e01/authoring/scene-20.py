# Authoring module for dix-pour-cent s03e01 scene 20 (cues 668-694).
# Build: python3 tools/compose.py out/dix-pour-cent/s03e01/authoring/scene-20.py --out out/dix-pour-cent/s03e01/scene-20.json

ID = "dix-pour-cent-s03e01-scene-20"
SHOW = "dix-pour-cent"
SEASON = 3
EPISODE = 1
SCENE = 20
TITLE = "Une explication nocturne  (A Late-Night Explanation)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "colette": "emilie"}
LABELS = {"lea": "Andréa", "colette": "Colette"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S03E01"
SOURCE_FILE = "sources/dix-pour-cent/s03/e01.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 668-694. In the kitchen late at night, Colette asks Andréa why she slept with Hicham in Cannes. "
    "Andréa tries to describe the sudden, confusing mix of rivalry and impulse that caused that night."
)

INTRO = (
    "Late in the evening, Colette and Andrea continue their frank conversation in the kitchen. "
    "Colette needs to understand why Andrea slept with Hicham during the Cannes Festival. "
    "Listen to their intimate exchange in French first."
)

STORY = [
    ("colette", "Cette histoire me tourmente sans cesse.",
     "This story torments me endlessly.",
     [(668, "C'est juste que j'arrête pas d'y penser. Ça m'obsède, en fait.")], ""),
    ("colette", "Pourquoi as-tu couché avec Hicham?",
     "Why did you sleep with Hicham?",
     [(669, "Pourquoi t'as couché avec lui ?")], ""),
    ("lea", "J'avais bu beaucoup de champagne.",
     "I had drunk a lot of champagne.",
     [(670, "J'étais bourrée. J'avais bu trop de champagne.")], ""),
    ("colette", "Ce n'est pas une explication suffisante.",
     "That is not a sufficient explanation.",
     [(671, "Mais tu couches pas avec un mec à chaque fois que tu bois trop de champagne ?")], ""),
    ("lea", "C'est difficile à expliquer calmement.",
     "It is difficult to explain calmly.",
     [(677, "C'est pas facile à expliquer.")], ""),
    ("colette", "J'ai besoin de comprendre cette nuit.",
     "I need to understand that night.",
     [(673, "J'ai besoin de savoir ce qui s'est passé dans ta tête.")], ""),
    ("lea", "Au départ, je regardais une fille.",
     "At first, I was looking at a girl.",
     [(678, "Bon, donc, au début, j'ai été attirée par cette fille.")], ""),
    ("lea", "Hicham a séduit cette jeune femme.",
     "Hicham seduced that young woman.",
     [(679, "Et donc, lui, il l'a emballée sous mon nez.")], ""),
    ("colette", "Et cela t'a mise en colère?",
     "And that made you angry?",
     [(680, "Et ça, ça m'a énervée. Qu'il le fasse et puis qu'elle marche.")], ""),
    ("lea", "Oui, la tension est devenue électrique.",
     "Yes, the tension became electric.",
     [(685, "Et c'est avec lui que c'est devenu électrique.")], ""),
    ("lea", "Je voulais absolument le dominer.",
     "I absolutely wanted to dominate him.",
     [(690, "J'avais envie de le dominer.")], ""),
    ("colette", "Arrête, cette image me fait mal!",
     "Stop, that image hurts me!",
     [(692, "Arrête, parce que tu visualises, là.")], ""),
    ("lea", "Je n'aurais pas dû tout raconter.",
     "I should not have told everything.",
     [(693, "Tu vois, j'aurais pas dû te raconter.")], ""),
    ("colette", "Nous venons de mondes différents.",
     "We come from different worlds.",
     [(695, "On vient vraiment pas de la même planète, toutes les deux.")], "")
]

OPENER = "Let us listen as Andrea attempts to explain what happened in Cannes."

WALK = [
    (0, None,
     "'This story torments me endlessly.' Colette confesses her constant obsession. "
     "The verb tourmenter means to torment or distress."),
    (1, None,
     "'Why did you sleep with Hicham?' Colette asks the painful direct question. "
     "The compound past as couché comes from coucher."),
    (2, None,
     "'I had drunk a lot of champagne.' Andrea cites the alcohol at the party. "
     "The pluperfect tense avais bu expresses a prior action."),
    (3, None,
     "'That is not a sufficient explanation.' Colette demands deeper emotional honesty. "
     "The adjective suffisante agrees with explication."),
    (4, None,
     "'It is difficult to explain calmly.' Andrea struggles to put her feelings into words. "
     "The adverb calmement means in a calm manner."),
    (5, None,
     "'I need to understand that night.' Colette seeks clarity for their relationship. "
     "The phrase avoir besoin de means to need."),
    (6, None,
     "'At first, I was looking at a girl.' Andrea recounts the beginning of the evening. "
     "The phrase au départ means initially."),
    (7, None,
     "'Hicham seduced that young woman.' Andrea describes Hicham's competitive behavior. "
     "The verb séduire means to charm or seduce."),
    (8, None,
     "'And that made you angry?' Colette asks about the emotional trigger. "
     "The idiom mettre en colère means to make someone angry."),
    (9, None,
     "'Yes, the tension became electric.' Andrea recalls the intense rivalry between them. "
     "The adjective électrique describes palpable tension."),
    (10, None,
     "'I absolutely wanted to dominate him.' Andrea admits her aggressive competitive impulse. "
     "The infinitive dominer expresses a desire for control."),
    (11, None,
     "'Stop, that image hurts me!' Colette feels hurt by the mental picture. "
     "The verbal phrase faire mal à means to hurt."),
    (12, None,
     "'I should not have told everything.' Andrea regrets being overly candid. "
     "The past conditional n'aurais pas dû expresses regret."),
    (13, None,
     "'We come from different worlds.' Colette reflects on their divergent perspectives. "
     "The preposition de indicates origin.")
]

TRANSITION = "Now let us listen to their candid discussion once more at normal pace."

OUTRO = (
    "Andrea and Colette confront painful truths about the past while seeking mutual understanding. "
    "Listen to the scene once more in French."
)

CLOSING = ("colette", "Nous venons de mondes différents.")
