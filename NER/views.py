from django.shortcuts import render


# Create your views here.

import re

cities_Andra_pradesh = 'Adoni | Anantapuram | Amaravati | Bhimavaram | Chilakaluripet | Chittoor | Dharmavaram | Eluru | Gudivada | Guntakal | Guntur | Hindupur | Kadapa | Kadiri | Kakinada | Kurnool | Machilipatnam | Madanapalle | Mangalagiri-Tadepalli | Nandyal | Narasaraopet | Nellore | Ongole | Proddatur | Rajamahendravaram | Srikakulam | Tadepalligudem | Tadipatri | Tenali | Tirupati | Vijayawada | Visakhapatnam | Vizianagaram'
towns_andra_pradesh ='Repalle | Venkatagiri | Amalapuram | Payakaraopeta | Jaggayyapeta | Parvathipuram | Palamaner | Rajampet | Puttur | Punganur | Pithapuram | Bheemunipatnam | Mandapeta | Sattenapalle | Bobbili | Samarlakota | Kandukuru | Macherla | Palasa | Nuzvid | Narasapuram | Dhone | Ponnur | Pileru | Rayadurgam | Nagari | Vinukonda | Piduguralla | Tadepalle | Pulivendula | Badvel | Bapatla | Markapuram | Gudur | Tanuku | Srikalahasti | Palakollu | Anakapalli | Kadiri | Kavali | Rayachoti | Chirala | Yemmiganur'
villages_andra_pradesh ='Ambugaon | Anderband | Antargaon | Arli | Arli T | Bandalnagapur | Belsari Rampur | Bheempoor | Dabbakuchi | Dhanora | Ghotkuri | Girgaon | Gollaghat | Gomutri | Gona | Guledi | Gunjala | Hasnapur | Jamdi | Kamathwada | Karanji | Khapperla | Nipani | Palodi Ramnagar | Pippalkhoti | Ponnari | Savargaon | Tamsi | Tamsi | Waddadi | Wadgaon | Wadoor | Adilabad | Ankapoor | Ankoli | Anukunta | Arli | Asodabhurki | Battisawargaon | Belluri | Bheemseri | Borenur | Chanda | Chichadhari | Chinchughat | Dimma | Hathigutta | Jamdapur | Jamuldhari | Kachkanti | Khanapoor | Khandala | Kottur | Nevegaon| Kumbhajheri | Landasangvi | Lohara | Lokari | Maleborgaon | Maregaon | Mavala | Nishanghat | Pippaldhari | Pochara | Ramai | Rampoor | Royati | Takli | Tippa | Tontoli | Waghapur | Wanwat | Yapalguda | Ada | Akoli | Akurla | Bahadurpur | Balapur | Ballori | Belgaon | Bhoraj | Deepaiguda | Dollara | Fouzpur | Gimma | Guda | Hashampur | Hathighat | Jainad | Jamini | Kamai | Kamtha | Kanpa | Mediguda | Karanji | Kedarpur | Khapri | Korta | Kowtha | Kura | Laxmipur |Uligan | Lekarwadi | Makoda | Mangurla | Moudagada | Muktapur | Nirala | Nizampur | Pardi  | Pardi | Khurd | Pendalwada | Pippalgaon | Pipparwada | Poosai | Rampurtaraf | Sangvi | Savapur | Sirsonna | Tarada  Umri | Awalpur | Bela | Bhadi | Bhedoda | Bhodod |Kopsi | Boregaon | Chandpalle | Chaprala | Dehegaon | Dhoptala | Douna | Ekori | Guda | Junoni | Kamgarpur | Karoni | Karoni | Khadki | Khagdur | Kobhai | Mangrool | Manyarpur | Masala  | Masala | Mohabatpur | Patan | Pitgaon | Pohar | Ponnala | Ramkam | Sadarpur | Sahej | Sangdi | Sangvi | Shamshabad | Sirsanna | Sonkhos | Syedpur | Takli | Toyaguda | Kora | Warur | Arli  | Bharampur | Dehegaon | Devapur | Dorli | Jhari | Kajjarla | Kappardevi | Khodad | Kosai | Kothur | Kuchalapoor | Lachampur | Lingi | Madnapoor | Nandigaon | Palasi  | Palasi| Palle  | Palle | Ratnapur | Ruyyadi | Saknapoor | Sunkidi | Talamadugu | Umadam | Umrei | Belluri | Dhampur | Dongargaon | Gondharkapur | Gudihathinur | Guruj | Kamalapur | Kolhari | Lingapur | Machapur | Malkapur | Mannur | Muthnur | Neradigonda | Rendlabori | Seetagondi'

