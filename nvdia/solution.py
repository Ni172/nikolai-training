def get_actual_text_from_logs(log_file):
    with open(log_file, 'r') as file:
        log_file = file.readlines()
    ip_list = []
    for line in log_file:
        message = line.split(' ')
        if '192.168.1.255' in message:
            for i in range(len(message)):
                if message[i] == 'inet':
                    ip_list.append(message[i+1])
    return ip_list

print(get_actual_text_from_logs('temp'))