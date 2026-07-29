from modules.encoder import (
    encode_base64,
    encode_xor,
    transform_rot13
)

from modules.obfuscator import (
    reverse_payload,
    convert_to_escape_sequence
)

from modules.detector import detect_signatures


# =========================================
# Analyze Single Transformation
# =========================================

def analyze_transformation(

    original_payload,

    transformed_payload,

    method_name

):

    original_detection = detect_signatures(

        original_payload

    )


    transformed_detection = detect_signatures(

        transformed_payload

    )


    original_detected = original_detection["detected"]

    transformed_detected = transformed_detection["detected"]


    if original_detected and not transformed_detected:

        result = "BYPASSED"

    elif original_detected and transformed_detected:

        result = "DETECTED"

    else:

        result = "NOT DETECTED"


    return {

        "method": method_name,

        "original_payload": original_payload,

        "transformed_payload": transformed_payload,

        "original_detection": (

            "DETECTED"

            if original_detected

            else "NOT DETECTED"

        ),

        "transformed_detection": (

            "DETECTED"

            if transformed_detected

            else "NOT DETECTED"

        ),

        "result": result

    }


# =========================================
# Run Complete Comparison
# =========================================

def run_comparison(original_payload, xor_key="SECURITY"):


    transformations = []


    # Base64

    base64_output = encode_base64(

        original_payload

    )


    transformations.append(

        analyze_transformation(

            original_payload,

            base64_output,

            "Base64"

        )

    )


    # XOR

    xor_output = encode_xor(

        original_payload,

        xor_key

    )


    transformations.append(

        analyze_transformation(

            original_payload,

            xor_output,

            "XOR"

        )

    )


    # ROT13

    rot13_output = transform_rot13(

        original_payload

    )


    transformations.append(

        analyze_transformation(

            original_payload,

            rot13_output,

            "ROT13"

        )

    )


    # Reverse

    reversed_output = reverse_payload(

        original_payload

    )


    transformations.append(

        analyze_transformation(

            original_payload,

            reversed_output,

            "Reverse"

        )

    )


    # Escape Sequence

    escape_output = convert_to_escape_sequence(

        original_payload

    )


    transformations.append(

        analyze_transformation(

            original_payload,

            escape_output,

            "Escape Sequence"

        )

    )


    return transformations


# =========================================
# Calculate Evasion Statistics
# =========================================

def calculate_statistics(results):

    total_tests = len(results)


    bypassed_tests = 0

    detected_tests = 0


    for result in results:


        if result["result"] == "BYPASSED":

            bypassed_tests += 1


        elif result["result"] == "DETECTED":

            detected_tests += 1


    if total_tests > 0:

        evasion_rate = (

            bypassed_tests / total_tests

        ) * 100

    else:

        evasion_rate = 0


    return {

        "total_tests": total_tests,

        "bypassed": bypassed_tests,

        "detected": detected_tests,

        "evasion_rate": round(

            evasion_rate,

            2

        )

    }


# =========================================
# Comparison Engine Test
# =========================================

if __name__ == "__main__":


    test_payload = "TEST_PAYLOAD_DEMO"


    results = run_comparison(

        test_payload

    )


    print("=" * 60)

    print("PAYLOAD TRANSFORMATION COMPARISON")

    print("=" * 60)


    for result in results:


        print("\nMethod:")

        print(result["method"])


        print("Original Detection:")

        print(result["original_detection"])


        print("Transformed Detection:")

        print(result["transformed_detection"])


        print("Result:")

        print(result["result"])


    statistics = calculate_statistics(

        results

    )


    print("\n")

    print("=" * 60)

    print("EVASION ANALYSIS")

    print("=" * 60)


    print(

        f"Total Tests: "

        f"{statistics['total_tests']}"

    )


    print(

        f"Bypassed: "

        f"{statistics['bypassed']}"

    )


    print(

        f"Detected: "

        f"{statistics['detected']}"

    )


    print(

        f"Evasion Rate: "

        f"{statistics['evasion_rate']}%"

    )
