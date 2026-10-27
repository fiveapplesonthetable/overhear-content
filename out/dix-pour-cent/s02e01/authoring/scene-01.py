# Authoring module for dix-pour-cent s02e01 scene 01 (cues 1-26).
# Build: python3 tools/compose.py out/dix-pour-cent/s02e01/authoring/scene-01.py --out out/dix-pour-cent/s02e01/scene-01.json

ID = "dix-pour-cent-s02e01-scene-01"
SHOW = "dix-pour-cent"
SEASON = 2
EPISODE = 1
SCENE = 1
TITLE = "Interview télévisée de Virginie et Ramzy  (TV Interview of Virginie and Ramzy)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "ramzy": "marcel", "journaliste": "theo"}
LABELS = {"lea": "Virginie", "ramzy": "Ramzy", "journaliste": "Journaliste"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S02E01"
SOURCE_FILE = "sources/dix-pour-cent/s02/e01.fr.dual.srt"
SOURCE_NOTE = ("Cues 1-26. Virginie Efira and Ramzy Bedia participate in a TV interview, "
               "projecting the image of a perfect couple and boasting about their equal pay. "
               "Adapted for A1 French.")

INTRO = ("Actors Virginie Efira and Ramzy Bedia are guests on a television talk show to promote their new comedy. "
         "They present themselves as the ideal celebrity couple, proud of their shared life and equal earnings. "
         "Let's listen to the interview in French first.")

STORY = [
 ("journaliste", "Vous vivez ensemble depuis de nombreuses années.",
  "You have lived together for many years.",
  [(2, "vous vivez ensemble depuis de nombreuses années")], ""),
 ("journaliste", "Et c'est votre premier film ensemble!",
  "And this is your first film together!",
  [(5, "c'est votre premier film ensemble.")], ""),
 ("journaliste", "Qu'est-ce qui vous a décidés à faire ce film?",
  "What made you decide to make this film?",
  [(6, "Qu'est-ce qui vous a décidés à faire ce film ?")], ""),
 ("lea", "Avec nos plannings, on ne se voit jamais.",
  "With our schedules, we never see each other.",
  [(8, "avec nos plannings"), (8, "on ne se voit jamais.")], "Simplified 'plannings de tournage' to 'plannings'"),
 ("journaliste", "Recevoir le même cachet était important pour vous?",
  "Was receiving the same fee important to you?",
  [(11, "recevoir le même cachet était important pour vous")], ""),
 ("ramzy", "Pour moi, oui!",
  "For me, yes!",
  [(12, "Pour moi, oui !")], ""),
 ("lea", "L'égalité des salaires est importante dans tous les métiers.",
  "Equal pay is important in every profession.",
  [(13, "L'égalité des salaires est importante dans tous les métiers.")], ""),
 ("ramzy", "Deux cachets égaux, sur le même compte.",
  "Two equal fees, into the same account.",
  [(15, "Deux cachets égaux, sur le même compte.")], ""),
 ("lea", "Tout le monde est content, même notre agent.",
  "Everyone is happy, even our agent.",
  [(16, "Tout le monde est content, même notre agent.")], ""),
 ("journaliste", "Vous avez le même agent?",
  "Do you have the same agent?",
  [(18, "Vous avez le même agent ?")], ""),
 ("ramzy", "On partage tout. Absolument tout.",
  "We share everything. Absolutely everything.",
  [(19, "On partage tout."), (20, "Absolument tout.")], ""),
 ("journaliste", "Bonne chance pour le film! Vous êtes angoissés?",
  "Good luck with the film! Are you anxious?",
  [(21, "Bonne chance pour le film"), (22, "Vous êtes angoissés ?")], ""),
 ("ramzy", "Jamais, je suis un pro.",
  "Never, I am a pro.",
  [(23, "Jamais, je suis un pro.")], ""),
 ("lea", "Ça va aller. Merci beaucoup.",
  "It will be fine. Thank you very much.",
  [(25, "Ça va aller."), (26, "Merci beaucoup.")], ""),
]

OPENER = "Let's examine how the couple answers questions during their television interview."

WALK = [
 (0, None,
  "'You have lived together for many years.' Notice the present tense with a duration preposition describing an ongoing state."),
 (1, None,
  "'And this is your first film together!' The presentative expression with a possessive adjective and an ordinal number."),
 (2, None,
  "'What made you decide to make this film?' A question formed with a past participle agreeing with the plural object."),
 (3, None,
  "'With our schedules, we never see each other.' The indefinite subject pronoun followed by a reflexive reciprocal verb."),
 (4, None,
  "'Was receiving the same fee important to you?' An infinitive functioning as the subject of the imperfect verb."),
 (5, None,
  "'For me, yes!' A short emphatic answer with an indirect pronoun."),
 (6, None,
  "'Equal pay is important in every profession.' An abstract noun phrase followed by a universal indefinite adjective."),
 (7, None,
  "'Two equal fees, into the same account.' A plural adjective modifying the noun fee in financial contexts."),
 (8, None,
  "'Everyone is happy, even our agent.' The idiomatic phrase meaning everybody followed by an adverb meaning even."),
 (9, None,
  "'Do you have the same agent?' A straightforward question checking a surprising professional arrangement."),
 (10, None,
  "'We share everything. Absolutely everything.' The verb meaning to share followed by an intensifying adverb."),
 (11, None,
  "'Good luck with the film! Are you anxious?' A polite well-wishing expression followed by a plural adjective."),
 (12, None,
  "'Never, I am a pro.' A negative frequency adverb followed by the verb to be."),
 (13, None,
  "'It will be fine. Thank you very much.' A reassuring conversational formula ending with gratitude."),
]

TRANSITION = "Now let's listen to the whole interview again at natural speed."

OUTRO = ("Virginie and Ramzy seem completely united on screen, but fame and intense schedules "
         "put heavy pressure on their relationship. In the next scene, a sudden crisis will threaten everything.")

CLOSING = ("lea", "Merci beaucoup.")
