def is_duplicate_memo(new_lead, leads):
    memo = {}

    def dp(index):
        if index >= len(leads):
            return False

        if index in memo:
            return memo[index]

        current = leads[index]

        if (
            new_lead["email"] == current["email"] or
            new_lead["telefone"] == current["telefone"] or
            new_lead["cpf"] == current["cpf"]
        ):
            memo[index] = True
            return True

        result = dp(index + 1)
        memo[index] = result
        return result

    return dp(0)

class LeadIndex:
    def __init__(self):
        self.emails = set()
        self.telefones = set()
        self.cpfs = set()

    def _extract(self, lead):
        if isinstance(lead, dict):
            return lead["email"], lead["telefone"], lead["cpf"]
        else:
            return lead.email, lead.telefone, lead.cpf

    def add(self, lead):
        email, telefone, cpf = self._extract(lead)
        self.emails.add(email)
        self.telefones.add(telefone)
        self.cpfs.add(cpf)

    def is_duplicate(self, lead):
        email, telefone, cpf = self._extract(lead)

        return (
            email in self.emails or
            telefone in self.telefones or
            cpf in self.cpfs
        )