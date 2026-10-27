# Authoring module for dix-pour-cent s03e01 scene 06 (cues 85-156).
# Build: python3 tools/compose.py out/dix-pour-cent/s03e01/authoring/scene-06.py --out out/dix-pour-cent/s03e01/scene-06.json

ID = "dix-pour-cent-s03e01-scene-06"
SHOW = "dix-pour-cent"
SEASON = 3
EPISODE = 1
SCENE = 6
TITLE = "Le mystère du contrat  (The Damaged Contract)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "gabriel": "theo", "camille": "emilie"}
LABELS = {"lea": "Andréa", "gabriel": "Gabriel", "camille": "Camille"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S03E01"
SOURCE_FILE = "sources/dix-pour-cent/s03/e01.fr.dual.srt"
SOURCE_NOTE = ("Cues 85-156. Gabriel and Camille discover that Jean Dujardin's phone is dead and the signed contract "
               "is moldy and unpresentable just as producer Maxime arrives. "
               "Adapted for A1 French.")

INTRO = ("In Gabriel's office, panic sets in as Jean Dujardin goes completely unreachable and his contract arrives in terrible condition. "
         "When the film's producer arrives expecting the signed agreement, Andrea steps in to stall for time. "
         "Let's listen to the scene in French first.")

STORY = [
 ("gabriel", "Le téléphone de Jean est totalement coupé.",
  "Jean's phone is completely turned off.",
  [(85, "Le téléphone de Jean est coupé")], "Gabriel tries to reach his star"),
 ("camille", "Le téléphone de sa femme ne répond pas.",
  "His wife's phone does not answer.",
  [(85, "celui de sa femme répond pas non plus.")], "Camille confirms the dead line"),
 ("gabriel", "Jean ne plaisante jamais avec ses contrats.",
  "Jean never jokes with his contracts.",
  [(88, "c'est un truc avec lequel il rigole pas,")], "Gabriel stresses seriousness"),
 ("camille", "Ce contrat sent vraiment la bête morte!",
  "This contract really smells like a dead animal!",
  [(100, "2000 pages moisies qui puent la bête morte.")], "Camille is disgusted by the odor"),
 ("camille", "Les pages sont complètement moisies et sales.",
  "The pages are completely moldy and dirty.",
  [(100, "pages moisies")], "Camille inspects the paper"),
 ("gabriel", "Va chercher un produit pour laver le papier!",
  "Go look for a product to clean the paper!",
  [(103, "tu cherches un produit qui lave le papier")], "Gabriel gives desperate orders"),
 ("camille", "Ça n'existe pas, un produit pour le papier!",
  "There is no such thing as a cleaner for paper!",
  [(105, "Ça n'existe pas, un produit qui lave le papier.")], "Camille objects logically"),
 ("camille", "Et que va dire la productrice pour la signature?",
  "And what will the producer say about the signature?",
  [(107, "Et pour la signature Émile Berthier, tu vas dire quoi ?")], "Camille raises the legal issue"),
 ("gabriel", "Arrête de faire ta maligne avec moi!",
  "Stop acting clever with me!",
  [(110, "Arrête de faire ta maligne")], "Gabriel snaps under stress"),
 ("lea", "Gabriel, ton rendez-vous avec la productrice arrive.",
  "Gabriel, your meeting with the producer is arriving.",
  [(113, "Ton rendez-vous est arrivé.")], "Andrea enters to warn him"),
 ("gabriel", "Dis-lui que le service juridique a du retard.",
  "Tell her that the legal department has a delay.",
  [(121, "c'est le service juridique.")], "Gabriel makes up an excuse"),
 ("lea", "Je vais la faire patienter dans mon bureau.",
  "I am going to keep her waiting in my office.",
  [(126, "Mais ça me fait plaisir de te voir.")], "Andrea agrees to buy time"),
 ("gabriel", "Trouvons une solution très vite pour ce contrat.",
  "Let us find a solution very quickly for this contract.",
  [(124, "donc on l'aura ce soir.")], "Gabriel urges urgent action"),
]

OPENER = "Let's examine how the agents react to the bizarre state of the contract step by step to explore emergency crisis management."

WALK = [
 (0, None,
  "'Jean's phone is completely turned off.' Gabriel fails repeatedly to contact his missing lead actor."),
 (1, None,
  "'His wife's phone does not answer.' Camille reports that all family contacts have gone completely silent."),
 (2, None,
  "'Jean never jokes with his contracts.' Gabriel emphasizes that financial negotiations are always strictly professional."),
 (3, None,
  "'This contract really smells like a dead animal!' Camille holds the putrid document away from her face."),
 (4, None,
  "'The pages are completely moldy and dirty.' Camille examines the damaged paperwork sent back from the woods."),
 (5, None,
  "'Go look for a product to clean the paper!' Gabriel issues an absurd command in a state of growing panic."),
 (6, None,
  "'There is no such thing as a cleaner for paper!' Camille points out the impossibility of washing documents."),
 (7, None,
  "'And what will the producer say about the signature?' Camille worries about explaining the fake name."),
 (8, None,
  "'Stop acting clever with me!' Gabriel lashes out defensively as pressure mounts on his shoulders."),
 (9, None,
  "'Gabriel, your meeting with the producer is arriving.' Andrea interrupts with urgent news about the lobby."),
 (10, None,
  "'Tell her that the legal department has a delay.' Gabriel invents an administrative delay to hide the disaster."),
 (11, None,
  "'I am going to keep her waiting in my office.' Andrea volunteers to distract the visiting executive."),
 (12, None,
  "'Let us find a solution very quickly for this contract.' Gabriel tries to regain control before the deal collapses."),
]

TRANSITION = "Now let's listen to the scene once more from start to finish."

OUTRO = ("The mystery behind Jean Dujardin's bizarre contract deepens as the agents scramble to stall an impatient producer. "
         "Let's review the key conversational expressions and vocabulary from this scene.")

CLOSING = ("gabriel", "Trouvons une solution très vite pour ce contrat.")
