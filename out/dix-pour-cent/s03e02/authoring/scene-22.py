# Authoring module for dix-pour-cent s03e02 scene 22 (cues 910-1006).
# Build: python3 tools/compose.py out/dix-pour-cent/s03e02/authoring/scene-22.py --out out/dix-pour-cent/s03e02/scene-22.json

ID = "dix-pour-cent-s03e02-scene-22"
SHOW = "dix-pour-cent"
SEASON = 3
EPISODE = 2
SCENE = 22
TITLE = "Tout nu à l'écran  (Completely Naked on Screen)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "gabriel": "theo"}
LABELS = {"lea": "Hervé", "gabriel": "Gabriel"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S03E02"
SOURCE_FILE = "sources/dix-pour-cent/s03/e02.fr.dual.srt"
SOURCE_NOTE = ("Cues 910-1006. Outside the cinema, Hervé confesses to Gabriel why he fled the screening: "
               "the director cut all clothed scenes, leaving Hervé exposed naked throughout the movie. Adapted for A1 French.")

INTRO = ("Standing outside the cinema doors, Herve explains why he rushed out of the preview screening room in absolute dismay. "
         "To his horror, the art-house director eliminated every single scene where Herve was wearing clothes. "
         "Let's listen to their conversation in French first.")

STORY = [
 ("lea", "Pardon d'être sorti de la salle.",
  "Sorry for leaving the screening room.",
  [(910, "Pardon, je suis sorti de la salle")], "Apologized for abrupt departure"),
 ("gabriel", "Ce n'est pas grave du tout.",
  "It is no big deal at all.",
  [(910, "c'est pas parce que le film était pas bien")], "Reassured about the departure"),
 ("lea", "Je suis à poil tout le temps!",
  "I am naked the entire time!",
  [(911, "je suis à poil tout le temps.")], "Revealed shocking screen nudity"),
 ("gabriel", "C'est un film d'auteur très audacieux.",
  "It is a very bold art film.",
  [(914, "C'est pas vraiment le mot.")], "Characterized artistic genre"),
 ("lea", "C'est tout simplement horrible pour moi.",
  "It is simply horrible for me.",
  [(913, "C'est horrible.")], "Expressed personal horror"),
 ("gabriel", "Le réalisateur a fait des choix artistiques.",
  "The director made artistic choices.",
  [(915, "au montage.")], "Defended directorial vision"),
 ("lea", "Il a coupé toutes les scènes habillées!",
  "He cut all the clothed scenes!",
  [(915, "il a tout coupé au montage.")], "Complained about edited scenes"),
 ("gabriel", "Ton jeu d'acteur reste remarquable, Hervé.",
  "Your acting remains remarkable, Herve.",
  [(916, "de toi.")], "Praised performance quality"),
 ("lea", "Ne parle surtout pas de ça à Julien.",
  "Above all do not speak of that to Julien.",
  [(919, "avec Julien")], "Requested strict confidentiality"),
 ("gabriel", "Je te promets de garder le secret.",
  "I promise you to keep the secret.",
  [(921, "Ok.")], "Pledged silence to friend"),
 ("lea", "Merci de ne rien lui dire, vraiment.",
  "Thank you for saying nothing to him, really.",
  [(923, "Et je te remercie de n'avoir rien dit à Julien,")], "Expressed heartfelt thanks"),
 ("gabriel", "Ce n'est pas à moi de parler.",
  "It is not my place to speak.",
  [(924, "C'est pas moi de le faire.")], "Acknowledged personal boundaries"),
 ("lea", "J'espère que le public comprendra ce film.",
  "I hope the public will understand this film.",
  [(927, "tout compris.")], "Wished for audience understanding"),
 ("gabriel", "Les spectateurs vont admirer ton grand courage.",
  "The viewers will admire your great courage.",
  [(932, "C'est très courageux")], "Predicted audience appreciation"),
]

OPENER = "Let's see how Herve confides his deepest artistic humiliation to an encouraging Gabriel."

WALK = [
 (0, None,
  "'Sorry for leaving the screening room.' In spoken French, the little word before 'for being' drops its final vowel and attaches with an apostrophe. In spoken French, the little word before 'for being' drops its final vowel and attaches with an apostrophe."),
 (1, None,
  "'It is no big deal at all.' A comforting reassurance minimizing the awkward exit. The adverb meaning 'not' gives the reply its conversational emphasis."),
 (2, None,
  "'I am naked the entire time!' The key noun here means 'naked', anchored by its matching French article. The key noun here means 'naked', anchored by its matching French article."),
 (3, None,
  "'It is a very bold art film.' An objective framing placing the role in an artistic context. The descriptive adjective for 'daring' agrees in gender and number with its noun."),
 (4, None,
  "'It is simply horrible for me.' The descriptive adjective for 'horrible' agrees in gender and number with its noun. The descriptive adjective for 'horrible' agrees in gender and number with its noun."),
 (5, None,
  "'The director made artistic choices.' The descriptive adjective for 'artistic' agrees in gender and number with its noun. The descriptive adjective for 'artistic' agrees in gender and number with its noun."),
 (6, None,
  "'He cut all the clothed scenes!' The verb meaning 'has' pairs naturally with the noun for 'scenes' in everyday conversation."),
 (7, None,
  "'Your acting remains remarkable, Herve.' A complimentary reassurance praising his screen performance. Notice how 'remains' leads directly into the noun meaning 'acting'."),
 (8, None,
  "'Above all do not speak of that to Julien.' The two-part French negation brackets the verb for 'speak' on both sides. The two-part French negation brackets the verb for 'speak' on both sides."),
 (9, None,
  "'I promise you to keep the secret.' A solemn pledge assuring confidentiality between friends. Notice how 'promise' leads directly into the noun meaning 'secret'."),
 (10, None,
  "'Thank you for saying nothing to him, really.' A grateful acknowledgment thanking him for discretion. The two-part negative frame surrounds 'to say' to mean 'nothing at all'."),
 (11, None,
  "'It is not my place to speak.' A respectful boundary recognizing personal privacy. Notice the classic French sandwich negation wrapping right around 'to speak'."),
 (12, None,
  "'I hope the public will understand this film.' A hopeful wish looking ahead to audience reception. The verb meaning 'I hope' pairs naturally with the noun for 'public' in everyday conversation."),
 (13, None,
  "'The viewers will admire your great courage.' An encouraging prediction supporting the artist's bravery. Notice how 'are going to' leads directly into the noun meaning 'viewers'."),
]

TRANSITION = "Now let's listen to Herve and Gabriel again at normal speed."

OUTRO = ("Reassured by Gabriel's praise for his artistic courage, Herve prepares to face the critics and the after-party buffet. "
         "Even when roles turn shockingly vulnerable, honest friendship keeps the agency united.")

CLOSING = ("gabriel", "Sois fier de ton travail, Hervé.")
