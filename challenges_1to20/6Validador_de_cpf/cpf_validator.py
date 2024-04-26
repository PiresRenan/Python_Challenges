class CPFValidator:
    def __init__(self, cpf):
        self.cpf = self._sanitize_cpf(cpf)

    def _sanitize_cpf(self, cpf):
        return ''.join(filter(str.isdigit, cpf))

    def _is_valid_cpf(self):
        if len(self.cpf) != 11:
            return False

        # Verificar se todos os dígitos são iguais
        if len(set(self.cpf)) == 1:
            return False

        # Calcular o primeiro dígito verificador
        total = sum(int(self.cpf[i]) * (10 - i) for i in range(9))
        digit_1 = (total * 10) % 11
        if digit_1 == 10:
            digit_1 = 0

        # Calcular o segundo dígito verificador
        total = sum(int(self.cpf[i]) * (11 - i) for i in range(10))
        digit_2 = (total * 10) % 11
        if digit_2 == 10:
            digit_2 = 0

        # Verificar se os dígitos verificadores estão corretos
        if int(self.cpf[9]) == digit_1 and int(self.cpf[10]) == digit_2:
            return True
        else:
            return False

    def is_valid(self):
        return self._is_valid_cpf()
