ID = 'aangan-haveli-s01e01-scene-02'
SHOW, SEASON, EPISODE, SCENE = 'aangan-haveli', 1, 1, 2
TITLE = 'गरम बन और दो घंटियाँ  (Warm Rolls and Two Rings)'
LEVEL, PAIR = 'A1 — beginner', 'hi-en'
LABELS = {'diya': 'दीया', 'kavya': 'काव्या', 'pratap': 'प्रताप'}

INTRO = ('In the four-table café corner off the courtyard, morning baker Diya pulls a tray of warm buns '
 'from the oven and comes out to meet Kavya while Pratap listens in. Hear the Hindi scene all the '
 'way through first.')
OPENER = "Now let's walk through the conversation one line at a time."
TRANSITION = "Now let's listen to the whole scene again from start to finish."
OUTRO = ('Kavya has met Diya, tasted a warm morning bun, and learned why the Room 4 buzzer rings twice by '
 'itself. We will check in with the guesthouse owner next. Until next time.')
CLOSING = ('diya', 'जल्द मिलेंगे!')

STORY = [('diya',
  'नमस्ते! तुम काव्या हो ना? मैं रसोई से दीया हूँ।',
  'Hello! You must be Kavya, right? I am Diya from the kitchen.'),
 ('kavya',
  'आपसे मिलकर ख़ुशी हुई, दीया। बहुत अच्छी ख़ुशबू आ रही है!',
  'Nice to meet you, Diya. Something smells wonderful!'),
 ('diya',
  'सुबह के ताज़े बन हैं! एक लो, अभी गरम है।',
  'Fresh morning buns! Take one while it is still warm.'),
 ('kavya',
  "धन्यवाद! क्या हम यहाँ आपस में 'तुम' बोलते हैं?",
  "Thank you! Do we use casual 'tum' with each other here?"),
 ('diya',
  'मेरे साथ हमेशा! भारी-भरकम आदर मेहमानों के लिए रखो।',
  'With me, always! Save the heavy formal talk for the guests.'),
 ('pratap',
  'दीया हमारी गली में सब से पुराने दोस्तों की तरह बात करती है।',
  'Diya talks to everyone on our lane like old friends.'),
 ('diya',
  'क्योंकि अच्छी कॉफ़ी और गरम ब्रेड लोगों को दोस्त बना देती हैं!',
  'Because good coffee and warm bread turn people into friends!'),
 ('kavya', 'वह कैसी घंटी थी? किसी ने दो बार बजाई!', 'What was that bell? Somebody rang twice!'),
 ('pratap',
  'वहाँ कोई नहीं है। वह कमरा चार की घंटी है।',
  'Nobody is there. That is the buzzer from room four.'),
 ('diya',
  'जब कमरा चार ख़ाली होता है, तब भी पुराना तार दो बार बजता है।',
  'Even when room four is empty, the old wire rings twice.'),
 ('kavya', 'तो हवेली अपने आप नमस्ते कहती है?', 'So the haveli says hello on its own?'),
 ('diya', 'बिल्कुल! तुम तो अभी से यहाँ घुल-मिल गईं।', 'Exactly! You already fit right in here.')]

WALK = [(0,
  None,
  ["'Hello! You must be Kavya, right? I am Diya from the kitchen.' Putting ",
   (None, 'ना?'),
   " at the end of a statement turns it into a friendly 'right?' or 'aren't you?'."]),
 (1,
  None,
  ["'Nice to meet you, Diya. Something smells wonderful!' Hindi speakers say a pleasant scent 'is "
   "coming', so ",
   (None, 'अच्छी ख़ुशबू आ रही है!'),
   " literally means 'good fragrance is coming'."]),
 (2,
  None,
  ["'Fresh morning buns! Take one while it is still warm.' Diya hands one over with ",
   (None, 'एक लो,'),
   ", a breezy 'take one' between peers."]),
 (3,
  None,
  ["'Thank you! Do we use casual tum with each other here?' Starting a sentence with ",
   (None, 'क्या'),
   ' flips a plain statement into a yes-or-no question without rearranging a single word.']),
 (4,
  None,
  ["'With me, always! Save the heavy formal talk for the guests.' Repeating the sound in ",
   (None, 'भारी-भरकम'),
   " pairs 'heavy' with an echo partner to mean 'stiff and overly formal'."]),
 (8,
  None,
  ["'Nobody is there. That is the buzzer from room four.' Notice how ",
   (None, 'कमरा चार की घंटी'),
   " uses 'kee'—Hindi's 'of' changes its ending to match 'ghantee' ('bell'), which is feminine."]),
 (10,
  None,
  ["'So the haveli says hello on its own?' The handy reflexive chunk ",
   (None, 'अपने आप'),
   " means 'by itself' or 'automatically', whether for people or creaky old wiring."]),
 (11,
  None,
  ["'Exactly! You already fit right in here.' That single word ",
   (None, 'बिल्कुल!'),
   " is one of everyday Hindi's most useful replies for 'absolutely!' or 'spot on!'."])]
