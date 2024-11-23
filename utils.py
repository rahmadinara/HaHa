def validasi_input(input_value, expected_type, error_message="Input salah"):
    try:
        return expected_type(input_value)
    except ValueError:
        print(error_message)
        return None