# Authoring module for dix-pour-cent s03e03 scene 01 (cues 1-103).
# Build: python3 tools/compose.py out/dix-pour-cent/s03e03/authoring/scene-01.py --out out/dix-pour-cent/s03e03/scene-01.json

ID = "dix-pour-cent-s03e03-scene-01"
SHOW = "dix-pour-cent"
SEASON = 3
EPISODE = 3
SCENE = 1
TITLE = "Une chance pour Samy  (A Chance for Samy)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "gerard": "marcel", "mathias": "theo"}
LABELS = {"lea": "Samy", "gerard": "Gérard", "mathias": "Mathias"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S03E03"
SOURCE_FILE = "sources/dix-pour-cent/s03/e03.fr.dual.srt"
SOURCE_NOTE = ("Cues 1-103. Gérard Lanvin and Mathias offer café waiter Samy a screen test for a bodyguard role in their film. Adapted for A1 French.")

INTRO = ("At a Parisian cafe, agent Mathias Barneville meets his star client Gerard Lanvin to discuss shooting dates. "
         "Noticing that their ambitious young waiter Samy dreams of acting, Gerard suggests giving him a screen test for a bodyguard role. "
         "Let's listen to the scene in French first.")

STORY = [
 ("mathias", "Samy, viens voir une minute.",
  "Samy, come see for a minute.",
  [(65, "Samy !"), (66, "Viens voir.")], "Summoned young waiter"),
 ("lea", "Oui, monsieur Barneville, j'arrive.",
  "Yes, Mr. Barneville, I am coming.",
  [(67, "Yes.")], "Answered promptly"),
 ("gerard", "Tu veux toujours faire du cinéma?",
  "Do you still want to do cinema?",
  [(68, "Ça t'intéresse toujours, le cinéma ?")], "Inquired about acting dream"),
 ("lea", "Oui, c'est mon grand rêve!",
  "Yes, it is my great dream!",
  [(70, "Oui.")], "Affirmed passion for cinema"),
 ("gerard", "Tu veux passer un casting?",
  "Do you want to audition?",
  [(71, "Tu veux passer un casting ?")], "Offered screen test"),
 ("lea", "Un casting? Vous êtes sérieux?",
  "An audition? Are you serious?",
  [(72, "Un casting ?"), (73, "Vous êtes sérieux ?")], "Expressed astonished excitement"),
 ("gerard", "C'est pour mon film À cran.",
  "It is for my film A cran.",
  [(75, "Pour ce film-là ? À cran ?")], "Specified the production title"),
 ("mathias", "As-tu un CV et des photos?",
  "Do you have a resume and photos?",
  [(77, "Vous avez un CV et des photos ?")], "Checked required actor portfolio"),
 ("lea", "J'ai tout dans mon sac.",
  "I have everything in my bag.",
  [(78, "Oui, j'ai tout ça."), (79, "Par contre, c'est dans mon sac.")], "Confirmed materials ready"),
 ("mathias", "Apporte-les tout de suite.",
  "Bring them right away.",
  [(80, "Je vous le ramène tout de suite.")], "Instructed prompt delivery"),
 ("lea", "Vous réalisez mon rêve aujourd'hui!",
  "You are making my dream come true today!",
  [(83, "c'est un rêve, là, que vous êtes en train de réaliser.")], "Voiced heartfelt gratitude"),
 ("mathias", "Attention, ce sont juste des essais.",
  "Careful, these are just screen tests.",
  [(84, "Attends, attends."), (85, "C'est des essais.")], "Grounded expectations"),
 ("gerard", "Si tu réussis, le rôle est à toi.",
  "If you succeed, the role is yours.",
  [(86, "Si tu les rates, on ne peut plus rien pour toi.")], "Encouraged young talent"),
 ("lea", "Merci, je vais donner le meilleur!",
  "Thank you, I will give my best!",
  [(87, "Ah non, mais il n'y a pas de problème.")], "Promised wholehearted effort"),
]

OPENER = "Let's observe as Gerard and Mathias offer Samy a screen test for the movie."

WALK = [
 (0, None,
  "'Samy, come see for a minute.' An informal call summoning the waiter for a conversation."),
 (1, None,
  "'Yes, Mr. Barneville, I am coming.' A polite affirmative answer confirming immediate arrival."),
 (2, None,
  "'Do you still want to do cinema?' An informal inquiry about artistic ambition in the film industry."),
 (3, None,
  "'Yes, it is my great dream!' An enthusiastic exclamation expressing genuine passion."),
 (4, None,
  "'Do you want to audition?' A direct question offering a casting opportunity."),
 (5, None,
  "'An audition? Are you serious?' A stunned reaction questioning the reality of the offer."),
 (6, None,
  "'It is for my film A cran.' A clarifying statement identifying the upcoming motion picture."),
 (7, None,
  "'Do you have a resume and photos?' A professional question checking standard actor materials."),
 (8, None,
  "'I have everything in my bag.' A confident confirmation of prepared audition documents."),
 (9, None,
  "'Bring them right away.' A direct imperative commanding immediate delivery of the files."),
 (10, None,
  "'You are making my dream come true today!' A joyous exclamation of heartfelt gratitude."),
 (11, None,
  "'Careful, these are just screen tests.' A grounding reminder setting realistic expectations."),
 (12, None,
  "'If you succeed, the role is yours.' A conditional encouragement motivating the young actor."),
 (13, None,
  "'Thank you, I will give my best!' An earnest commitment promising maximum effort."),
]

TRANSITION = "Now let's listen to Samy, Gerard, and Mathias again at full speed."

OUTRO = ("Samy rushes to fetch his resume and headshots, thrilled by the sudden opportunity offered by Gerard Lanvin. "
         "Mathias prepares to contact the production team, giving the passionate waiter a shot at the big screen.")

CLOSING = ("mathias", "Bonne chance pour tes essais.")
