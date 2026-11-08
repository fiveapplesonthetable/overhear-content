ID = 'aangan-haveli-s01e01-scene-05'
SHOW, SEASON, EPISODE, SCENE = 'aangan-haveli', 1, 1, 5
TITLE = 'ये मेरे कपड़े नहीं हैं!  (Not My Clothes!)'
LEVEL, PAIR = 'A1 — beginner', 'hi-en'
LABELS = {'kavya': 'काव्या', 'pratap': 'प्रताप', 'sudha': 'सुधा'}

INTRO = ('Minutes after going upstairs to Room 4, Sudha rings the front desk bell in alarm. Kavya and '
 'Pratap hurry up the stairs to see what happened. Listen to the Hindi scene first.')
OPENER = "Now let's walk through the conversation one line at a time."
TRANSITION = "Now let's listen to the whole scene again from start to finish."
OUTRO = ("Someone at Jaipur station swapped an identical dark-blue suitcase for Sudha's! They carry the "
 'heavy bag downstairs to examine the small paper tag in the light.')
CLOSING = ('kavya', 'फिर मिलेंगे!')

STORY = [('kavya',
  'सुधा मैडम, क्या सब ठीक है? आपने घंटी बजाई!',
  'Madam Sudha, is everything alright? You rang the bell!'),
 ('sudha',
  'इस सूटकेस के अंदर देखो, काव्या! यह मेरा बैग नहीं है!',
  'Look inside this suitcase, Kavya! This is not my bag!'),
 ('kavya',
  'रुकिए—यह तो गहरा नीला है, बिल्कुल आपके बैग जैसा!',
  'Wait—it is dark blue, just like your bag!'),
 ('sudha',
  'बाहर से बिल्कुल वैसा ही है, हाँ! पर अंदर देखिए!',
  'From the outside it is identical, yes! But look inside!'),
 ('pratap',
  'मर्दों के बड़े भूरे जूतों के दो जोड़े और स्लेटी स्वेटर।',
  "Two pairs of big brown men's shoes and grey sweaters."),
 ('kavya',
  'और यह सफ़ेद काग़ज़ में क्या लिपटा है? लकड़ी की एक छोटी रेलगाड़ी!',
  'And what is this wrapped in white paper? A little wooden train!'),
 ('sudha', 'मैं दस नंबर के जूते तो बिल्कुल नहीं पहनती!', 'I certainly do not wear size ten shoes!'),
 ('pratap', 'तभी यह इतना भारी था। लकड़ी और चमड़ा!', 'No wonder it was so heavy. Wood and leather!'),
 ('sudha',
  'रेलवे स्टेशन पर किसी ने ग़लती से मेरा नीला सूटकेस उठा लिया!',
  'Someone at the railway station picked up my blue suitcase by mistake!'),
 ('kavya',
  'कृपया बैठिए, मैडम। चिंता मत कीजिए, हम अभी इसका टैग देखते हैं।',
  'Please sit down, madam. Do not worry, we will check its tag right now.'),
 ('pratap',
  'बगल के हैंडल से काग़ज़ का एक छोटा कार्ड बँधा है।',
  'There is a small paper card tied to the side handle.'),
 ('sudha', 'आइए, इसे नीचे रोशनी में ले चलते हैं!', 'Come, let us bring it downstairs into the light!')]

WALK = [(0,
  None,
  ["'Madam Sudha, is everything alright? You rang the bell!' For completed past actions like 'rang', "
   "Hindi marks the doer with 'ne', turning 'aap' into ",
   (None, 'आपने घंटी बजाई!'),
   " while 'bajaayee' matches feminine 'ghantee'."]),
 (1,
  None,
  ["'Look inside this suitcase, Kavya! This is not my bag!' ",
   (None, 'के अंदर'),
   " means 'inside', and just like other location words in Hindi it sits after 'this suitcase', not "
   'before it.']),
 (2,
  None,
  ["'Wait—it is dark blue, just like your bag!' ",
   (None, 'आपके बैग जैसा!'),
   " tacks 'jaisaa' ('like') right onto 'your bag' to say 'just like yours'."]),
 (5,
  None,
  ["'And what is this wrapped in white paper? A little wooden train!' Hindi builds 'wooden' with ",
   (None, 'लकड़ी की'),
   ", literally 'of wood', using 'kee' to match feminine 'relgaaree' ('train')."]),
 (6,
  None,
  ["'I certainly do not wear size ten shoes!' In India shoe sizes follow numbers like nine or ten, and ",
   (None, 'दस नंबर के जूते'),
   " is how shoppers naturally say 'size ten shoes'."]),
 (7,
  None,
  ["'No wonder it was so heavy. Wood and leather!' Opening with ",
   (None, 'तभी'),
   "—literally 'right then / for that very reason'—gives a punchy one-word 'no wonder!'."]),
 (8,
  None,
  ["'Someone at the railway station picked up my blue suitcase by mistake!' Remember ",
   (None, 'ग़लती से'),
   ", literally 'from mistake', the everyday chunk for 'by mistake' or 'accidentally'."]),
 (9,
  None,
  ["'Please sit down, madam. Do not worry, we will check its tag right now.' ",
   (None, 'चिंता मत कीजिए,'),
   " is the gentle, respectful way to tell someone 'please don't worry'."])]
