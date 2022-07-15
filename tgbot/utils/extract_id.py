





def extract_id(text: str) -> int:
    """
    Extracts the id from a string.
    """
    try:
        return int(text.split()[0][1:])
    except:
        return None