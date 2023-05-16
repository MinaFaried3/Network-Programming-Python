from dns.resolver import *


def convert_to_ip(domain: str):
    # convert to ip4 ip6
    for query_type in 'A', 'AAAA':
        answer = query(domain, query_type, raise_on_no_answer=False)
        if answer.rrset is not None:
            for record in answer.rrset:
                print(record.address)
        else:
            print('no record type', query_type, ' for ', domain)
    # can have cname
    answer = query(domain, 'CNAME', raise_on_no_answer=False)
    if answer.rrset is not None:
        for record in answer:
            convert_to_ip(record.address)


def resolve_email_domain(domain: str):
    answer = query(domain, 'MX', raise_on_no_answer=False)
    if answer.rrset is not None:
        records = sorted(answer.rrset)
        for record in records:
            print(record)
            name = record.exchange.to_text(omit_final_dot=True)
            print(name)
            convert_to_ip(name)
    else:
        print("no email domain for this")
        convert_to_ip(domain)


# resolve_email_domain('bard.google.com')
resolve_email_domain('google.com')
