import json
def get_actual_frequency_from_logs(log_file):
    actual_frequency = {}
    with open(log_file, 'r') as file:
        log_file = file.readlines()
    # sum all the times that message is in the log for each id
    for line in log_file:
        message = line.split(', ')
        message_id = message[2].split('x')[1]
        if message_id in actual_frequency:
            actual_frequency[message_id] = actual_frequency[message_id] + 1
        else:
            actual_frequency[message_id] = 1
    return actual_frequency

def verify_fps(actual_frequency, json_file, protocol_version):
    fps_table = {36: 164, 18: 84, 9: 48}
    wrong_fps = []
    if protocol_version not in [1, 2]:
        return 'protocol version should be 1 or 2'
    with open(json_file, 'r') as file:
        configuration_file = json.loads(file.read())
    for protocol_id in actual_frequency:
        fps = configuration_file['Protocols'][protocol_id]['fps']
        expected_messages_frequency = fps_table[fps]
        if expected_messages_frequency != actual_frequency[protocol_id]:
            wrong_fps.append(protocol_id)
    return wrong_fps

def find_missing_protocols_in_the_data_file(actual_frequency, json_file, protocol_version):
    wrong_fps = []
    if protocol_version not in [1, 2]:
        return 'protocol version should be 1 or 2'
    with open(json_file, 'r') as file:
        configuration_file = json.loads(file.read())
    for protocol_id in configuration_file['protocols_by_version']['Version' + str(protocol_version)]:
        if protocol_id not in actual_frequency:
            wrong_fps.append(protocol_id)
    return wrong_fps

def find_logs_protocols_that_not_in_the_configuration(actual_frequency, json_file, protocol_version):
    wrong_fps = []
    if protocol_version not in [1, 2]:
        return 'protocol version should be 1 or 2'
    with open(json_file, 'r') as file:
        configuration_file = json.loads(file.read())
    for protocol_id in actual_frequency:
        if protocol_id not in configuration_file['protocols_by_version']['Version' + str(protocol_version)]:
            wrong_fps.append(protocol_id)
    return wrong_fps

if __name__ == '__main__':
    actual_frequency = get_actual_frequency_from_logs(log_file='[MESTP].jzf')
    list_of_wrong_fps = verify_fps(actual_frequency=actual_frequency, json_file='protocol.json', protocol_version=1)
    print('this fps was wrong', list_of_wrong_fps)
    list_of_missing_from_logs = find_missing_protocols_in_the_data_file(actual_frequency=actual_frequency, json_file='protocol.json', protocol_version=1)
    print('this protocols are missing from the data file', list_of_missing_from_logs)
    list_of_not_configured = find_logs_protocols_that_not_in_the_configuration(actual_frequency=actual_frequency, json_file='protocol.json', protocol_version=1)
    print('this protocols are in the log but not configured', list_of_not_configured)