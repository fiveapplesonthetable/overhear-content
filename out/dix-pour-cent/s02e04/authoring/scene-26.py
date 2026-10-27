# Authoring module for dix-pour-cent s02e04 scene 26 (cues 764-783).
# Build: python3 tools/compose.py out/dix-pour-cent/s02e04/authoring/scene-26.py --out out/dix-pour-cent/s02e04/scene-26.json

ID = "dix-pour-cent-s02e04-scene-26"
SHOW = "dix-pour-cent"
SEASON = 2
EPISODE = 4
SCENE = 26
TITLE = "Pas d'ingérence extérieure  (No Outside Interference)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "gabriel": "theo", "julien": "marcel"}
LABELS = {"lea": "Sofia", "gabriel": "Gabriel", "julien": "Julien"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S02E04"
SOURCE_FILE = "sources/dix-pour-cent/s02/e04.fr.dual.srt"
SOURCE_NOTE = ("Cues 764-783. Gabriel reveals to Julien Dore that he and Sofia are in a relationship. "
               "Julien reacts calmly but firmly insists on complete creative freedom with no outside interference. "
               "Adapted for A1 French.")

INTRO = ("In the recording studio, Gabriel admits to Julien Dore that he and Sofia are dating. "
         "Julien accepts the news but insists that outside personal ties must not interfere with his creative work. "
         "Let's listen to the scene in French first.")

STORY = [
 ("julien", "Tu travailles dur aujourd'hui, Sofia?",
  "Are you working hard today, Sofia?",
  [(764, "Tu travailles dur ?")], "Julien greets Sofia"),
 ("gabriel", "Pardon, nous sommes ensemble tous les deux.",
  "Sorry, the two of us are together.",
  [(765, "Désolé, on ne vous a pas dit ? On est ensemble.")], "Gabriel reveals relationship"),
 ("julien", "D'accord, je comprends la situation.",
  "Okay, I understand the situation.",
  [(766, "-D'accord. -Pardon.")], "Julien acknowledges"),
 ("lea", "Nous voulions éviter les bavardages inutiles.",
  "We wanted to avoid unnecessary gossip.",
  [(767, "On n'a pas dit parce que..."), (769, "Les gens jasent, ils vont dire qu'elle avait des relations.")], "Sofia explains secrecy"),
 ("gabriel", "Gardez cela pour vous, s'il vous plaît.",
  "Keep this to yourself, please.",
  [(770, "Vous savez comment ce milieu fonctionne."), (771, "C'est dur. Gardez ça pour vous.")], "Gabriel requests discretion"),
 ("julien", "J'aurais préféré le savoir plus tôt.",
  "I would have preferred knowing sooner.",
  [(772, "Bien sûr, c'est juste que j'aurais préféré le savoir dès le début.")], "Julien expresses preference"),
 ("gabriel", "Cela ne change rien au projet.",
  "That changes nothing about the project.",
  [(773, "-Ça ne change rien. -Un peu quand même.")], "Gabriel reassures"),
 ("julien", "Pour moi, l'essentiel reste le film.",
  "For me, the essential thing remains the film.",
  [(774, "L'essentiel, c'est le film.")], "Julien prioritizes the movie"),
 ("julien", "Je refuse toute interférence dans mon travail.",
  "I refuse any interference in my work.",
  [(775, "Je ne veux rien qui interfère avec mon travail.")], "Julien sets boundaries"),
 ("lea", "Il n'y aura aucun problème ici.",
  "There will be no problem here.",
  [(776, "-Bien sûr. -Il n'y aura aucun problème.")], "Sofia reassures"),
 ("julien", "Je ne veux aucune ingérence extérieure.",
  "I want no outside interference.",
  [(777, "Je ne veux aucune ingérence extérieure.")], "Julien emphasizes independence"),
 ("gabriel", "Bien sûr, nous respectons votre démarche.",
  "Of course, we respect your approach.",
  [(778, "Absolument ! Bien sûr que non.")], "Gabriel shows agreement"),
 ("julien", "Sans totale liberté, l'art est inutile.",
  "Without total freedom, art is useless.",
  [(779, "Sans liberté, c'est un exercice inutile.")], "Julien states his philosophy"),
 ("gabriel", "Très bien, fais comme tu veux, Julien.",
  "Very well, do as you wish, Julien.",
  [(781, "Très bien, fais comme tu veux, Julien.")], "Gabriel yields control"),
 ("gabriel", "Sofia est ton actrice pour ce film.",
  "Sofia is your actress for this film.",
  [(782, "C'est ton actrice."), (783, "D'accord.")], "Gabriel reaffirms Sofia's role"),
]

OPENER = "Let's examine how Gabriel and Julien negotiate professional boundaries and creative independence step by step."

WALK = [
 (0, None,
  "'Are you working hard today, Sofia?' Julien asks Sofia in an easygoing, friendly tone."),
 (1, None,
  "'Sorry, the two of us are together.' Gabriel interrupts politely to disclose their romantic relationship."),
 (2, None,
  "'Okay, I understand the situation.' Julien takes in the surprising confession without getting angry."),
 (3, None,
  "'We wanted to avoid unnecessary gossip.' Sofia clarifies why they chose to keep their romance quiet."),
 (4, None,
  "'Keep this to yourself, please.' Gabriel asks Julien to maintain complete secrecy within the industry."),
 (5, None,
  "'I would have preferred knowing sooner.' Julien admits he would rather have had full transparency upfront."),
 (6, None,
  "'That changes nothing about the project.' Gabriel insists that personal feelings will not disrupt the shoot."),
 (7, None,
  "'For me, the essential thing remains the film.' Julien refocuses the discussion on the artistic production."),
 (8, None,
  "'I refuse any interference in my work.' Julien makes it clear that he will not accept meddling."),
 (9, None,
  "'There will be no problem here.' Sofia reassures Julien about her professional commitment."),
 (10, None,
  "'I want no outside interference.' Julien repeats his strict condition regarding creative autonomy."),
 (11, None,
  "'Of course, we respect your approach.' Gabriel readily agrees to give Julien full artistic leeway."),
 (12, None,
  "'Without total freedom, art is useless.' Julien compares making art under constraint to windsurfing without wind."),
 (13, None,
  "'Very well, do as you wish, Julien.' Gabriel gracefully steps back to let the director lead."),
 (14, None,
  "'Sofia is your actress for this film.' Gabriel places his full trust in Julien's creative vision."),
]

TRANSITION = "Now let's listen to the scene once more from start to finish."

OUTRO = ("Julien sets clear artistic boundaries while accepting Sofia and Gabriel's relationship with professional grace. "
         "Let's review the creative and boundary-setting vocabulary from this scene.")

CLOSING = ("julien", "Sans totale liberté, l'art est inutile.")
