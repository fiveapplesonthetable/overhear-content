# Authoring module for dix-pour-cent s03e01 scene 10 (cues 175-237).
# Build: python3 tools/compose.py out/dix-pour-cent/s03e01/authoring/scene-10.py --out out/dix-pour-cent/s03e01/scene-10.json

ID = "dix-pour-cent-s03e01-scene-10"
SHOW = "dix-pour-cent"
SEASON = 3
EPISODE = 1
SCENE = 10
TITLE = "La première contraction  (The First Contraction)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "theo": "theo", "emilie": "emilie"}
LABELS = {"lea": "Andréa", "theo": "Gabriel", "emilie": "Sofia"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S03E01"
SOURCE_FILE = "sources/dix-pour-cent/s03/e01.fr.dual.srt"
SOURCE_NOTE = ("Cues 175-237. At ASK, Sofia celebrates her new movie poster with Gabriel, "
               "while a heavily pregnant Andréa suddenly feels her first contraction and defends her right to work. "
               "Adapted for A1 French.")

INTRO = ("At the agency, Sofia celebrates her upcoming film poster with Gabriel. "
         "The lighthearted office mood suddenly shifts when heavily pregnant agent Andrea experiences her first contraction. "
         "Let's listen to the scene in French first.")

STORY = [
 ("emilie", "Oui, on a bossé comme des fous, tu vois.",
  "Yes, we worked like crazy, you see.",
  [(175, "Oui, on a bossé comme des fous,")], ""),
 ("theo", "J'adore l'affiche, elle est trop belle.",
  "I love the poster, it is so beautiful.",
  [(177, "J'adore l'affiche."), (178, "Elle est trop belle.")], ""),
 ("emilie", "Merci les gars! Vous me manquez beaucoup.",
  "Thanks guys! I miss you a lot.",
  [(184, "Merci, les gars."), (185, "Vous me manquez")], "Adapted gratitude"),
 ("theo", "Mais toi aussi, tu nous manques.",
  "We miss you too.",
  [(186, "Mais toi aussi.")], "Adapted reassurance"),
 ("lea", "Je vais chez Dujardin pour régler un problème.",
  "I am going to Dujardin's place to settle a problem.",
  [(193, "je vais chez Dujardin.")], "Adapted departure"),
 ("lea", "Oh, putain!",
  "Oh, damn it!",
  [(196, "Oh, putain !")], ""),
 ("theo", "Qu'est-ce qui se passe? Ça va?",
  "What is going on? Are you alright?",
  [(197, "Qu'est-ce qui se passe ? Ça va ?")], ""),
 ("lea", "Ça va, c'est rien.",
  "I am fine, it is nothing.",
  [(198, "Ça va, c'est rien.")], ""),
 ("lea", "C'est bon, c'est bon.",
  "It is okay, it is okay.",
  [(199, "C'est bon, c'est bon.")], ""),
 ("lea", "C'est juste une contraction, ça va.",
  "It is just a contraction, I am fine.",
  [(200, "C'est juste une contraction, ça va.")], ""),
 ("theo", "Elle accouche! Tu as besoin d'un médecin!",
  "She is in labor! You need a doctor!",
  [(205, "Elle accouche !")], "Adapted alarm"),
 ("lea", "Non, je n'accouche pas du tout!",
  "No, I am not in labor at all!",
  [(205, "Elle accouche !")], "Adapted denial"),
 ("theo", "Travailler autant, c'est mauvais pour le bébé.",
  "Working so much is bad for the baby.",
  [(220, "c'est mauvais pour le bébé.")], "Adapted warning"),
 ("lea", "J'aime mon travail, je ne veux pas m'arrêter.",
  "I love my work, I do not want to stop.",
  [(225, "j'aime mon travail, j'ai pas envie de m'arrêter.")], ""),
 ("theo", "Tu dois te reposer un peu, Andréa.",
  "You must rest a little, Andrea.",
  [(220, "c'est mauvais pour le bébé.")], "Adapted advice"),
 ("lea", "Personne ne me dit comment il faut que je sois enceinte!",
  "Nobody tells me how I should be pregnant!",
  [(235, "personne me dit comment il faut que je sois enceinte.")], ""),
]

OPENER = "Let's explore the conversation line by line and unpack the French phrases."

WALK = [
 (0, None,
  "'Yes, we worked like crazy, you see.' Sofia talks about the hard film shoot. "
  "The colloquial idiom 'bosser comme des fous' means to work extremely hard."),
 (1, None,
  "'I love the poster, it is so beautiful.' Gabriel expresses admiration for the promo artwork. "
  "The adjective 'belle' agrees with the feminine noun 'affiche'."),
 (2, None,
  "'Thanks guys! I miss you a lot.' Sofia expresses genuine fondness for her former coworkers. "
  "The verb 'manquer' places the persons missed as the subject."),
 (3, None,
  "'We miss you too.' Gabriel reassures her with reciprocal affection. "
  "The emphatic pronoun 'toi' highlights the mutual feeling."),
 (4, None,
  "'I am going to Dujardin's place to settle a problem.' Andrea announces her emergency client visit. "
  "The preposition 'chez' denotes going to someone's home."),
 (5, None,
  "'Oh, damn it!' Andrea groans in sudden physical distress. "
  "The colloquial exclamation expresses abrupt pain."),
 (6, None,
  "'What is going on? Are you alright?' Gabriel reacts immediately with concern. "
  "The question 'qu'est-ce qui se passe' asks what is happening."),
 (7, None,
  "'I am fine, it is nothing.' Andrea attempts to downplay the pain. "
  "The reassuring formula 'c'est rien' minimizes the medical scare."),
 (8, None,
  "'It is okay, it is okay.' Andrea repeats the phrase to steady herself. "
  "The repetition of 'c'est bon' serves to calm the anxious bystanders."),
 (9, None,
  "'It is just a contraction, I am fine.' Andrea identifies the physiological symptom. "
  "The feminine noun 'contraction' refers to pregnancy labor spasms."),
 (10, None,
  "'She is in labor! You need a doctor!' Gabriel panics dramatically. "
  "The verb 'accoucher' means to give birth."),
 (11, None,
  "'No, I am not in labor at all!' Andrea rejects his alarmist reaction. "
  "The emphatic negative 'pas du tout' firmly denies his assumption."),
 (12, None,
  "'Working so much is bad for the baby.' Gabriel cautions against overworking during pregnancy. "
  "The adjective 'mauvais' indicates a potential health risk."),
 (13, None,
  "'I love my work, I do not want to stop.' Andrea asserts her professional dedication. "
  "The verb 'arreter' is used reflexively to mean stopping activity."),
 (14, None,
  "'You must rest a little, Andrea.' Gabriel urges her to take care of her health. "
  "The reflexive infinitive 'se reposer' expresses physical rest."),
 (15, None,
  "'Nobody tells me how I should be pregnant!' Andrea vehemently asserts her personal autonomy. "
  "The negative indefinite pronoun 'personne' takes the verb modifier 'ne'."),
]

TRANSITION = "Now let's listen to the entire dialogue once more to lock in what you have learned."

OUTRO = ("Sofia visits ASK to share her poster before Andrea experiences a sudden contraction. "
         "Despite Gabriel's anxious concerns, Andrea fiercely asserts her independence and dedication to her job.")
CLOSING = ("lea", "Personne ne me dit comment il faut que je sois enceinte!")
