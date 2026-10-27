# Authoring module for dix-pour-cent s03e05 scene 09 (cues 306-350).
# Build: python3 tools/compose.py out/dix-pour-cent/s03e05/authoring/scene-09.py --out out/dix-pour-cent/s03e05/scene-09.json

ID = "dix-pour-cent-s03e05-scene-09"
SHOW = "dix-pour-cent"
SEASON = 3
EPISODE = 5
SCENE = 9
TITLE = "La fuite de Béatrice  (Béatrice's Escape)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "arlette": "emilie"}
LABELS = {"lea": "Andréa", "arlette": "Arlette"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S03E05"
SOURCE_FILE = "sources/dix-pour-cent/s03/e05.fr.dual.srt"
SOURCE_NOTE = ("Cues 306-350. Outside ASK, Arlette informs Andrea that Beatrice Dalle walked off the set "
               "after being tricked into an unwanted nude scene. Adapted for A1 French.")

INTRO = ("Outside the agency, Arlette rushes to Andrea with alarming news from the film set. "
         "Beatrice Dalle has walked out on director Pascal after a deceitful nude scene demand. "
         "Let's listen to their conversation in French first.")

OPENER = "Let's explore the conversation line by line and unpack the French phrases."
TRANSITION = "Now let's listen to the entire dialogue once more to lock in what you have learned."

STORY = [
 ("arlette", "Andréa, Pascal vient de m'appeler.",
  "Andrea, Pascal just called me.",
  [(306, "Pascal m'a appelé")], "Reporting phone call"),
 ("arlette", "Béatrice est partie du tournage en colère.",
  "Beatrice left the shoot in anger.",
  [(307, "Béatrice est barrée du tournage")], "Walkout news"),
 ("lea", "Mais qu'est-ce qui s'est passé?",
  "But what happened?",
  [(308, "Qu'est-ce qui lui a pris encore assez de l'âme ?")], "Inquiring reason"),
 ("arlette", "Le réalisateur a menti à Béatrice.",
  "The director lied to Beatrice.",
  [(316, "Il a menti à Béatrice,")], "Revealing deceit"),
 ("arlette", "Il voulait la forcer à se déshabiller.",
  "He wanted to force her to undress.",
  [(316, "il a demandé à un acteur de la foutre à poil")], "Explaining misconduct"),
 ("lea", "C'est scandaleux, elle a eu raison.",
  "That is outrageous, she was right.",
  [(317, "Oh merde, le con")], "Supporting Beatrice"),
 ("arlette", "Mais où est Béatrice maintenant?",
  "But where is Beatrice now?",
  [(319, "Et elle est où, la Béatrice ?")], "Asking location"),
 ("lea", "Elle est montée dans un taxi rapidement.",
  "She jumped into a taxi quickly.",
  [(322, "elle a foncé dans un taxi")], "Taxi escape"),
 ("lea", "Je n'ai pas pu la rattraper.",
  "I could not catch up with her.",
  [(323, "c'était pas pratique de courir derrière")], "Stroller complication"),
 ("arlette", "Tu as essayé de lui téléphoner?",
  "Did you try phoning her?",
  [(324, "Appelle-la")], "Urging phone call"),
 ("lea", "J'arrête pas de tomber sur sa messagerie.",
  "I keep reaching her voicemail.",
  [(325, "J'arrête pas de l'appeler, je tombe sur sa messagerie")], "Voicemail frustration"),
 ("arlette", "La production menace de faire un procès.",
  "The production threatens a lawsuit.",
  [(328, "Qu'est-ce qu'on fait en attendant aussi un procès pour rupture de contrats")], "Lawsuit threat"),
 ("lea", "Attends, mon téléphone sonne enfin.",
  "Wait, my phone is ringing at last.",
  [(331, "Ah putain, ça sonne")], "Phone rings"),
 ("lea", "Allô Béatrice? Où es-tu exactement?",
  "Hello Beatrice? Where are you exactly?",
  [(333, "Allô Béatrice, ça va ? T'es où là ?")], "Answering call"),
]

WALK = [
 (0, None,
  "'Andrea, Pascal just called me.' Arlette breaks the urgent news. "
  "The recent past 'vient d'appeler' reports an immediate event."),
 (1, None,
  "'Beatrice left the shoot in anger.' Arlette explains Beatrice's sudden exit. "
  "The prepositional phrase 'en colere' expresses fury."),
 (2, None,
  "'But what happened?' Andrea reacts with concern. "
  "The interrogative phrase 'qu'est-ce qui' asks about recent events."),
 (3, None,
  "'The director lied to Beatrice.' Arlette reveals the director's deceit. "
  "The passe compose 'a menti' indicates dishonesty."),
 (4, None,
  "'He wanted to force her to undress.' Arlette explains the boundary violation. "
  "The reflexive verb 'se deshabiller' means to undress."),
 (5, None,
  "'That is outrageous, she was right.' Andrea defends her client fiercely. "
  "The idiom 'avoir raison' means to be justified."),
 (6, None,
  "'But where is Beatrice now?' Arlette asks for the actress's whereabouts. "
  "The interrogative adverb 'ou' inquires about location."),
 (7, None,
  "'She jumped into a taxi quickly.' Andrea describes Beatrice's hasty departure. "
  "The verb 'monter dans' means to get into a vehicle."),
 (8, None,
  "'I could not catch up with her.' Andrea laments that she could not run fast enough with the stroller. "
  "The verb 'rattraper' means to catch up."),
 (9, None,
  "'Did you try phoning her?' Arlette asks about phone contact. "
  "The verb 'telephoner a' takes an indirect object."),
 (10, None,
  "'I keep reaching her voicemail.' Andrea vents her frustration. "
  "The idiom 'tomber sur la messagerie' means reaching voicemail."),
 (11, None,
  "'The production threatens a lawsuit.' Arlette warns of legal repercussions. "
  "The noun 'proces' means lawsuit or trial."),
 (12, None,
  "'Wait, my phone is ringing at last.' Andrea notices an incoming call. "
  "The verb 'sonner' refers to a phone ringing."),
 (13, None,
  "'Hello Beatrice? Where are you exactly?' Andrea answers urgently. "
  "The greeting 'allo' opens phone dialogues."),
]

OUTRO = ("Andrea breathes a sigh of relief as Beatrice finally reaches out by phone. "
         "Defusing the breach-of-contract dispute will require strategic skill and patience. "
         "Now, let's review the scene once more.")

CLOSING = ("lea", "Allô Béatrice? Où es-tu exactement?")
