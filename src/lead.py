class Lead:
    def __init__(self, nome, email, telefone, cpf):
        self.nome = self._normalize_nome(nome)
        self.email = self._normalize_email(email)
        self.telefone = self._normalize_telefone(telefone)
        self.cpf = self._normalize_cpf(cpf)

    def _normalize_nome(self, nome):
        return nome.strip().lower()

    def _normalize_email(self, email):
        return email.strip().lower()

    def _normalize_telefone(self, telefone):
        return ''.join(filter(str.isdigit, telefone))

    def _normalize_cpf(self, cpf):
        return ''.join(filter(str.isdigit, cpf))

    def get_comparison_keys(self):
        return (self.email, self.telefone, self.cpf)

    def __eq__(self, other):
        if not isinstance(other, Lead):
            return False
        return self.get_comparison_keys() == other.get_comparison_keys()

    def __hash__(self):
        return hash(self.get_comparison_keys())

    def to_dict(self):
        return {
            "nome": self.nome,
            "email": self.email,
            "telefone": self.telefone,
            "cpf": self.cpf
        }


    def __repr__(self):
        return f"Lead(email={self.email}, telefone={self.telefone}, cpf={self.cpf})"