states = ' Andhra Pradesh | Arunachal Pradesh | Assam | Bihar | Chhattisgarh | Goa |goa| Goa| Gujarat | Haryana | Himachal Pradesh | Jharkhand | Karnataka | Kerala | Madhya Pradesh | Maharashtra | Manipur | Meghalaya | Mizoram | Nagaland | Odisha | Punjab | Rajasthan | Sikkim | Tamil Nadu | Telangana | Tripura | Uttar Pradesh | Uttarakhand | West Bengal |Andaman and Nicobar Islands | Chandigarh | Dadra and Nagar Haveli and Daman and Diu | Delhi | Lakshadweep | Jammu and Kashmir | Ladakh | Puducherry'
cities =  'Mumbai | bombay | Bambai | Calcutta | Bangalore | Kolkata | Chennai | Hyderabad | Ahmedabad | Pune | Jaipur | Surat | Lucknow | Kanpur | Nagpur | Visakhapatnam | Vadodara | Ghaziabad | Rajkot | Coimbatore | Patna | Agra | Madurai | Nashik | Faridabad | Ludhiana | Vijayawada | Aurangabad | Bhopal | Jodhpur | Guwahati | Kochi | Mysore | Dehradun | Indore | Itanagar | Naharlagun | Dibrugarh | Silchar | Jorhat | Gaya | Bhagalpur | Muzaffarpur | Raipur | Bhilai | Bilaspur | Panaji | Margao | Vasco da Gama | Gurgaon | Ambala | Shimla | Dharamshala | Mandi | Ranchi | Jamshedpur | Dhanbad | Thiruvananthapuram | Kozhikode | Bhubaneswar | Cuttack | Rourkela | Amritsar | Jalandhar | Udaipur | Gangtok | Warangal | Agartala | Siliguri | Durgapur |Mumbai| bombay| Bambai| Calcutta | Bangalore| Kolkata| Chennai| Hyderabad| Ahmedabad| Pune| Jaipur| Surat| Lucknow| Kanpur| Nagpur| Visakhapatnam| Vadodara| Ghaziabad| Rajkot| Coimbatore| Patna| Agra| Madurai| Nashik| Faridabad| Ludhiana| Vijayawada| Aurangabad| Bhopal| Jodhpur| Guwahati| Kochi| Mysore| Dehradun| Indore| Itanagar| Naharlagun| Dibrugarh| Silchar| Jorhat| Gaya| Bhagalpur| Muzaffarpur| Raipur| Bhilai| Bilaspur| Panaji| Margao| Vasco da Gama| Gurgaon| Ambala| Shimla| Dharamshala| Mandi| Ranchi| Jamshedpur| Dhanbad| Thiruvananthapuram| Kozhikode| Bhubaneswar| Cuttack| Rourkela| Amritsar| Jalandhar| Udaipur| Gangtok| Warangal| Agartala| Siliguri| Durgapur|Mumbai |bombay |Bambai |Calcutta |Bangalore |Kolkata |Chennai |Hyderabad |Ahmedabad |Pune |Jaipur |Surat |Lucknow |Kanpur |Nagpur |Visakhapatnam |Vadodara |Ghaziabad |Rajkot |Coimbatore |Patna |Agra |Madurai |Nashik |Faridabad |Ludhiana |Vijayawada |Aurangabad |Bhopal |Jodhpur |Guwahati |Kochi |Mysore |Dehradun |Indore |Itanagar |Naharlagun |Dibrugarh |Silchar |Jorhat |Gaya |Bhagalpur |Muzaffarpur |Raipur |Bhilai |Bilaspur |Panaji |Margao |Vasco da Gama |Gurgaon |Ambala |Shimla |Dharamshala |Mandi |Ranchi |Jamshedpur |Dhanbad |Thiruvananthapuram |Kozhikode |Bhubaneswar |Cuttack |Rourkela |Amritsar |Jalandhar |Udaipur |Gangtok |Warangal |Agartala |Siliguri |Durgapur '


