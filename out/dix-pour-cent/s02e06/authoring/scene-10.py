# Authoring module for dix-pour-cent s02e06 scene 10 (cues 208-228).
# Build: python3 tools/compose.py out/dix-pour-cent/s02e06/authoring/scene-10.py --out out/dix-pour-cent/s02e06/scene-10.json

ID = "dix-pour-cent-s02e06-scene-10"
SHOW = "dix-pour-cent"
SEASON = 2
EPISODE = 6
SCENE = 10
TITLE = "Le garde du corps  (The Jewelry Bodyguard)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "theo": "theo"}
LABELS = {"lea": "Andréa", "theo": "Renard"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S02E06"
SOURCE_FILE = "sources/dix-pour-cent/s02/e06.fr.dual.srt"
SOURCE_NOTE = ("Cues 208-228. Outside Juliette Binoche's hotel suite in Cannes, Andréa meets Renard, "
               "the stern bodyguard protecting the Chopard jewelry, and gains access to the room. "
               "Adapted for A1 French.")

INTRO = ("Outside Juliette Binoche's hotel room in Cannes, Andrea encounters an unyielding private security guard. "
         "Tasked with protecting multi-million euro festival jewels, the guard refuses to let anyone pass without strict clearance. "
         "Let's listen to the scene in French first.")

STORY = [
 ("lea", "J'en déduis que les bijoux Chopard sont arrivés. Bonjour.",
  "I deduce that the Chopard jewelry has arrived. Hello.",
  [(213, "J'en déduis que les bijoux Chopard sont arrivés. Bonjour.")], ""),
 ("theo", "Qui êtes-vous, madame?",
  "Who are you, madam?",
  [(217, "Qui êtes-vous, madame ?")], ""),
 ("lea", "Andréa Martel, l'agent de Juliette Binoche.",
  "Andrea Martel, Juliette Binoche's agent.",
  [(218, "Andréa Martel, l'agent de Juliette Binoche.")], ""),
 ("theo", "Vous devez attendre ici, madame.",
  "You must wait here, madam.",
  [(217, "madame ?")], "Adapted security instruction"),
 ("lea", "Vous n'êtes pas le garde du corps des bijoux?",
  "Aren't you the jewelry bodyguard?",
  [(215, "Vous n'êtes pas le garde du corps des bijoux ?")], ""),
 ("theo", "Je protège la sécurité de la chambre.",
  "I protect the security of the room.",
  [(222, "la chambre 403.")], "Adapted security role"),
 ("lea", "Quoi, alors? Antiterrorisme?",
  "What then? Counter-terrorism?",
  [(216, "Quoi, alors ? Antiterrorisme ?")], ""),
 ("theo", "Ici Renard. J'ai une certaine Martel à la chambre 403.",
  "Renard here. I have a certain Martel at room 403.",
  [(222, "Ici Renard. J'ai une certaine Martel à la chambre 403.")], ""),
 ("lea", "Une certaine Martel? Je suis son agent exclusif!",
  "A certain Martel? I am her exclusive agent!",
  [(218, "l'agent de Juliette Binoche.")], "Adapted indignant reaction"),
 ("theo", "Je vérifie les autorisations.",
  "I am checking the authorizations.",
  [(223, "D'accord, j'ai compris.")], "Adapted security procedure"),
 ("lea", "Ne mettez pas vos grosses pattes partout.",
  "Do not put your big paws everywhere.",
  [(220, "Ne mettez pas vos grosses pattes partout.")], ""),
 ("lea", "Pas vous, bien sûr.",
  "Not you, of course.",
  [(221, "Pas vous, bien sûr.")], ""),
 ("theo", "D'accord, j'ai compris.",
  "Okay, I understand.",
  [(223, "D'accord, j'ai compris.")], ""),
 ("theo", "C'est bon, vous pouvez entrer.",
  "It is all right, you can go in.",
  [(227, "C'est bon, vous pouvez entrer.")], ""),
 ("lea", "Merci beaucoup, Renard.",
  "Thank you very much, Renard.",
  [(228, "Merci... Renard.")], ""),
 ("theo", "Bonne journée, madame.",
  "Have a good day, madam.",
  [(217, "madame ?")], "Adapted polite closing"),
]

OPENER = "Let's explore the conversation line by line and unpack the French phrases."

WALK = [
 (0, None,
  "'I deduce that the Chopard jewelry has arrived. Hello.' Andrea remarks on the imposing security guard. "
  "The verb 'deduire' expresses logical deduction from visual evidence."),
 (1, None,
  "'Who are you, madam?' Renard demands formal identification. "
  "The interrogative pronoun 'qui' introduces a direct question."),
 (2, None,
  "'Andrea Martel, Juliette Binoche's agent.' Andrea introduces herself with authority. "
  "The noun 'agent' specifies her professional role representing the star."),
 (3, None,
  "'You must wait here, madam.' Renard blocks the entrance impassively. "
  "The modal verb 'devez attendre' conveys a strict administrative order."),
 (4, None,
  "'Aren't you the jewelry bodyguard?' Andrea quips about his defensive presence. "
  "The compound noun 'garde du corps' denotes a personal bodyguard."),
 (5, None,
  "'I protect the security of the room.' Renard defines his strict protective mission. "
  "The verb 'proteger' governs the direct object noun phrase 'la securite'."),
 (6, None,
  "'What then? Counter-terrorism?' Andrea teases his solemn demeanor. "
  "The technical noun 'antiterrorisme' humorously exaggerates the security level."),
 (7, None,
  "'Renard here. I have a certain Martel at room 403.' Renard radios his central command. "
  "The adjective 'certaine' conveys cool, detached impersonality."),
 (8, None,
  "'A certain Martel? I am her exclusive agent!' Andrea bristles at being treated like a stranger. "
  "The adjective 'exclusif' highlights her indispensable status."),
 (9, None,
  "'I am checking the authorizations.' Renard follows protocol without emotion. "
  "The verb 'verifier' denotes a routine security check."),
 (10, None,
  "'Do not put your big paws everywhere.' Andrea snaps into her phone while waiting. "
  "The colloquial noun 'pattes' refers metaphorically to clumsy hands."),
 (11, None,
  "'Not you, of course.' Andrea quickly clarifies her phone insult to the guard. "
  "The polite exception 'pas vous' prevents an awkward misunderstanding."),
 (12, None,
  "'Okay, I understand.' Renard receives confirmation on his radio. "
  "The phrase 'j'ai compris' signals receipt of clearance."),
 (13, None,
  "'It is all right, you can go in.' Renard steps aside to permit entry. "
  "The colloquial expression 'c'est bon' grants permission to enter."),
 (14, None,
  "'Thank you very much, Renard.' Andrea acknowledges the bodyguard with cool irony. "
  "The formal thanks are addressed directly using the guard's radio call sign."),
 (15, None,
  "'Have a good day, madam.' Renard concludes the exchange with professional courtesy. "
  "The courteous formula 'bonne journee' wraps up the gatekeeper encounter."),
]

TRANSITION = "Now let's listen to the entire dialogue once more to lock in what you have learned."

OUTRO = ("Andrea encounters rigorous security outside Juliette Binoche's suite. "
         "After radioing for clearance, the taciturn bodyguard Renard grants Andrea access to her star.")
CLOSING = ("theo", "C'est bon, vous pouvez entrer.")
