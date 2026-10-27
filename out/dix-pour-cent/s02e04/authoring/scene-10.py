# Authoring module for dix-pour-cent s02e04 scene 10 (cues 251-300).
# Build: python3 tools/compose.py out/dix-pour-cent/s02e04/authoring/scene-10.py --out out/dix-pour-cent/s02e04/scene-10.json

ID = "dix-pour-cent-s02e04-scene-10"
SHOW = "dix-pour-cent"
SEASON = 2
EPISODE = 4
SCENE = 10
TITLE = "Rencontre avec Hartman  (Meeting Hartman)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "theo": "theo"}
LABELS = {"lea": "Andréa", "theo": "Sacha"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S02E04"
SOURCE_FILE = "sources/dix-pour-cent/s02/e04.fr.dual.srt"
SOURCE_NOTE = ("Cues 251-300. At his hotel suite, director Sacha Hartman explains to Andréa why he refuses "
               "to work with Isabelle Adjani. Andréa tactfully reverses his stubborn pride. "
               "Adapted for A1 French.")

INTRO = ("In his hotel suite, director Sacha Hartman vents his bitter resentment toward Isabelle Adjani after her sudden absence. "
         "Andrea listens patiently and uses sharp psychology to change his mind. "
         "Let's listen to the scene in French first.")

STORY = [
 ("lea", "Elle n'a pas pu venir. Elle s'en excuse.",
  "She could not come. She apologizes.",
  [(251, "Elle n'a pas pu venir. Elle s'en excuse.")], ""),
 ("theo", "C'est ridicule. Une actrice légendaire!",
  "It is ridiculous. A legendary actress!",
  [(253, "C'est ridicule."), (254, "Une actrice légendaire !")], ""),
 ("theo", "Personne ne sait mieux que moi qui est Isabelle Adjani.",
  "Nobody knows better than me who Isabelle Adjani is.",
  [(258, "Personne ne sait mieux que moi qui est Isabelle Adjani.")], ""),
 ("theo", "Enfant, j'avais les os fragiles et j'étais souvent hospitalisé.",
  "As a child, I had fragile bones and I was often hospitalized.",
  [(260, "Enfant, j'avais les os fragiles."), (263, "j'ai été hospitalisé")], "Adapted phrase"),
 ("theo", "Vous connaissez la solitude d'un enfant malade?",
  "Do you know the loneliness of a sick child?",
  [(264, "Vous connaissez la solitude d'un enfant malade ?")], ""),
 ("lea", "Non, je connais la solitude d'un enfant qui s'ennuie.",
  "No, I know the loneliness of a bored child.",
  [(265, "Non"), (266, "Je connais la solitude d'un enfant qui s'ennuie.")], ""),
 ("theo", "C'est comme ça que j'ai découvert Isabelle Adjani.",
  "That is how I discovered Isabelle Adjani.",
  [(270, "C'est comme ça que j'ai découvert Isabelle Adjani.")], ""),
 ("theo", "Elle était tout pour moi. Je voulais faire des films pour elle.",
  "She was everything to me. I wanted to make films for her.",
  [(273, "elle était tout."), (276, "Je voulais faire des films pour elle.")], ""),
 ("theo", "Je lui ai écrit, mais la réponse était froide et stupide.",
  "I wrote to her, but the reply was cold and stupid.",
  [(278, "Je lui ai écrit"), (279, "La réponse était froide, stupide...")], ""),
 ("theo", "Je ne lui pardonnerai jamais. Cette femme est morte pour moi.",
  "I will never forgive her. That woman is dead to me.",
  [(280, "Je ne lui pardonnerai jamais."), (284, "Cette femme est morte pour moi.")], ""),
 ("lea", "Elle va penser qu'elle vous intimide.",
  "She will think that she intimidates you.",
  [(287, "Ou penser qu'elle vous intimide.")], "Adapted Ou to Elle va"),
 ("theo", "N'importe quoi. Je n'ai pas peur d'elle.",
  "Nonsense. I am not afraid of her.",
  [(288, "N'importe quoi."), (292, "Je n'ai pas peur d'elle.")], ""),
 ("lea", "Vous savez quoi? Laissez tomber.",
  "You know what? Forget it.",
  [(295, "Vous savez quoi ? Laissez tomber.")], ""),
 ("lea", "Qu'est-ce qu'on s'en fiche de ce que pense Adjani?",
  "Who cares what Adjani thinks?",
  [(296, "Qu'est-ce qu'on s'en fiche de ce que pense Adjani ?")], ""),
 ("theo", "Je vais la voir, on va mettre les choses au clair.",
  "I am going to see her, we are going to clear things up.",
  [(299, "Je vais la voir, on va mettre les choses au clair.")], ""),
 ("lea", "Bien sûr, c'est vous qui décidez.",
  "Of course, you are the one who decides.",
  [(300, "Bien sûr, c'est vous qui décidez.")], ""),
]

OPENER = "Let's explore the conversation line by line and unpack the French phrases."

WALK = [
 (0, None,
  "'She could not come. She apologizes.' Andrea conveys Isabelle's polite excuse. "
  "The pronominal verb 's'en excuser' expresses regret or an apology for a situation."),
 (1, None,
  "'It is ridiculous. A legendary actress!' Sacha expresses his sharp frustration. "
  "The adjective 'legendaire' highlights the grand reputation of the movie star."),
 (2, None,
  "'Nobody knows better than me who Isabelle Adjani is.' Sacha asserts his deep childhood connection. "
  "The negative pronoun 'personne' combines with the comparative 'mieux que moi'."),
 (3, None,
  "'As a child, I had fragile bones and I was often hospitalized.' Sacha recalls his painful youth. "
  "The imperfect 'j'avais' describes an ongoing physiological condition during childhood."),
 (4, None,
  "'Do you know the loneliness of a sick child?' Sacha asks a poignant rhetorical question. "
  "The noun 'solitude' expresses isolation, qualified by the adjective 'malade'."),
 (5, None,
  "'No, I know the loneliness of a bored child.' Andrea replies with honest empathy. "
  "The relative clause 'qui s'ennuie' comes from the reflexive verb 's'ennuyer'."),
 (6, None,
  "'That is how I discovered Isabelle Adjani.' Sacha recounts his cinematic revelation. "
  "The idiomatic formula 'c'est comme ca que' introduces an explanatory narrative."),
 (7, None,
  "'She was everything to me. I wanted to make films for her.' Sacha describes his artistic inspiration. "
  "The pronoun 'tout' functions here as a predicate noun meaning everything in the world."),
 (8, None,
  "'I wrote to her, but the reply was cold and stupid.' Sacha shares his painful childhood rejection. "
  "The adjectives 'froide' and 'stupide' describe the hurtful letter he received."),
 (9, None,
  "'I will never forgive her. That woman is dead to me.' Sacha declares his lasting grudge. "
  "The future tense 'pardonnerai' is negated by 'ne ... jamais' with indirect pronoun 'lui'."),
 (10, None,
  "'She will think that she intimidates you.' Andrea skillfully challenges his masculine ego. "
  "The near future 'va penser' introduces a subordinate clause with the transitive verb 'intimider'."),
 (11, None,
  "'Nonsense. I am not afraid of her.' Sacha reacts defensively to the implication. "
  "The idiom 'avoir peur de' takes the stressed disjunctive pronoun 'elle'."),
 (12, None,
  "'You know what? Forget it.' Andrea pretends to abandon the negotiation. "
  "The imperative 'laissez tomber' is a common colloquial French phrase meaning drop it."),
 (13, None,
  "'Who cares what Adjani thinks?' Andrea dismisses the actress to provoke his competitive instinct. "
  "The colloquial expression 's'en ficher' means not to care at all."),
 (14, None,
  "'I am going to see her, we are going to clear things up.' Sacha resolves to confront the star directly. "
  "The idiomatic phrase 'mettre les choses au clair' means to clarify a misunderstanding."),
 (15, None,
  "'Of course, you are the one who decides.' Andrea seals her psychological triumph smoothly. "
  "The cleft sentence 'c'est vous qui' places the emphasis on the decision-maker."),
]

TRANSITION = "Now let's listen to the entire dialogue once more to lock in what you have learned."

OUTRO = ("Andrea masterfully reverses Sacha Hartman's childhood resentment by questioning his courage. "
         "Provoked by her subtle reverse psychology, Sacha agrees to meet Isabelle Adjani face to face.")
CLOSING = ("lea", "Bien sûr, c'est vous qui décidez.")