cities_Arunachal_Pradesh = 'Bordumsa | Changlang | Jairampur | Kharsang | Khemiyong | Manmao | Miao | Nampong | Vijaynagar | Vijoypur | Anini | Bameng | Bana | Chyangtajo | Khenewa | P.kessang | Palizi | Pipu-dipu | Seijosa | Seppa | Thrizino | Veo | Adipasi | Boleng | Borguli | Damro | Gtc | Pasighat | Ruksin | Chakma | Danglat | Kamlang Nagar | Kherem | Lohitpur | Medo | Namsai | Tezu | Wakro | Bomdila | Dirang | Kalaktang | Tawang | Basar | Likabali | Logum Jining | Roing | Daporijo | Balukpong'

villages_Arunachal_Pradesh = 'Bubang | Chopelling | Deban | Dharampur | Gandhigrams | Bisa | Kutum | Lallung | Manabhum | Namchik | Namdang | Namphai | Namtok | New Kamlao | New Mohang | Rajanagar | Rangfrah | Ranglom | Two-hat | Yangkang | Alinye | Anelih | Etalin | Ayeng | Balek | Bilat | Dalbing | Debing | Hill Top | Kebang | Korang | Koyu | Ledum | Mebo | Nari | Ngopok | Oyan | Pangin | Rani | Renging | Riga | Sille | Silluk | Sirem | Yagrung | Mirem | Mikong | Chambang | Damin | Hiya | Nyapin | Palin | Sangram | Sarli | Tali | Alubari | Changliang | Chowkham | Gohaingaon | Innao | Jaipur | Kumari Kachari | Kumsai | Lathao | Loiliang | Mahadevpur | Momong | Nanam | Peyong | Podumani | Sunpura | Tafragram | Tindolong | Udaipur | Wingko | Yealing | Abango | Anupam | Bijari | Bomjir | Dambuk | Desali | Elopa | Hunli | Iduli | Jia | Koranu | Kronli | Meka | Paglam | Parbuk | Santipur | Boasimla | Deed | Godak | Hija | Joram | Mengio | Raga | Talo | Yazali | Ziro | A P Sectt | Balijan | Hawa Camp | Kheel | Kimin | Kokila | Midpu | Model Village | Naharlagun | Nirjuli | Ram Krishna Mission | Sonajuli | Vivek Vihar | Gispu | Lhou | Lumberdung | Mukto | Sakpret | Temple Gompa | Thingbu | Zimithang | Borduria | Dadam | K/nokno | Kaimai | Khela | Kheti | Khonsa Basti | Khotnu | Lazu | Longfong | Minthong | Namsang Mukh | Narottam Nagar | Nginu | Niausa | Panchou | Senewa | Soha | Thinsa | Tupi | Valley View | Geku | Gelling | Karko | Mariyang | Migging | Shimong | Singa | Tuting | Dumporijo | Giba | Lemiking | Lepajaring | Muri | Nacho | Sippi | Siyum | Tabarijo | Taksing | Taliha | Balemu | Bhalukpong | Dahung | Dedza | Dirang Basti | Khellong | Lish | Munna Camp | Nafra | Rupa | Salari | Sangti | Senge | Shergaon | Singchung | Tenga Market | Tenzingaon | Tippi | Bagra | Bame | Bene | Dali | Darak | Daring | Darka | Garu | Gensi | Kambang | Kaying | Kombo | Likabali | Liromoba | Mechuka | Monigong | Nikte | Payum | Rumgong | Tato | Tirbin | Vivek Nagar | Yomcha' 


