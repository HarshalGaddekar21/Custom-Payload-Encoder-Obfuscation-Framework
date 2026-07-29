import base64


# =========================================
# Base64 Encoding
# =========================================

def encode_base64(payload):

    payload_bytes = payload.encode("utf-8")

    encoded_bytes = base64.b64encode(payload_bytes)

    encoded_payload = encoded_bytes.decode("utf-8")

    return encoded_payload


# =========================================
# Base64 Decoding
# =========================================

def decode_base64(encoded_payload):

    encoded_bytes = encoded_payload.encode("utf-8")

    decoded_bytes = base64.b64decode(encoded_bytes)

    decoded_payload = decoded_bytes.decode("utf-8")

    return decoded_payload


# =========================================
# XOR Transformation
# =========================================

def xor_transform(payload, key):

    if not key:

        raise ValueError("XOR key cannot be empty.")


    transformed_bytes = []

    key_length = len(key)


    for index, character in enumerate(payload):

        payload_value = ord(character)

        key_value = ord(key[index % key_length])

        transformed_value = payload_value ^ key_value

        transformed_bytes.append(transformed_value)


    return transformed_bytes


# =========================================
# XOR Encoding
# =========================================

def encode_xor(payload, key):

    transformed_bytes = xor_transform(payload, key)


    encoded_payload = base64.b64encode(

        bytes(transformed_bytes)

    ).decode("utf-8")


    return encoded_payload


# =========================================
# XOR Decoding
# =========================================

def decode_xor(encoded_payload, key):

    if not key:

        raise ValueError("XOR key cannot be empty.")


    encoded_bytes = base64.b64decode(encoded_payload)

    decoded_characters = []


    key_length = len(key)


    for index, byte_value in enumerate(encoded_bytes):

        key_value = ord(key[index % key_length])

        original_value = byte_value ^ key_value

        decoded_characters.append(chr(original_value))


    return "".join(decoded_characters)


# =========================================
# ROT13 Encoding / Decoding
# =========================================

def transform_rot13(payload):

    transformed_characters = []


    for character in payload:


        if "a" <= character <= "z":

            transformed_character = chr(

                (ord(character) - ord("a") + 13) % 26

                + ord("a")

            )


        elif "A" <= character <= "Z":

            transformed_character = chr(

                (ord(character) - ord("A") + 13) % 26

                + ord("A")

            )


        else:

            transformed_character = character


        transformed_characters.append(transformed_character)


    return "".join(transformed_characters)


# =========================================
# Encoding Test
# =========================================

if __name__ == "__main__":


    test_payload = "TEST_PAYLOAD_DEMO"

    test_key = "SECURITY"


    print("Original Payload:")

    print(test_payload)


    print("\nBase64 Encoded:")

    base64_output = encode_base64(test_payload)

    print(base64_output)


    print("\nBase64 Decoded:")

    print(decode_base64(base64_output))


    print("\nXOR Encoded:")

    xor_output = encode_xor(test_payload, test_key)

    print(xor_output)


    print("\nXOR Decoded:")

    print(decode_xor(xor_output, test_key))


    print("\nROT13 Transformed:")

    rot13_output = transform_rot13(test_payload)

    print(rot13_output)


    print("\nROT13 Reversed:")

    print(transform_rot13(rot13_output))
