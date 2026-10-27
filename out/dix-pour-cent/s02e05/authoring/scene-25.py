# Authoring module for dix-pour-cent s02e05 scene 25 (cues 818-855).
# Build: python3 tools/compose.py out/dix-pour-cent/s02e05/authoring/scene-25.py --out out/dix-pour-cent/s02e05/scene-25.json

ID = "dix-pour-cent-s02e05-scene-25"
SHOW = "dix-pour-cent"
SEASON = 2
EPISODE = 5
SCENE = 25
TITLE = "Le financement refusé  (Financing Denied)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "julien": "theo", "gabriel": "marcel"}
LABELS = {"lea": "Sofia", "julien": "Julien", "gabriel": "Gabriel"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S02E05"
SOURCE_FILE = "sources/dix-pour-cent/s02/e05.fr.dual.srt"
SOURCE_NOTE = ("Cues 818-855. Julien Dore learns that France 2 has pulled all funding from his musical film "
               "over an absurd rumor of hidden penophagy. Gabriel and Sofia attempt to keep him from abandoning the project. "
               "Adapted for A1 French.")

INTRO = ("In the recording studio, Julien Dore learns that television executives have refused to finance his movie. "
         "Furious over an absurd misunderstanding, Julien threatens to quit the project while Gabriel and Sofia urge him to persist. "
         "Let's listen to the scene in French first.")

STORY = [
 ("julien", "France 2 refuse de financer notre film!",
  "France 2 refuses to finance our film!",
  [(818, "Les salopards !"), (820, "France 2 ne va pas nous financer.")], "Julien breaks the bad news"),
 ("gabriel", "Qu'est-ce qui se passe exactement ce matin?",
  "What is happening exactly this morning?",
  [(819, "Qu'est-ce qui se passe ?"), (823, "Mon producteur était là ce matin.")], "Gabriel asks for details"),
 ("julien", "C'est un refus total, pas d'argent!",
  "It is a total refusal, no money!",
  [(822, "C'est non à tout !"), (824, "Pas d'argent !")], "Julien vents anger"),
 ("lea", "Alors notre grand projet est complètement mort?",
  "So our big project is completely dead?",
  [(825, "Alors c'est mort ?")], "Sofia fears cancellation"),
 ("gabriel", "Il doit y avoir un simple malentendu.",
  "There must be a simple misunderstanding.",
  [(826, "C'est pas possible, il doit y avoir un malentendu.")], "Gabriel seeks explanation"),
 ("julien", "Élisabeth prétend qu'il y a un scandale.",
  "Elisabeth claims that there is a scandal.",
  [(827, "C'est cette garce, Élisabeth Lecœur,"), (831, "Elle prétend qu'il y a de la « pénophagie cachée » dans mon film.")], "Julien cites accusation"),
 ("lea", "Mais de quel scandale parles-tu donc?",
  "But what scandal are you talking about?",
  [(832, "C'est quoi la « pénophagie » ?")], "Sofia asks for clarification"),
 ("julien", "Elle a inventé un mot totalement absurde.",
  "She invented a totally absurd word.",
  [(836, "Elle a trouvé ça où ?"), (837, "Je sais pas. C'est ridicule.")], "Julien decries rumor"),
 ("gabriel", "Je vais vérifier cette histoire bizarre maintenant.",
  "I will verify this strange story now.",
  [(839, "Je vais vérifier parce que ça me paraît vraiment bizarre.")], "Gabriel investigates"),
 ("gabriel", "Ce mot n'existe nulle part, regarde!",
  "This word exists nowhere, look!",
  [(841, "-Aucun résultat pour « pénophagie ». -Là !"), (842, "Ça n'existe pas.")], "Gabriel checks online"),
 ("julien", "Ils détruisent trois ans de mon travail!",
  "They destroy three years of my work!",
  [(848, "et foutent en l'air trois ans de travail en une putain de matinée !")], "Julien laments lost effort"),
 ("gabriel", "Nous pouvons trouver un autre financement ailleurs.",
  "We can find another financing elsewhere.",
  [(850, "Écoute, il y a d'autres solutions."), (851, "Il y a d'autres moyens de trouver un financement.")], "Gabriel offers solutions"),
 ("julien", "Non, c'est fini, je laisse tomber.",
  "No, it is finished, I give up.",
  [(852, "Tu sais quoi ? On laisse tomber."), (853, "C'est fini, j'arrête tout.")], "Julien throws in towel"),
 ("lea", "Julien, garde espoir pour ce beau film.",
  "Julien, keep hope for this beautiful film.",
  [(854, "Non, Julien, non.")], "Sofia encourages Julien"),
 ("gabriel", "Ne baisse pas les bras si vite, Julien.",
  "Do not give up so quickly, Julien.",
  [(854, "Non, Julien, non.")], "Gabriel urges resilience"),
]

OPENER = "Let's examine how Julien reacts to the funding cancellation and how Gabriel tries to rescue the film step by step."

WALK = [
 (0, None,
  "'France 2 refuses to finance our film!' Julien announces the shock cancellation of their television funding."),
 (1, None,
  "'What is happening exactly this morning?' Gabriel asks for specifics about what went wrong with the broadcaster."),
 (2, None,
  "'It is a total refusal, no money!' Julien emphasizes the definitive rejection by the production network."),
 (3, None,
  "'So our big project is completely dead?' Sofia worries that all their preparations have come to nothing."),
 (4, None,
  "'There must be a simple misunderstanding.' Gabriel tries to remain rational and identify the root cause."),
 (5, None,
  "'Elisabeth claims that there is a scandal.' Julien identifies the executive who spread rumors about the script."),
 (6, None,
  "'But what scandal are you talking about?' Sofia seeks to understand what could possibly justify the decision."),
 (7, None,
  "'She invented a totally absurd word.' Julien explains that the objection relies on pure fabrication."),
 (8, None,
  "'I will verify this strange story now.' Gabriel uses his tablet to research the bizarre accusation immediately."),
 (9, None,
  "'This word exists nowhere, look!' Gabriel confirms that the alleged term has zero linguistic existence."),
 (10, None,
  "'They destroy three years of my work!' Julien expresses acute anguish over years of artistic dedication lost."),
 (11, None,
  "'We can find another financing elsewhere.' Gabriel suggests pitching alternative partners and investors."),
 (12, None,
  "'No, it is finished, I give up.' Julien sinks into despair and declares his intention to walk away."),
 (13, None,
  "'Julien, keep hope for this beautiful film.' Sofia appeals to his passion for their collaborative project."),
 (14, None,
  "'Do not give up so quickly, Julien.' Gabriel uses the idiom baisser les bras to encourage perseverance."),
]

TRANSITION = "Now let's listen to the scene once more from start to finish."

OUTRO = ("Despite the sudden setback from France 2, Gabriel and Sofia stand firmly by Julien's artistic vision. "
         "Let's review the financing and crisis-management vocabulary from this scene.")

CLOSING = ("gabriel", "Nous pouvons trouver un autre financement ailleurs.")
