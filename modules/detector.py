# =========================================
# Simulated Signature Detection Engine
# =========================================


# Controlled educational test signatures

SIGNATURE_DATABASE = [

    "TEST_PAYLOAD",

    "MALWARE_SIMULATION",

    "SUSPICIOUS_COMMAND",

    "DEMO_THREAT_PATTERN"

]


# =========================================
# Signature Detection
# =========================================

def detect_signatures(payload):

    if not payload:

        return {

            "detected": False,

            "matched_signatures": [],

            "reason": "Empty input."

        }


    matched_signatures = []


    for signature in SIGNATURE_DATABASE:

        if signature.lower() in payload.lower():

            matched_signatures.append(signature)


    if matched_signatures:

        return {

            "detected": True,

            "matched_signatures": matched_signatures,

            "reason": "Known test signature matched."

        }


    return {

        "detected": False,

        "matched_signatures": [],

        "reason": "No known test signature matched."

    }


# =========================================
# Compare Original and Transformed Payload
# =========================================

def compare_detection(original_payload, transformed_payload):

    original_result = detect_signatures(original_payload)

    transformed_result = detect_signatures(transformed_payload)


    if original_result["detected"]:

        original_status = "DETECTED"

    else:

        original_status = "NOT DETECTED"


    if transformed_result["detected"]:

        transformed_status = "DETECTED"

    else:

        transformed_status = "NOT DETECTED"


    if (

        original_result["detected"]

        and not transformed_result["detected"]

    ):

        evasion_status = "BYPASSED SIMULATED SIGNATURE"


    elif (

        original_result["detected"]

        and transformed_result["detected"]

    ):

        evasion_status = "DETECTED AFTER TRANSFORMATION"


    else:

        evasion_status = "ORIGINAL NOT DETECTED"


    return {

        "original_status": original_status,

        "transformed_status": transformed_status,

        "original_matches": original_result["matched_signatures"],

        "transformed_matches": transformed_result["matched_signatures"],

        "evasion_status": evasion_status

    }


# =========================================
# Detection Engine Test
# =========================================

if __name__ == "__main__":


    original_payload = "TEST_PAYLOAD_DEMO"


    transformed_payload = "GRFG_CNLYBNQ_QRZB"


    result = compare_detection(

        original_payload,

        transformed_payload

    )


    print("Original Payload:")

    print(original_payload)


    print("\nOriginal Detection:")

    print(result["original_status"])


    print("\nTransformed Payload:")

    print(transformed_payload)


    print("\nTransformed Detection:")

    print(result["transformed_status"])


    print("\nMatched Original Signatures:")

    print(result["original_matches"])


    print("\nMatched Transformed Signatures:")

    print(result["transformed_matches"])


    print("\nFinal Result:")

    print(result["evasion_status"])
