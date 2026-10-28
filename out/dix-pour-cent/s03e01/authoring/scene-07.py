# Authoring module for dix-pour-cent s03e01 scene 07 (cues 157-160).
# Build: python3 tools/compose.py out/dix-pour-cent/s03e01/authoring/scene-07.py --out out/dix-pour-cent/s03e01/scene-07.json

ID = "dix-pour-cent-s03e01-scene-07"
SHOW = "dix-pour-cent"
SEASON = 3
EPISODE = 1
SCENE = 7
TITLE = "Le pitch du Déserteur  (The Deserter's Story)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "maxime": "theo"}
LABELS = {"lea": "Andréa", "maxime": "Maxime"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S03E01"
SOURCE_FILE = "sources/dix-pour-cent/s03/e01.fr.dual.srt"
SOURCE_NOTE = ("Cues 157-160. In Andrea's office, Andréa explains the grueling plot of Jean Dujardin's "
               "First World War film to reassure the producer and build anticipation for behind-the-scenes footage. "
               "Adapted for A1 French.")

INTRO = ("In her office, Andrea tries to soothe producer Maxime's impatience by pitching the artistic premise of Jean Dujardin's latest film. "
         "Describing the harrowing story of a wartime deserter, she prepares him to watch confidential footage. "
         "Let's listen to the scene in French first.")

STORY = [
 ("maxime", "Alors Andréa, parle-moi de ce fameux film.",
  "So Andrea, tell me about this famous movie.",
  [(145, "Mais qu'est-ce qu'il est allé faire sur ce tournage")], "Maxime inquires skeptically"),
 ("lea", "C'est l'histoire d'un brave soldat blessé.",
  "It is the story of a brave wounded soldier.",
  [(157, "C'est l'histoire d'un soldat blessé")], "Andrea begins her pitch"),
 ("lea", "Ce pauvre homme déserte pendant la guerre.",
  "This poor man deserts during the war.",
  [(157, "qui a déserté pendant la guerre de 14")], "Andrea details the plot"),
 ("maxime", "Pendant la Première Guerre mondiale, c'est ça?",
  "During the First World War, is that it?",
  [(157, "pendant la guerre de 14")], "Maxime asks for historical context"),
 ("lea", "Oui, pendant la terrible guerre de quatorze.",
  "Yes, during the terrible war of nineteen fourteen.",
  [(157, "guerre de 14")], "Andrea confirms the setting"),
 ("lea", "Il se cache seul dans une grande forêt.",
  "He hides alone in a vast forest.",
  [(158, "et qui se cache dans la forêt pendant des années")], "Andrea evokes isolation"),
 ("maxime", "Pourquoi se cache-t-il dans les bois sauvages?",
  "Why is he hiding in the wild woods?",
  [(159, "pour échapper à la peine de mort.")], "Maxime seeks motivation"),
 ("lea", "Il veut échapper à la peine de mort.",
  "He wants to escape the death penalty.",
  [(159, "pour échapper à la peine de mort.")], "Andrea explains the stakes"),
 ("maxime", "C'est une histoire tragique et très sombre.",
  "It is a tragic and very dark story.",
  [(160, "On connaît ça.")], "Maxime acknowledges the dramatic weight"),
 ("lea", "Jean Dujardin y joue avec une intensité folle.",
  "Jean Dujardin acts with wild intensity in it.",
  [(152, "C'est des images de tournage.")], "Andrea hypes the acting"),
 ("maxime", "Le public aime ce genre de drame historique.",
  "The audience loves this genre of historical drama.",
  [(142, "J'ai beaucoup de respect pour le cinéma d'auteur")], "Maxime reflects on appeal"),
 ("lea", "Regarde cet extrait vidéo sur mon écran d'ordinateur.",
  "Watch this video excerpt on my computer screen.",
  [(151, "Tiens, regarde. Tu vas voir.")], "Andrea sets up the laptop"),
 ("maxime", "Montre-moi ces images secrètes du tournage.",
  "Show me these secret shots from the film set.",
  [(153, "C'est archi-confidentiel")], "Maxime leans in closer"),
]

OPENER = "Let's examine how Andrea pitches the dramatic war story step by step to explore cinema marketing and storytelling."

WALK = [
 (0, None,
  "'So Andrea, tell me about this famous movie.' Maxime demands an explanation for Dujardin's long absence. The verb meaning 'tell me' pairs naturally with the noun for 'movie.' in everyday conversation."),
 (1, None,
  "'It is the story of a brave wounded soldier.' Andrea introduces the central protagonist of the period drama. The verb meaning 'it is' pairs naturally with the noun for 'the story' in everyday conversation."),
 (2, None,
  "'This poor man deserts during the war.' Andrea highlights the soldier's moral crisis on the battlefield. The descriptive adjective for 'poor' agrees in gender and number with its noun."),
 (3, None,
  "'During the First World War, is that it?' Maxime clarifies the exact historical period of the narrative. The verb meaning 'is it' pairs naturally with the noun for 'War' in everyday conversation."),
 (4, None,
  "'Yes, during the terrible war of nineteen fourteen.' Andrea emphasizes the brutal conditions of the conflict. The key noun here means 'war', anchored by its matching French article."),
 (5, None,
  "'He hides alone in a vast forest.' Andrea paints a picture of extreme survival away from civilization. The verb meaning 'hides' pairs naturally with the noun for 'forest.' in everyday conversation."),
 (6, None,
  "'Why is he hiding in the wild woods?' Maxime asks about the character's desperate motives. The verb meaning 'does he hide' pairs naturally with the noun for 'woods' in everyday conversation."),
 (7, None,
  "'He wants to escape the death penalty.' Andrea explains that deserters faced immediate execution by firing squad. The verb meaning 'wants' pairs naturally with the noun for 'penalty' in everyday conversation."),
 (8, None,
  "'It is a tragic and very dark story.' Maxime recognizes the somber tone common in festival arthouse cinema. The descriptive adjective for 'tragic' agrees in gender and number with its noun."),
 (9, None,
  "'Jean Dujardin acts with wild intensity in it.' Andrea praises the star's radical commitment to the role. The verb meaning 'acts' pairs naturally with the noun for 'intensity' in everyday conversation."),
 (10, None,
  "'The audience loves this genre of historical drama.' Maxime admits that intense wartime narratives attract critical acclaim. Notice how 'loves' leads directly into the noun meaning 'audience'."),
 (11, None,
  "'Watch this video excerpt on my computer screen.' Andrea turns her monitor to reveal exclusive behind-the-scenes files. The verb meaning 'look at' pairs naturally with the noun for 'clip' in everyday conversation."),
 (12, None,
  "'Show me these secret shots from the film set.' Maxime leans forward eagerly to inspect Dujardin's performance. The verb meaning 'show me' pairs naturally with the noun for 'footage' in everyday conversation."),
]

TRANSITION = "Now let's listen to the scene once more from start to finish."

OUTRO = ("Andrea artfully pitches the grim historical narrative of Le Deserteur to build excitement before revealing shocking footage. "
         "Let's review the key storytelling and film vocabulary from this scene.")

CLOSING = ("maxime", "Montre-moi ces images secrètes du tournage.")
