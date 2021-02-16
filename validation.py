import re


class Valid:
    """clase que comprueba si el campo titulo es alphanumeric recibiendo como parametro el texto
    en el input titulo y me devuele un TRUE o FALSE"""

    def esAlpha(self, element):
        user_input = element
        result = re.match("^[a-zA-Z][\w]*$", user_input)
        if result:
            return True
        else:
            return False
