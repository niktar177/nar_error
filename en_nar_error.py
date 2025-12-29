# 0.01
ERROR_MESSAGES = {
    1: "Error 1: Invalid syntax",
    2: "Error 2: Invalid digit for the given numeral system",
    3: "Error 3: Division by zero",
    4: "Error 4: Negative subtraction result",
    5: "Error 5: Unknown operation",
    6: "Error 6: Invalid proportion (must be 0-100)",
    7: "Error 7: Invalid format",
    8: "Error 8: Invalid color component value (must be 0-255)"
    9: "Error 9: Invalid file extension (must be .txt)"
    10: "Error 10: File access error (file not found or no permissions)"
    11: "Error 11: File write error (no write permission or file is busy)"
    12: "Error 12: Invalid argument type"
    13: "Error 13: Index out of range"
    14: "Error 14: Invalid range (start position greater than end position)"
    }

def nar_error(code):
    if code in ERROR_MESSAGES:
        raise ValueError(ERROR_MESSAGES[code])
    else:
        raise ValueError(f"Unknown error code: {code}")
