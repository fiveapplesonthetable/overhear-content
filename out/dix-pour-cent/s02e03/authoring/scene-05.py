# Authoring module for dix-pour-cent s02e03 scene 05 (cues 117-143).
# Build: python3 tools/compose.py out/dix-pour-cent/s02e03/authoring/scene-05.py --out out/dix-pour-cent/s02e03/scene-05.json

ID = "dix-pour-cent-s02e03-scene-05"
SHOW = "dix-pour-cent"
SEASON = 2
EPISODE = 3
SCENE = 5
TITLE = "Andréa et Aymeline  (Andréa and Aymeline)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "aymeline": "emilie"}
LABELS = {"lea": "Andréa", "aymeline": "Aymeline"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S02E03"
SOURCE_FILE = "sources/dix-pour-cent/s02/e03.fr.dual.srt"
SOURCE_NOTE = ("Cues 117-143. Andrea meets with model Aymeline Val in her office to pitch a serious acting career. "
               "Aymeline distances herself from commercial fashion modeling, while Andrea praises her talent. "
               "Adapted for A1 French.")

INTRO = ("In her office at ASK, Andrea welcomes high-fashion model Aymeline Val. "
         "While Aymeline insists she is not an ordinary runway model, Andrea seeks to convince her that she has a genuine future as a screen actress. "
         "Let's listen to the scene in French first.")

STORY = [
 ("lea", "Merci d'être venue pendant la Fashion Week.",
  "Thank you for coming during Fashion Week.",
  [(117, "Merci d'être venue,"), (118, "pendant la Fashion Week,")], "Andrea welcomes Aymeline"),
 ("aymeline", "Je ne fais pas de défilés.",
  "I do not do fashion shows.",
  [(119, "Je ne fais pas de défilés.")], "Aymeline clarifies her work"),
 ("lea", "Je pensais que tu étais mannequin.",
  "I thought you were a model.",
  [(120, "en tant que mannequin...")], "Andrea asks"),
 ("aymeline", "Je suis juste payée pour porter des vêtements.",
  "I am just paid to wear clothes.",
  [(121, "Je suis juste payée pour porter des vêtements.")], "Aymeline downplays modeling"),
 ("lea", "Mais tu poses dans des magazines.",
  "But you pose in magazines.",
  [(122, "Tu poses dans des magazines...")], "Andrea counters"),
 ("aymeline", "Je travaille avec des artistes photographes.",
  "I work with photographic artists.",
  [(123, "je travaille avec des artistes photographes.")], "Aymeline emphasizes art"),
 ("lea", "D'abord, on ouvre la fenêtre pour fumer.",
  "First, we open the window to smoke.",
  [(127, "D'abord, on ouvre la fenêtre"), (128, "avant que l'alarme incendie")], "Andrea opens the window"),
 ("lea", "Ensuite, parlons de ta future carrière.",
  "Next, let's talk about your future career.",
  [(129, "Ensuite, parlons de ta carrière."), (130, "Celle que tu pourrais avoir.")], "Andrea shifts focus"),
 ("aymeline", "J'ai déjà un agent pour la publicité.",
  "I already have an agent for advertising.",
  [(131, "J'ai déjà un agent."), (132, "Pour la pub. C'est différent.")], "Aymeline notes"),
 ("lea", "Ici, il s'agit de vrais artistes.",
  "Here, it is about real artists.",
  [(133, "Il s'agit de travailler"), (134, "avec de vrais artistes.")], "Andrea explains ASK's value"),
 ("lea", "Tu es une vraie actrice, pas un cintre.",
  "You are a real actress, not a coat hanger.",
  [(140, "Tu es une vraie actrice, pas un cintre.")], "Andrea flatters her talent"),
 ("aymeline", "Tu as des nouvelles de Norman?",
  "Do you have any news about Norman?",
  [(141, "Des nouvelles de Norman ?")], "Aymeline asks about Norman Thavaud"),
 ("lea", "Deux mois d'attente, c'est une catastrophe.",
  "Two months of waiting, it is a disaster.",
  [(142, "Deux mois d'attente. Catastrophe !")], "Andrea gives bad news"),
]

OPENER = "Let's examine Andrea and Aymeline's conversation step by step."

WALK = [
 (0, None,
  "'Thank you for coming during Fashion Week.' Andrea welcomes model Aymeline Val to her office during busy Paris Fashion Week."),
 (1, None,
  "'I do not do fashion shows.' Aymeline immediately clarifies that she does not walk in runway shows."),
 (2, None,
  "'I thought you were a model.' Andrea expresses her assumption using the imperfect tense."),
 (3, None,
  "'I am just paid to wear clothes.' Aymeline ironically reduces modeling to merely being paid to wear clothes."),
 (4, None,
  "'But you pose in magazines.' Andrea points out her editorial appearances in top publications."),
 (5, None,
  "'I work with photographic artists.' Aymeline insists that she collaborates with serious artists."),
 (6, None,
  "'First, we open the window to smoke.' Andrea opens the window so the smoke does not set off the fire alarm."),
 (7, None,
  "'Next, let's talk about your future career.' Andrea moves to the main subject: launching her acting career."),
 (8, None,
  "'I already have an agent for advertising.' Aymeline notes that she is already represented for commercials."),
 (9, None,
  "'Here, it is about real artists.' Andrea insists that cinema acting involves working with genuine auteur artists."),
 (10, None,
  "'You are a real actress, not a coat hanger.' Andrea pays her a sharp compliment to convince her she belongs on screen."),
 (11, None,
  "'Do you have any news about Norman?' Aymeline inquires about the film project with Norman Thavaud."),
 (12, None,
  "'Two months of waiting, it is a disaster.' Andrea laments the two-month delay facing the production."),
]

TRANSITION = "Now let's listen to the scene once more from start to finish."

OUTRO = ("Andrea successfully flatters Aymeline Val into considering cinema representation with ASK, "
         "even as production delays complicate the project. "
         "Let's review the key vocabulary from this meeting.")

CLOSING = ("aymeline", "Je travaille avec des artistes photographes.")
