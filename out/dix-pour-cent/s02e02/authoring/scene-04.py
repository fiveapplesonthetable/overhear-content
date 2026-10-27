# Authoring module for dix-pour-cent s02e02 scene 04 (cues 130-152).
# Build: python3 tools/compose.py out/dix-pour-cent/s02e02/authoring/scene-04.py --out out/dix-pour-cent/s02e02/scene-04.json

ID = "dix-pour-cent-s02e02-scene-04"
SHOW = "dix-pour-cent"
SEASON = 2
EPISODE = 2
SCENE = 4
TITLE = "L'audition chez Constance  (The Audition at Constance's)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "constance": "emilie"}
LABELS = {"lea": "Sofia", "constance": "Constance"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S02E02"
SOURCE_FILE = "sources/dix-pour-cent/s02/e02.fr.dual.srt"
SOURCE_NOTE = ("Cues 130-152. Sofia auditions for casting director Constance, who insults her, "
               "prompting Sofia to defend her dignity. Adapted for A1 French.")

INTRO = ("In the casting director's studio, Sofia performs a test scene for an upcoming movie. "
         "However, the harsh casting director Constance brutally interrupts her, questioning her talent and insinuating favoritism. "
         "Let's listen to the intense confrontation in French first.")

STORY = [
 ("lea", "Tiens, quelle surprise de vous croiser ici!",
  "Fancy meeting you here!",
  [(130, "Tiens, quelle surprise de vous croiser ici.")], ""),
 ("lea", "La saucisse de Morteau est spectaculaire.",
  "The Morteau sausage is spectacular.",
  [(132, "La saucisse de Morteau est spectaculaire.")], ""),
 ("constance", "Stop! Vous m'avez coupé l'appétit.",
  "Stop! You ruined my appetite.",
  [(134, "Stop."), (134, "vous m'avez coupé l'appétit.")], ""),
 ("constance", "Votre regard est vide, il ne se passe rien.",
  "Your look is blank, nothing is happening.",
  [(135, "Votre regard est vide, il ne se passe rien.")], ""),
 ("constance", "Franchement, c'est très ennuyeux.",
  "Frankly, it is very boring.",
  [(137, "Franchement, c'est ennuyeux.")], "Added intensifier 'très'"),
 ("constance", "Le personnage n'est pas compliqué.",
  "The character is not complicated.",
  [(138, "Ce n'est pas compliqué.")], "Specified subject 'le personnage'"),
 ("constance", "Elle est mignonne et elle couche pour réussir.",
  "She is cute and sleeps her way to success.",
  [(139, "Elle est mignonne, elle couche pour réussir...")], ""),
 ("constance", "Elle n'est pas si différente de vous.",
  "She is not so different from you.",
  [(140, "Pas si différente de vous.")], "Framed as complete sentence"),
 ("lea", "Pardon? Qu'est-ce que vous avez dit?",
  "Excuse me? What did you say?",
  [(142, "Pardon ?"), (143, "Qu'est-ce que vous avez dit ?")], ""),
 ("constance", "Calmez-vous, tout le monde le sait.",
  "Calm down, everyone knows it.",
  [(145, "Bon, calmez-vous !"), (146, "tout le monde le sait.")], ""),
 ("constance", "Une actrice qui couche avec son agent pour des rôles.",
  "An actress who sleeps with her agent for roles.",
  [(147, "Une actrice qui couche avec son agent")], "Added purpose phrase"),
 ("constance", "Ce rôle ne demande pas beaucoup d'efforts.",
  "This role does not require much effort.",
  [(148, "Ce rôle ne devrait pas vous demander beaucoup d'efforts.")], "Simplified modal auxiliary"),
 ("constance", "Le rôle a été écrit pour vous!",
  "The role was written for you!",
  [(150, "Le rôle a été écrit pour vous.")], ""),
 ("constance", "Allez, recommencez quand vous voulez.",
  "Come on, start again whenever you want.",
  [(151, "Allez, on y va."), (152, "Quand vous voulez...")], "Adapted prompt"),
]

OPENER = "Let's examine how Constance criticizes Sofia during the audition."

WALK = [
 (0, None,
  "'Fancy meeting you here!' Sofia performs her opening audition line with playful surprise."),
 (1, None,
  "'The Morteau sausage is spectacular.' A humorous culinary line from the audition script."),
 (2, None,
  "'Stop! You ruined my appetite.' Constance harshly cuts off the performance before Sofia can finish."),
 (3, None,
  "'Your look is blank, nothing is happening.' A blunt critical evaluation of the actress's facial expression."),
 (4, None,
  "'Frankly, it is very boring.' An honest and unvarnished reaction from the casting director."),
 (5, None,
  "'The character is not complicated.' Constance insists that the role requires little psychological depth."),
 (6, None,
  "'She is cute and sleeps her way to success.' A cynical breakdown of the female role."),
 (7, None,
  "'She is not so different from you.' A cruel personal attack aimed directly at Sofia's integrity."),
 (8, None,
  "'Excuse me? What did you say?' Sofia reacts with shock and immediate anger at the insult."),
 (9, None,
  "'Calm down, everyone knows it.' Constance dismisses Sofia's outrage with gossipy arrogance."),
 (10, None,
  "'An actress who sleeps with her agent for roles.' The casting director openly voices industry rumors."),
 (11, None,
  "'This role does not require much effort.' A snide remark belittling the effort required for the part."),
 (12, None,
  "'The role was written for you!' A poisonous compliment intended to undermine Sofia's self-worth."),
 (13, None,
  "'Come on, start again whenever you want.' Constance coldly signals that Sofia can resume the audition."),
]

TRANSITION = "Now let's listen to the cruel casting session again without stopping."

OUTRO = ("Constance's vicious remarks deeply wound Sofia, attacking both her personal life and talent. "
         "Sofia must decide whether to endure the humiliation or stand up for herself.")

CLOSING = ("lea", "Je ne couche pas pour réussir.")
