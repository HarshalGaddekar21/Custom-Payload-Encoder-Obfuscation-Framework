import re
import math
from collections import Counter


# =========================================
# Calculate Shannon Entropy
# =========================================

def calculate_entropy(value):

    if not value:

        return 0.0


    length = len(value)

    frequencies = Counter(value)


    entropy = 0.0


    for count in frequencies.values():

        probability = count / length

        entropy -= (

            probability

            * math.log2(probability)

        )


    return round(entropy, 3)


# =========================================
# Detect Base64-Like Representation
# =========================================

def detect_base64_pattern(value):

    pattern = (

        r"^[A-Za-z0-9+/]+={0,2}$"

    )


    return bool(

        re.fullmatch(

            pattern,

            value

        )

    )


# =========================================
# Detect Escape Sequences
# =========================================

def detect_escape_sequences(value):

    return bool(

        re.search(

            r"\\x[0-9a-fA-F]{2}",

            value

        )

    )


# =========================================
# Detect Concatenation Patterns
# =========================================

def detect_concatenation(value):

    return (

        '"' in value

        and "+" in value

    )


# =========================================
# Analyze Transformation Indicators
# =========================================

def analyze_transformation(value):

    indicators = []

    score = 0


    # =========================================
    # Base64 Detection
    # =========================================

    if detect_base64_pattern(value):

        indicators.append(

            "Base64-like encoded representation"

        )

        score += 30


    # =========================================
    # Escape Sequence Detection
    # =========================================

    if detect_escape_sequences(value):

        indicators.append(

            "Escape-sequence representation"

        )

        score += 30


    # =========================================
    # String Concatenation Detection
    # =========================================

    if detect_concatenation(value):

        indicators.append(

            "String concatenation pattern"

        )

        score += 25


    # =========================================
    # Entropy Analysis
    # =========================================

    entropy = calculate_entropy(value)


    if entropy >= 4.5:

        indicators.append(

            "High character entropy"

        )

        score += 30


    elif entropy >= 3.5:

        score += 15


    # =========================================
    # No Transformation Indicators
    # =========================================

    if not indicators:

        indicators.append(

            "No obvious transformation indicators"

        )


    # =========================================
    # Limit Score to 100
    # =========================================

    score = min(score, 100)


    # =========================================
    # Risk Classification
    # =========================================

    if score >= 60:

        risk_level = "HIGH"


    elif score >= 30:

        risk_level = "MEDIUM"


    else:

        risk_level = "LOW"


    return {

        "entropy": entropy,

        "indicators": indicators,

        "risk_score": score,

        "risk_level": risk_level

    }






# =========================================
# Module Test
# =========================================

if __name__ == "__main__":


    test_values = [

        "TEST_PAYLOAD_DEMO",

        "VEVTVF9QQVlMT0FEX0RFTU8=",

        r"\x54\x45\x53\x54",

        '"TES" + "T_PAYLOAD"'

    ]


    for value in test_values:


        result = analyze_transformation(

            value

        )


        print(

            "\nValue:",

            value

        )


        print(

            "Entropy:",

            result["entropy"]

        )


        print(

            "Indicators:",

            result["indicators"]

        )


        print(

            "Risk Level:",

            result["risk_level"]

        )

        print(

            "Risk Score:",

            result["risk_score"],

            "/100"

        )






