import unittest
from src.deduplication import is_duplicate_memo, LeadIndex
from src.lead import Lead


class TestDeduplication(unittest.TestCase):

    def setUp(self):
        self.leads = [
            Lead("João", "a@gmail.com", "11999999999", "11111111111"),
            Lead("Maria", "b@gmail.com", "11888888888", "22222222222"),
            Lead("Pedro", "c@gmail.com", "11777777777", "33333333333"),
        ]

    def test_duplicate_email(self):
        new_lead = Lead("Outro", "a@gmail.com", "000", "999")
        result = is_duplicate_memo(new_lead.to_dict(), [l.to_dict() for l in self.leads])
        self.assertTrue(result)

    def test_no_duplicate(self):
        new_lead = Lead("Novo", "novo@gmail.com", "11122233344", "99999999999")
        result = is_duplicate_memo(new_lead.to_dict(), [l.to_dict() for l in self.leads])
        self.assertFalse(result)

    def test_index_duplicate(self):
        index = LeadIndex()
        for l in self.leads:
            index.add(l)

        new_lead = Lead("Outro", "a@gmail.com", "000", "999")
        self.assertTrue(index.is_duplicate(new_lead))

    def test_index_no_duplicate(self):
        index = LeadIndex()
        for l in self.leads:
            index.add(l)

        new_lead = Lead("Novo", "novo@gmail.com", "11122233344", "99999999999")
        self.assertFalse(index.is_duplicate(new_lead))


if __name__ == "__main__":
    unittest.main()