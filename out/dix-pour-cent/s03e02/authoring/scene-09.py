# Authoring module for dix-pour-cent s03e02 scene 09 (cues 548-588).
# Build: python3 tools/compose.py out/dix-pour-cent/s03e02/authoring/scene-09.py --out out/dix-pour-cent/s03e02/scene-09.json

ID = "dix-pour-cent-s03e02-scene-09"
SHOW = "dix-pour-cent"
SEASON = 3
EPISODE = 2
SCENE = 9
TITLE = "Les confidences de Noémie  (Noémie's Confessions)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "theo": "theo"}
LABELS = {"lea": "Noémie", "theo": "Hervé"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S03E02"
SOURCE_FILE = "sources/dix-pour-cent/s03/e02.fr.dual.srt"
SOURCE_NOTE = ("Cues 548-588. At ASK, Hervé invites Noémie to a sold-out theater play, "
               "but Noémie reveals she cannot make it because she is still passionately dreaming about Philippe. "
               "Adapted for A1 French.")

INTRO = ("At the talent agency, Herve invites fellow assistant Noemie to an exclusive theater show. "
         "When Noemie declines, Herve questions her and learns that she is still deeply captivated by memories of Philippe. "
         "Let's listen to the scene in French first.")

STORY = [
 ("theo", "Noémie, tu serais libre ce soir?",
  "Noemie, would you be free tonight?",
  [(551, "Noémie ?"), (552, "Tu serais libre ce soir ?")], ""),
 ("theo", "J'ai une place pour un spectacle de théâtre complet.",
  "I have a ticket for a sold-out theater show.",
  [(554, "Pour un super spectacle de théâtre archi complet.")], "Adapted invite"),
 ("theo", "Tu pourrais être ma tête chercheuse.",
  "You could be my talent scout.",
  [(558, "tu pourrais peut-être être ma tête chercheuse.")], ""),
 ("lea", "Non, désolée, ce soir je ne peux pas du tout.",
  "No, sorry, tonight I cannot make it at all.",
  [(559, "non, désolée, ce soir, je peux pas du tout,")], "Adapted negative"),
 ("theo", "Tu ne revois pas Philippe, au moins?",
  "You are not seeing Philippe again, at least?",
  [(560, "Tu revois pas Philippe, au moins ?")], "Adapted negative"),
 ("lea", "Mais non, pas du tout!",
  "Of course not, not at all!",
  [(561, "Non.")], "Adapted denial"),
 ("theo", "Tu ne replonges pas, hein?",
  "You are not falling back into it, are you?",
  [(563, "Tu replonges pas, hein ?")], "Adapted negative"),
 ("theo", "Les amis servent à rappeler des vérités.",
  "Friends serve to remind us of truths.",
  [(566, "les amis, ça sert aussi à rappeler des vérités")], ""),
 ("lea", "On a vécu des choses très belles avec lui.",
  "We shared very beautiful things with him.",
  [(567, "on a vécu des choses très belles,")], ""),
 ("lea", "Ensemble, on se libérait vraiment.",
  "Together, we really freed ourselves.",
  [(571, "On se libérait, en fait.")], ""),
 ("lea", "On devenait différent de la vie normale.",
  "We became different from normal life.",
  [(572, "on devenait différent de ce qu'on était dans la vie.")], "Adapted comparison"),
 ("lea", "C'était vraiment incroyable entre nous.",
  "It was really incredible between us.",
  [(580, "C'était incroyable.")], "Adapted romance"),
 ("lea", "J'avais l'impression d'être une magicienne.",
  "I had the impression of being a magician.",
  [(581, "J'avais l'impression d'être une magicienne.")], ""),
 ("theo", "Noémie, cet homme est toxique pour toi.",
  "Noemie, this man is toxic for you.",
  [(564, "ce type, c'est un déchet toxique.")], "Adapted warning"),
 ("lea", "C'est difficile d'oublier des souvenirs pareils.",
  "It is hard to forget memories like that.",
  [(567, "faut pas l'oublier,")], "Adapted feeling"),
 ("theo", "Viens au théâtre avec moi pour penser à autre chose.",
  "Come to the theater with me to think about something else.",
  [(554, "spectacle de théâtre")], "Adapted closing advice"),
]

OPENER = "Let's explore the conversation line by line and unpack the French phrases."

WALK = [
 (0, None,
  "'Noemie, would you be free tonight?' Herve asks casually at the office. "
  "The conditional 'serais libre' frames a polite invitation."),
 (1, None,
  "'I have a ticket for a sold-out theater show.' Herve pitches an exclusive cultural outing. "
  "The adjective phrase 'complet' denotes a sold-out venue."),
 (2, None,
  "'You could be my talent scout.' Herve proposes that Noemie scout new actors. "
  "The idiom 'tete chercheuse' designates a talent scout."),
 (3, None,
  "'No, sorry, tonight I cannot make it at all.' Noemie turns down the offer. "
  "The emphatic negative 'pas du tout' stresses absolute unavailability."),
 (4, None,
  "'You are not seeing Philippe again, at least?' Herve suspects an illicit rendezvous. "
  "The interrogative 'au moins' seeks reassurance against backsliding."),
 (5, None,
  "'Of course not, not at all!' Noemie quickly defends herself. "
  "The phrase 'mais non' expresses indignant denial."),
 (6, None,
  "'You are not falling back into it, are you?' Herve warns against repeating past romantic mistakes. "
  "The verb 'replonger' metaphorically describes a relapse."),
 (7, None,
  "'Friends serve to remind us of truths.' Herve defines genuine friendship. "
  "The verb phrase 'servir a' expresses utility and duty."),
 (8, None,
  "'We shared very beautiful things with him.' Noemie fondly defends her past affair. "
  "The compound past 'avons vecu' recalls shared moments."),
 (9, None,
  "'Together, we really freed ourselves.' Noemie describes an exhilarating emotional escape. "
  "The reflexive verb 'se liberer' conveys personal liberation."),
 (10, None,
  "'We became different from normal life.' Noemie contrasts romance with daily routine. "
  "The imperfect 'devenait' depicts a transformative mental state."),
 (11, None,
  "'It was really incredible between us.' Noemie highlights the extraordinary passion. "
  "The adjective 'incroyable' underscores intense romance."),
 (12, None,
  "'I had the impression of being a magician.' Noemie remembers feeling uniquely powerful. "
  "The noun phrase 'une magicienne' evokes enchanting romantic influence."),
 (13, None,
  "'Noemie, this man is toxic for you.' Herve provides sobering objective advice. "
  "The adjective 'toxique' describes harmful emotional dynamics."),
 (14, None,
  "'It is hard to forget memories like that.' Noemie acknowledges lingering attachment. "
  "The infinitive 'oublier' is governed by the adjective 'difficile'."),
 (15, None,
  "'Come to the theater with me to think about something else.' Herve suggests a healthy distraction. "
  "The imperative 'viens' encourages her to join him."),
]

TRANSITION = "Now let's listen to the entire dialogue once more to lock in what you have learned."

OUTRO = ("At ASK, Herve offers Noemie a theater ticket, only to find her daydreaming about her past lover Philippe. "
         "Herve cautions her against getting hurt, urging her to move forward.")
CLOSING = ("lea", "J'avais l'impression d'être une magicienne.")
