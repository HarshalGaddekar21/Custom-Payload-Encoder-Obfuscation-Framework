from flask import Flask, render_template, request

from modules.detector import detect_signatures

from modules.encoder import (
    encode_base64,
    encode_xor,
    transform_rot13
)

from modules.obfuscator import (
    insert_random_characters,
    create_concatenated_representation,
    reverse_payload,
    convert_to_escape_sequence
)

from modules.database import (
    initialize_database,
    save_encoding_history,
    save_obfuscation_history,
    save_evasion_result,
    get_dashboard_statistics,
    get_encoding_history,
    get_obfuscation_history,
    get_evasion_history,
    get_advanced_dashboard_analytics,
    get_transformation_analytics
)

from modules.comparison import (
    run_comparison,
    calculate_statistics
)

from modules.defensive_analyzer import (
    analyze_transformation
)


# ============================================================
# Flask Application Configuration
# ============================================================

app = Flask(__name__)

app.config["SECRET_KEY"] = "payloadshield-lab-development-key"


# ============================================================
# Database Initialization
# ============================================================

initialize_database()


# ============================================================
# Dashboard
# ============================================================

@app.route("/")
def home():

    statistics = get_dashboard_statistics()

    analytics = get_advanced_dashboard_analytics()

    transformation_analytics = get_transformation_analytics()

    return render_template(
        "dashboard.html",
        statistics=statistics,
        analytics=analytics,
        transformation_analytics=transformation_analytics
    )


# ============================================================
# Encoding Lab
# ============================================================

@app.route(
    "/encoder",
    methods=["GET", "POST"]
)
def encoder():

    result = None
    error = None

    if request.method == "POST":

        payload = request.form.get(
            "payload",
            ""
        ).strip()

        method = request.form.get(
            "method",
            ""
        ).strip()

        xor_key = request.form.get(
            "xor_key",
            ""
        ).strip()

        try:

            if not payload:

                raise ValueError(
                    "Payload cannot be empty."
                )

            if method == "base64":

                result = encode_base64(
                    payload
                )

                method_name = "Base64"

            elif method == "xor":

                if not xor_key:

                    raise ValueError(
                        "XOR key is required."
                    )

                result = encode_xor(
                    payload,
                    xor_key
                )

                method_name = "XOR"

            elif method == "rot13":

                result = transform_rot13(
                    payload
                )

                method_name = "ROT13"

            else:

                raise ValueError(
                    "Please select an encoding method."
                )

            save_encoding_history(
                payload,
                method_name,
                result
            )

        except Exception as exception:

            error = str(exception)

    return render_template(
        "encoder.html",
        result=result,
        error=error
    )


# ============================================================
# Obfuscation Lab
# ============================================================

@app.route(
    "/obfuscator",
    methods=["GET", "POST"]
)
def obfuscator():

    result = None
    error = None

    if request.method == "POST":

        payload = request.form.get(
            "payload",
            ""
        ).strip()

        method = request.form.get(
            "method",
            ""
        ).strip()

        try:

            if not payload:

                raise ValueError(
                    "Payload cannot be empty."
                )

            if method == "random":

                result = insert_random_characters(
                    payload
                )

                method_name = (
                    "Random Character Insertion"
                )

            elif method == "split":

                result = create_concatenated_representation(
                    payload
                )

                method_name = (
                    "Character Splitting"
                )

            elif method == "reverse":

                result = reverse_payload(
                    payload
                )

                method_name = (
                    "Reversible Transformation"
                )

            elif method == "escape":

                result = convert_to_escape_sequence(
                    payload
                )

                method_name = (
                    "Escape Sequence"
                )

            else:

                raise ValueError(
                    "Please select an obfuscation method."
                )

            save_obfuscation_history(
                payload,
                method_name,
                result
            )

        except Exception as exception:

            error = str(exception)

    return render_template(
        "obfuscator.html",
        result=result,
        error=error
    )


