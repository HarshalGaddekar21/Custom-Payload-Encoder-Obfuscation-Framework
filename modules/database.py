import sqlite3

from pathlib import Path


# =========================================
# Database Configuration
# =========================================

BASE_DIR = Path(__file__).resolve().parent.parent

DATABASE_DIR = BASE_DIR / "database"

DATABASE_FILE = DATABASE_DIR / "payload_framework.db"


# =========================================
# Ensure Database Directory Exists
# =========================================

DATABASE_DIR.mkdir(exist_ok=True)


# =========================================
# Database Connection
# =========================================

def get_database_connection():

    connection = sqlite3.connect(DATABASE_FILE)

    connection.row_factory = sqlite3.Row

    return connection


# =========================================
# Create Database Tables
# =========================================

def create_tables():

    connection = get_database_connection()

    cursor = connection.cursor()


    # =========================================
    # Users Table
    # =========================================

    cursor.execute("""

        CREATE TABLE IF NOT EXISTS users (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            username TEXT UNIQUE NOT NULL,

            password TEXT NOT NULL,

            role TEXT DEFAULT 'Analyst',

            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

        )

    """)


    # =========================================
    # Encoding History Table
    # =========================================

    cursor.execute("""

        CREATE TABLE IF NOT EXISTS encoding_history (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            original_payload TEXT NOT NULL,

            encoding_method TEXT NOT NULL,

            encoded_output TEXT NOT NULL,

            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

        )

    """)


    # =========================================
    # Obfuscation History Table
    # =========================================

    cursor.execute("""

        CREATE TABLE IF NOT EXISTS obfuscation_history (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            original_payload TEXT NOT NULL,

            obfuscation_method TEXT NOT NULL,

            obfuscated_output TEXT NOT NULL,

            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

        )

    """)


    # =========================================
    # Evasion Results Table
    # =========================================

    cursor.execute("""

        CREATE TABLE IF NOT EXISTS evasion_results (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            original_payload TEXT NOT NULL,

            transformation_method TEXT NOT NULL,

            transformed_payload TEXT NOT NULL,

            original_detection TEXT NOT NULL,

            transformed_detection TEXT NOT NULL,

            evasion_status TEXT NOT NULL,

            risk_score INTEGER DEFAULT 0,

            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

        )

    """)


    connection.commit()

    connection.close()


# =========================================
# Initialize Database
# =========================================

def initialize_database():

    create_tables()


# =========================================
# Save Encoding History
# =========================================

def save_encoding_history(

    original_payload,

    encoding_method,

    encoded_output

):

    connection = get_database_connection()

    cursor = connection.cursor()


    cursor.execute(

        """

        INSERT INTO encoding_history (

            original_payload,

            encoding_method,

            encoded_output

        )

        VALUES (?, ?, ?)

        """,

        (

            original_payload,

            encoding_method,

            encoded_output

        )

    )


    connection.commit()

    connection.close()


# =========================================
# Save Obfuscation History
# =========================================

def save_obfuscation_history(

    original_payload,

    obfuscation_method,

    obfuscated_output

):

    connection = get_database_connection()

    cursor = connection.cursor()


    cursor.execute(

        """

        INSERT INTO obfuscation_history (

            original_payload,

            obfuscation_method,

            obfuscated_output

        )

        VALUES (?, ?, ?)

        """,

        (

            original_payload,

            obfuscation_method,

            obfuscated_output

        )

    )


    connection.commit()

    connection.close()


# =========================================
# Save Evasion Test Result
# =========================================

def save_evasion_result(

    original_payload,

    transformation_method,

    transformed_payload,

    original_detection,

    transformed_detection,

    evasion_status,

    risk_score

):

    connection = get_database_connection()

    cursor = connection.cursor()


    cursor.execute(

        """

        INSERT INTO evasion_results (

            original_payload,

            transformation_method,

            transformed_payload,

            original_detection,

            transformed_detection,

            evasion_status,

            risk_score

        )

        VALUES (?, ?, ?, ?, ?, ?, ?)

        """,

        (

            original_payload,

            transformation_method,

            transformed_payload,

            original_detection,

            transformed_detection,

            evasion_status,

            risk_score

        )

    )


    connection.commit()

    connection.close()


# =========================================
# Get Dashboard Statistics
# =========================================

