ID = "dix-pour-cent-s01e04-scene-27"
SHOW = "dix-pour-cent"
SEASON = 1
EPISODE = 4
SCENE = 27
TITLE = "Vingt mille euros  (Twenty Thousand Euros)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "andrea": "emilie", "mathias": "theo"}
LABELS = {"lea": "Audrey", "andrea": "Andréa", "mathias": "Mathias"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S01E04"
SOURCE_FILE = "sources/dix-pour-cent/s01/e04.fr.dual.srt"

INTRO = ("While Andréa and Gabriel were pretending to be lovers at the Hotel Saint-Georges, a scandal broke out in the press. "
         "After giving up Augustin's film to stay with her children, Audrey still needed money urgently to pay her tax bill. "
         "So she secretly went to the Russian billionaire Kadropov's birthday party for twenty thousand euros — and the paparazzi took photos. "
         "After Andréa shows the magazines at the agency, Mathias goes straight to Audrey's flat. "
         "Here it is in French first. Let the words wash over you and catch what you can.")

STORY = [
 ("andrea", "Regardez! C'est dans tous les journaux.", "Look! It's in all the papers.",
  [(703, "Regardez")], "at ASK; 'Partout' expanded to 'C'est dans tous les journaux'"),
 ("andrea", "Audrey est allée à la fête de Kadropov pour vingt mille euros!", "Audrey went to Kadropov's party for twenty thousand euros!",
  [(699, "Audrey"), (699, "euros")], "'20 000' written out as 'vingt mille'"),
 ("andrea", "Ce n'est pas possible! Tu t'en occupes, Mathias?", "That's not possible! Will you deal with it, Mathias?",
  [(700, "pas possible"), (714, "Tu t'en occupes")], "swearing omitted"),
 ("lea", "Mathias! Il m'avait promis le secret.", "Mathias! He had promised me secrecy.",
  [(715, "Mathias"), (716, "Il m'avait promis")], "at Audrey's flat; simplified from 716"),
 ("mathias", "Si Kadropov sort avec une belle femme comme toi, il le dit à tout le monde!", "If Kadropov goes out with a beautiful woman like you, he tells everyone!",
  [(720, "Si Kadropov sort avec une"), (721, "tout le monde")], "simplified from 720-721"),
 ("lea", "Tu me trouves belle?", "Do you think I'm beautiful?",
  [(722, "Tu me trouves belle")], ""),
 ("mathias", "Oui, tu es très belle.", "Yes, you're very beautiful.",
  [(723, "tu es belle")], ""),
 ("lea", "C'est tellement gentil.", "That's so kind.",
  [(724, "C'est tellement gentil")], ""),
 ("lea", "Je suis fatiguée, Mathias. Je n'en peux plus.", "I'm tired, Mathias. I can't take it anymore.",
  [(727, "Je suis"), (727, "en peux plus")], "'épuisée' -> 'fatiguée'"),
 ("lea", "Maman ne pleure pas vraiment, mon cœur.", "Mummy isn't really crying, sweetheart.",
  [(730, "Maman ne pleure pas vraiment"), (731, "mon cœur")], "to her small child who walks in"),
 ("lea", "Je répète un rôle. Va jouer dans ta chambre.", "I'm rehearsing a part. Go and play in your room.",
  [(731, "Je répète"), (732, "Va jouer dans ta chambre")], ""),
 ("lea", "Je les aime tellement.", "I love them so much.",
  [(733, "Je les aime tellement")], ""),
 ("lea", "Je suis là pour eux tous les jours, mais ça ne suffit jamais.", "I'm here for them every day, but it's never enough.",
  [(735, "Je suis là pour eux"), (736, "suffit jamais")], "'24h/24' -> 'tous les jours'"),
 ("mathias", "Non, ça ne suffit jamais.", "No, it's never enough.",
  [(736, "Ça ne suffit jamais")], ""),
 ("mathias", "Comment on fait pour être un bon père?", "How do you be a good father?",
  [(737, "Comment on fait pour être un bon père")], ""),
 ("mathias", "Je ne suis pas un bon père.", "I'm not a good father.",
  [(738, "Je ne suis pas un bon père")], ""),
]

OPENER = ("Let's go through it together. First we're at the agency with Andréa, and then at Audrey's flat.")

WALK = [
 (0, None,
  "'Look! It's in all the papers.' The plural for 'newspaper' ends with an X sound, changes its ending from 'al' to 'aux'."),
 (1, None,
  "'Audrey went to Kadropov's party for twenty thousand euros!' The past tense of 'to go' uses 'to be' as its helper verb, and takes a feminine ending for Audrey."),
 (2, None,
  "'That's not possible! Will you deal with it, Mathias?' Literally 'you take care of it'. The little word for 'of it' sits right before the verb."),
 (3, None,
  "'Mathias! He had promised me secrecy.' Now we are at Audrey's flat. She thought nobody would ever know about the party."),
 (4, None,
  "'If Kadropov goes out with a beautiful woman like you, he tells everyone!' Even though Mathias is scolding her, he slips in a compliment."),
 (5, None,
  "'Do you think I'm beautiful?' Literally 'do you find me beautiful?'. French uses 'to find' for 'to think someone is'."),
 (6, None,
  "'Yes, you're very beautiful.' Mathias drops his tough tone and means it."),
 (7, None,
  "'That's so kind.' The word before 'kind' means 'so' or 'so much'. Audrey starts to cry."),
 (8, None,
  "'I'm tired, Mathias. I can't take it anymore.' The second sentence is a fixed expression: literally 'I cannot of it any more'."),
 (9, None,
  "'Mummy isn't really crying, sweetheart.' Her little boy walks into the room, and she calls him 'my heart'."),
 (10, None,
  "'I'm rehearsing a part. Go and play in your room.' The verb for 'to repeat' also means 'to rehearse' for an actor."),
 (11, None,
  "'I love them so much.' Once the child goes back to his room, Audrey lets her guard down. The word for 'them' comes before the verb."),
 (12, None,
  "'I'm here for them every day, but it's never enough.' Instead of 'not', the negation uses 'never' after the verb 'is enough'."),
 (13, None,
  "'No, it's never enough.' Mathias repeats her words quietly, thinking of his own children, Camille and Hippolyte."),
 (14, None,
  "'How do you be a good father?' Literally 'how does one do in order to be a good father?'."),
 (15, None,
  "'I'm not a good father.' A rare honest moment from Mathias, who is making a mess of his own family."),
]

TRANSITION = "Let's listen to the whole scene one more time."

OUTRO = ("Mathias and Audrey forgive each other, and now Mathias has to find a way to save Audrey's image after the Kadropov photos. "
         "Notice how French uses 'to find' to say what you think of someone: 'you find me beautiful?'. See you next time.")
CLOSING = ("lea", "C'est tellement gentil.")
