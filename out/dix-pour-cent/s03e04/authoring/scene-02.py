# Authoring module for dix-pour-cent s03e04 scene 02 (cues 68-152).
# Build: python3 tools/compose.py out/dix-pour-cent/s03e04/authoring/scene-02.py --out out/dix-pour-cent/s03e04/scene-02.json

ID = "dix-pour-cent-s03e04-scene-02"
SHOW = "dix-pour-cent"
SEASON = 3
EPISODE = 4
SCENE = 2
TITLE = "Dans la loge d'Isabelle  (In Isabelle's Dressing Room)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "gabriel": "theo"}
LABELS = {"lea": "Isabelle", "gabriel": "Gabriel"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S03E04"
SOURCE_FILE = "sources/dix-pour-cent/s03/e04.fr.dual.srt"
SOURCE_NOTE = ("Cues 68-152. Gabriel visits Isabelle Huppert in her dressing room between filming sessions and theatre rehearsals. Adapted for A1 French.")

INTRO = ("In her movie set dressing room, acclaimed actress Isabelle Huppert rehearses Shakespeare between grueling film shoots. "
         "Agent Gabriel Sarda drops in to check on her stamina and make sure she stays focused on her immediate shoot. "
         "Let's listen to the scene in French first.")

STORY = [
 ("gabriel", "Bonjour Isabelle, comment te sens-tu?",
  "Hello Isabelle, how are you feeling?",
  [(70, "Ça va ?"), (76, "Ça va, Gabriel ?")], "Asked after star's condition"),
 ("lea", "J'étais en train de répéter Hamlet.",
  "I was in the middle of rehearsing Hamlet.",
  [(86, "ça, c'est Hamlet."), (94, "Je joue Hamlet.")], "Shared rehearsal activity"),
 ("gabriel", "Tu joues Hamlet en mars prochain?",
  "You are playing Hamlet next March?",
  [(88, "je jouais Hamlet en mars à l'Odéon.")], "Expressed surprise at theater role"),
 ("lea", "Oui, avec la magnifique Scarlett Johansson.",
  "Yes, with the magnificent Scarlett Johansson.",
  [(117, "Scarlett Johansson."), (119, "Et c'est elle qui va jouer Ophélie.")], "Announced famous co-star"),
 ("gabriel", "Tu n'es pas trop fatiguée?",
  "Are you not too exhausted?",
  [(125, "T'es pas trop crevée, les deux tournages, là ?")], "Worried about physical strain"),
 ("lea", "Je suis lessivée mais tellement heureuse.",
  "I am wiped out but so happy.",
  [(126, "Je te cache pas, je suis lessivée")], "Confessed fatigue and joy"),
 ("gabriel", "Comment tiens-tu avec deux tournages?",
  "How do you cope with two shoots?",
  [(125, "les deux tournages")], "Asked about grueling schedule"),
 ("lea", "La fatigue me plonge dans une transe.",
  "Exhaustion plunges me into a trance.",
  [(131, "T'es comme une transe.")], "Described transcendent focus"),
 ("gabriel", "C'est un état presque euphorisant!",
  "It is an almost euphoric state!",
  [(132, "c'est très euphorisant.")], "Marveled at artistic stamina"),
 ("lea", "C'est une sensation artistique absolument divine.",
  "It is an absolutely divine artistic feeling.",
  [(132, "c'est très euphorisant.")], "Praised creative flow"),
 ("gabriel", "Prends-tu des médicaments pour tenir?",
  "Do you take medicine to keep going?",
  [(134, "Tu te drogues ?")], "Inquired about stimulants"),
 ("lea", "Ma seule drogue, ce sont les fruits secs!",
  "My only drug is dried fruit!",
  [(140, "Ma seule drogue, c'est les fruits secs.")], "Joked about healthy snacking"),
 ("gabriel", "Mets vite ton chapeau pour Delphine.",
  "Put on your hat quickly for Delphine.",
  [(149, "tu joues Delphine, dans She's a Femme Fatale."), (151, "Delphine, le chapeau.")], "Reminded of current character costume"),
 ("lea", "J'y vais, le plateau m'attend!",
  "I am going, the set is waiting for me!",
  [(147, "Yes, coming.")], "Hurried toward the cameras"),
]

OPENER = "Let's observe as Gabriel checks on Isabelle in her dressing room."

WALK = [
 (0, None,
  "'Hello Isabelle, how are you feeling?' The informal 'you' form around 'do you feel' marks a direct, personal relationship. The informal 'you' form around 'do you feel' marks a direct, personal relationship."),
 (1, None,
  "'I was in the middle of rehearsing Hamlet.' An artistic explanation accounting for theatrical intensity. Notice how 'was' leads directly into the noun meaning 'train'."),
 (2, None,
  "'You are playing Hamlet next March?' The verb meaning 'play' pairs naturally with the noun for 'March' in everyday conversation."),
 (3, None,
  "'Yes, with the magnificent Scarlett Johansson.' A short, idiomatic conversational reply that keeps the exchange moving naturally. A short, idiomatic conversational reply that keeps the exchange moving naturally."),
 (4, None,
  "'Are you not too exhausted?' The adverb meaning 'too' gives the reply its conversational emphasis."),
 (5, None,
  "'I am wiped out but so happy.' The adverb meaning 'so' gives the reply its conversational emphasis."),
 (6, None,
  "'How do you cope with two shoots?' Notice how 'do you keep up' leads directly into the noun meaning 'filming sessions'. Notice how 'do you keep up' leads directly into the noun meaning 'filming sessions'."),
 (7, None,
  "'Exhaustion plunges me into a trance.' A poetic psychological description of high-intensity artistic immersion. The reflexive pronoun sits right in front of the verb for 'plunges', turning the action back onto the subject."),
 (8, None,
  "'It is an almost euphoric state!' The descriptive adjective for 'euphoric' agrees in gender and number with its noun. The descriptive adjective for 'euphoric' agrees in gender and number with its noun."),
 (9, None,
  "'It is an absolutely divine artistic feeling.' A transcendent summary celebrating the joy of performance. The key noun here means 'sensation', anchored by its matching French article."),
 (10, None,
  "'Do you take medicine to keep going?' Inverting the verb and pronoun around 'do you take' creates a crisp, polished question. Inverting the verb and pronoun around 'do you take' creates a crisp, polished question."),
 (11, None,
  "'My only drug is dried fruit!' A humorous denial pointing to healthy natural snacks as her energy source. The key noun here means 'drug', anchored by its matching French article."),
 (12, None,
  "'Put on your hat quickly for Delphine.' The verb meaning 'put' pairs naturally with the noun for 'hat' in everyday conversation."),
 (13, None,
  "'I am going, the set is waiting for me!' A spirited departure answering the director's call to set. Dropping the subject pronoun turns the verb for 'am going' into a direct, punchy command."),
]

TRANSITION = "Now let's listen to Isabelle and Gabriel again at full speed."

OUTRO = ("Isabelle Huppert dashes onto the soundstage wearing Delphine's signature hat, energized by her endless love of performance. "
         "Gabriel watches her in admiration, relieved that her legendary spirit remains indestructible.")

CLOSING = ("gabriel", "Bon tournage pour cette scène, Isabelle.")
