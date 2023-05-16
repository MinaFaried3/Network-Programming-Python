from dns.resolver import *


def lookup(domain: str):
    for query_type in 'A', 'AAAA', 'CNAME', 'MX', 'NS', 'TXT':
        answer = query(domain, query_type, raise_on_no_answer=False)
        if answer.rrset is not None:
            print(answer.rrset)
        else:
            print('no record type', query_type, ' for ', domain)


lookup('google.com')
