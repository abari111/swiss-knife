import re

def email_parser(file_path:str, output_file:str='email_addr.txt')->None:
    pattern = re.compile(r'\w*@gmail\.com')
    o_file = open(output_file, 'w')
    
    with open(file_path, 'r') as file:
        lines = file.readlines()
        
    for line in lines:
        matches = pattern.finditer(line)
        for match in matches:  
            email_addr = line[match.span()[0]:match.span()[1]]
            print(email_addr)
            o_file.writelines(email_addr + '\n')
    o_file.close()