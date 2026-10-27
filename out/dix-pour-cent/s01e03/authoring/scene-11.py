# Authoring module for dix-pour-cent s01e03 scene 11 (cues 215-258).
# Build: python3 tools/compose.py out/dix-pour-cent/s01e03/authoring/scene-11.py --out out/dix-pour-cent/s01e03/scene-11.json

ID = "dix-pour-cent-s01e03-scene-11"
SHOW = "dix-pour-cent"
SEASON = 1
EPISODE = 3
SCENE = 11
TITLE = "Clément aux impôts  (Clément at the Tax Office)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "clement": "theo"}
LABELS = {"lea": "Andréa", "clement": "Clément"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S01E03"
SOURCE_FILE = "sources/dix-pour-cent/s01/e03.fr.dual.srt"

INTRO = ("While Gabriel is on the phone trying to talk Laura Smet into doing the film with her mother, "
         "Andréa has gone straight to the tax office to save the agency from its audit. "
         "An old ex-boyfriend of hers, Clément, works there now, and she hasn't seen him in ten years. "
         "She's hoping old feelings, or a few cinema perks, will buy the agency some help. "
         "We'll hear their conversation in French first; don't worry about catching every word.")

STORY = [
 ("lea", "Clément, ça fait plaisir de te voir.", "Clément, it's nice to see you.",
  [(215, "Clément, ça fait plaisir de te voir")], ""),
 ("clement", "Andréa. Ça fait combien de temps? Dix ans?", "Andréa. How long has it been? Ten years?",
  [(216, "Andréa"), (217, "Ça fait combien de temps"), (218, "Dix")], ""),
 ("clement", "Alors, c'est pour quoi? Un contrôle fiscal?", "So, what is it for? A tax audit?",
  [(220, "Alors, c'est pour quoi"), (224, "Un contrôle fiscal")], "omits bodily-fluids joke in 223"),
 ("lea", "Pas moi, mon agence. Je suis agent maintenant.", "Not me, my agency. I'm an agent now.",
  [(225, "Pas moi, mon"), (226, "Je suis agent maintenant")], "'mon lieu de travail' -> 'mon agence'"),
 ("clement", "Qui fait le contrôle?", "Who is doing the audit?",
  [(229, "qui fait le contrôle")], "'C'est qui qui' -> 'Qui'"),
 ("lea", "Une femme. Colette Brancillon.", "A woman. Colette Brancillon.",
  [(229, "Une femme"), (231, "Colette Brancillon")], ""),
 ("clement", "Je la connais. Elle est jeune et motivée.", "I know her. She's young and keen.",
  [(232, "je la connais"), (234, "Elle est jeune et motivée")], ""),
 ("clement", "Ce n'est vraiment pas bon pour toi.", "That's really not good for you.",
  [(236, "vraiment pas bon pour toi")], "restores 'ne'"),
 ("lea", "Tu peux faire quelque chose? Tu aimes toujours le cinéma?", "Can you do something? Do you still like the cinema?",
  [(237, "tu peux faire quelque chose"), (238, "Tu aimes toujours le cinéma")], ""),
 ("clement", "Je t'écoute.", "I'm listening.",
  [(238, "Je t'écoute")], ""),
 ("lea", "Des invitations à Cannes, et une chambre au Carlton.", "Invitations to Cannes, and a room at the Carlton.",
  [(239, "Cannes"), (240, "Des invitations"), (241, "Une chambre au Carlton")], ""),
 ("clement", "Une suite?", "A suite?",
  [(241, "Une suite")], ""),
 ("lea", "Allez, Clément! Je veux juste un service d'un vieil ami.", "Come on, Clément! I just want a favour from an old friend.",
  [(242, "Allez, Clément"), (244, "Je veux juste un service d'un vieil ami")], ""),
 ("clement", "Un vieil ami? Tu m'as quitté avec un SMS!", "An old friend? You broke up with me by text!",
  [(244, "Un vieil ami"), (245, "Tu m'as"), (247, "un SMS")], "'largué' and sister line cleaned up to 'quitté avec un SMS'"),
 ("clement", "Au revoir, Andréa. Et bonne chance pour l'audit.", "Goodbye, Andréa. And good luck with the audit.",
  [(249, "Au revoir, Andréa. Et bonne chance pour l'audit")], ""),
 ("lea", "Attends, Clément! D'accord pour la suite.", "Wait, Clément! Okay for the suite.",
  [(250, "Attends, Clément"), (251, "D'accord pour la suite")], ""),
 ("clement", "Et une invitation pour les Césars. Donne-moi une semaine.", "And an invitation to the Césars. Give me a week.",
  [(252, "Et une invitation pour les Césars"), (256, "Donne-moi une semaine")], ""),
 ("clement", "Je vais remplacer Brancillon. En attendant, sois sympa avec elle.", "I'll replace Brancillon. In the meantime, be nice to her.",
  [(254, "remplacer Brancillon"), (258, "Sois sympa avec elle")], "'essayer de faire remplacer' simplified to 'Je vais remplacer'"),
]

OPENER = "Let's walk through it together. Andréa walks into Clément's office with her warmest smile."

WALK = [
 (0, None,
  "'Clément, it's nice to see you.' Literally 'it makes pleasure to see you', a very common, warm greeting."),
 (1, None,
  "'Andréa. How long has it been? Ten years?' That same 'it makes' expression is how French asks how long something has been going on."),
 (2, "Alors, c'est pour quoi?",
  "'So, what is it for?' Clément skips the small talk; he knows she hasn't come just to say hello."),
 (2, "Un contrôle fiscal?",
  "'A tax audit?' In French the adjective for 'tax' comes right after the word for 'check' or 'audit'."),
 (3, None,
  "'Not me, my agency. I'm an agent now.' Notice the masculine possessive word before 'agency' because 'agency' begins with a vowel."),
 (4, None,
  "'Who is doing the audit?' Short and direct: the question word for 'who' followed by the verb 'does'."),
 (5, None,
  "'A woman. Colette Brancillon.' Remember that name; we're going to meet her very soon."),
 (6, None,
  "'I know her. She's young and keen.' The little word for 'her' sits right before the verb 'know'."),
 (7, None,
  "'That's really not good for you.' Clément tells her that Colette Brancillon follows every rule in the book."),
 (8, "Tu peux faire quelque chose?",
  "'Can you do something?' The verb 'can' followed by 'to do something'."),
 (8, "Tu aimes toujours le cinéma?",
  "'Do you still like the cinema?' The word after the verb means both 'always' and 'still'. Here comes the bribe."),
 (9, None,
  "'I'm listening.' Literally 'I listen to you', with the object word shortened before a vowel."),
 (10, None,
  "'Invitations to Cannes, and a room at the Carlton.' The grand hotel on the seafront during the film festival."),
 (11, None,
  "'A suite?' Clément knows how to negotiate."),
 (12, None,
  "'Come on, Clément! I just want a favour from an old friend.' The word for 'old' takes a special masculine form before a noun starting with a vowel."),
 (13, None,
  "'An old friend? You broke up with me by text!' Past tense with 'have', and the word for 'me' shortened before the verb. Clément hasn't forgotten."),
 (14, None,
  "'Goodbye, Andréa. And good luck with the audit.' He stands up to show her the door."),
 (15, None,
  "'Wait, Clément! Okay for the suite.' Andréa gives in immediately."),
 (16, None,
  "'And an invitation to the Césars. Give me a week.' He adds one more prize to the deal, and asks for seven days."),
 (17, "Je vais remplacer Brancillon.",
  "'I'll replace Brancillon.' Literally 'I am going to replace' her with someone friendlier."),
 (17, "En attendant, sois sympa avec elle.",
  "'In the meantime, be nice to her.' That's the command form of the verb 'to be': be nice to her until then."),
]

TRANSITION = "Now let's hear the whole negotiation again from start to finish."

OUTRO = ("Andréa has her deal: one week of being polite to Colette Brancillon, and the audit problem should vanish. "
         "See you in the next scene.")
CLOSING = ("lea", "Merci, Clément!")
