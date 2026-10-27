# Authoring module for dix-pour-cent s01e02 scene 11 (cues 325-359, with merged scene 10 = cues 313-324 in the bridge).
# Build: python3 tools/compose.py out/dix-pour-cent/s01e02/authoring/scene-11.py --out out/dix-pour-cent/s01e02/scene-11.json

ID = "dix-pour-cent-s01e02-scene-11"
SHOW = "dix-pour-cent"
SEASON = 1
EPISODE = 2
SCENE = 11
TITLE = "Un film ne meurt jamais  (A Film Never Dies)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "emma": "emilie"}
LABELS = {"lea": "Andréa", "emma": "Emma"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S01E02"
SOURCE_FILE = "sources/dix-pour-cent/s01/e02.fr.dual.srt"

INTRO = ("So Gabriel has just offered Line Renaud the part, without a word to anyone. "
         "Back at the agency, nobody knows yet. Hervé and Camille are busy with the guest lists for Samuel's funeral: "
         "Gabriel said eighty people at most, but Mathias alone has fifty names on his list, "
         "in proportion, he says, to the money he brings in, and somebody adds Gabor Rajevski to theirs. "
         "Then Sofia shows in a visitor who is looking for Andréa: Emma, the producer of Gabor's film. "
         "She is furious, and she's here to say so. Andréa will defend herself, make a big promise, "
         "and then try to keep it, by phone. "
         "You'll hear it all in French first. Don't worry about the details; feel the argument.")

STORY = [
 ("emma", "Françoise a appelé. Elle dit que vous étiez odieux.", "Françoise phoned. She says you were odious.",
  [(325, "Françoise a appelé, elle dit que vous étiez odieux")], "'vous' = the agency, hence the masculine plural"),
 ("lea", "C'est tellement malhonnête! Elle avait déjà pris sa décision.", "That's so dishonest! She'd already made her decision.",
  [(326, "C'est tellement malhonnête ! Elle avait déjà pris sa décision")], ""),
 ("emma", "Et Piccoli ne fait pas le film sans Françoise.", "And Piccoli won't do the film without Françoise.",
  [(327, "Piccoli")], "retold from 'si ce n'est pas Françoise, il ne le fait pas'"),
 ("emma", "Sans Samuel, vous vous effondrez!", "Without Samuel, you're falling apart!",
  [(328, "Sans Samuel, vous vous effondrez")], ""),
 ("lea", "C'est vraiment bas, Emma.", "That's really low, Emma.",
  [(329, "c'est vraiment bas, Emma")], "the first half ('using Samuel's death against us') told by the narrator"),
 ("emma", "Je travaille sur ce projet depuis quatre ans!", "I've been working on this project for four years!",
  [(330, "Je travaille sur ce projet depuis quatre ans")], ""),
 ("emma", "Mais ce film est mort.", "But this film is dead.",
  [(333, "est mort")], "'il' made explicit as 'ce film'"),
 ("lea", "Non, c'est Samuel qui est mort.", "No, it's Samuel who is dead.",
  [(334, "Non, c'est Samuel qui est mort")], ""),
 ("lea", "Un film ne meurt jamais!", "A film never dies!",
  [(335, "Un film ne meurt jamais")], ""),
 ("lea", "On va trouver une solution.", "We'll find a solution.",
  [(336, "On va trouver une solution")], "Emma's mocking echo told by the narrator"),
 ("emma", "Une solution? Une grande actrice de quatre-vingts ans, libre dans trois semaines?",
  "A solution? A great eighty-year-old actress, free in three weeks?",
  [(338, "Une grande actrice de"), (339, "libre dans trois semaines")], "'que Gabor apprécie, qui n'a pas Alzheimer' left out"),
 ("lea", "On n'est pas obligés de remplacer Françoise Fabian.", "We don't have to replace Françoise Fabian.",
  [(340, "On n'est pas obligés de remplacer Françoise Fabian")], ""),
 ("lea", "Je vais la convaincre de revenir. J'en suis capable.", "I'm going to persuade her to come back. I can do it.",
  [(341, "Je vais la convaincre de revenir"), (342, "J'en suis capable")], ""),
 ("lea", "Allô, Françoise, c'est Andréa Martel.", "Hello, Françoise, it's Andréa Martel.",
  [(343, "Allô, Françoise, c'est Andréa Martel")], "the first voicemail"),
 ("lea", "Je voudrais m'excuser pour hier.", "I'd like to apologise for yesterday.",
  [(344, "Je voudrais m'excuser pour hier")], ""),
 ("lea", "J'ai une grande admiration pour vous.", "I have great admiration for you.",
  [(352, "J'ai une grande admiration pour vous")], "from the second voicemail"),
 ("lea", "Je me sens vraiment... nulle!", "I really feel... useless!",
  [(354, "Je me sens vraiment... nulle")], "the English subtitle is cruder; the French 'nulle' is clean"),
 ("lea", "Réservez-moi un massage, s'il vous plaît.", "Book me a massage, please.",
  [(359, "Réservez-moi un massage, s'il vous plaît")], "to Camille; 'pas avant vingt heures' dropped"),
]

OPENER = ("Let's go back through it. Emma comes straight in with what Françoise told her.")

WALK = [
 (0, "Françoise a appelé.",
  "'Françoise phoned.' The past tense with 'has' plus the verb, the everyday way to say something happened."),
 (0, "Elle dit que vous étiez odieux.",
  "'She says you were odious.' Here the polite 'you' is really plural: it means the whole agency, "
  "so 'odious' has a masculine plural ending, even though Andréa is a woman."),
 (1, "C'est tellement malhonnête!",
  "'That's so dishonest!' The long word in the middle means 'so', 'so very'."),
 (1, "Elle avait déjà pris sa décision.",
  "'She'd already made her decision.' In French you 'take' a decision, you don't make one. Emma has worse news."),
 (2, None,
  "'And Piccoli won't do the film without Françoise.' The negative wraps around the verb again: not, does, not. "
  "Then she goes for the jugular."),
 (3, None,
  "'Without Samuel, you're falling apart!' You hear the word for 'you' twice: once as the subject, "
  "once as 'yourselves', because this verb always comes with a 'self'."),
 (4, None,
  "'That's really low, Emma.' Andréa says it's low to use Samuel's death against them. Emma doesn't back down."),
 (5, None,
  "'I've been working on this project for four years!' A key pattern: French uses the present tense, plus a word meaning "
  "'since', for something that started in the past and is still going on. Literally 'I work on it since four years'."),
 (6, None,
  "'But this film is dead.' Two words, and Andréa won't accept them."),
 (7, None,
  "'No, it's Samuel who is dead.' That's what 'dead' means, she adds. It's sharp, and sad."),
 (8, None,
  "'A film never dies!' Not, then the verb, then 'never' instead of the usual second half. Andréa's battle cry."),
 (9, None,
  "'We'll find a solution.' The verb 'to go' plus another verb is the near future: we are going to find. "
  "Emma repeats it back to her, mockingly."),
 (10, None,
  "'A solution? A great eighty-year-old actress, free in three weeks?' In French you say 'an actress of eighty years'. "
  "Emma thinks no such person exists."),
 (11, None,
  "'We don't have to replace Françoise Fabian.' Literally 'we are not obliged to replace'. "
  "The word for 'obliged' takes a plural ending, because 'we' is plural."),
 (12, "Je vais la convaincre de revenir.",
  "'I'm going to persuade her to come back.' The near future once more, and the tiny word for 'her' sits right before "
  "the verb it belongs to."),
 (12, "J'en suis capable.",
  "'I can do it.' Literally 'I am capable of it'. Brave words. Emma leaves, and Andréa picks up the phone. "
  "Françoise doesn't answer, so she has to leave a message."),
 (13, None,
  "'Hello, Françoise, it's Andréa Martel.' On the phone, this is how you say who's calling: it's me, Andréa."),
 (14, None,
  "'I'd like to apologise for yesterday.' This 'would like' is the polite form of 'want'. "
  "But the message goes wrong, she gets tangled up, and the voicemail robot offers to let her record it again. She tries a second time."),
 (15, None,
  "'I have great admiration for you.' The word for 'great' comes before the noun, and it's feminine to match 'admiration'."),
 (16, None,
  "'I really feel... useless!' This verb comes with a 'self' too: I feel myself. And the word for 'useless' is feminine, "
  "for Andréa. On the third try the robot simply tells her she may hang up, and she says something very rude. "
  "So she turns to Camille."),
 (17, None,
  "'Book me a massage, please.' A polite command to her assistant, and the polite way of saying please, "
  "literally 'if it pleases you'. After a morning like this, who can blame her?"),
]

TRANSITION = "Okay. Now the whole thing again, from Emma's first line."

OUTRO = ("A rough morning for Andréa, but you came through it fine. "
         "Next time you hear someone say they've been doing something for years, listen for that present tense. Until next time.")
CLOSING = ("lea", "Bon courage!")
