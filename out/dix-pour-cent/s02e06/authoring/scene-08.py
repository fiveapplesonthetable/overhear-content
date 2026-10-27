# Authoring module for dix-pour-cent s02e06 scene 08 (cues 158-168).
# Build: python3 tools/compose.py out/dix-pour-cent/s02e06/authoring/scene-08.py --out out/dix-pour-cent/s02e06/scene-08.json

ID = "dix-pour-cent-s02e06-scene-08"
SHOW = "dix-pour-cent"
SEASON = 2
EPISODE = 6
SCENE = 8
TITLE = "Le scénario de l'écrivain  (The Writer's Pitch)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "writer": "theo"}
LABELS = {"lea": "Hervé", "writer": "L'écrivain"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S02E06"
SOURCE_FILE = "sources/dix-pour-cent/s02/e06.fr.dual.srt"
SOURCE_NOTE = ("Cues 158-168. In the ASK agency, an internet technician pitches a bizarre screenplay to Hervé, "
               "hoping he will take it to Cannes for Isabelle Huppert. "
               "Adapted for A1 French.")

INTRO = ("Alone at the ASK reception desk, Herve supervises an internet technician setting up high-speed routers for the team. "
         "The technician unexpectedly pitches an eccentric screenplay about domestic secrets, asking Herve to deliver it to movie stars at Cannes. "
         "Let's listen to the scene in French first.")

STORY = [
 ("writer", "Voilà une connexion internet parfaite pour Cannes.",
  "Here is a perfect internet connection for Cannes.",
  [(157, "ça vous donnera une connexion parfaite pour Cannes.")], "The technician presents the setup"),
 ("writer", "C'est du très haut débit pour vous.",
  "It is high-speed broadband for you.",
  [(158, "Le très haut débit pour toute votre équipe.")], "The technician praises the connection"),
 ("lea", "Merci beaucoup, c'est vraiment très pratique.",
  "Thank you very much, it is really very practical.",
  [(159, "Merci, c'est parfait.")], "Herve thanks the technician"),
 ("writer", "Vous savez, moi aussi je suis écrivain.",
  "You know, I am a writer too.",
  [(160, "Moi aussi je suis écrivain.")], "The technician introduces his ambition"),
 ("writer", "On voit des choses folles chez les gens.",
  "One sees crazy things in people's homes.",
  [(161, "ce qu'on voit quand on entre chez les gens !")], "The technician mentions inspiration"),
 ("lea", "Non, je ne peux pas imaginer ça.",
  "No, I cannot imagine that.",
  [(162, "Non, je n'imaginerais pas.")], "Herve acts skeptical"),
 ("writer", "J'ai tout écrit dans ce nouveau scénario.",
  "I wrote everything in this new screenplay.",
  [(163, "J'ai tout raconté dans ce scénario.")], "The technician presents his script"),
 ("writer", "C'est incroyable derrière les portes fermées.",
  "It is unbelievable behind closed doors.",
  [(164, "ce qu'on voit derrière les portes fermées.")], "The technician hypes the plot"),
 ("writer", "Vous pourriez l'emporter à Cannes pour moi?",
  "Could you take it to Cannes for me?",
  [(166, "que vous pourriez l'emporter à Cannes")], "The technician makes his request"),
 ("writer", "Vous pouvez le donner à des acteurs connus.",
  "You can give it to famous actors.",
  [(166, "et le donner à des acteurs.")], "The technician dreams of stardom"),
 ("lea", "Isabelle Huppert rêve de jouer un routeur!",
  "Isabelle Huppert dreams of playing a router!",
  [(167, "Isabelle Huppert a toujours rêvé de jouer un routeur !")], "Herve makes a sarcastic joke"),
 ("lea", "Je plaisante, mais je ne vais pas là-bas.",
  "I am joking, but I am not going there.",
  [(168, "C'est juste que je ne vais pas à Cannes.")], "Herve clarifies"),
 ("lea", "Je reste ici pour garder l'agence.",
  "I stay here to look after the agency.",
  [(168, "C'est juste que je ne vais pas à Cannes.")], "Herve explains his assignment"),
]

OPENER = "Let's examine Herve's comical interaction with the enthusiastic technician step by step to explore unexpected script submissions."

WALK = [
 (0, None,
  "'Here is a perfect internet connection for Cannes.' The technician finishes installing the office broadband link."),
 (1, None,
  "'It is high-speed broadband for you.' The installer highlights the fast internet speed for the traveling agents."),
 (2, None,
  "'Thank you very much, it is really very practical.' Herve appreciates the technical support for the office."),
 (3, None,
  "'You know, I am a writer too.' The technician reveals his hidden artistic ambitions."),
 (4, None,
  "'One sees crazy things in people's homes.' The technician claims that house calls inspire wild stories."),
 (5, None,
  "'No, I cannot imagine that.' Herve politely reacts with polite skepticism."),
 (6, None,
  "'I wrote everything in this new screenplay.' The technician shows off his written manuscript."),
 (7, None,
  "'It is unbelievable behind closed doors.' The installer hypes up his sensational dramatic material."),
 (8, None,
  "'Could you take it to Cannes for me?' The technician asks Herve to smuggle his script to the festival."),
 (9, None,
  "'You can give it to famous actors.' The amateur writer hopes to reach major stars on the red carpet."),
 (10, None,
  "'Isabelle Huppert dreams of playing a router!' Herve mocks the absurd pitch with dry sarcasm."),
 (11, None,
  "'I am joking, but I am not going there.' Herve gently lets the technician down."),
 (12, None,
  "'I stay here to look after the agency.' Herve laments being stuck in Paris holding down the fort."),
]

TRANSITION = "Now let's listen to the scene once more from start to finish."

OUTRO = ("Herve contends with an eccentric writer while holding the fort at ASK as his colleagues pack their bags for the festival. "
         "Let's review the key vocabulary from this scene.")

CLOSING = ("lea", "Je reste ici pour garder l'agence.")
