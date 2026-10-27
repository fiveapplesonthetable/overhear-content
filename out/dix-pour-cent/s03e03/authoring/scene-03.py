# Authoring module for dix-pour-cent s03e03 scene 03 (cues 214-244).
# Build: python3 tools/compose.py out/dix-pour-cent/s03e03/authoring/scene-03.py --out out/dix-pour-cent/s03e03/scene-03.json

ID = "dix-pour-cent-s03e03-scene-03"
SHOW = "dix-pour-cent"
SEASON = 3
EPISODE = 3
SCENE = 3
TITLE = "La visite de Catherine  (Catherine's Visit)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "catherine": "emilie"}
LABELS = {"lea": "Noémie", "catherine": "Catherine"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S03E03"
SOURCE_FILE = "sources/dix-pour-cent/s03/e03.fr.dual.srt"
SOURCE_NOTE = ("Cues 214-244. Catherine Barneville visits Noémie at home with a gift, and the two discuss yoga, meditation, and shamanism. Adapted for A1 French.")

INTRO = ("At her apartment, recovering assistant Noemie Leclerc receives a surprise visit from Catherine Barneville. "
         "Bringing a comforting gift to make amends for the street accident, Catherine discovers Noemie's growing interest in spiritual healing. "
         "Let's listen to the scene in French first.")

STORY = [
 ("catherine", "Bonjour Noémie, je peux entrer?",
  "Hello Noemie, may I come in?",
  [(214, "Bonjour, Noémie."), (216, "Je peux entrer ?")], "Greeted host politely"),
 ("lea", "Bonjour Catherine, entrez, je vous en prie.",
  "Hello Catherine, come in, please.",
  [(217, "Oui, oui.")], "Welcomed guest warmly"),
 ("catherine", "Ce joli pull vous va très bien.",
  "This pretty sweater suits you very well.",
  [(219, "Ça vous va bien !")], "Complimented new clothing"),
 ("lea", "Merci pour ce magnifique cadeau.",
  "Thank you for this wonderful gift.",
  [(221, "Oh non, mais merci.")], "Expressed sincere appreciation"),
 ("catherine", "C'est normal après ce terrible accident.",
  "It is natural after that terrible accident.",
  [(223, "C'est la moindre des choses.")], "Acknowledged past mishap"),
 ("lea", "Ne vous inquiétez pas, j'ai les os solides.",
  "Do not worry, I have sturdy bones.",
  [(224, "j'ai les os solides.")], "Reassured with gentle humor"),
 ("catherine", "Vous lisez un livre sur le chamanisme?",
  "Are you reading a book about shamanism?",
  [(227, "Réveillez le chamane qui est en vous.")], "Noticed spiritual book"),
 ("lea", "Oui, j'essaie de réveiller mon chamane.",
  "Yes, I am trying to awaken my shaman.",
  [(227, "Réveillez le chamane qui est en vous."), (229, "j'essaie.")], "Quoted book title playfully"),
 ("catherine", "Ce sujet spirituel m'intéresse beaucoup.",
  "This spiritual subject interests me very much.",
  [(231, "ça m'intéresse vachement.")], "Revealed personal curiosity"),
 ("lea", "Vraiment? Vous vous intéressez à ces pratiques?",
  "Really? Are you interested in these practices?",
  [(232, "Ah bon ?")], "Asked with pleasant surprise"),
 ("catherine", "Je fais de la méditation et du yoga.",
  "I do meditation and yoga.",
  [(236, "je fais de la méditation, du yoga.")], "Described mindfulness routine"),
 ("lea", "Tenez, prenez ce livre pour vous.",
  "Here, take this book for yourself.",
  [(240, "tenez, prenez-le.")], "Offered self-help book"),
 ("catherine", "Merci Noémie, vous êtes une vraie perle.",
  "Thank you Noemie, you are a real gem.",
  [(243, "Oh, vous êtes une perle.")], "Thanked host warmly"),
 ("lea", "Cette lecture vous fera du bien.",
  "This reading will do you good.",
  [(240, "tenez, prenez-le.")], "Wished positive inspiration"),
]

OPENER = "Let's observe as Catherine and Noemie share a warm moment of connection."

WALK = [
 (0, None,
  "'Hello Noemie, may I come in?' A polite greeting asking permission to enter the apartment."),
 (1, None,
  "'Hello Catherine, come in, please.' A welcoming formula inviting the visitor inside."),
 (2, None,
  "'This pretty sweater suits you very well.' A complimentary observation appreciating the gifted clothing."),
 (3, None,
  "'Thank you for this wonderful gift.' An expression of polite gratitude for the present."),
 (4, None,
  "'It is natural after that terrible accident.' An empathetic reassurance acknowledging past misfortune."),
 (5, None,
  "'Do not worry, I have sturdy bones.' A humorous physical reassurance comforting the concerned guest."),
 (6, None,
  "'Are you reading a book about shamanism?' An observant question noticing spiritual literature on the table."),
 (7, None,
  "'Yes, I am trying to awaken my shaman.' A playful literal quote echoing the self-help title."),
 (8, None,
  "'This spiritual subject interests me very much.' A genuine confession of personal curiosity in wellness."),
 (9, None,
  "'Really? Are you interested in these practices?' An intrigued inquiry exploring shared spiritual interests."),
 (10, None,
  "'I do meditation and yoga.' A personal revelation describing daily mindfulness habits."),
 (11, None,
  "'Here, take this book for yourself.' A generous imperative offering the book as an exchange."),
 (12, None,
  "'Thank you Noemie, you are a real gem.' A warm metaphor praising gracious hospitality."),
 (13, None,
  "'This reading will do you good.' A benevolent future prediction wishing mental peace."),
]

TRANSITION = "Now let's listen to Catherine and Noemie again at full speed."

OUTRO = ("Catherine and Noemie connect beyond professional boundaries, sharing thoughts on meditation and personal well-being. "
         "With mutual respect restored, their unexpected bond brings comfort to both women.")

CLOSING = ("catherine", "Je vous souhaite un prompt rétablissement.")
