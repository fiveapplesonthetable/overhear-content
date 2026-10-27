# Authoring module for dix-pour-cent s03e04 scene 03 (cues 153-190).
# Build: python3 tools/compose.py out/dix-pour-cent/s03e04/authoring/scene-03.py --out out/dix-pour-cent/s03e04/scene-03.json

ID = "dix-pour-cent-s03e04-scene-03"
SHOW = "dix-pour-cent"
SEASON = 3
EPISODE = 4
SCENE = 3
TITLE = "L'avertissement de Charles  (Charles's Warning)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "mathias": "theo"}
LABELS = {"lea": "Charles", "mathias": "Mathias"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S03E04"
SOURCE_FILE = "sources/dix-pour-cent/s03/e04.fr.dual.srt"
SOURCE_NOTE = ("Cues 153-190. Lawyer Charles Hirsch discreetly warns his longtime friend Mathias about suspicious maneuvers within ASK. Adapted for A1 French.")

INTRO = ("At the Paris courthouse, attorney Charles Hirsch asks his longtime friend Mathias Barneville to meet on urgent business. "
         "Risking professional ethics, Charles discreetly warns Mathias that internal collaborators are secretly preparing to abandon ASK. "
         "Let's listen to the scene in French first.")

STORY = [
 ("lea", "Désolé de te faire venir ici.",
  "Sorry to make you come here.",
  [(153, "Désolé de t'avoir fait venir ici")], "Apologized for courthouse venue"),
 ("mathias", "Je t'en prie, je comprends parfaitement.",
  "Please, I understand perfectly.",
  [(155, "Je t'en prie.")], "Politely accepted location"),
 ("lea", "Comment se passent les affaires chez ASK?",
  "How are business matters going at ASK?",
  [(165, "Et chez ASK, alors, comment ça se passe")], "Inquired about agency health"),
 ("mathias", "Les projets s'enchaînent bien ces temps-ci.",
  "Projects keep coming along well these days.",
  [(174, "les projets s'enchaînent, c'est l'essentiel.")], "Reported steady workflow"),
 ("lea", "Nous nous connaissons depuis trente ans.",
  "We have known each other for thirty years.",
  [(177, "on se connaît depuis 30 ans,")], "Cited decades of friendship"),
 ("mathias", "Oui, tu es un ami fidèle.",
  "Yes, you are a loyal friend.",
  [(177, "on se connaît depuis 30 ans,")], "Acknowledged enduring trust"),
 ("lea", "Je ne peux pas me taire.",
  "I cannot stay silent.",
  [(178, "je ne peux pas ne rien te dire.")], "Felt duty to speak"),
 ("mathias", "Que se passe-t-il dans mon agence?",
  "What is happening inside my agency?",
  [(179, "Il se passe des choses..."), (180, "dans ton agence.")], "Asked about internal trouble"),
 ("lea", "Des collaborateurs préparent un départ secret.",
  "Collaborators are preparing a secret departure.",
  [(183, "D'autres collaborateurs."), (187, "Elle va partir.")], "Warned of planned defection"),
 ("mathias", "Parles-tu d'Andréa Martel en particulier?",
  "Are you speaking about Andrea Martel in particular?",
  [(185, "Andréa Martel ?")], "Guessed key collaborator"),
 ("lea", "Je ne peux pas violer le secret.",
  "I cannot violate professional secrecy.",
  [(186, "Je peux rien te dire.")], "Upheld confidentiality limit"),
 ("mathias", "C'est une trahison totalement inattendue!",
  "It is a totally unexpected betrayal!",
  [(184, "Tu devrais te méfier.")], "Voiced anger at betrayal"),
 ("lea", "À ta place, j'assurerais mes arrières.",
  "If I were in your place, I would watch my back.",
  [(188, "À ta place, j'assurerai mes arrières.")], "Advised defensive measures"),
 ("mathias", "Merci pour cet avertissement précieux, Charles.",
  "Thank you for this valuable warning, Charles.",
  [(190, "Merci, Charles.")], "Expressed gratitude for counsel"),
]

OPENER = "Let's observe as Charles gives Mathias a confidential warning about his agency."

WALK = [
 (0, None,
  "'Sorry to make you come here.' An apologetic opening acknowledging an inconvenient meeting place."),
 (1, None,
  "'Please, I understand perfectly.' A courteous reassurance accepting the sudden invitation."),
 (2, None,
  "'How are business matters going at ASK?' A polite inquiry opening the confidential discussion."),
 (3, None,
  "'Projects keep coming along well these days.' An optimistic update reporting continuous agency activity."),
 (4, None,
  "'We have known each other for thirty years.' A poignant reminder appealing to decades of personal trust."),
 (5, None,
  "'Yes, you are a loyal friend.' A sincere affirmation confirming mutual loyalty."),
 (6, None,
  "'I cannot stay silent.' A moral resolve declaring an inability to conceal impending danger."),
 (7, None,
  "'What is happening inside my agency?' An alarmed question sensing hidden trouble at the firm."),
 (8, None,
  "'Collaborators are preparing a secret departure.' A discreet disclosure revealing an imminent breakaway."),
 (9, None,
  "'Are you speaking about Andrea Martel in particular?' A sharp deduction guessing the ringleader's identity."),
 (10, None,
  "'I cannot violate professional secrecy.' A cautious refusal preserving statutory client privilege."),
 (11, None,
  "'It is a totally unexpected betrayal!' A shocked reaction expressing profound professional injury."),
 (12, None,
  "'If I were in your place, I would watch my back.' A direct colloquial recommendation advising self-defense."),
 (13, None,
  "'Thank you for this valuable warning, Charles.' A grateful acknowledgment thanking an old friend for the tip."),
]

TRANSITION = "Now let's listen to Charles and Mathias again at full speed."

OUTRO = ("Armed with Charles's warning, Mathias realizes that Andrea Martel and her allies are quietly organizing a mutiny. "
         "Determined to defend his life's work, Mathias prepares to take counter-measures to protect ASK.")

CLOSING = ("mathias", "Je vais surveiller cette affaire de très près.")
