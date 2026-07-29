import random


# =========================================
# Random Character Insertion
# =========================================

def insert_random_characters(payload, count=2):

    if not payload:

        raise ValueError("Payload cannot be empty.")


    random_characters = "abcdefghijklmnopqrstuvwxyz"

    result = []


    for character in payload:

        result.append(character)


        for _ in range(count):

            random_character = random.choice(random_characters)

            result.append(random_character)


    return "".join(result)


# =========================================
# Character Splitting
# =========================================

def split_into_chunks(payload, chunk_size=3):

    if not payload:

        raise ValueError("Payload cannot be empty.")


    chunks = []


    for index in range(0, len(payload), chunk_size):

        chunk = payload[index:index + chunk_size]

        chunks.append(chunk)


    return chunks


# =========================================
# Character Splitting and Concatenation
# =========================================

def create_concatenated_representation(payload, chunk_size=3):

    chunks = split_into_chunks(payload, chunk_size)


    formatted_chunks = []


    for chunk in chunks:

        formatted_chunks.append(f'"{chunk}"')


    return " + ".join(formatted_chunks)


# =========================================
# Reversible Transformation
# =========================================

def reverse_payload(payload):

    if not payload:

        raise ValueError("Payload cannot be empty.")


    return payload[::-1]


# =========================================
# Escape-Sequence Representation
# =========================================

def convert_to_escape_sequence(payload):

    if not payload:

        raise ValueError("Payload cannot be empty.")


    escape_sequence = []


    for character in payload:

        escape_sequence.append(

            f"\\x{ord(character):02x}"

        )


    return "".join(escape_sequence)


# =========================================
# Obfuscation Test
# =========================================

if __name__ == "__main__":


    test_payload = "TEST_PAYLOAD_DEMO"


    print("Original Payload:")

    print(test_payload)


    print("\nRandom Character Insertion:")

    print(insert_random_characters(test_payload))


    print("\nCharacter Splitting and Concatenation:")

    print(create_concatenated_representation(test_payload))


    print("\nReversible Transformation:")

    reversed_payload = reverse_payload(test_payload)

    print(reversed_payload)


    print("\nReversed Back:")

    print(reverse_payload(reversed_payload))


    print("\nEscape-Sequence Representation:")

    print(convert_to_escape_sequence(test_payload))
