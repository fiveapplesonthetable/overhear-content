# Authoring module for dix-pour-cent s02e05 scene 12 (cues 341-360).
# Build: python3 tools/compose.py out/dix-pour-cent/s02e05/authoring/scene-12.py --out out/dix-pour-cent/s02e05/scene-12.json

ID = "dix-pour-cent-s02e05-scene-12"
SHOW = "dix-pour-cent"
SEASON = 2
EPISODE = 5
SCENE = 12
TITLE = "Le destin frappe à la porte  (Destiny Knocking)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "emilie": "emilie"}
LABELS = {"lea": "Camille", "emilie": "Andréa"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S02E05"
SOURCE_FILE = "sources/dix-pour-cent/s02/e05.fr.dual.srt"
SOURCE_NOTE = ("Cues 341-360. In the agency restroom, Camille weeps over the agency's resentment. "
               "Andréa comforts her, reassuring her that destiny is knocking at her door. "
               "Adapted for A1 French.")

INTRO = ("In the ASK restroom, Camille weeps after the harsh accusations from Herve. "
         "Andrea comes in to comfort her, explaining that she earned her opportunity and that destiny rarely knocks twice. "
         "Let's listen to the scene in French first.")

STORY = [
 ("emilie", "Ma Camille. Ne pleure pas.",
  "My Camille. Do not cry.",
  [(341, "Ma Camille.")], "Added Ne pleure pas"),
 ("lea", "Tout le monde me déteste maintenant.",
  "Everyone hates me now.",
  [(341, "Ma Camille.")], "Adapted distress"),
 ("emilie", "Je te crois. Je sais que tu ne le voulais pas.",
  "I believe you. I know you did not want it.",
  [(342, "Je te crois."), (343, "Je sais que tu ne le voulais pas.")], ""),
 ("lea", "Hervé pense que mon père a tout arrangé.",
  "Herve thinks that my father arranged everything.",
  [(343, "tu ne le voulais pas.")], "Adapted explanation"),
 ("emilie", "C'est le destin qui frappe à ta porte.",
  "It is destiny knocking at your door.",
  [(344, "C'est le destin qui frappe à ta porte.")], ""),
 ("emilie", "Et des filles comme nous, nous n'avons pas le droit de refuser.",
  "And girls like us, we have no right to refuse.",
  [(345, "nous n'avons pas le droit de refuser.")], ""),
 ("emilie", "Parce qu'il ne reviendra pas frapper. Tu comprends?",
  "Because it will not come back knocking. Do you understand?",
  [(346, "Parce qu'il ne reviendra pas frapper. Tu comprends ?")], ""),
 ("lea", "Oui, je comprends très bien, Andréa.",
  "Yes, I understand very well, Andrea.",
  [(346, "Tu comprends ?")], "Adapted agreement"),
 ("emilie", "Tu sais, ton histoire avec Christophe Lambert...",
  "You know, your story with Christophe Lambert...",
  [(347, "Tu sais..."), (348, "ton histoire avec Christophe Lambert...")], ""),
 ("emilie", "Je n'y ai jamais cru.",
  "I never believed it.",
  [(349, "Je n'y ai jamais cru.")], ""),
 ("emilie", "Cérébralement, si, mais pas au fond de moi.",
  "Intellectually, yes, but not deep down.",
  [(350, "Cérébralement, si."), (352, "pas au fond de moi.")], ""),
 ("emilie", "J'ai toujours su qu'il y avait autre chose.",
  "I always knew there was something else.",
  [(353, "J'ai toujours su que..."), (354, "il y avait autre chose,")], ""),
 ("emilie", "Quelque chose de plus profond, qui nous rapprocherait un jour.",
  "Something deeper, that would bring us closer one day.",
  [(355, "quelque chose de plus profond, qui nous rapprocherait un jour.")], ""),
 ("lea", "Et tu n'es pas en colère contre moi?",
  "And you are not angry with me?",
  [(346, "Tu comprends ?")], "Adapted question"),
 ("emilie", "Non, pas du tout. Nous sommes comme une famille.",
  "No, not at all. We are like a family.",
  [(356, "Comme une famille.")], "Added Nous sommes"),
 ("lea", "Merci, Andréa. Ça me fait du bien.",
  "Thank you, Andrea. That makes me feel good.",
  [(341, "Ma Camille.")], "Adapted gratitude"),
]

OPENER = "Let's explore the conversation line by line and unpack the French phrases."

WALK = [
 (0, None,
  "'My Camille. Do not cry.' Andrea comforts the weeping assistant warmly. "
  "The affectionate possessive 'ma Camille' softens the negative imperative 'ne pleure pas'."),
 (1, None,
  "'Everyone hates me now.' Camille expresses her overwhelming feeling of isolation. "
  "The indefinite subject 'tout le monde' takes the 3rd person singular verb 'deteste'."),
 (2, None,
  "'I believe you. I know you did not want it.' Andrea reassures Camille of her unconditional trust. "
  "The transitive verb 'croire' takes the direct object pronoun 'te'."),
 (3, None,
  "'Herve thinks that my father arranged everything.' Camille explains the hurtful accusation. "
  "The verb 'arranger' indicates orchestrating or fixing an outcome behind the scenes."),
 (4, None,
  "'It is destiny knocking at your door.' Andrea frames the sudden opportunity poetically. "
  "The metaphor 'frapper a ta porte' symbolizes life-changing opportunities."),
 (5, None,
  "'And girls like us, we have no right to refuse.' Andrea identifies with Camille's struggle. "
  "The idiom 'avoir le droit de' means to have the right or permission to do something."),
 (6, None,
  "'Because it will not come back knocking. Do you understand?' Andrea stresses the urgency of seizing one's chance. "
  "The future 'ne reviendra pas frapper' emphasizes the rarity of such career breaks."),
 (7, None,
  "'Yes, I understand very well, Andrea.' Camille absorbs her mentor's advice. "
  "The adverbial intensifier 'tres bien' indicates complete clarity and comprehension."),
 (8, None,
  "'You know, your story with Christophe Lambert...' Andrea recalls Camille's earlier romantic cover story. "
  "The noun 'histoire' refers to Camille's fabricated excuse about her secret father."),
 (9, None,
  "'I never believed it.' Andrea confesses her lasting skepticism. "
  "The adverbial pronoun 'y' stands for the unbelievable cover story."),
 (10, None,
  "'Intellectually, yes, but not deep down.' Andrea contrasts head and heart. "
  "The adverb 'cerebralement' denotes rational acceptance, contrasted with 'au fond de moi'."),
 (11, None,
  "'I always knew there was something else.' Andrea explains her instinctive intuition. "
  "The compound tense 'j'ai toujours su' expresses continuous inner certainty."),
 (12, None,
  "'Something deeper, that would bring us closer one day.' Andrea speaks of an enduring bond. "
  "The conditional 'rapprocherait' suggests a predestined emotional connection."),
 (13, None,
  "'And you are not angry with me?' Camille seeks final reassurance. "
  "The prepositional phrase 'en colere contre' expresses anger directed at someone."),
 (14, None,
  "'No, not at all. We are like a family.' Andrea reaffirms their sisterly connection. "
  "The comparative preposition 'comme' establishes the warmth of kinship."),
 (15, None,
  "'Thank you, Andrea. That makes me feel good.' Camille finds comfort in her friendship. "
  "The idiom 'faire du bien' means to provide emotional relief or comfort."),
]

TRANSITION = "Now let's listen to the entire dialogue once more to lock in what you have learned."

OUTRO = ("In an intimate conversation in the restroom, Andrea offers heartfelt support to Camille. "
         "Reassuring her that opportunity rarely knocks twice, Andrea encourages Camille to embrace her new role.")
CLOSING = ("emilie", "C'est le destin qui frappe à ta porte.")
