# Authoring module for dix-pour-cent s03e04 scene 07 (cues 441-460).
# Build: python3 tools/compose.py out/dix-pour-cent/s03e04/authoring/scene-07.py --out out/dix-pour-cent/s03e04/scene-07.json

ID = "dix-pour-cent-s03e04-scene-07"
SHOW = "dix-pour-cent"
SEASON = 3
EPISODE = 4
SCENE = 7
TITLE = "L'invitation de Catherine  (Catherine's Invitation)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "theo": "theo"}
LABELS = {"lea": "Catherine", "theo": "Mathias"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S03E04"
SOURCE_FILE = "sources/dix-pour-cent/s03/e04.fr.dual.srt"
SOURCE_NOTE = ("Cues 441-460. Catherine visits Noemie at ASK to check on her neck brace and invites her "
               "to dinner with her charming physiotherapist while Mathias watches with unease. Adapted for A1 French.")

INTRO = ("At the ASK agency, Catherine Barneville drops by to visit Noemie, who is wearing a neck brace. "
         "When Mathias arrives, Catherine reveals she has invited Noemie over for dinner with her handsome physical therapist. "
         "Let's listen to their conversation in French first.")

OPENER = "Let's explore the conversation line by line and unpack the French phrases."
TRANSITION = "Now let's listen to the entire dialogue once more to lock in what you have learned."

STORY = [
 ("theo", "Catherine, tu voulais me voir?",
  "Catherine, did you want to see me?",
  [(445, "Catherine, tu voulais me voir ?")], "Inquiring about visit"),
 ("lea", "Non mon chéri, je viens voir Noémie.",
  "No my darling, I am visiting Noemie.",
  [(446, "Non, non, mon chéri, non."), (447, "je suis venue rendre visite à notre Noémie.")], "Explaining purpose"),
 ("lea", "Elle porte un corset depuis quinze jours.",
  "She has been wearing a brace for two weeks.",
  [(442, "Et ce corset, là, vous en avez pour combien de temps ?"), (443, "Oh, je pense 15 jours minimum.")], "Brace duration"),
 ("theo", "Oui, elle doit bien se reposer.",
  "Yes, she needs to rest properly.",
  [(444, "Ah oui, quand même...")], "Agreeing on recovery"),
 ("lea", "Je la trouve vraiment très rayonnante.",
  "I find her truly very radiant.",
  [(448, "Et je suis ravie de la voir aussi rayonnante.")], "Paying compliment"),
 ("theo", "C'est gentil d'être passée à l'agence.",
  "It is kind of you to stop by the agency.",
  [(449, "Bon, ben, merci.")], "Polite thanks"),
 ("lea", "Je l'ai invitée à dîner ce soir.",
  "I invited her to dinner tonight.",
  [(451, "Qu'est-ce que vous faites ce soir ?"), (453, "Vous voulez pas venir dîner à la maison ?")], "Dinner invitation"),
 ("theo", "Tu l'as invitée chez nous?",
  "You invited her to our place?",
  [(453, "Vous voulez pas venir dîner à la maison ?")], "Surprised inquiry"),
 ("lea", "Oui, avec quelques amis très sympathiques.",
  "Yes, with a few very nice friends.",
  [(454, "J'ai invité quelques amis,")], "Guest list"),
 ("lea", "Mon kiné Alexandre sera là aussi.",
  "My physiotherapist Alexandre will be there too.",
  [(454, "dont Alexandre, mon kiné, justement.")], "Introducing Alexandre"),
 ("theo", "Tu penses que c'est une bonne idée?",
  "Do you think that is a good idea?",
  [(458, "Elle va l'adorer. Tu crois pas ?")], "Questioning matchmaking"),
 ("lea", "Il est charmant et extrêmement doué.",
  "He is charming and extremely talented.",
  [(456, "Il est extrêmement doué."), (457, "En plus d'être charmant.")], "Praising Alexandre"),
 ("lea", "Il va beaucoup l'aider pour sa rééducation.",
  "He will help her a lot with her rehabilitation.",
  [(455, "Pour votre rééducation.")], "Therapeutic benefit"),
 ("theo", "D'accord, nous verrons bien ce soir.",
  "Okay, we shall see tonight.",
  [(460, "Oh, ben, certainement.")], "Reluctant acceptance"),
]

WALK = [
 (0, None,
  "'Catherine, did you want to see me?' Mathias asks his wife about her visit. "
  "The imperfect 'tu voulais' inquires about her intention."),
 (1, None,
  "'No my darling, I am visiting Noemie.' Catherine explains she came to see Noemie. "
  "The affectionate term 'mon cheri' addresses her husband."),
 (2, None,
  "'She has been wearing a brace for two weeks.' Catherine notes Noemie's neck brace. "
  "The verb 'porter' means to wear."),
 (3, None,
  "'Yes, she needs to rest properly.' Mathias agrees on the necessity of recovery. "
  "The modal verb 'devoir' expresses an obligation."),
 (4, None,
  "'I find her truly very radiant.' Catherine compliments Noemie's healthy appearance. "
  "The feminine adjective 'rayonnante' describes someone looking bright and well."),
 (5, None,
  "'It is kind of you to stop by the agency.' Mathias acknowledges her visit politely. "
  "The adjective 'gentil' expresses appreciation."),
 (6, None,
  "'I invited her to dinner tonight.' Catherine announces the dinner invitation. "
  "The passe compose 'j'ai invitee' shows agreement with the preceding direct object."),
 (7, None,
  "'You invited her to our place?' Mathias reacts with nervous surprise. "
  "The prepositional phrase 'chez nous' means at our home."),
 (8, None,
  "'Yes, with a few very nice friends.' Catherine describes the guest list. "
  "The indefinite determiner 'quelques' introduces plural nouns."),
 (9, None,
  "'My physiotherapist Alexandre will be there too.' Catherine mentions her physical therapist. "
  "The noun 'kine' is a colloquial short form for kinesitherapeute."),
 (10, None,
  "'Do you think that is a good idea?' Mathias questions the matchmaking scheme. "
  "The verb phrase 'une bonne idee' questions her initiative."),
 (11, None,
  "'He is charming and extremely talented.' Catherine praises Alexandre's qualities. "
  "The adverb 'extremement' intensifies the adjective 'doue'."),
 (12, None,
  "'He will help her a lot with her rehabilitation.' Catherine justifies the match with therapeutic benefits. "
  "The noun 'reeducation' refers to physical therapy."),
 (13, None,
  "'Okay, we shall see tonight.' Mathias concedes with quiet hesitation. "
  "The simple future 'nous verrons' anticipates the outcome."),
]

OUTRO = ("Mathias looks uneasy as Catherine departs after organizing the unexpected dinner party. "
         "Bringing Noemie and her new physiotherapist under the same roof promises an awkward evening. "
         "Now, let's review the scene once more.")

CLOSING = ("lea", "Il va beaucoup l'aider pour sa rééducation.")
