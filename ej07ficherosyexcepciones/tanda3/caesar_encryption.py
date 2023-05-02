"""
Clase para manejar la encriptación César.

Autor: Rafael del Castillo Gomariz
"""
import string
from typeguard import typechecked

@typechecked
class CaesarEncryptionError(Exception):

    def __init__(self, message):
        super().__init__(message)


class CaesarEncryption:
    __LETTERS = string.ascii_lowercase + "áéíóúüñ"

    @classmethod
    def encrypt_file(cls, source_filename: str, destination_filename: str, scrolling: int):
        try:
            with open(source_filename) as file:
                source_file_lines = file.readlines()
            with open(destination_filename, "w") as file:
                for line in source_file_lines:
                    file.write(cls.encrypt_str(line, scrolling))

        except (FileNotFoundError, PermissionError, ValueError) as e:
            raise CaesarEncryptionError(f"Excepción al abrir el fichero: {e}")

    @classmethod
    def decrypt_file(cls, source_filename: str, destination_filename: str, scrolling):
        cls.encrypt_file(source_filename, destination_filename, -scrolling)

    @classmethod
    def encrypt_str(cls, str_to_encrypt: str, scrolling: int):
        encrypted_str = ""
        for char in str_to_encrypt:
            if char.lower() in cls.__LETTERS:  # si el carácter es alfabético encriptamos
                letters = cls.__LETTERS if char.islower() else cls.__LETTERS.upper()
                index_in_letters = letters.find(char)
                index_encrypted_char = (index_in_letters + scrolling) % len(letters)
                encrypted_char = letters[index_encrypted_char]
            else:
                encrypted_char = char
            encrypted_str += encrypted_char
        return encrypted_str

    @classmethod
    def decrypt_str(cls, str_to_decrypt: str, scrolling: int):
        return cls.encrypt_str(str_to_decrypt, scrolling)
