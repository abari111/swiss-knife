import re
from typing import List

def email_parser(file_path:str, output_file:str='email_addr.txt', domain_label:str=None, tld:str=None )->List[str]:
    
    pattern = re.compile(r'\w+@\w+\.\w+')
    o_file = open(output_file, 'w')
    emails_addr = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
        
    for line in lines:
        matches = pattern.finditer(line)
        for match in matches:  
            email_addr = line[match.span()[0]:match.span()[1]]
            if not (tld and check_email_tld(email_addr, tld)):
                continue
            
            emails_addr.append(email_addr)
            o_file.writelines(email_addr + '\n')
            
    o_file.close()
    
    return emails_addr


def check_email_tld(email, tld):
    pattern = r'^(?P<username>[a-zA-Z0-9._%+-]+)@(?P<domain>[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})$'

    match = re.match(pattern, email)
    if match:
        username = match.group('username')
        domain = match.group('domain')
        # Split domain into subdomain and top-level domain (TLD)
        domain_parts = domain.rsplit('.', 2)
        subdomain = domain_parts[0]
        ext_tld = '.'.join(domain_parts[1:])
    
    if ext_tld.lower() == tld.lower():
        return True
    return False


if __name__ == '__main__':
    addrs = email_parser('assets/text_emails.txt', tld='com')
    print(addrs)