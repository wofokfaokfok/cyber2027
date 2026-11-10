import math
def english_score(text):
    """
    מקבלת צופן (קיסר או טרנספוזיציה) ומחזירה את המשפט המפוענח.
    המפתח לא ידוע, ולכן מנסים את כל האפשרויות ושומרים אותן ברשימה all_options.
    הפענוח הנכון נמצא לפי רשימת המילים הקצרות (COMMON_WORDS)
    ורשימת המילים השכיחות (ENGLISH_WORDS).
    """
    # רשימת המילים הנפוצות הקצרות (אות אחת או שתיים) - למציאת הפענוח הנכון
    COMMON_WORDS = {
        "A", "I", "AM", "AN", "AS", "AT", "BE", "BY", "DO", "GO", "HE", "HI", "IF",
        "IN", "IS", "IT", "ME", "MY", "NO", "OF", "OH", "ON", "OR", "SO", "TO", "UP",
        "US", "WE",
    }

    # רשימת מילים שכיחות באנגלית
    ENGLISH_WORDS = {
        "ABOUT", "ABOVE", "ACROSS", "ACTOR", "ADD", "AFTER", "AGAIN", "AGAINST", "ALL",
        "ALLOW", "ALSO", "ALWAYS", "AND", "ANY", "APPLAUD", "ARE", "AROUND", "ARRIVE",
        "ARRIVES", "ARTIST", "ASK", "BABIES", "BABY", "BACK", "BAKE", "BAKER", "BAND", "BEAR",
        "BECAUSE", "BEEN", "BEFORE", "BEGIN", "BELIEVE", "BELL", "BELLS", "BELOW", "BETWEEN",
        "BIG", "BIRD", "BIRDS", "BLOCKS", "BLUE", "BOAT", "BODY", "BOILS", "BOOK", "BOWS",
        "BOX", "BOY", "BREAD", "BRIDGE", "BRIGHT", "BRING", "BROTHER", "BROTHERS", "BUILD",
        "BUS", "BUT", "CALL", "CALM", "CAMP", "CAN", "CANDLES", "CAPTAIN", "CARE", "CAREFUL",
        "CASE", "CAT", "CATS", "CELEBRATE", "CHANGE", "CHEERS", "CHEF", "CHILD", "CHILDREN",
        "CITY", "CLAP", "CLASS", "CLEARS", "CLIMB", "CLOCK", "CLOSES", "CLOUDS", "COLD",
        "COME", "COMET", "CONTEST", "COOK", "COOKS", "COOL", "COULD", "COWS", "CRAWL", "CREAK",
        "CREATE", "CROWD", "DANCES", "DAWN", "DAY", "DEPART", "DEPARTS", "DETECTIVE", "DID",
        "DIFFERENT", "DIFFICULT", "DIG", "DINNER", "DOES", "DOG", "DOGS", "DOOR", "DOORS",
        "DRAW", "DREAM", "DREAMS", "DRIFT", "DRIPS", "DRIVER", "DRIVERS", "DRUMMER", "DUCK",
        "DURING", "EACH", "EARLY", "EASY", "EVEN", "EVENING", "EVERY", "EXPERIMENT", "FACE",
        "FADES", "FAIR", "FALL", "FALLS", "FAMILY", "FANS", "FARMER", "FAST", "FATHER", "FEEL",
        "FENCE", "FERRY", "FESTIVAL", "FEW", "FIND", "FIRST", "FLASHES", "FLICKER", "FLIES",
        "FLOW", "FLOWERS", "FLY", "FOLLOW", "FOR", "FOREST", "FOUND", "FOX", "FRIEND",
        "FRIENDS", "FROGS", "FROM", "FUN", "GAME", "GARDEN", "GARDENERS", "GATE", "GATHER",
        "GENTLE", "GET", "GIRL", "GIVE", "GLOW", "GOOD", "GRANDMOTHER", "GRAZE", "GREAT",
        "GREEN", "GROWS", "HAD", "HAND", "HAPPEN", "HARD", "HAS", "HAVE", "HEALTH", "HEAR",
        "HELLO", "HELP", "HEN", "HER", "HERE", "HIGH", "HIM", "HIS", "HISTORY", "HOLD",
        "HOLIDAY", "HOME", "HOMEWORK", "HONEST", "HOPE", "HOPS", "HORSE", "HOT", "HOUR",
        "HOUSE", "HOW", "HOWL", "ICE", "IDEA", "IMPORTANT", "INSIDE", "INTO", "ISLAND", "ITS",
        "JOKE", "JUMP", "JUMPS", "JUST", "KEEP", "KETTLE", "KEY", "KID", "KIDS", "KIND",
        "KNOCK", "KNOW", "LAND", "LANDS", "LANTERNS", "LARGE", "LAST", "LATE", "LAUGH", "LEAD",
        "LEAP", "LEARN", "LEAVE", "LEAVES", "LEFT", "LET", "LEVEL", "LIBRARY", "LIFE",
        "LIGHTNING", "LIGHTS", "LIKE", "LINE", "LITTLE", "LIVE", "LOCAL", "LONG", "LOOK",
        "LOOKS", "LOSE", "LOST", "LOVE", "LOW", "MAKE", "MAN", "MANY", "MAP", "MARKET",
        "MATTER", "MEET", "MELTS", "MESSAGE", "MIDNIGHT", "MIGHT", "MONEY", "MONKEYS", "MONTH",
        "MOON", "MORE", "MORNING", "MOST", "MOTHER", "MOTHERS", "MOVE", "MUCH", "MUSEUM",
        "MUSIC", "MUST", "NAME", "NEAR", "NEIGHBORS", "NEST", "NESTS", "NEVER", "NEW", "NEXT",
        "NOON", "NOT", "NOW", "OFFER", "OFFICE", "OFTEN", "OLD", "ONE", "ONLY", "OPEN",
        "OPENS", "OTHER", "OUR", "OUT", "OUTSIDE", "OVER", "OWN", "OWNER", "PAINTS", "PAPER",
        "PARTY", "PASS", "PASSES", "PATIENCE", "PAY", "PEOPLE", "PERSON", "PHONE", "PLACE",
        "PLAN", "PLANE", "PLANES", "PLANTS", "PLAY", "PLAYS", "PLEASE", "POWER", "PRAY",
        "PROJECT", "PULL", "PUPPY", "PUSH", "QUIETLY", "RABBIT", "RAIN", "REACH", "READ",
        "READS", "REMEMBER", "REPORT", "REST", "RESTS", "RIDE", "RIGHT", "RING", "RINGS",
        "RISES", "RIVERS", "ROBOT", "ROOF", "ROOM", "ROOTS", "RUN", "RUNNERS", "RUNS", "SAFE",
        "SAME", "SANG", "SAY", "SCHOOL", "SCIENCE", "SEA", "SEASONS", "SEE", "SEEM", "SELL",
        "SEND", "SETS", "SHALL", "SHE", "SHEEP", "SHIP", "SHORT", "SHOULD", "SHOW", "SING",
        "SINGS", "SISTER", "SISTERS", "SKY", "SLEEP", "SLEEPS", "SLOW", "SLOWLY", "SLOWS",
        "SMALL", "SMILE", "SMILES", "SNAKES", "SNOW", "SOFA", "SOFTLY", "SOME", "SONG", "SOUP",
        "SPARKLE", "SPEAK", "SPEND", "STAND", "STANDS", "STARS", "STAY", "STILL", "STOP",
        "STOPS", "STORM", "STORMS", "STORY", "STREET", "STRONG", "STUDENTS", "STUDY",
        "SUCCESSFUL", "SUCH", "SUN", "SUNLIGHT", "SWIM", "SWIMS", "TAKE", "TALK", "TALKS",
        "TEA", "TEAM", "TELL", "TESTING", "THAN", "THANKS", "THAT", "THE", "THEIR", "THEM",
        "THEN", "THERE", "THESE", "THEY", "THINK", "THIS", "THROUGH", "TICKS", "TIME", "TODAY",
        "TOMORROW", "TOWER", "TOWN", "TRAIL", "TRAIN", "TRAINS", "TROTS", "TRY", "TURN",
        "TURTLES", "TWO", "UNDER", "USE", "VERY", "VISITOR", "VOLUNTEERS", "WAIT", "WALK",
        "WALKS", "WANT", "WARM", "WAS", "WATCH", "WATER", "WAVE", "WAY", "WEATHER", "WEEK",
        "WELL", "WERE", "WHAT", "WHEN", "WHERE", "WHICH", "WHILE", "WHISPERS", "WHO", "WHY",
        "WILL", "WIN", "WINDS", "WINNERS", "WINS", "WITH", "WITHOUT", "WOLF", "WOLVES",
        "WOMAN", "WONDERS", "WOODEN", "WORD", "WORDS", "WORK", "WORKERS", "WORKS", "WORLD",
        "WOULD", "WRITE", "WRITERS", "YEAR", "YOU", "YOUNG", "YOUR",
    }

    text = text.upper()
    if len(text) == 0:
        return 0

    # --- כל האפשרויות לפענוח ---
    all_options = []

    # צופן קיסר: כל 26 ההזזות
    for shift in range(26):
        option = []
        for ch in text:
            if ch.isalpha():
                option.append(chr((ord(ch) - ord('A') - shift) % 26 + ord('A')))
            else:
                option.append(ch)
        all_options.append(''.join(option))

    # צופן טרנספוזיציה: כל המפתחות (מספר עמודות) האפשריים
    for key in range(1, len(text) + 1):
        num_rows = math.ceil(len(text) / key)
        remainder = len(text) % key
        if remainder == 0:
            remainder = key

        columns = []
        position = 0
        for col in range(key):
            column_length = num_rows if col < remainder else num_rows - 1
            columns.append(text[position:position + column_length])
            position += column_length

        option = []
        for row in range(num_rows):
            for col in range(key):
                if row < len(columns[col]):
                    option.append(columns[col][row])
        all_options.append(''.join(option))

    # --- מציאת הפענוח הנכון ---
    # מילה קצרה תקינה (COMMON_WORDS) מוסיפה נקודה, מילה קצרה לא תקינה מורידה נקודה,
    # ובנוסף כל מילה שנמצאת ב-ENGLISH_WORDS מוסיפה נקודה.
    # האפשרות עם הכי הרבה נקודות היא הפענוח הנכון.
    best_option = ""
    best_points = None
    for option in all_options:
        points = 0
        for w in option.split():
            w = w.strip(".,!?;:")
            if w in COMMON_WORDS:
                points += 1
            elif len(w) <= 2:
                points -= 1
            if w in ENGLISH_WORDS:
                points += 1

        if best_points is None or points > best_points:
            best_points = points
            best_option = option
    return best_option
    return best_option
