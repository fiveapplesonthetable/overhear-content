# Authoring module for dix-pour-cent s02e06 scene 09 (cues 169-207).
# Build: python3 tools/compose.py out/dix-pour-cent/s02e06/authoring/scene-09.py --out out/dix-pour-cent/s02e06/scene-09.json

ID = "dix-pour-cent-s02e06-scene-09"
SHOW = "dix-pour-cent"
SEASON = 2
EPISODE = 6
SCENE = 9
TITLE = "Le problème du smoking  (The Tuxedo Problem)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "emilie": "emilie"}
LABELS = {"lea": "Juliette", "emilie": "Andréa"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S02E06"
SOURCE_FILE = "sources/dix-pour-cent/s02/e06.fr.dual.srt"
SOURCE_NOTE = ("Cues 169-207. In Cannes, Andréa breaks the news to Juliette Binoche that she cannot wear "
               "her planned tuxedo to the opening ceremony because jury member Gong Li has chosen the same outfit. "
               "Adapted for A1 French.")

INTRO = ("At a luxury Cannes hotel suite, Andrea arrives with frustrating news for client Juliette Binoche. "
         "Another major international star has chosen the exact same tuxedo for the opening red carpet. "
         "Let's listen to the scene in French first.")

STORY = [
 ("emilie", "Bienvenue à Cannes, Juliette.",
  "Welcome to Cannes, Juliette.",
  [(171, "Bienvenue à Cannes.")], "Added Juliette"),
 ("lea", "Bonjour Andréa, comment vas-tu?",
  "Hello Andrea, how are you?",
  [(170, "Bonjour.")], "Added Andréa, comment vas-tu"),
 ("emilie", "Nous avons un problème avec le smoking.",
  "We have a problem with the tuxedo.",
  [(173, "Nous avons un problème avec le smoking.")], ""),
 ("emilie", "L'actrice chinoise Gong Li en porte un pour la cérémonie d'ouverture.",
  "The Chinese actress Gong Li is wearing one for the opening ceremony.",
  [(174, "L'actrice chinoise Gong Li,"), (175, "pour la cérémonie d'ouverture.")], ""),
 ("lea", "Un Armani aussi?",
  "An Armani too?",
  [(176, "Un Armani aussi ?")], ""),
 ("emilie", "Non, un autre créateur. Mais c'est quand même un smoking.",
  "No, another designer. But it is still a tuxedo.",
  [(176, "Non, un autre créateur."), (177, "Mais c'est quand même un smoking.")], ""),
 ("emilie", "On ne peut pas avoir deux femmes dans la même tenue en même temps.",
  "We cannot have two women in the same outfit at the same time.",
  [(178, "On ne peut pas avoir deux femmes dans la même tenue en même temps.")], ""),
 ("lea", "Mais tous les hommes peuvent s'habiller pareil!",
  "But all the men can dress the same!",
  [(179, "Mais tous les hommes peuvent s'habiller pareil !")], ""),
 ("lea", "Je me sentais très bien dans ce smoking.",
  "I felt very good in that tuxedo.",
  [(182, "Je me sentais très bien dans ce smoking.")], ""),
 ("emilie", "Je vais appeler son agent et on en discutera.",
  "I will call her agent and we will discuss it.",
  [(184, "Je vais appeler l'agent de Gong Li et on en discutera.")], "Adapted pronoun"),
 ("lea", "Ça ne servira à rien.",
  "That will be useless.",
  [(185, "Ça ne servira à rien.")], ""),
 ("emilie", "Gong Li est l'icône de L'Oréal, le partenaire principal du festival.",
  "Gong Li is the icon of L'Oreal, the main partner of the festival.",
  [(187, "Gong Li est l'icône de L'Oréal en Chine."), (188, "Le partenaire principal du festival.")], ""),
 ("emilie", "Mais nous avons une bonne nouvelle. Votre second choix a été réparé.",
  "But we have good news. Your second choice has been repaired.",
  [(190, "Mais nous avons une bonne nouvelle."), (191, "Votre second choix a été réparé.")], ""),
 ("lea", "Mais c'est toute une production! Et j'ai besoin de talons de quinze centimètres.",
  "But it is a whole production! And I need fifteen-centimeter heels.",
  [(192, "Mais c'est toute une production, avec ça."), (193, "Et j'ai besoin de talons de quinze centimètres.")], ""),
 ("emilie", "On pourrait organiser un nouvel essayage avec trois tenues.",
  "We could arrange a new fitting with three outfits.",
  [(194, "On pourrait organiser un nouvel essayage avec Dune,"), (195, "avec seulement trois tenues.")], ""),
 ("lea", "Non, je pense que ça ira très bien.",
  "No, I think that will be very fine.",
  [(197, "Non, ça ira très bien."), (198, "Je pense que ça ira très bien.")], ""),
]

OPENER = "Let's explore the conversation line by line and unpack the French phrases."

WALK = [
 (0, None,
  "'Welcome to Cannes, Juliette.' Andrea arrives at the hotel with an affectionate greeting. "
  "The formula 'bienvenue a' takes a geographical destination without an article."),
 (1, None,
  "'Hello Andrea, how are you?' Juliette welcomes her agent warmly. "
  "The polite inquiry 'comment vas-tu' uses the informal 2nd person singular."),
 (2, None,
  "'We have a problem with the tuxedo.' Andrea delivers the diplomatic wardrobe dilemma. "
  "The masculine noun 'smoking' refers specifically to a formal tuxedo or dinner jacket."),
 (3, None,
  "'The Chinese actress Gong Li is wearing one for the opening ceremony.' Andrea explains the conflict. "
  "The adverbial pronoun 'en' replaces 'un smoking' with the verb porter."),
 (4, None,
  "'An Armani too?' Juliette checks the specific fashion house. "
  "The adverb 'aussi' queries whether both outfits share the same luxury designer."),
 (5, None,
  "'No, another designer. But it is still a tuxedo.' Andrea insists on the visual clash. "
  "The concessive locution 'quand meme' underscores the visual redundancy on the red carpet."),
 (6, None,
  "'We cannot have two women in the same outfit at the same time.' Andrea states the red-carpet protocol. "
  "The phrase 'en meme temps' emphasizes simultaneous public exposure."),
 (7, None,
  "'But all the men can dress the same!' Juliette points out the unfair double standard. "
  "The reflexive verb 's'habiller' is paired with the adverbial 'pareil'."),
 (8, None,
  "'I felt very good in that tuxedo.' Juliette expresses her disappointment. "
  "The imperfect 'je me sentais' describes her prior comfort and confidence."),
 (9, None,
  "'I will call her agent and we will discuss it.' Andrea offers to negotiate a resolution. "
  "The near future 'je vais appeler' promises immediate intervention."),
 (10, None,
  "'That will be useless.' Juliette realistically assesses the balance of power. "
  "The simple future 'servira a rien' comes from the idiom servir a rien."),
 (11, None,
  "'Gong Li is the icon of L'Oreal, the main partner of the festival.' Andrea admits the corporate clout. "
  "The noun 'icone' describes a global ambassador for a cosmetics brand."),
 (12, None,
  "'But we have good news. Your second choice has been repaired.' Andrea presents an alternative. "
  "The passive structure 'a ete repare' uses the compound past auxiliary."),
 (13, None,
  "'But it is a whole production! And I need fifteen-centimeter heels.' Juliette highlights the complexity. "
  "The expression 'toute une production' denotes an elaborate and exhausting undertaking."),
 (14, None,
  "'We could arrange a new fitting with three outfits.' Andrea proposes a quick styling session. "
  "The conditional 'on pourrait organiser' suggests a practical compromise."),
 (15, None,
  "'No, I think that will be very fine.' Juliette decides to make the best of the backup gown. "
  "The colloquial future 'ca ira tres bien' accepts the solution cheerfully."),
]

TRANSITION = "Now let's listen to the entire dialogue once more to lock in what you have learned."

OUTRO = ("Andrea navigates a classic Cannes red-carpet crisis: when another A-list star wears a tuxedo, "
         "Juliette Binoche graciously pivots to her backup dress to ensure an unforgettable festival opening.")
CLOSING = ("emilie", "Mais nous avons une bonne nouvelle. Votre second choix a été réparé.")