offensive_words = [
    # English offensive words (with common variations)
    "abuse", "idiot", "stupid", "dumb", "fool", "fuck", "benchod",
    "bastard", "moron", "loser", "jerk", "trash",
    "scum", "psycho", "dirtbag", "weirdo", "clown",
    "crazy", "lazy", "douche", "pervert", "creep",
    "scumbag", "useless", "annoying", "lame", 
    "disgusting", "filthy", "gross", "pathetic", 
    "worthless", "unworthy", "cheater", "liar", 
    "backstabber", "snake", "traitor", 
    "cuss", "curse", "damn", "hell", "piss", 
    "suck", "crap", "bull", "garbage", "dirt", 

    # Highly offensive English words (censored versions)
    "f***", "fck", "fk", "f**k", 
    "sh*t", "sh1t", "sht", 
    "b***h", "b!tch", "b1tch", 
    "c**k", "c0ck", "cok", 
    "a**", "a$$", "assh***", "ashole", 
    "p***", "p*rn", "p0rn", 
    "d***", "d**k", "d1ck", 
    "s**t", "sht", "sc*mb*g", 
    "wh***", "w***e", "wh0re", "hoe", 
    "sl*t", "sl**", "s1ut", 
    "m***", "mf", "m*therf*cker", 
    "r**ard", "r3tard", "idi*t", 
    "d***head", "douchebag", "a**hole", "ashole", 

    # Hinglish abusive words (common in India/Pakistan region)
    "chutiya", "ch*tiya", "chutiye", "c#utiya", 
    "madarchod", "m**c", "m@darchod", 
    "bhenchod", "b**c", "b#nchod", 
    "bhosdike", "bh0sdike", "bh0sdi", 
    "randi", "r@ndi", "randwa", 
    "gandu", "ga**u", "g@ndu", 
    "suar", "s**r", "s*ar", 
    "chinal", "ch**al", "ch#nal", 
    "harami", "h**rami", "h@rami", 
    "kutta", "k#tta", "kutti", "k*tti", 
    "launde", "la**de", "l@unde", 
    "kamina", "k*mina", "k@mina", 
    "tatti", "ta**i", "t@tti", 
    "ghatiya", "ghat*ya", "g@tiya", 
    "nalayak", "n@layak", "n*layak", 
    "lafanga", "l@fanga", "laf*nga", 
    "bevda", "b#vda", "bev**a", 
    "bhikhari", "b#khari", "bh*khari", 

    # Variations of known Hinglish terms
    "chut", "choot", "ch0ot", 
    "bhosda", "bh0sda", 
    "mc", "bc", 
    "r**di", "r@ndi", 
    "bkl", "bekar", 
    "gaand", "g**nd", "g@and", 
    "chu", "choo", "ch0o", 
    "chodu", "chodu", "chod**", 
    "tatte", "ta**e", 
    "katwa", "k@twa", 
    "kameena", "k@m**na", 
    "chutiyapa", "ch*t**pa", 
    "bakchod", "b@kchod", 
    "ullu", "ul**u", 
    "kutta", "kutya", "kut**", 
    "bevakoof", "bev*koof", 

    # Internet/online disguised versions (used to avoid censorship)
    "f4ck", "phuck", "phk", "p0rn", "p@rn", 
    "fuk", "fuc*", "fu*k", 
    "sux", "scks", "sck", 
    "c*ck", "c0ck", "c@ck", 
    "sht", "sh1t", "sh*t", 
    "b1tch", "b*tch", "b!tch", 
    "s1ut", "sl*t", "s|ut", 
    "a$$", "4$$", "a55", 
    "h3ll", "h3ll", "he||", 
    "cr@p", "cr4p", "sh1t", 
    "f*ck", "f*ck", "f|ck", 
    "a**", "a55", "4$$", 
    "p*rn", "p0rn", "p@rn", 

    # Offensive animal references
    "pig", "p!g", "dog", "d0g", "donkey", 
    "ass", "coward", "chicken", "goat", 
    "rat", "snitch", "monkey", 
    "buffalo", "bhains", "bhais", "bhandar", 

    # Offensive words related to social status or race
    "slave", "servant", "dog", 
    "beggar", "bhikhari", "pest", 
    "cheap", "gutter", "sewer", 
    "untouchable", "unclean", "low-class", 
    "trash", "poor", "beg", 
    "downtrodden", "peasant", "serf", 
    "drunkard", "alcoholic", "addict", 
    "sinner", "infidel", "heretic", 

    # 🚨 **Extreme English Offensive Words**
    "f***", "f**k", "fck", "f*ck", "f4ck", 
    "b***h", "b*tch", "b1tch", "b!tch", "b!t", 
    "sh*t", "sh1t", "sht", "s**t", "sh!t", 
    "d***", "d1ck", "d!ck", "d!k", "dic*", 
    "c**k", "c0ck", "cok", "c*ck", 
    "a**", "a55", "a$$", "ashole", 
    "wh***", "wh0re", "wh*re", "w***e", "w**re", 
    "p***", "p0rn", "p*rn", "p@rn", "p0rn0", 
    "s**t", "sht", "s!ht", "s**tbag", 
    "d***head", "d**khead", "d*ckhead", 
    "a**hole", "a$$hole", "a**h**e", 
    "r***rd", "r3tard", "r*tard", 
    "f*g", "f@g", "f4g", "f*ggot", 
    "c***", "c*nt", "c@nt", "c*nt", 
    "d***face", "d*ckface", "d1ckface", 
    "m***erf***er", "m*therf*cker", "mf", "m*f", 
    "bastard", "jerk", "scum", "trash", 
    "douche", "douchebag", "creep", "pervert", 
    "lame", "loser", "psycho", "scumbag", 
    "a**wipe", "a**clown", "a**hat", 
    "sucker", "dirtbag", "clown", "filth", 

    # 🚨 **Extreme Hinglish Offensive Words**
    "chutiya", "ch*tiya", "chutiyapa", "ch#tiya", 
    "madarchod", "m**c", "m@darchod", "mc", 
    "bhenchod", "b**c", "bc", 
    "bhosdike", "bh0sdike", "b#sdike", 
    "randi", "r@ndi", "randiwa", 
    "gandu", "g@ndu", "ga**u", "gndu", 
    "launde", "la**de", "la#nde", 
    "kamina", "k@mina", "k*mina", 
    "harami", "h@rami", "h*rmi", 
    "kutta", "k#tta", "k*tta", 
    "chodu", "chodu", "ch0du", 
    "tatte", "ta**e", "tat**", 
    "gaand", "g*nd", "g@and", 
    "tatti", "ta**i", "tat*i", 
    "chut", "choot", "cho*t", 
    "bevda", "b#vda", "bev*da", 
    "lafanga", "laf*nga", "l@fnga", 
    "bhikhari", "b#khari", "b!khari", 
    "chinal", "ch*nal", "chinali", 
    "ullu", "ul**u", "ul#u", 
    "katwa", "k*twa", "k@tw@", 
    "bekar", "b@kar", "b*kar", 
    "nalayak", "nal*yak", "n@layak", 
    "bakchod", "b@kchod", "bak**od", 
    "bhosda", "bh0sda", "bh0sd", 

    # 🚨 **Animal-based Insults**
    "pig", "p!g", "swine", "dog", "d0g", 
    "kutta", "kutti", "k@tti", "rat", "snake", 
    "monkey", "donkey", "buffalo", "bhains", 
    "bhondar", "bhandar", "bakri", "goat", 
    "chuha", "ch*ha", "billi", "cat", 
    "gadha", "ghada", "g*dha", "coward", 

    # 🚨 **Racial and Discriminatory Words**
    "slave", "s*ave", "servant", 
    "beggar", "bhikhari", "pest", 
    "cheap", "ch*p", "gutter", 
    "trash", "poor", "beg", 
    "peasant", "serf", "drunkard", 
    "alcoholic", "addict", 
    "sinner", "infidel", "heretic", 
    "low-class", "unclean", 
    "untouchable", "unworthy", 

    # 🚨 **Offensive Variations Used Online (Bypassing Filters)**
    "f4ck", "phuck", "phk", "fuk", 
    "sux", "scks", "sck", 
    "c*ck", "c0ck", "c@ck", 
    "sh1t", "b1tch", "sl*t", 
    "s|ut", "4$$", "a55", 
    "he||", "h3ll", "cr@p", 
    "cr4p", "sh1t", "a55", 
    "p*rn", "p0rn", "p@rn", 
    "c**k", "c0ck", "a55h0le", 
    "d0uche", "duche", "f***er", 
    "f|ck", "f*ck", "fu*k", 
    "w|tch", "b*tch", "b!tch", 

    # 🚨 **Insults Related to Looks, Intelligence, or Status**
    "ugly", "stupid", "idiot", 
    "dumb", "moron", "retard", 
    "weirdo", "freak", "clown", 
    "disgusting", "pathetic", "filthy", 
    "worthless", "garbage", "trash", 
    "lazy", "slow", "dummy", 
    "worthless", "unworthy", 
    "backstabber", "liar", 
    "snake", "traitor", "two-faced", 
    "waste", "annoying", 
    "loser", "psycho", "useless", 


    # Common Hinglish abusive words
    "chutiya", "chutiyapa", "chutiye", 
    "madarchod", "maderchod", "madarchod", 
    "bhenchod", "bhenchod", "bhencho", 
    "bhosdike", "bhosdi", "bhosda", 
    "randi", "randwa", 
    "gandu", "gandu", 
    "suar", "suar", 
    "chinal", "chinal", 
    "harami", "haramkhor", 
    "kutta", "kutti", 
    "launde", "launda", 
    "kamina", "kamina", 
    "tatti", "tatti", 
    "ghatiya", "ghatiya", 
    "nalayak", "nalayak", 
    "lafanga", "lafanga", 
    "bevda", "bevda", 
    "bhikhari", "bhikhari", 

    # Variations of Hinglish offensive words
    "chut", "choot", 
    "bhosda", "bhoda", 
    "mc", "bc", 
    "randi", "rand", 
    "bekar", 
    "gaand", "gand", 
    "chu", "choo", 
    "chodu", "chodu", 
    "tatte", "tatte", 
    "katwa", 
    "kameena", "kameena", 
    "chutiyapa", 
    "bakchod", 
    "ullu", 
    "kutya", 
    "bevakoof", 

    # Animal references used as insults
    "kutta", "kutti", 
    "suar", "bhains", "bhais", "bhandar", 
    "gadha", "gadhi", 
    "ullu", 

    # Words targeting social status or class
    "bhikhari", "beggar", 
    "gutter", "gandagi", 
    "cheap", "nalayak", 
    "bevda", 
    "peasant", 
    "lafanga", 

    # Blended Hinglish slang used online
    "mc", "bc", "chut", 
    "gandu", "harami", 
    "kutta", "kameena", 
    "madarchod", "bhenchod", 
    "chinal", 
    "nalayak", 
    "launda", "launde", 
    "bakchod", 
    "bevkuf", "bevakoof", 
    "chutiyapa", 
    "ullu",

    
    "fool", "idiot", "stupid", "dumb", "bastard", "moron", "loser", "jerk", "trash", "scum", 
    "psycho", "dirtbag", "weirdo", "clown", "crazy", "lazy", "douche", "pervert", "creep", 
    "scumbag", "useless", "annoying", "lame", "disgusting", "filthy", "gross", "pathetic", 
    "worthless", "unworthy", "cheater", "liar", "backstabber", "snake", "traitor", "cuss", 
    "curse", "damn", "hell", "piss", "suck", "crap", "bull", "garbage", "dirt", "retard", 
    "coward", "slave", "beggar", "drunkard", "junkie", "degenerate", "lowlife", "failure", 
    "disgrace", "leech", "parasite", "burden", "mistake", "freak", "lunatic", "failure", 
    "pig", "dog", "rat", "snake", "donkey", "buffalo", "goat", "chicken", "insect", "worm", 
    "cockroach", "mosquito", "pest", "cock", "dick", "penis", "vagina", "asshole", "scumbag", 
    "dirtbag", "a**hole", "whore", "slut", "prostitute", "harlot", "wench", "witch",
    
    # sexual harrasment
    "sexual abuse", "rape", "molestation", "assault", "groping", "harassment", "victim", 
    "sexual predator", "pervert", "creep", "masturbation", "pornography", "incest", 
    "sexually explicit", "sex offender", "sexual exploitation", "victim blaming", 
    "objectification", "sexual object", "unwanted touch", "sexual misconduct", "rape culture", 
    "locker room talk", "sexual assault", "disrespect", "inappropriate comments", "predatory behavior", 
    "catcalling", "whistling", "stalking", "sexual comments", "lewd behavior", "sexual intimidation", 
    "sexist", "misogyny", "chauvinistic", "toxic masculinity", "victim shaming", "harasser", 
    "perpetrator", "assailant", "degrading", "humiliating", "shaming", "invasive behavior", 
    "exploitation", "unwanted advances", "disrespectful", "degrading language", "sexist remarks", 
    "unwanted flirtation", "harassing behavior", "inappropriate touch", "unwanted sexual attention",

    # hindi words abuse

    "balatkaar", "balatkaarhi", "khaali raat", "dushkarman", "ashlil baatein", "lingik atyachaar", 
    "jabarjasti", "gharwahi", "chhedchaad", "ghilaaf", "saahasik dushkarman", "nindak", "pratirodh", 
    "balaatkaar", "yatharth", "chhupke se", "mahila atyachaar", "buri niyat", "unkahi baatein", 
    "beizzati", "jamakhori", "apraadhik vyavhaar", "sarvashaktimaan", "anuchit prabhaav", 
    "bhoolbhalai", "manoviya atyachaar", "yaun anuchit vyavhaar", "jabarjasti sambandh", "ganda vyavhaar", 
    "lingik ghatanayein", "bhayankar anubhav", "yaun uttejan", "sahasik atyachaar", "unhoon ki vyavhaar", 
    "kudrati chhedchhad", "zabardasti", "hinsa", "jameen ka ganda vyavhaar", "nafrat ka prabhav", 
    "krodh bhari baatein", "vyaktiyon ka atyachaar", "abhiprerit vyavhaar", "shaktishaali vyavhaar", 
    "shabd ganda karne wali", "vyavhaar apmaanjanak", "laajh se jyada", "ganda soch", "krodh yukt baatein", 
    "sahasik samarthan", "unnat vyavhaar", "chhupke se nafrat", "jandali hinsa", "dhoka dena", 
    "pareshani ko badhawa dena", "ashlil soch", "maasoomiyon ko dikhawa dena", "apmaanjanak vyavhaar",


]

