# Authoring module for dix-pour-cent s04e01 scene 12 (cues 654-660).
# Build: python3 tools/compose.py overhear-content/out/dix-pour-cent/s04e01/authoring/scene-12.py --out overhear-content/out/dix-pour-cent/s04e01/scene-12.json

ID = "dix-pour-cent-s04e01-scene-12"
SHOW = "dix-pour-cent"
SEASON = 4
EPISODE = 1
SCENE = 12
TITLE = "La frayeur du soir  (The Evening Fright)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "colette": "emilie"}
LABELS = {"lea": "Andréa", "colette": "Colette"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S04E01"
SOURCE_FILE = "sources/dix-pour-cent/s04/e01.fr.dual.srt"
SOURCE_NOTE = ("Cues 654-660. Returning home late, Andréa accidentally startles "
               "Colette holding baby Flora in the hallway.")

INTRO = ("Returning home late to their dark apartment, Andrea accidentally startles Colette in the hallway. "
         "Holding baby Flora in her arms, Colette tries to calm the crying child while Andrea apologizes. "
         "Let's listen to their conversation in French first.")

OPENER = "Let's examine the conversation line by line and explore the French expressions."
TRANSITION = "Now let's listen to the complete discussion once more to reinforce the vocabulary."

STORY = [
 ("lea", "Ah, je suis désolée, Colette!",
  "Ah, I am sorry, Colette!",
  [(654, "Je suis désolée")], "Apologizing"),
 ("colette", "Tu m'as fait peur dans l'entrée.",
  "You scared me in the hallway.",
  [(655, "Tu m'as fait peur")], "Expressing shock"),
 ("lea", "Je ne t'avais pas vue ici.",
  "I had not seen you here.",
  [(656, "Je ne t'avais pas vue")], "Explaining surprise"),
 ("colette", "Flora s'est réveillée en sursaut.",
  "Flora woke up with a start.",
  [(655, "Tu m'as fait peur")], "Noting baby"),
 ("lea", "Excuse-moi, je rentre trop tard.",
  "Forgive me, I return too late.",
  [(658, "Excuse-moi")], "Admitting lateness"),
 ("colette", "Elle pleure depuis une heure entière.",
  "She is crying for a whole hour.",
  [(658, "Excuse-moi")], "Sharing fatigue"),
 ("lea", "Donne-moi le bébé un instant.",
  "Give me the baby a moment.",
  [(658, "Tiens")], "Offering help"),
 ("colette", "Viens là, ma petite fille chérie.",
  "Come here, my darling little girl.",
  [(659, "Viens là")], "Comforting infant"),
 ("lea", "Je peux la bercer doucement.",
  "I can rock her gently.",
  [(659, "Viens là")], "Offering care"),
 ("colette", "Là, là, maman est là.",
  "There, there, mommy is here.",
  [(660, "Maman est là")], "Soothing child"),
 ("lea", "Elle commence à se calmer enfin.",
  "She begins to calm down at last.",
  [(660, "Maman est là")], "Observing calm"),
 ("colette", "Cette journée a été très difficile.",
  "This day was very difficult.",
  [(654, "Je suis désolée")], "Sighing softly"),
 ("lea", "Repose-toi, je prends le relais.",
  "Rest, I take over now.",
  [(658, "Excuse-moi")], "Reassuring partner"),
 ("colette", "Merci Andréa, j'en avais grand besoin.",
  "Thank you Andrea, I really needed it.",
  [(658, "Excuse-moi")], "Expressing gratitude"),
]

WALK = [
 (0, None,
  "'Ah, I am sorry, Colette!' Andrea expresses her immediate remorse. "
  "The feminine past participle 'desolee' agrees with the speaker."),
 (1, None,
  "'You scared me in the hallway.' Colette explains her sudden shock. "
  "The idiom 'faire peur a quelqu'un' means to frighten someone."),
 (2, None,
  "'I had not seen you here.' Andrea explains why she made a noise. "
  "The plus-que-parfait 'avais pas vue' describes an earlier state."),
 (3, None,
  "'Flora woke up with a start.' Colette points to the startled baby. "
  "The reflexive verb 'se reveiller' indicates waking up."),
 (4, None,
  "'Forgive me, I return too late.' Andrea acknowledges her late arrival. "
  "The adverbial locution 'trop tard' signals an excessive delay."),
 (5, None,
  "'She is crying for a whole hour.' Colette describes the prolonged distress. "
  "The preposition 'depuis' indicates an ongoing action started in the past."),
 (6, None,
  "'Give me the baby a moment.' Andrea offers to take the child. "
  "The imperative 'donne-moi' makes a direct caring request."),
 (7, None,
  "'Come here, my darling little girl.' Colette speaks tenderly to her daughter. "
  "The affectionate term 'cherie' expresses motherly love."),
 (8, None,
  "'I can rock her gently.' Andrea offers a soothing gesture. "
  "The verb 'bercer' means to rock or cradle an infant."),
 (9, None,
  "'There, there, mommy is here.' Colette reassures baby Flora softly. "
  "The repeated interjection 'la, la' is common when comforting children."),
 (10, None,
  "'She begins to calm down at last.' Andrea notices the baby relaxing. "
  "The pronominal verb 'se calmer' means to quiet down."),
 (11, None,
  "'This day was very difficult.' Colette sighs under the weight of fatigue. "
  "The adjective 'difficile' describes an arduous daily experience."),
 (12, None,
  "'Rest, I take over now.' Andrea encourages Colette to take a break. "
  "The idiom 'prendre le relais' means to take over duties."),
 (13, None,
  "'Thank you Andrea, I really needed it.' Colette accepts the welcome relief. "
  "The expression 'avoir grand besoin' highlights an urgent necessity."),
]

OUTRO = ("Andrea steps in to support Colette with baby Flora after a long day at ASK. "
         "Balancing demanding agency duties and family life remains a daily challenge for Andrea. "
         "Now, let's review the scene one last time.")

CLOSING = ("colette", "Merci Andréa, j'en avais grand besoin.")