# ============================================================
# Evasion Testing
# ============================================================

@app.route(
    "/evasion",
    methods=["GET", "POST"]
)
def evasion():

    result = None
    error = None

    if request.method == "POST":

        original_payload = request.form.get(
            "original_payload",
            ""
        ).strip()

        transformed_payload = request.form.get(
            "transformed_payload",
            ""
        ).strip()

        transformation_method = request.form.get(
            "transformation_method",
            ""
        ).strip()

        try:

            if not original_payload:

                raise ValueError(
                    "Original payload cannot be empty."
                )

            if not transformed_payload:

                raise ValueError(
                    "Transformed payload cannot be empty."
                )

            if not transformation_method:

                raise ValueError(
                    "Please select a transformation method."
                )

            original_detection = detect_signatures(
                original_payload
            )

            transformed_detection = detect_signatures(
                transformed_payload
            )

            original_status = (

                "DETECTED"

                if original_detection["detected"]

                else "NOT DETECTED"

            )

            transformed_status = (

                "DETECTED"

                if transformed_detection["detected"]

                else "NOT DETECTED"

            )

            if (

                original_detection["detected"]

                and not transformed_detection["detected"]

            ):

                evasion_status = (

                    "BYPASSED SIMULATED SIGNATURE"

                )

            elif (

                original_detection["detected"]

                and transformed_detection["detected"]

            ):

                evasion_status = (

                    "DETECTED AFTER TRANSFORMATION"

                )

            else:

                evasion_status = (

                    "ORIGINAL NOT DETECTED"

                )

            defensive_analysis = analyze_transformation(
                transformed_payload
            )

            result = {

                "original_status": original_status,

                "transformed_status": transformed_status,

                "original_matches": (
                    original_detection[
                        "matched_signatures"
                    ]
                ),

                "transformed_matches": (
                    transformed_detection[
                        "matched_signatures"
                    ]
                ),

                "evasion_status": evasion_status,

                "defensive_analysis": (
                    defensive_analysis
                )

            }

            save_evasion_result(

                original_payload,

                transformation_method,

                transformed_payload,

                original_status,

                transformed_status,

                evasion_status,

                defensive_analysis[
                    "risk_score"
                ]

            )

        except Exception as exception:

            error = str(exception)

    return render_template(
        "evasion.html",
        result=result,
        error=error
    )


# ============================================================
# Transformation Comparison
# ============================================================

@app.route(
    "/comparison",
    methods=["GET", "POST"]
)
def comparison():

    results = None

    statistics = None

    error = None

    if request.method == "POST":

        payload = request.form.get(
            "payload",
            ""
        ).strip()

        xor_key = request.form.get(
            "xor_key",
            "SECURITY"
        ).strip()

        try:

            if not payload:

                raise ValueError(
                    "Test string cannot be empty."
                )

            if not xor_key:

                raise ValueError(
                    "XOR key cannot be empty."
                )

            results = run_comparison(
                payload,
                xor_key
            )

            statistics = calculate_statistics(
                results
            )

        except Exception as exception:

            error = str(exception)

    return render_template(
        "comparison.html",
        results=results,
        statistics=statistics,
        error=error
    )


# ============================================================
# About Project
# ============================================================

@app.route("/about")
def about():

    return render_template(
        "about.html"
    )


# ============================================================
# Reports and Historical Analysis
# ============================================================

@app.route("/reports")
def reports():

    encoding_history = (
        get_encoding_history()
    )

    obfuscation_history = (
        get_obfuscation_history()
    )

    evasion_history = (
        get_evasion_history()
    )

    return render_template(

        "reports.html",

        encoding_history=encoding_history,

        obfuscation_history=obfuscation_history,

        evasion_history=evasion_history

    )


# ============================================================
# Application Entry Point
# ============================================================

if __name__ == "__main__":

    app.run(
        debug=True
    )


