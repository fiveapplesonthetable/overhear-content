# Authoring module for dix-pour-cent s02e05 scene 01 (cues 1-26).
# Build: python3 tools/compose.py out/dix-pour-cent/s02e05/authoring/scene-01.py --out out/dix-pour-cent/s02e05/scene-01.json

ID = "dix-pour-cent-s02e05-scene-01"
SHOW = "dix-pour-cent"
SEASON = 2
EPISODE = 5
SCENE = 1
TITLE = "Une balade à vélo  (Riding a Bike)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "guy": "marcel"}
LABELS = {"lea": "Hippolyte", "guy": "Guy"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S02E05"
SOURCE_FILE = "sources/dix-pour-cent/s02/e05.fr.dual.srt"
SOURCE_NOTE = ("Cues 1-26. Hippolyte Girardot tells Guy Marchand about his biking routine "
               "as they prepare to rehearse their lines on set. Adapted for A1 French.")

INTRO = ("On the movie set of a historical drama, actor Hippolyte Girardot chats with veteran star Guy Marchand. "
         "While Hippolyte describes his morning bike ride to the set, Guy prepares to rehearse his lines. "
         "Let's listen to the scene in French first.")

STORY = [
 ("lea", "Je me suis mis au vélo récemment.",
  "I took up cycling recently.",
  [(1, "Je m'y suis mis il y a quelques années.")], "Simplified temporal expression"),
 ("lea", "J'adore vraiment faire du sport le matin.",
  "I really love doing sport in the morning.",
  [(2, "J'adore ça.")], "Added routine description"),
 ("guy", "Tu fais beaucoup de kilomètres par semaine?",
  "Do you do many kilometers per week?",
  [(3, "J'essaie de faire 150 kilomètres par semaine.")], "Formulated question"),
 ("lea", "Oui, environ cent cinquante kilomètres chaque semaine.",
  "Yes, about one hundred fifty kilometers every week.",
  [(3, "J'essaie de faire 150 kilomètres par semaine.")], "Spelled out numbers"),
 ("guy", "C'est impressionnant, c'est beaucoup de route!",
  "That is impressive, that is a lot of road!",
  [(4, "C'est beaucoup.")], "Added adjective"),
 ("lea", "Je suis venu au plateau à vélo.",
  "I came to the movie set by bicycle.",
  [(5, "Je suis venu à vélo ce matin. Une heure et demie sur des petites routes.")], "Simplified commute description"),
 ("lea", "Ça m'aide à rester calme et concentré.",
  "It helps me stay calm and focused.",
  [(6, "Ça m'aide à me concentrer et à me calmer.")], "Turned to adjective state"),
 ("guy", "Moi, je dois réviser mes répliques.",
  "Me, I must go over my lines.",
  [(7, "« Elle s'appelle Marianne."), (10, "Elle était encore plus belle qu'avant. » Merde !")], "Expressed line practice"),
 ("lea", "Est-ce que vous stressez un peu aujourd'hui?",
  "Are you stressing out a bit today?",
  [(11, "Vous stressez ?")], "Expanded question"),
 ("guy", "Un peu, oui, le tournage commence.",
  "A bit, yes, shooting is starting.",
  [(12, "Un peu, oui.")], "Added context"),
 ("lea", "Vous êtes toujours impeccable dans vos films.",
  "You are always flawless in your movies.",
  [(20, "Mais vous, non, vous êtes impeccable.")], "Polite compliment"),
 ("guy", "Merci Hippolyte, c'est très gentil à vous.",
  "Thank you Hippolyte, that is very kind of you.",
  [(23, "Eh bien, merci. C'est gentil de le dire.")], "Added personal address"),
 ("lea", "Voulez-vous qu'on répète notre texte ensemble?",
  "Do you want us to rehearse our text together?",
  [(24, "Vous voulez qu'on répète les répliques ?")], "Clarified rehearsal offer"),
 ("guy", "Oui, volontiers, cela me fera du bien.",
  "Yes, gladly, that will do me good.",
  [(25, "Ça me fera du bien aussi."), (26, "Oui, volontiers. Merci.")], "Combined enthusiastic agreement"),
]

OPENER = "Let's examine how Hippolyte and Guy encourage each other before the rehearsal."

WALK = [
 (0, None,
  "'I took up cycling recently.' A pronominal idiom expressing taking up a new sporting hobby."),
 (1, None,
  "'I really love doing sport in the morning.' An enthusiastic verb of preference followed by routine."),
 (2, None,
  "'Do you do many kilometers per week?' An interrogative phrase inquiring about training distance."),
 (3, None,
  "'Yes, about one hundred fifty kilometers every week.' A cardinal distance total showing athletic discipline."),
 (4, None,
  "'That is impressive, that is a lot of road!' An appreciative exclamatory evaluation acknowledging effort."),
 (5, None,
  "'I came to the movie set by bicycle.' A compound past motion verb detailing morning commute."),
 (6, None,
  "'It helps me stay calm and focused.' A causation verb governing coordinated infinitive benefits."),
 (7, None,
  "'Me, I must go over my lines.' A stressed personal pronoun introducing professional study."),
 (8, None,
  "'Are you stressing out a bit today?' An inverted polite question checking on colleague anxiety."),
 (9, None,
  "'A bit, yes, shooting is starting.' A candid admission of tension on the first day of filming."),
 (10, None,
  "'You are always flawless in your movies.' Generous peer praise recognizing consistent screen quality."),
 (11, None,
  "'Thank you Hippolyte, that is very kind of you.' A gracious polite formula acknowledging the compliment."),
 (12, None,
  "'Do you want us to rehearse our text together?' A cooperative proposal suggesting line rehearsal."),
 (13, None,
  "'Yes, gladly, that will do me good.' An appreciative acceptance welcoming rehearsal support."),
]

TRANSITION = "Now let's listen to Hippolyte and Guy's friendly chat again at full speed."

OUTRO = ("Hippolyte and Guy share mutual respect as actors, preparing to rehearse their upcoming scene together. "
         "Their relaxed conversation masks the underlying pressure of the first day on set.")

CLOSING = ("guy", "Merci beaucoup, Hippolyte.")
