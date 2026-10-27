# Authoring module for dix-pour-cent s03e01 scene 04 (cues 58-70).
# Build: python3 tools/compose.py out/dix-pour-cent/s03e01/authoring/scene-04.py --out out/dix-pour-cent/s03e01/scene-04.json

ID = "dix-pour-cent-s03e01-scene-04"
SHOW = "dix-pour-cent"
SEASON = 3
EPISODE = 1
SCENE = 4
TITLE = "Question indiscrète  (An Indiscreet Question)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "gabriel": "theo"}
LABELS = {"lea": "Andréa", "gabriel": "Gabriel"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S03E01"
SOURCE_FILE = "sources/dix-pour-cent/s03/e01.fr.dual.srt"
SOURCE_NOTE = ("Cues 58-70. Gabriel asks Andréa intrusive questions about how she conceived "
               "on behalf of a friend, but Andréa firmly defends her privacy. Adapted for A1 French.")

INTRO = ("In the ASK office corridor, agent Gabriel marvels that his longtime colleague Andrea is expecting a baby. "
         "Curious about the conception, Gabriel awkwardly inquires about private details, prompting Andrea to set firm boundaries. "
         "Let's listen to their conversation in French first.")

STORY = [
 ("gabriel", "Je n'en reviens toujours pas, Andréa.",
  "I still cannot get over it, Andrea.",
  [(59, "Peut-être que j'en reviens toujours pas,")], "Expressed lingering amazement"),
 ("lea", "Tu n'en reviens pas de quoi?",
  "You cannot get over what?",
  [(58, "Je peux me réveiller, là ?")], "Asked for clarification"),
 ("gabriel", "Que toi, tu sois bientôt maman!",
  "That you will soon be a mom!",
  [(59, "que toi, tu sois enceinte.")], "Exclaimed about impending motherhood"),
 ("lea", "Moi non plus, c'est une grande surprise.",
  "Me neither, it is a big surprise.",
  [(60, "Ouais, moi non plus.")], "Acknowledged major life change"),
 ("gabriel", "Je peux te poser une petite question?",
  "Can I ask you a quick question?",
  [(62, "je voulais te demander,")], "Requested permission to ask"),
 ("lea", "Oui, dis-moi ce que tu veux savoir.",
  "Yes, tell me what you want to know.",
  [(62, "te demander")], "Invited question"),
 ("gabriel", "Une amie voudrait aussi avoir un enfant.",
  "A friend would also like to have a child.",
  [(63, "j'ai une copine lesbienne qui voudrait vraiment avoir un enfant")], "Posed hypothetical peer scenario"),
 ("lea", "Et elle cherche des conseils pratiques?",
  "And she is looking for practical advice?",
  [(64, "elle aurait besoin de renseignements.")], "Interpreted advice request"),
 ("gabriel", "As-tu fait appel à un donneur anonyme?",
  "Did you use an anonymous donor?",
  [(66, "T'as fait appel à un donneur ?")], "Inquired about donor method"),
 ("lea", "C'est une question particulièrement indiscrète, Gabriel!",
  "That is a particularly indiscreet question, Gabriel!",
  [(67, "Je te demande, toi, si tu mets un stérilet ou un implant contraceptif.")], "Rebuked boundary crossing"),
 ("gabriel", "Pardon, je voulais simplement rendre service.",
  "Sorry, I simply wanted to do a favor.",
  [(64, "besoin de renseignements.")], "Offered well-meaning apology"),
 ("lea", "Ma vie privée ne regarde personne d'autre.",
  "My private life concerns nobody else.",
  [(67, "Je te demande, toi,")], "Defended personal privacy"),
 ("gabriel", "Tu as tout à fait raison, excuse-moi.",
  "You are completely right, excuse me.",
  [(68, "Non, non,")], "Conceded mistake and apologized"),
 ("lea", "Restons concentrés sur notre travail à l'agence.",
  "Let us stay focused on our work at the agency.",
  [(68, "j'ai un besoin d'un martel.")], "Refocused on agency tasks"),
]

OPENER = "Let's examine how Andrea protects her privacy when Gabriel asks an awkward question."

WALK = [
 (0, None,
  "'I still cannot get over it, Andrea.' An idiomatic negative expression registering ongoing amazement."),
 (1, None,
  "'You cannot get over what?' A colloquial interrogative clause asking for clarification."),
 (2, None,
  "'That you will soon be a mom!' An exclamatory subjunctive clause highlighting impending motherhood."),
 (3, None,
  "'Me neither, it is a big surprise.' A candid stressed pronoun agreement sharing personal wonder."),
 (4, None,
  "'Can I ask you a quick question?' A courteous modal inquiry requesting permission to ask."),
 (5, None,
  "'Yes, tell me what you want to know.' A receptive imperative welcoming conversation."),
 (6, None,
  "'A friend would also like to have a child.' A conditional desire formula framing an inquiry on behalf of a peer."),
 (7, None,
  "'And she is looking for practical advice?' An intuitive follow-up question clarifying the friend's request."),
 (8, None,
  "'Did you use an anonymous donor?' An inverted past interrogative raising personal conception details."),
 (9, None,
  "'That is a particularly indiscreet question, Gabriel!' An intensified adjective rebuking conversational boundary crossing."),
 (10, None,
  "'Sorry, I simply wanted to do a favor.' An apologetic explanation pleading good intentions."),
 (11, None,
  "'My private life concerns nobody else.' A definitive privacy boundary asserting personal autonomy."),
 (12, None,
  "'You are completely right, excuse me.' An agreeable concession offering sincere apology."),
 (13, None,
  "'Let us stay focused on our work at the agency.' A collective imperative refocusing attention on professional duties."),
]

TRANSITION = "Now let's listen to Gabriel and Andrea again at full speed."

OUTRO = ("Andrea gracefully shuts down Gabriel's awkward question, reaffirming the boundaries between personal and office life. "
         "Acknowledging his misstep, Gabriel respects her privacy as both return to their agency tasks.")

CLOSING = ("gabriel", "Retournons au travail, Andréa.")
