# Authoring module for dix-pour-cent s01e06 scene 04 (cues 92-118).
# Build: python3 tools/compose.py out/dix-pour-cent/s01e06/authoring/scene-04.py --out out/dix-pour-cent/s01e06/scene-04.json

ID = "dix-pour-cent-s01e06-scene-04"
SHOW = "dix-pour-cent"
SEASON = 1
EPISODE = 6
SCENE = 4
TITLE = "Je ne sais pas nager  (I Can't Swim)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "francois": "marcel", "gabriel": "theo"}
LABELS = {"lea": "Andrea", "francois": "Francois", "gabriel": "Gabriel"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S01E06"
SOURCE_FILE = "sources/dix-pour-cent/s01/e06.fr.dual.srt"
SOURCE_NOTE = ("Cues 92-118. Francois Berleand demands that Andrea get the swimming pool removed from Christophe Bel's play. "
               "Gabriel tries to joke about the pretty actresses in swimsuits, but Francois storms out. "
               "When Andrea presses him for the truth, Francois admits why he refuses to jump into the water: he cannot swim.")

INTRO = ("Back at the agency, the crisis over Dom Juan is escalating. Francois Berleand is furious about the "
         "avant-garde rehearsal and demands that Andrea fix the conflict with director Christophe Bel at once. "
         "Let's listen to the scene in French first.")

STORY = [
 ("lea", "Qu'est-ce qu'elle a de si mauvais, cette scène?",
  "What is so bad about that scene?",
  [(92, "Qu'est-ce qu'elle a de si mauvais, cette scène ?")], ""),
 ("francois", "Je ne vous demande pas de comprendre, je vous demande de régler ça.",
  "I am not asking you to understand, I am asking you to fix it.",
  [(93, "Je ne vous demande pas de comprendre, je vous demande de régler ça.")], ""),
 ("francois", "Dis-lui que je jouerai dans son spectacle, mais qu'il n'y aura pas de piscine.",
  "Tell him I will act in his show, but there will be no pool.",
  [(95, "Dis-lui que je jouerai dans son spectacle,"),
   (96, "mais qu'il n'y aura pas de piscine.")], ""),
 ("lea", "Pas de piscine? Toute la scénographie est construite autour.",
  "No pool? The entire set design is built around it.",
  [(97, "Pas de piscine ? Toute la scénographie est construite autour.")], ""),
 ("francois", "Alors ils la changent. Je ne suis pas pressé.",
  "Then they change it. I am in no hurry.",
  [(98, "Alors ils la changent. Je ne suis pas pressée.")], "Subtitle typo 'pressée' normalized to masculine 'pressé'"),
 ("lea", "C'est de la folie! La première, c'est dans une semaine.",
  "That is madness! Opening night is in a week.",
  [(99, "C'est de la folie ! La première, c'est dans une semaine.")], ""),
 ("lea", "Et pourquoi travailler avec Christophe Bel si on l'empêche d'être Christophe Bel?",
  "And why work with Christophe Bel if we stop him being Christophe Bel?",
  [(100, "Et pourquoi travailler avec Christophe Bel si on l'empêche d'être Christophe Bel ?")], ""),
 ("francois", "Le mec est un génie? Un canard géant, de la mauvaise musique... Ouais, un vrai génie!",
  "The guy is a genius? A giant duck, bad music... Yeah, a real genius!",
  [(101, "Le mec est un génie."),
   (103, "un canard"),
   (104, "De la daube des années 80,"),
   (105, "Ouais, un vrai génie !")], "Vulgar phrases cleaned up"),
 ("gabriel", "Arrête, tu es vraiment injuste! Tu as beaucoup de chance.",
  "Stop it, you are being really unfair! You are very lucky.",
  [(106, "Arrête, t'es vraiment injuste."),
   (107, "T'as beaucoup de chance.")], "Spoken contractions expanded to standard A1 French"),
 ("gabriel", "Une ambiance sexy, des maillots de bain... La petite Mathurine est superbe!",
  "A sexy atmosphere, swimsuits... Little Mathurine is gorgeous!",
  [(108, "Une ambiance sexy"),
   (109, "La petite Mathurine est canon ! Tu sais si elle a un agent ?")], "Slang 'canon' adapted to 'superbe'"),
 ("francois", "Laisse tomber, oublie ça.",
  "Drop it, forget about it.",
  [(110, "Laisse tomber, oublie ça.")], ""),
 ("lea", "Mais, François! Aide-moi à comprendre! En dix ans, je ne t'ai jamais vu comme ça.",
  "But, Francois! Help me understand! In ten years, I have never seen you like this.",
  [(111, "Mais, François !"),
   (112, "Aide-moi à comprendre ! En dix ans, je t'ai jamais vu comme ça.")], "Formal negative particle restored"),
 ("lea", "C'est quoi? Allez, dis-moi!",
  "What is it? Come on, tell me!",
  [(113, "C'est quoi ?"),
   (116, "C'est quoi ? Allez, dis-moi !")], ""),
 ("francois", "Je ne sais pas nager.",
  "I do not know how to swim.",
  [(117, "Je ne sais pas nager.")], "Francois admits his secret fear of the water"),
]

OPENER = "Let's examine the conversation step by step to see how Francois reveals his secret."

WALK = [
 (0, None,
  "'What is so bad about that scene?' Andrea asks why he finds the rehearsal scene so intolerable."),
 (1, None,
  "'I am not asking you to understand, I am asking you to fix it.' Francois insists that an agent should solve problems rather than ask questions."),
 (2, None,
  "'Tell him I will act in his show, but there will be no pool.' The future tense indicates his firm condition for continuing."),
 (3, None,
  "'No pool? The entire set design is built around it.' Andrea points out that the stage cannot easily be redesigned."),
 (4, None,
  "'Then they change it. I am in no hurry.' Francois is completely unbothered by the delay."),
 (5, None,
  "'That is madness! Opening night is in a week.' Andrea stresses the urgent timeline of the production."),
 (6, None,
  "'And why work with Christophe Bel if we stop him being Christophe Bel?' She argues that hiring a visionary director means trusting his ideas."),
 (7, None,
  "'The guy is a genius? A giant duck, bad music... Yeah, a real genius!' He sarcastically mocks the absurd props and soundtrack."),
 (8, None,
  "'Stop it, you are being really unfair! You are very lucky.' Gabriel steps in to defend the production."),
 (9, None,
  "'A sexy atmosphere, swimsuits... Little Mathurine is gorgeous!' Gabriel praises the lively beach mood and the young cast."),
 (10, None,
  "'Drop it, forget about it.' Francois cuts the conversation short and refuses to listen."),
 (11, None,
  "'But, Francois! Help me understand! In ten years, I have never seen you like this.' Andrea begs him to explain what is really going on."),
 (12, None,
  "'What is it? Come on, tell me!' She urges him to open up and tell the truth."),
 (13, None,
  "'I do not know how to swim.' Francois finally confesses the childhood secret he has kept hidden for decades."),
]

TRANSITION = "Now let's listen to the entire dialogue once more from beginning to end."

OUTRO = ("Francois has finally told Andrea the truth: he cannot swim, which is why he refuses to dive into the pool. "
         "Now Andrea must find a way to save the play without exposing her client to public embarrassment. "
         "See you in the next scene.")

CLOSING = ("francois", "Je ne sais pas nager.")

if __name__ == "__main__":
    import subprocess, sys
    from pathlib import Path
    root = Path(__file__).resolve().parents[4]
    out = Path(__file__).resolve().parents[1] / f"scene-{SCENE:02d}.json"
    sys.exit(subprocess.call([sys.executable, str(root / "tools/compose.py"), __file__, "--out", str(out)]))
