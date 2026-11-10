import math


def english_score(text):
    """
    מקבלת צופן (קיסר או טרנספוזיציה) ומחזירה ציון בין 0 ל-100 לאנגלית של הפענוח הנכון.
    המפתח לא ידוע, ולכן מנסים את כל האפשרויות ושומרים אותן ברשימה all_options.
    שלב 1: מוצאים את הפענוח הנכון לפי רשימת המילים הקצרות (COMMON_WORDS).
    שלב 2: נותנים לו ציון לפי רשימת המילים השכיחות: כל מילה ברשימה מוסיפה 10 נקודות, עד 100.
    """
    # רשימת המילים הנפוצות הקצרות (אות אחת או שתיים) - למציאת הפענוח הנכון
    COMMON_WORDS = {
        "A", "I", "AM", "AN", "AS", "AT", "BE", "BY", "DO", "HE", "IF", "IN", "IS",
        "IT", "ME", "MY", "NO", "OF", "ON", "OR", "SO", "TO", "UP", "US", "WE",
    }

    # רשימת מילים שכיחות באנגלית - לחישוב הציון של הפענוח שנמצא
    ENGLISH_WORDS = {
        "THE", "BE", "TO", "OF", "AND", "A", "IN", "THAT", "HAVE", "I", "IT", "FOR",
        "NOT", "ON", "WITH", "HE", "AS", "YOU", "DO", "AT", "THIS", "BUT", "HIS",
        "BY", "FROM", "THEY", "WE", "SAY", "HER", "SHE", "OR", "AN", "WILL", "MY",
        "ONE", "ALL", "WOULD", "THERE", "THEIR", "WHAT", "SO", "UP", "OUT", "IF",
        "ABOUT", "WHO", "GET", "WHICH", "GO", "ME", "WHEN", "MAKE", "CAN", "LIKE",
        "TIME", "NO", "JUST", "HIM", "KNOW", "TAKE", "PEOPLE", "INTO", "YEAR",
        "YOUR", "GOOD", "SOME", "COULD", "THEM", "SEE", "OTHER", "THAN", "THEN",
        "NOW", "LOOK", "ONLY", "COME", "ITS", "OVER", "THINK", "ALSO", "BACK",
        "AFTER", "USE", "TWO", "HOW", "OUR", "WORK", "FIRST", "WELL", "WAY", "EVEN",
        "NEW", "WANT", "BECAUSE", "ANY", "THESE", "GIVE", "DAY", "MOST", "US",
        "IS", "WAS", "ARE", "WERE", "HAS", "HAD", "BEEN", "DOES", "DID", "MORE",
        "VERY", "MANY", "MUCH", "SUCH", "EACH", "EVERY", "BEFORE", "UNDER", "BETWEEN",
        "THROUGH", "DURING", "WITHOUT", "AGAIN", "AGAINST", "ALWAYS", "NEVER",
        "OFTEN", "EARLY", "LATE", "OLD", "YOUNG", "LARGE", "SMALL", "LONG", "SHORT",
        "HIGH", "LOW", "GREAT", "LITTLE", "OWN", "SAME", "DIFFERENT", "IMPORTANT",
        "MAN", "WOMAN", "CHILD", "WORLD", "LIFE", "HAND", "PLACE", "CASE", "WEEK",
        "COMPANY", "SYSTEM", "PROGRAM", "QUESTION", "GOVERNMENT", "NUMBER", "NIGHT",
        "POINT", "HOME", "WATER", "ROOM", "MOTHER", "AREA", "MONEY", "STORY",
        "FACT", "MONTH", "RIGHT", "STUDY", "BOOK", "EYE", "JOB", "WORD", "BUSINESS",
        "ISSUE", "SIDE", "KIND", "HEAD", "HOUSE", "SERVICE", "FRIEND", "FATHER",
        "POWER", "HOUR", "GAME", "LINE", "END", "MEMBER", "LAW", "CAR", "CITY",
        "COMMUNITY", "NAME", "PRESIDENT", "TEAM", "MINUTE", "IDEA", "KID", "BODY",
        "INFORMATION", "BACK", "PARENT", "FACE", "OTHERS", "LEVEL", "OFFICE", "DOOR",
        "HEALTH", "PERSON", "ART", "WAR", "HISTORY", "PARTY", "WITHIN", "GROW",
        "OPEN", "WALK", "WIN", "OFFER", "REMEMBER", "LOVE", "CONSIDER", "APPEAR",
        "BUY", "WAIT", "SERVE", "DIE", "SEND", "EXPECT", "BUILD", "STAY", "FALL",
        "CUT", "REACH", "KILL", "REMAIN", "SUGGEST", "RAISE", "PASS", "SELL",
        "REQUIRE", "REPORT", "DECIDE", "PULL", "MORNING", "EVENING", "WEATHER",
        "STILL", "WHILE", "WHERE", "WHY", "SHOULD", "MIGHT", "MUST", "SHALL",
        "MAY", "AROUND", "ABOVE", "BELOW", "NEAR", "FAR", "HERE", "TODAY",
        "TOMORROW", "YESTERDAY", "HARD", "EASY", "BIG", "FEW", "LAST", "NEXT",
        "FIND", "TELL", "ASK", "SEEM", "FEEL", "TRY", "LEAVE", "CALL", "KEEP",
        "LET", "BEGIN", "SHOW", "HEAR", "PLAY", "RUN", "MOVE", "LIVE", "BELIEVE",
        "BRING", "HAPPEN", "WRITE", "SIT", "STAND", "LOSE", "PAY", "MEET", "INCLUDE",
        "CONTINUE", "SET", "LEARN", "CHANGE", "LEAD", "UNDERSTAND", "WATCH",
        "FOLLOW", "STOP", "CREATE", "SPEAK", "READ", "SPEND", "ALLOW", "ADD",
        "ARRIVE", "ARRIVED", "OPENED", "WALKED", "CHECKED", "CROSSED",
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

    # --- שלב 1: מציאת הפענוח הנכון לפי המילים הקצרות (COMMON_WORDS) ---
    # מילה קצרה תקינה מוסיפה נקודה, מילה קצרה לא תקינה מורידה נקודה
    best_option = ""
    best_short = None
    for option in all_options:
        short_score = 0
        for w in option.split():
            if w in COMMON_WORDS:
                short_score += 1
            elif len(w) <= 2:
                short_score -= 1

        if best_short is None or short_score > best_short:
            best_short = short_score
            best_option = option

    # --- שלב 2: ציון לפענוח שנמצא לפי המילים השכיחות (ENGLISH_WORDS) ---
    score = 0
    for w in best_option.split():
        if w in ENGLISH_WORDS:
            score += 5

    return min(score, 100)


if __name__ == "__main__":
    caesar = "C UOCNN DQCV ETQUUGF VJG NCMG GCTNA KP VJG OQTPKPI DGHQTG VJG UVQTO CTTKXGF VJG OWUGWO QRGPGF C PGY GZJKDKVKQP CDQWV VJG JKUVQTA"
    transposition = "TRIODAT ER BCARHAER LUM MTOKTIERT ALROOAOREHD Y S  ERLN  DEGN RTLFSND TA REEHOUAO I WHNT WAODRRENFAEDHT SMYG VGIL  EHL S ELE SKHC EIQ A ERTHEAHW BUFNHCYHEDREEB"
    print(english_score(caesar))
    print(english_score(transposition))