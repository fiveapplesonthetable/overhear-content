# Authoring module for dix-pour-cent s01e03 scene 16 (cues 375-413).
# Build: python3 tools/compose.py out/dix-pour-cent/s01e03/authoring/scene-16.py --out out/dix-pour-cent/s01e03/scene-16.json

ID = "dix-pour-cent-s01e03-scene-16"
SHOW = "dix-pour-cent"
SEASON = 1
EPISODE = 3
SCENE = 16
TITLE = "Fais une Bardot  (Do a Bardot)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "nathalie": "emilie", "gabriel": "theo"}
LABELS = {"lea": "Laura", "nathalie": "Nathalie", "gabriel": "Gabriel"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S01E03"
SOURCE_FILE = "sources/dix-pour-cent/s01/e03.fr.dual.srt"
SOURCE_NOTE = ("Cues 375-413. Laura is the viewpoint character (lea). The sexual joke in cue 404 is omitted and "
               "vulgar 'chiante' in cue 405 is replaced by 'capricieuse' from cue 409. Hervé's objection at the end "
               "(410-413) is folded into Laura's own hesitation to stay within three speaking roles.")

INTRO = ("Nathalie Baye and her daughter Laura Smet have just told their agents in private that three months "
         "together on a film shoot would be a nightmare: Nathalie wants to act the story, not live it. Now both "
         "women look back on the last time they lived under the same roof, a disastrous summer when Laura broke "
         "her ankle. Yet when it comes to saying no, Laura panics that she will break her mother's heart, and "
         "Gabriel comes up with a risky scheme. Listen to the French first; you don't need to catch every word.")

STORY = [
 ("nathalie", "Été deux mille onze. Elle s'est cassé la cheville.", "Summer twenty eleven. She broke her ankle.",
  [(378, "cassé la cheville"), (379, "Été")], "'2011' written out in words; 'je me suis' -> 'elle s'est'"),
 ("lea", "Je ne pouvais pas marcher. Je suis restée chez ma mère.", "I couldn't walk. I stayed at my mother's.",
  [(381, "ne pouvait pas marcher"), (382, "Je suis restée chez ma mère")], "'Elle ne pouvait' -> 'Je ne pouvais'"),
 ("nathalie", "L'horreur absolue! C'était comme si elle avait treize ans.", "Total horror! It was as if she were thirteen.",
  [(383, "L'horreur absolue"), (384, "C'était comme si elle avait"), (384, "ans")], "'13' written out in words"),
 ("lea", "J'ai complètement craqué. On s'est dit des choses horribles.", "I completely lost it. We said horrible things to each other.",
  [(387, "J'ai complètement craqué"), (389, "On s'est dit des choses horribles")], ""),
 ("nathalie", "Jamais plus! Je ne vais pas sacrifier notre relation pour un film.", "Never again! I'm not going to sacrifice our relationship for a film.",
  [(390, "Jamais plus"), (392, "je ne vais pas sacrifier notre relation pour un film")], ""),
 ("lea", "Mais moi, si je dis non, elle va croire que c'est à cause d'elle!", "But as for me, if I say no, she'll think it's because of her!",
  [(395, "Elle va croire que"), (397, "c'est à cause d'elle")], ""),
 ("lea", "C'est horrible! Ça va lui briser le cœur.", "That's horrible! It's going to break her heart.",
  [(396, "C'est horrible"), (398, "Ça va lui briser le cœur")], ""),
 ("lea", "Tu as raison, Gabriel. Je ne peux pas refuser.", "You're right, Gabriel. I can't refuse.",
  [(399, "Tu as raison, je ne peux pas refuser")], ""),
 ("gabriel", "Si. Tu peux faire en sorte qu'elle refuse.", "Yes, you can. You can make sure that she refuses.",
  [(399, "Si"), (399, "faire en sorte qu'elle refuse")], "'Tu pourrais' -> 'Tu peux'"),
 ("lea", "Qui?", "Who?",
  [(400, "Qui")], ""),
 ("gabriel", "Solveig! Fais juste une Bardot.", "Solveig! Just do a Bardot.",
  [(401, "Solveig"), (403, "Fais juste une Bardot")], ""),
 ("lea", "C'est quoi, ça?", "What's that?",
  [(404, "C'est quoi")], "sex joke in cue 404 omitted"),
 ("gabriel", "Tu deviens capricieuse, une star difficile comme Brigitte Bardot.", "You become capricious, a difficult star like Brigitte Bardot.",
  [(405, "tu deviens"), (405, "une star comme Brigitte Bardot"), (409, "capricieuse")], "vulgar 'chiante' replaced by 'capricieuse' from cue 409"),
 ("gabriel", "Akerfelt déteste ça!", "Akerfelt hates that!",
  [(408, "Akerfelt"), (408, "déteste ça")], ""),
 ("lea", "Mais c'est ridicule! C'est une très mauvaise idée.", "But that's ridiculous! It's a very bad idea.",
  [(410, "c'est ridicule"), (411, "Une très mauvaise idée")], ""),
 ("lea", "Je ne vais quand même pas faire une Bardot!", "I'm not actually going to do a Bardot!",
  [(412, "quand même pas"), (413, "faire une Bardot")], "'Tu ne vas' -> 'Je ne vais'"),
]

OPENER = ("Let's go through it step by step. First, both women remember the summer of twenty eleven.")

WALK = [
 (0, None,
  "'Summer twenty eleven. She broke her ankle.' With parts of the body, French uses a reflexive verb and the word "
  "for 'the' instead of 'her'."),
 (1, None,
  "'I couldn't walk. I stayed at my mother's.' The first verb describes how things were, and the second is a single "
  "event. The preposition before 'my mother' means 'at the home of'."),
 (2, None,
  "'Total horror! It was as if she were thirteen.' Again, French expresses age with the verb 'to have': she had "
  "thirteen years."),
 (3, None,
  "'I completely lost it. We said horrible things to each other.' The first verb literally means to crack or snap."),
 (4, "Jamais plus!",
  "'Never again!' Literally 'never more'. Both mother and daughter swear the same thing."),
 (4, "Je ne vais pas sacrifier notre relation pour un film.",
  "'I'm not going to sacrifice our relationship for a film.' Nathalie tells Mathias her decision is final. Yet in "
  "Gabriel's office, Laura has no idea her mother is saying no."),
 (5, None,
  "'But as for me, if I say no, she'll think it's because of her!' The three-word phrase near the end means "
  "'because of'."),
 (6, None,
  "'That's horrible! It's going to break her heart.' Literally 'break the heart to her', with the indirect object "
  "word before the verb 'break'."),
 (7, None,
  "'You're right, Gabriel. I can't refuse.' Literally 'you have reason', the standard French idiom for 'you are "
  "right'."),
 (8, None,
  "'Yes, you can. You can make sure that she refuses.' Notice the special word for 'yes' at the start, contradicting "
  "Laura's negative sentence."),
 (9, None,
  "'Who?' A single short question word, because Laura thinks that Gabriel still means her mother."),
 (10, None,
  "'Solveig! Just do a Bardot.' He means the famous French icon Brigitte Bardot, using her name for a whole way of "
  "behaving."),
 (11, None,
  "'What's that?' Literally 'it is what, that?', the casual spoken way to ask what something means."),
 (12, None,
  "'You become capricious, a difficult star like Brigitte Bardot.' Gabriel wants Laura to act like a spoiled diva "
  "at her audition."),
 (13, None,
  "'Akerfelt hates that!' A strict Scandinavian art-house director won't tolerate diva behaviour for a second."),
 (14, None,
  "'But that's ridiculous! It's a very bad idea.' The adjective for 'bad' is in its feminine form to match 'idea'."),
 (15, None,
  "'I'm not actually going to do a Bardot!' The two-word phrase inside the negative adds 'all the same' or "
  "'really'. And yet, in the very next scenes, both mother and daughter will try to sabotage their auditions."),
]

TRANSITION = "Now let's listen to the whole conversation again."

OUTRO = ("So Nathalie wants to sabotage her audition, and Gabriel wants Laura to sabotage hers by playing the "
         "diva. Next come the auditions themselves. See you there.")
CLOSING = ("gabriel", "Mais si, Laura!")
