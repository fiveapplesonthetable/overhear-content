# Authoring module for dix-pour-cent s02e06 scene 03 (cues 78-83).
# Build: python3 tools/compose.py out/dix-pour-cent/s02e06/authoring/scene-03.py --out out/dix-pour-cent/s02e06/scene-03.json

ID = "dix-pour-cent-s02e06-scene-03"
SHOW = "dix-pour-cent"
SEASON = 2
EPISODE = 6
SCENE = 3
TITLE = "Garder Jean Gabin  (Looking After Jean Gabin)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "herve": "theo"}
LABELS = {"lea": "Arlette", "herve": "Hervé"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S02E06"
SOURCE_FILE = "sources/dix-pour-cent/s02/e06.fr.dual.srt"
SOURCE_NOTE = ("Cues 78-83. Arlette asks Hervé to dog-sit Jean Gabin while she attends Cannes, "
               "explaining the dog's unfortunate habit around evening dresses. Adapted for A1 French.")

INTRO = ("Before packing her bags for the Cannes Film Festival, senior agent Arlette approaches assistant Herve with a personal favor. "
         "She needs someone trustworthy to look after her beloved dog, Jean Gabin, during the glamorous two-week event. "
         "Let's listen to their playful conversation in French first.")

STORY = [
 ("lea", "Dis-moi une chose, mon cher Hervé.",
  "Tell me one thing, my dear Herve.",
  [(78, "Dis-moi, Hervé...")], "Opened friendly conversation"),
 ("herve", "Oui Arlette, qu'est-ce qu'il y a?",
  "Yes Arlette, what is the matter?",
  [(78, "Dis-moi, Hervé...")], "Inquired politely"),
 ("lea", "Tu peux t'occuper de Jean Gabin?",
  "Can you take care of Jean Gabin?",
  [(79, "Tu peux t'occuper de Jean Gabin ?")], "Asked pet sitting favor"),
 ("herve", "Tu ne l'emmènes pas à Cannes?",
  "You are not taking him to Cannes?",
  [(80, "Je ne peux pas l'emmener à Cannes,")], "Asked about travel plans"),
 ("lea", "Non, c'est impossible avec les robes.",
  "No, that is impossible with the dresses.",
  [(80, "il prend les robes du soir pour des lampadaires.")], "Stated practical incompatibility"),
 ("herve", "Pourquoi est-ce impossible avec les robes?",
  "Why is it impossible with the dresses?",
  [(80, "il prend les robes du soir pour des lampadaires.")], "Asked for clarification"),
 ("lea", "Il prend les robes pour des lampadaires!",
  "He takes dresses for lampposts!",
  [(80, "il prend les robes du soir pour des lampadaires.")], "Shared humorous habit"),
 ("herve", "C'est une très mauvaise habitude, en effet.",
  "That is a very bad habit, indeed.",
  [(80, "lampadaires.")], "Acknowledged humorous problem"),
 ("lea", "S'il te plaît, accepte de le garder.",
  "Please, agree to look after him.",
  [(81, "S'il te plaît.")], "Pleaded courteously"),
 ("herve", "Je n'ai jamais eu de chien chez moi.",
  "I have never had a dog at my place.",
  [(83, "Tu voudras le garder.")], "Noted inexperience"),
 ("lea", "Il est très doux et très sage.",
  "He is very gentle and very well-behaved.",
  [(82, "Il te fera du bien.")], "Described gentle temperament"),
 ("herve", "Et s'il s'ennuie sans toi?",
  "And what if he gets bored without you?",
  [(82, "Il te fera du bien.")], "Expressed caring worry"),
 ("lea", "Il te fera beaucoup de bien, tu verras.",
  "He will do you a lot of good, you will see.",
  [(82, "Il te fera du bien.")], "Promised warm companionship"),
 ("herve", "D'accord, amène-le ce soir chez moi.",
  "All right, bring him tonight to my place.",
  [(83, "S'il te plaît !")], "Agreed to dog-sit"),
]

OPENER = "Let's examine how Arlette convinces Herve to dog-sit during the festival."

WALK = [
 (0, None,
  "'Tell me one thing, my dear Herve.' A polite conversational opening setting an affectionate personal tone."),
 (1, None,
  "'Yes Arlette, what is the matter?' A ready inquiry asking for clarification."),
 (2, None,
  "'Can you take care of Jean Gabin?' A direct pronominal request asking for pet sitting help."),
 (3, None,
  "'You are not taking him to Cannes?' A surprised negative question inquiring about festival company."),
 (4, None,
  "'No, that is impossible with the dresses.' A blunt negative asserting high-fashion incompatibility."),
 (5, None,
  "'Why is it impossible with the dresses?' An interrogative phrase seeking practical explanation."),
 (6, None,
  "'He takes dresses for lampposts!' A humorous idiom illustrating the dog's mischievous outdoor habit."),
 (7, None,
  "'That is a very bad habit, indeed.' An amused acknowledgment conceding canine misbehavior."),
 (8, None,
  "'Please, agree to look after him.' A courteous imperative pleading for temporary pet care."),
 (9, None,
  "'I have never had a dog at my place.' A past experience statement noting domestic inexperience."),
 (10, None,
  "'He is very gentle and very well-behaved.' Complementary descriptive adjectives praising pet temperament."),
 (11, None,
  "'And what if he gets bored without you?' A conditional question worrying about separation anxiety."),
 (12, None,
  "'He will do you a lot of good, you will see.' A reassuring prediction promising beneficial companionship."),
 (13, None,
  "'All right, bring him tonight to my place.' An agreeable consent arranging evening handover."),
]

TRANSITION = "Now let's listen to Arlette and Herve again at full speed."

OUTRO = ("Herve agrees to look after Jean Gabin, finding comfort in canine company while remaining in Paris. "
         "Arlette departs for Cannes knowing her faithful companion is in caring hands.")

CLOSING = ("lea", "Merci de tout cœur, Hervé.")
