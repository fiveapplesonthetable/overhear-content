ID = 'aangan-haveli-s01e02-scene-02'
SHOW, SEASON, EPISODE, SCENE = 'aangan-haveli', 1, 2, 2
TITLE = 'फ़्रिज में दूध नहीं है  (No Milk in the Fridge)'
LEVEL, PAIR = 'A1 — beginner', 'hi-en'
LABELS = {'diya': 'दीया', 'kavya': 'काव्या', 'mohan': 'मोहन'}

INTRO = ('Twenty minutes before the morning café opens, Diya bursts out of the kitchen looking at her '
 'phone in dismay. Mohan and Kavya rush over to see what went wrong. Listen to the Hindi scene '
 'first.')
OPENER = "Now let's walk through the conversation one line at a time."
TRANSITION = "Now let's listen to the whole scene again from start to finish."
OUTRO = ('With five hundred rupees from the cash box and a shopping bag in hand, Kavya sprints out toward '
 "the corner market. Let's see if she makes it back before seven thirty!")
CLOSING = ('kavya', 'चलती हूँ!')

STORY = [('diya',
  'अरे नहीं! मोहन जी, काव्या, रसोई में बड़ी मुसीबत हो गई है!',
  'Oh no! Mr Mohan, Kavya, we have a big emergency in the kitchen!'),
 ('mohan',
  'मेरी सुबह की कॉफ़ी से पहले कृपया मुसीबत शब्द मत बोलो!',
  'Please do not say the word emergency before my morning coffee!'),
 ('diya',
  'दूध वाली गाड़ी का टायर शहर के बाहर पंचर हो गया है। फ़्रिज में देखिए!',
  'The dairy van has a flat tyre outside town. Look in the fridge!'),
 ('kavya',
  'बस थोड़ा सा दूध, दो अंडे, और मक्खन तो बिल्कुल नहीं है!',
  'Only a tiny splash of milk, two eggs, and no butter at all!'),
 ('mohan',
  'साढ़े सात बजे आठ भूखे मेहमान सीढ़ियों से नीचे आएँगे!',
  'At seven thirty, eight hungry guests will come down the stairs!'),
 ('diya', 'कम से कम ओवन में मेरे बन का आटा तैयार है।', 'My bread is already in the oven, at least.'),
 ('kavya',
  'मुझे एक थैला और थोड़े नक़द पैसे दीजिए! कोने वाला बाज़ार सात बजे खुलता है।',
  'Give me a cloth bag and some cash! The corner market opens at seven.'),
 ('mohan',
  'क्या तुम दस मिनट में जाकर वापस आ सकती हो?',
  'Can you go there and come back in ten minutes?'),
 ('kavya',
  'अभी देखिए! ठीक-ठीक बताइए क्या-क्या ख़रीदना है।',
  'Watch me! Tell me exactly what all to buy.'),
 ('diya',
  'दूध की तीन बोतलें, बीस अंडे, मक्खन, पनीर और लाल सेब!',
  'Three bottles of milk, twenty eggs, butter, cottage cheese, and red apples!'),
 ('mohan',
  'गल्ले से ये पाँच सौ रुपये लो। पक्की रसीद ज़रूर लाना!',
  'Here are five hundred rupees from the cash box. Be sure to bring back a proper receipt!'),
 ('kavya',
  'मोर्चा सँभालिए—मैं तो दरवाज़े से बाहर निकल भी गई!',
  'Hold the fort—I am already out the door!')]

WALK = [(0,
  None,
  ["'Oh no! Mr Mohan, Kavya, we have a big emergency in the kitchen!' Everyday ",
   (None, 'बड़ी मुसीबत'),
   " means 'big trouble' or 'a real crisis' without sounding stiff or clinical."]),
 (1,
  None,
  ["'Please do not say the word emergency before my morning coffee!' ",
   (None, 'से पहले'),
   " follows 'my morning coffee' to say 'before my morning coffee'."]),
 (3,
  None,
  ["'Only a tiny splash of milk, two eggs, and no butter at all!' ",
   (None, 'थोड़ा सा दूध,'),
   " softens 'thoraa' ('a little') with 'saa' to mean 'just a tiny bit of milk'."]),
 (5,
  None,
  ["'At least my bun dough is ready in the oven.' Handy ",
   (None, 'कम से कम'),
   "—literally 'less than less'—is the exact Hindi match for 'at least'."]),
 (7,
  None,
  ["'Can you go there and come back in ten minutes?' Adding 'saknaa' onto a stem builds 'can', so ",
   (None, 'वापस आ सकती हो?'),
   " asks 'can you come back?'."]),
 (8,
  None,
  ["'Watch me! Tell me exactly what all to buy.' Doubling 'what' in ",
   (None, 'क्या-क्या'),
   " turns a single question into a list question: 'what all items?'."]),
 (10,
  None,
  ["'Here are five hundred rupees from the cash box. Be sure to bring back a proper receipt!' ",
   (None, 'पाँच सौ रुपये'),
   " combines 'paanch' ('five') and 'sau' ('hundred')—notice 'sau' never adds a plural ending."]),
 (11,
  None,
  ["'Hold the fort—I am already out the door!' Idiomatic ",
   (None, 'मोर्चा सँभालिए'),
   " literally says 'hold the front post', used playfully whenever you leave teammates in charge."])]