def get_dashboard_statistics():

    connection = get_database_connection()

    cursor = connection.cursor()


    # Total encoded payloads

    cursor.execute(

        """

        SELECT COUNT(*)

        FROM encoding_history

        """

    )

    encoded_payloads = cursor.fetchone()[0]


    # Total evasion tests

    cursor.execute(

        """

        SELECT COUNT(*)

        FROM evasion_results

        """

    )

    total_tests = cursor.fetchone()[0]


    # Bypassed simulated signatures

    cursor.execute(

        """

        SELECT COUNT(*)

        FROM evasion_results

        WHERE evasion_status =

        'BYPASSED SIMULATED SIGNATURE'

        """

    )

    bypassed = cursor.fetchone()[0]


    # Detected after transformation

    cursor.execute(

        """

        SELECT COUNT(*)

        FROM evasion_results

        WHERE transformed_detection =

        'DETECTED'

        """

    )

    detected = cursor.fetchone()[0]


    connection.close()


    return {

        "total_tests": total_tests,

        "encoded_payloads": encoded_payloads,

        "detected": detected,

        "bypassed": bypassed

    }


# =========================================
# Retrieve Encoding History
# =========================================

def get_encoding_history():

    connection = get_database_connection()

    cursor = connection.cursor()


    cursor.execute(

        """

        SELECT *

        FROM encoding_history

        ORDER BY created_at DESC

        """

    )


    records = cursor.fetchall()

    connection.close()


    return records


# =========================================
# Retrieve Obfuscation History
# =========================================

def get_obfuscation_history():

    connection = get_database_connection()

    cursor = connection.cursor()


    cursor.execute(

        """

        SELECT *

        FROM obfuscation_history

        ORDER BY created_at DESC

        """

    )


    records = cursor.fetchall()

    connection.close()


    return records


# =========================================
# Retrieve Evasion History
# =========================================

def get_evasion_history():

    connection = get_database_connection()

    cursor = connection.cursor()


    cursor.execute(

        """

        SELECT *

        FROM evasion_results

        ORDER BY created_at DESC

        """

    )


    records = cursor.fetchall()

    connection.close()


    return records


# =========================================
# Get Advanced Dashboard Analytics
# =========================================

def get_advanced_dashboard_analytics():

    connection = get_database_connection()

    cursor = connection.cursor()


    # =========================================
    # Total Evasion Tests
    # =========================================

    cursor.execute(

        """

        SELECT COUNT(*)

        FROM evasion_results

        """

    )

    total_tests = cursor.fetchone()[0]


    # =========================================
    # Bypassed Tests
    # =========================================

    cursor.execute(

        """

        SELECT COUNT(*)

        FROM evasion_results

        WHERE evasion_status =

        'BYPASSED SIMULATED SIGNATURE'

        """

    )

    bypassed = cursor.fetchone()[0]


    # =========================================
    # Evasion Rate
    # =========================================

    if total_tests > 0:

        evasion_rate = round(

            (bypassed / total_tests) * 100,

            2

        )

    else:

        evasion_rate = 0


    # =========================================
    # Average Risk Score
    # =========================================

    cursor.execute(

        """

        SELECT AVG(risk_score)

        FROM evasion_results

        WHERE risk_score > 0

        """

    )

    average_score = cursor.fetchone()[0]


    if average_score is None:

        average_score = 0

    else:

        average_score = round(

            average_score,

            2

        )


    # =========================================
    # Most Used Transformation Method
    # =========================================

    cursor.execute(

        """

        SELECT

            transformation_method,

            COUNT(*) AS usage_count

        FROM evasion_results

        GROUP BY transformation_method

        ORDER BY usage_count DESC

        LIMIT 1

        """

    )


    most_used = cursor.fetchone()


    if most_used:

        most_used_method = most_used[0]

    else:

        most_used_method = "N/A"


    connection.close()


    return {

        "evasion_rate": evasion_rate,

        "average_score": average_score,

        "most_used_method": most_used_method

    }


# =========================================
# Get Transformation Analytics
# =========================================

def get_transformation_analytics():

    connection = get_database_connection()

    cursor = connection.cursor()


    cursor.execute(

        """

        SELECT

            transformation_method,


            SUM(

                CASE

                    WHEN transformed_detection =

                    'DETECTED'

                    THEN 1

                    ELSE 0

                END

            ) AS detected_count,


            SUM(

                CASE

                    WHEN transformed_detection =

                    'NOT DETECTED'

                    THEN 1

                    ELSE 0

                END

            ) AS bypassed_count


        FROM evasion_results

        GROUP BY transformation_method

        ORDER BY transformation_method

        """

    )


    results = cursor.fetchall()

    connection.close()


    analytics = []


    for row in results:

        analytics.append({

            "method": row[0],

            "detected": row[1],

            "bypassed": row[2]

        })


    return analytics


# =========================================
# Module Test
# =========================================

if __name__ == "__main__":

    initialize_database()

    print(

        "Database initialized successfully."

    )
