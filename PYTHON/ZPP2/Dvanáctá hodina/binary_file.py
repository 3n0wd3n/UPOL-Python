# Modul pro čtení a zápis seznamu bajtů do souboru.
# Seznam bajtů (byte list) je seznam celých čísel v rozsahu 0 až 255.

def write_byte_list(file, byte_list):
    """Zapíše seznam bajtů do souboru."""
    file.write(bytes(byte_list))

def read_byte_list(file, size = -1):
    """Přečte ze souboru seznam bajtů o velikosti size."""
    return list(file.read(size))