import re

class ner_logic:
    
    def build(self, inp):
        results = ''
        words= offensive_words
        patterns = r'\b(' + '|'.join(map(re.escape, words)) + r')\b'
        matches_offensive_words = re.findall(patterns, inp.lower())
    
        match_find_cities = re.findall(r'\b(?:' + '|'.join(cities.split(' | ')) + r')\b', inp, re.IGNORECASE)
    
        match_find_cities_andra_pradesh = re.findall(r'\b(?:' + '|'.join(cities_Andra_pradesh.split(' | ')) + r')\b', inp, re.IGNORECASE)
        match_find_cities_Arunachal_Pradesh = re.findall(r'\b(?:' + '|'.join(cities_Arunachal_Pradesh.split(' | ')) + r')\b', inp, re.IGNORECASE)
        
        match_find_town_andra_pradesh = re.findall(r'\b(?:' + '|'.join(towns_andra_pradesh.split(' | ')) + r')\b', inp, re.IGNORECASE)
        match_find_villages_or_town_Arunachal_Pradesh = re.findall(r'\b(?:' + '|'.join(villages_Arunachal_Pradesh.split(' | ')) + r')\b', inp, re.IGNORECASE)
        
        match_find_village_andra_pradesh = re.findall(r'\b(?:' + '|'.join(villages_andra_pradesh.split(' | ')) + r')\b', inp, re.IGNORECASE)
        match_find_states = re.findall(r'\b(?:'+ '|'.join(states.split(' | ')) + r')\b', inp, re.IGNORECASE)

        pattern1= r'\b[6-9]\d{9}\b|\(\d{3}\)-\d{3}-\d{4}|\(\d{3}\) \d{3}-\d{4}'

        Mobile_No=re.findall(pattern1,inp)

        pattern2= r'[^ ]*\@[^ ]*'

        email= re.findall(pattern2,inp)

        results = [] 
        
        if match_find_cities_andra_pradesh or match_find_town_andra_pradesh or match_find_village_andra_pradesh or match_find_states or match_find_cities_Arunachal_Pradesh or match_find_villages_or_town_Arunachal_Pradesh or match_find_cities or matches_offensive_words or Mobile_No or email:
        
       
            results.append(f"Offensive words detected:{matches_offensive_words}")
            # results.append(f"States :{match_find_states}")
            # results.append(f"cities :{match_find_cities_andra_pradesh + match_find_cities_Arunachal_Pradesh + match_find_cities }")
            results.append(f"states/Towns/village: {match_find_states + match_find_cities_andra_pradesh + match_find_cities_Arunachal_Pradesh + match_find_cities + match_find_town_andra_pradesh + match_find_village_andra_pradesh + match_find_villages_or_town_Arunachal_Pradesh }")
            results.append(f"Email: {email}")
            results.append(f"Mobile No: {Mobile_No}")

        return "\n".join(results) if results else "No matches found."