import re

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        e_address = set()

        for email in emails:
            name, domain = email.split("@")
            name = name.split("+")[0].replace(".","")
            e_address.add((name, domain))
                
        return len(e_address)
        