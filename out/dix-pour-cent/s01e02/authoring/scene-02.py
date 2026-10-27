ID = "dix-pour-cent-s01e02-scene-02"
SHOW = "dix-pour-cent"
SEASON = 1
EPISODE = 2
SCENE = 2
TITLE = "Ne me tutoyez pas  (Don't Be So Familiar)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "herve": "theo", "mathias": "marcel"}
LABELS = {"lea": "Camille", "herve": "Hervé", "mathias": "Mathias"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S01E02"
SOURCE_FILE = "sources/dix-pour-cent/s01/e02.fr.dual.srt"

INTRO = ("At the florist's, Andréa just told Françoise Fabian that her whims should stop at her age, and Françoise "
         "wondered aloud why she stays with the agency. "
         "Now it's morning in the agency's lobby. Camille, the new assistant, has been working for Andréa for ten days, "
         "and she is worn out. She moans to Hervé, Gabriel's chatty assistant, then takes the lift, and Mathias gets "
         "in too. Remember: Mathias is Camille's father, and nobody at the agency knows. "
         "We'll hear it in French first; just follow the feeling of it.")

STORY = [
 ("lea", "Je travaille tous les jours jusqu'à vingt-deux heures. C'est dingue.",
  "I work until ten at night every day. It's crazy.",
  [(54, "tous les jours"), (54, "c'est dingue")], "'Travailler jusqu'après vingt-deux heures' -> 'Je travaille ... jusqu'à vingt-deux heures'"),
 ("lea", "Je suis épuisée après seulement dix jours.", "I'm exhausted after only ten days.",
  [(55, "Je suis épuisée après seulement 10 jours")], "number written out"),
 ("lea", "Comment vous faites pour avoir une vie?", "How do you all manage to have a life?",
  [(56, "Comment vous faites pour avoir une vie ?")], ""),
 ("herve", "On n'en a pas.", "We don't have one.",
  [(57, "On n'en a pas")], ""),
 ("lea", "Je suis seule depuis trois mois.", "I've been on my own for three months.",
  [(63, "depuis trois mois")], "her blunter line retold cleanly"),
 ("herve", "Trois mois, Camille! C'est malsain.", "Three months, Camille! It's unhealthy.",
  [(68, "Trois mois, Camille"), (69, "C'est malsain")], ""),
 ("lea", "Et je ne vais pas rencontrer quelqu'un ici.", "And I'm not going to meet anyone here.",
  [(66, "rencontrer quelqu'un ici")], "'je ne suis pas près de' -> 'je ne vais pas'"),
 ("herve", "Je monte à pied. Tu viens?", "I'm walking up. Are you coming?",
  [(70, "Je monte à pied. Tu viens ?")], ""),
 ("lea", "Hors de question!", "No way!",
  [(70, "Hors de question")], ""),
 ("lea", "Bonjour. Qu'est-ce qui va se passer maintenant?", "Hello. What's going to happen now?",
  [(74, "Bonjour"), (75, "Qu'est-ce qui va se passer maintenant")], "'que ton patron est...' dropped"),
 ("mathias", "Je ne sais pas. On attend l'avocat.", "I don't know. We're waiting for the lawyer.",
  [(75, "Je ne sais pas"), (76, "On attend"), (76, "l'avocat")], "'de l'avocat pour connaître les dernières volontés' simplified"),
 ("mathias", "Ne me tutoyez pas.", "Don't be so familiar.",
  [(77, "Ne me tutoyez pas")], ""),
 ("lea", "On est seuls ici.", "We're alone here.",
  [(77, "On est seuls ici")], ""),
 ("mathias", "Camille!", "Camille, stop that!",
  [(78, "Camille !")], ""),
 ("lea", "Est-ce que j'ai fait quelque chose de mal?", "Have I done something wrong?",
  [(79, "Est-ce que j'ai fait quelque chose")], "'d'inapproprié' -> 'de mal'"),
 ("mathias", "À part avoir trouvé un travail ici?", "Apart from getting a job here?",
  [(80, "À part avoir")], "'décroché un poste' -> 'trouvé un travail'"),
 ("lea", "Je fais juste mon travail. Je ne te regarde même pas.", "I'm just doing my job. I don't even look at you.",
  [(81, "Je fais juste mon travail, je ne te regarde même pas")], ""),
 ("lea", "Moi-même, je ne sais pas que je suis ta fille!", "Even I don't know that I'm your daughter!",
  [(82, "Moi-même, je ne sais pas que je suis ta fille")], ""),
]

OPENER = ("Let's take it slowly. Camille and Hervé walk in together, and she starts complaining straight away.")

WALK = [
 (0, "Je travaille tous les jours jusqu'à vingt-deux heures.",
  "'I work until ten at night every day.' On the twenty-four-hour clock, ten at night is twenty-two hours."),
 (0, "C'est dingue.",
  "'It's crazy.' A casual word, very common among young people."),
 (1, None,
  "'I'm exhausted after only ten days.' The word for exhausted takes a feminine ending, because Camille is a "
  "woman."),
 (2, None,
  "'How do you all manage to have a life?' Here the polite-looking 'you' is really the plural: she means all of "
  "the assistants. Hervé's answer is short."),
 (3, None,
  "'We don't have one.' The little word in the middle stands for 'of it', here 'of a life'. Then Camille admits "
  "something personal."),
 (4, None,
  "'I've been on my own for three months.' French uses the present tense with this word for 'since' or 'for': "
  "literally 'I am alone since three months'. In the show she puts it far more bluntly."),
 (5, None,
  "'Three months, Camille! It's unhealthy.' Hervé, who is gay and loves to tease, is outraged on her behalf."),
 (6, None,
  "'And I'm not going to meet anyone here.' The near future again, made negative: the two little negative words "
  "go around 'to go'."),
 (7, None,
  "'I'm walking up. Are you coming?' Literally 'I go up on foot'. Hervé takes the stairs, and they use the casual "
  "'you', like all the assistants."),
 (8, None,
  "'No way!' Literally 'out of the question'. Camille takes the lift, and Mathias steps in."),
 (9, "Qu'est-ce qui va se passer maintenant?",
  "'What's going to happen now?' She means now that Samuel is dead. Listen: she uses the casual 'you' with "
  "Mathias, as she does in private."),
 (10, None,
  "'I don't know. We're waiting for the lawyer.' They are waiting to hear Samuel's last wishes."),
 (11, None,
  "'Don't be so familiar.' Literally 'don't call me the casual you'. French has a verb that means 'to say the casual you to someone', and Mathias uses it in the "
  "negative, with the polite form himself. At work, he wants her to keep her distance."),
 (12, None,
  "'We're alone here.' The word for 'alone' is plural, because there are two of them."),
 (13, None,
  "'Camille!' Just her name, said as a warning."),
 (14, None,
  "'Have I done something wrong?' The two words at the start simply announce a question. Then the everyday past "
  "tense: 'I have done'."),
 (15, None,
  "'Apart from getting a job here?' That's what bothers him: she is working in his own agency."),
 (16, None,
  "'I'm just doing my job. I don't even look at you.' The word for 'even' sits right after the negative."),
 (17, None,
  "'Even I don't know that I'm your daughter!' A bitter joke: she plays along with the secret so well that she "
  "has almost forgotten it herself."),
]

TRANSITION = "Here is the whole thing once more, from the lobby to the lift."

OUTRO = ("You've just seen the casual and the polite 'you' used as a weapon, in a lift. Don't worry if it went fast; "
         "the main lines will jump out at you when you watch. See you next time.")
CLOSING = ("herve", "Allez, courage!")
