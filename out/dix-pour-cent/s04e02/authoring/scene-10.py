# Authoring module for dix-pour-cent s04e02 scene 10 (cues 456-610).
# Build: python3 tools/compose.py overhear-content/out/dix-pour-cent/s04e02/authoring/scene-10.py --out overhear-content/out/dix-pour-cent/s04e02/scene-10.json

ID = "dix-pour-cent-s04e02-scene-10"
SHOW = "dix-pour-cent"
SEASON = 4
EPISODE = 2
SCENE = 10
TITLE = "Le feng shui de Nathalie  (Nathalie's Feng Shui)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "nathalie": "emilie", "mathias": "theo"}
LABELS = {"lea": "Andréa", "nathalie": "Nathalie Baye", "mathias": "Mathias"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S04E02"
SOURCE_FILE = "sources/dix-pour-cent/s04/e02.fr.dual.srt"
SOURCE_NOTE = ("Cues 456-610. In the sublet law office at ASK, Nathalie Baye rearranges desks according to feng shui, "
               "prompting a confrontation with Andrea, who is shocked when Nathalie selects Camille as her agent.")

INTRO = ("Mathias escorts Nathalie Baye to his old office suite, only to find the entire floor sublet to busy lawyers. "
         "Horrified by their cramped workspace, Nathalie impulsively begins reorganizing their desks with feng shui principles "
         "just as Andrea arrives to intervene. Let's listen to their conversation in French first.")

OPENER = "Let's examine the conversation line by line and explore the French expressions."
TRANSITION = "Now let's listen to the complete discussion once more to reinforce the vocabulary."

STORY = [
 ("mathias", "Bienvenue dans mon ancien bureau, chère Nathalie.",
  "Welcome to my former office, dear Nathalie.",
  [(477, "C'est pas votre ancien bureau ?"), (478, "Si, c'est ça.")], "Welcoming client to former office"),
 ("nathalie", "On dirait plutôt un corral d'avocats!",
  "It looks more like a lawyers' corral!",
  [(482, "C'est un \"corral d'avocats\" !")], "Commenting on cramped workspace"),
 ("mathias", "L'agence a dû sous-louer cet étage entier.",
  "The agency had to sublet this entire floor.",
  [(479, "J'imagine qu'ASK a dû sous-louer l'étage en dessous")], "Explaining sublease necessity"),
 ("nathalie", "Il faut faire circuler l'énergie ici!",
  "We must circulate the energy here!",
  [(488, "Faisons circuler l'énergie.")], "Proposing energy realignment"),
 ("nathalie", "Une belle plante verte changera toute l'ambiance.",
  "A nice green plant will change the whole ambiance.",
  [(489, "D'abord, une plante ne fera pas de mal.")], "Adding greenery to room"),
 ("mathias", "Attention Nathalie, ce n'est pas votre travail.",
  "Careful Nathalie, this is not your job.",
  [(490, "Oui, mais ce n'est pas votre travail.")], "Advising restraint"),
 ("nathalie", "Qui a déjà entendu parler du feng shui?",
  "Who has already heard of feng shui?",
  [(496, "Qui a entendu parler du \"feng shui\" ?")], "Addressing puzzled attorneys"),
 ("lea", "Nathalie! Que faites-vous dans cette pièce?",
  "Nathalie! What are you doing in this room?",
  [(483, "Andréa arrive.")], "Entering in surprise"),
 ("nathalie", "J'aide ces pauvres avocats à mieux respirer.",
  "I am helping these poor lawyers breathe better.",
  [(487, "Changeons tout.")], "Explaining humanitarian layout"),
 ("lea", "Mathias, tu essaies encore de voler mes clients?",
  "Mathias, are you still trying to steal my clients?",
  [(473, "Nathalie Baye ne va pas plus loin")], "Confronting former rival"),
 ("mathias", "J'offre simplement un conseil amical à Nathalie.",
  "I am simply offering friendly advice to Nathalie.",
  [(466, "la réunion ait lieu à l'agence.")], "Defending his presence"),
 ("nathalie", "Andréa, j'adore votre grande énergie formidable.",
  "Andrea, I love your great wonderful energy.",
  [(540, "Vos clients ont beaucoup de chance de vous avoir.")], "Praising Andrea warmly"),
 ("nathalie", "Mais pour ce film, je préfère Camille.",
  "But for this film, I prefer Camille.",
  [(545, "Elle est plus discrète, plus ce qu'il me faut.")], "Choosing young agent Camille"),
 ("lea", "Camille? C'est une excellente idée pour vous!",
  "Camille? That is an excellent idea for you!",
  [(545, "ce qu'il me faut.")], "Supporting junior colleague gracefully"),
]

WALK = [
 (0, None,
  "'Welcome to my former office, dear Nathalie.' Mathias welcomes the actress into ASK. "
  "The adjective 'ancien' placed before a noun denotes former status."),
 (1, None,
  "'It looks more like a lawyers' corral!' Nathalie compares the open desks to a cattle pen. "
  "The noun 'corral' refers humorously to an enclosure."),
 (2, None,
  "'The agency had to sublet this entire floor.' Mathias explains the financial sublet. "
  "The verb 'sous-louer' means to sublet space."),
 (3, None,
  "'We must circulate the energy here!' Nathalie invokes harmonious energy flow. "
  "The causative verb 'faire circuler' means to cause to move or flow."),
 (4, None,
  "'A nice green plant will change the whole ambiance.' Nathalie introduces natural decor. "
  "The noun phrase 'plante verte' denotes a houseplant."),
 (5, None,
  "'Careful Nathalie, this is not your job.' Mathias warns her against interfering with staff. "
  "The warning interjection 'attention' urges caution."),
 (6, None,
  "'Who has already heard of feng shui?' Nathalie addresses the astonished lawyers. "
  "The idiom 'entendre parler de' means to hear about something."),
 (7, None,
  "'Nathalie! What are you doing in this room?' Andrea bursts into the suite out of breath. "
  "The noun 'piece' refers to a room inside a building."),
 (8, None,
  "'I am helping these poor lawyers breathe better.' Nathalie justifies her impromptu redesign. "
  "The comparative adverb 'mieux' modifies the infinitive respirer."),
 (9, None,
  "'Mathias, are you still trying to steal my clients?' Andrea accuses Mathias of poaching. "
  "The verb 'voler' here colloquially means to poach or steal clients."),
 (10, None,
  "'I am simply offering friendly advice to Nathalie.' Mathias denies any underhanded tactics. "
  "The adjective 'amical' describes warm friendly support."),
 (11, None,
  "'Andrea, I love your great wonderful energy.' Nathalie cushions her upcoming choice. "
  "The adjective 'formidable' expresses genuine admiration."),
 (12, None,
  "'But for this film, I prefer Camille.' Nathalie selects Camille for her calmer approach. "
  "The verb 'preferer' denotes choice between options."),
 (13, None,
  "'Camille? That is an excellent idea for you!' Andrea embraces the decision graciously. "
  "The adjective 'excellente' affirms strong agreement."),
]

OUTRO = ("Nathalie Baye's energetic feng shui session ends with an unexpected triumph for ASK. "
         "Though Andrea missed out on personal representation, Camille gains an illustrious star client. "
         "Now, let's review the scene one last time.")

CLOSING = ("lea", "Camille? C'est une excellente idée pour vous!")
