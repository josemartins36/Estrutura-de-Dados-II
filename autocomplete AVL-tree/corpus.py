from PyPDF2 import PdfReader
import string
import re

class Corpus:
    """
    Carregar pdf e converter em texto
    """

    def __init__(self, file_path):
        self.file_path = file_path
        self.text = self._load_text()

    def _load_text(self):
        """
        Carregar o texto
        """
        print("Carregando...")
        pdf_text = ""
        with open(self.file_path, "rb") as file:
            pdf_reader = PdfReader(file)
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                pdf_text += page.extract_text()
        print("Término")
        return pdf_text

    def _lower_text(self):
        """
        Transforma pra minuscula
        """
        self.text = self.text.lower()

    def _remove_punctuation(self):
        """
        Remove pontuação
        """
        translator = str.maketrans("", "", string.punctuation)
        self.text = self.text.translate(translator)

    def _remove_digits(self):
        """
        Remove dígitos
        """
        translator = str.maketrans("", "", string.digits)
        self.text = self.text.translate(translator)

    def _remove_roman_numerals(self):
        """
        Remove números romanos
        """
        self.text = re.sub(r"\b[IVXLCDM]+\b", "", self.text)

    def process_text(self, lower_text: bool = True, remove_punctuation: bool = True, remove_digits: bool = True, remove_roman_numerals: bool = True,) -> None:
        if remove_roman_numerals:
            self._remove_roman_numerals()
        if lower_text:
            self._lower_text()
        if remove_punctuation:
            self._remove_punctuation()
        if remove_digits:
            self._remove_digits()

    def get_text(self):
        return self.text

    def get_words(self):
        return self.text.split()