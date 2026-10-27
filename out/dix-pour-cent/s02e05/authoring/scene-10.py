# Authoring module for dix-pour-cent s02e05 scene 10 (cues 277-308).
# Build: python3 tools/compose.py out/dix-pour-cent/s02e05/authoring/scene-10.py --out out/dix-pour-cent/s02e05/scene-10.json

ID = "dix-pour-cent-s02e05-scene-10"
SHOW = "dix-pour-cent"
SEASON = 2
EPISODE = 5
SCENE = 10
TITLE = "L'histoire de Chet Baker  (The Chet Baker Story)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "theo": "theo"}
LABELS = {"lea": "Arlette", "theo": "Gabriel"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S02E05"
SOURCE_FILE = "sources/dix-pour-cent/s02/e05.fr.dual.srt"
SOURCE_NOTE = ("Cues 277-308. At the agency, Arlette confides in Gabriel about her past relationship "
               "with Guy Marchand and how she left him for Chet Baker in New York. "
               "Adapted for A1 French.")

INTRO = ("In the hallway at ASK, Gabriel talks with senior agent Arlette about her complicated past with client Guy Marchand. "
         "Arlette shares the romantic story of leaving him for legendary jazz musician Chet Baker. "
         "Let's listen to the scene in French first.")

STORY = [
 ("theo", "Ça fait toujours cet effet, même après 50 ans?",
  "Does it still have that effect, even after 50 years?",
  [(277, "Ça fait toujours cet effet, même après 50 ans ?")], ""),
 ("lea", "Pardon? De quoi parlez-vous?",
  "Pardon? What are you talking about?",
  [(278, "Pardon ?")], "Added De quoi parlez-vous"),
 ("theo", "Je veux dire, vous et Guy Marchand.",
  "I mean, you and Guy Marchand.",
  [(279, "Je veux dire, vous et Guy.")], "Added Marchand"),
 ("theo", "C'est quoi exactement? De la rancœur? Du ressentiment?",
  "What is it exactly? Rancor? Resentment?",
  [(280, "C'est quoi exactement ? De la rancœur ? Du ressentiment ?")], ""),
 ("lea", "Le ressentiment est voulu, la rancœur ne se contrôle pas.",
  "Resentment is deliberate, rancor cannot be controlled.",
  [(282, "Le ressentiment est voulu, la rancœur ne se contrôle pas.")], ""),
 ("theo", "Alors, c'est lequel entre vous deux?",
  "So, which is it between the two of you?",
  [(283, "Alors, c'est lequel ?")], "Added entre vous deux"),
 ("lea", "Rien de ma part. C'est lui.",
  "Nothing on my part. It is him.",
  [(284, "Rien de ma part. C'est lui.")], ""),
 ("lea", "Il m'en veut parce que je l'ai quitté pour Chet Baker.",
  "He holds a grudge against me because I left him for Chet Baker.",
  [(285, "Il m'en veut parce que je l'ai quitté pour Chet Baker.")], ""),
 ("lea", "J'aimais la vie et les artistes, lui voulait se marier.",
  "I loved life and artists, he wanted to get married.",
  [(287, "J'aimais la vie et les artistes, lui voulait se marier.")], ""),
 ("lea", "Il ne me l'a jamais pardonné.",
  "He never forgave me for it.",
  [(288, "Il ne me l'a jamais pardonné.")], ""),
 ("theo", "Alors c'est vrai, cette histoire avec Chet Baker?",
  "So it is true, that story with Chet Baker?",
  [(293, "Alors c'est vrai, toi et Chet ?")], "Adapted phrasing"),
 ("lea", "Vous me preniez pour une menteuse?",
  "Did you take me for a liar?",
  [(294, "Vous me preniez pour une menteuse ?")], ""),
 ("theo", "Non, mais c'est dingue. Chet Baker!",
  "No, but it is crazy. Chet Baker!",
  [(295, "Non, mais c'est dingue."), (296, "Chet Baker !")], ""),
 ("lea", "C'était à New York, au club de jazz où il jouait.",
  "It was in New York, at the jazz club where he was playing.",
  [(298, "C'était à New York,"), (299, "le club de jazz où il jouait.")], ""),
 ("lea", "Il est tombé éperdument amoureux de moi. Et je l'ai suivi.",
  "He fell madly in love with me. And I followed him.",
  [(300, "Il est tombé éperdument amoureux de moi."), (301, "Et je l'ai suivi.")], ""),
 ("lea", "La jalousie, c'est tellement stupide.",
  "Jealousy is so stupid.",
  [(289, "La jalousie, c'est tellement stupide.")], ""),
]

OPENER = "Let's explore the conversation line by line and unpack the French phrases."

WALK = [
 (0, None,
  "'Does it still have that effect, even after 50 years?' Gabriel probes Arlette's lingering tension. "
  "The idiom 'faire cet effet' means to produce that particular emotional reaction."),
 (1, None,
  "'Pardon? What are you talking about?' Arlette feigns innocence. "
  "The question 'de quoi parlez-vous' uses the preposition 'de' with the interrogative 'quoi'."),
 (2, None,
  "'I mean, you and Guy Marchand.' Gabriel names the legendary singer. "
  "The idiom 'je veux dire' clarifies an implicit reference casually."),
 (3, None,
  "'What is it exactly? Rancor? Resentment?' Gabriel asks for precise psychological nuances. "
  "The nouns 'rancoeur' and 'ressentiment' contrast instinctive bitterness with conscious grudge."),
 (4, None,
  "'Resentment is deliberate, rancor cannot be controlled.' Arlette offers a subtle philosophical distinction. "
  "The reflexive passive 'ne se controle pas' denotes an uncontrollable emotion."),
 (5, None,
  "'So, which is it between the two of you?' Gabriel presses for a direct answer. "
  "The interrogative pronoun 'lequel' selects between the two distinct options."),
 (6, None,
  "'Nothing on my part. It is him.' Arlette disclaims any personal bitterness. "
  "The phrase 'de ma part' indicates one's own side of a dispute."),
 (7, None,
  "'He holds a grudge against me because I left him for Chet Baker.' Arlette reveals the historic romantic betrayal. "
  "The idiom 'en vouloir a quelqu'un' means to hold a grudge against someone."),
 (8, None,
  "'I loved life and artists, he wanted to get married.' Arlette contrasts their youthful ambitions. "
  "The imperfect verbs 'aimais' and 'voulait' describe ongoing desires in the past."),
 (9, None,
  "'He never forgave me for it.' Arlette notes his enduring heartache. "
  "The double pronoun 'ne me l'a jamais pardonne' places the indirect pronoun before the direct."),
 (10, None,
  "'So it is true, that story with Chet Baker?' Gabriel seeks confirmation of the showbiz legend. "
  "The adjective 'vrai' inquires into the factual truth of the anecdote."),
 (11, None,
  "'Did you take me for a liar?' Arlette reacts with sharp theatrical indignance. "
  "The expression 'prendre quelqu'un pour' means to assume someone is something."),
 (12, None,
  "'No, but it is crazy. Chet Baker!' Gabriel marvels at the legendary name. "
  "The colloquial adjective 'dingue' expresses utter amazement."),
 (13, None,
  "'It was in New York, at the jazz club where he was playing.' Arlette paints the romantic setting. "
  "The relative adverb 'ou' introduces the venue where Chet Baker performed."),
 (14, None,
  "'He fell madly in love with me. And I followed him.' Arlette describes her whirlwind adventure. "
  "The idiom 'tomber amoureux' combines with the intensive adverb 'eperdument'."),
 (15, None,
  "'Jealousy is so stupid.' Arlette philosophizes on romantic possessiveness. "
  "The definite noun 'la jalousie' receives a categorical judgment with 'tellement stupide'."),
]

TRANSITION = "Now let's listen to the entire dialogue once more to lock in what you have learned."

OUTRO = ("Arlette shares her glamorous past with Gabriel, recounting how her romance with jazz legend Chet Baker "
         "created a fifty-year rift with Guy Marchand.")
CLOSING = ("lea", "La jalousie, c'est tellement stupide.")
