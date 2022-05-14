
found = 0
# with open(,'r') as file:
#     lines = file.readlines()
#     lines = [line.rstrip() for line in lines]
#     print(lines)

def get_search_elem(file_name):
    line_found = 0
    with open(file_name) as f:
        for index, line in enumerate(f):
            if "/home/nutanix/bin/counters_collector" in line.strip():
                line_found = index
        if line_found:
            modify_line(file_name, line_found+1)


def modify_line(file_name, line_to_modify):
    current_file = open(file_name, "r")
    list_of_lines = current_file.readlines()
    print("modifying below line")
    print(list_of_lines[line_to_modify])
    list_of_lines[line_to_modify] = '  enabled: false\n'

    current_file = open(file_name, "w")
    current_file.writelines(list_of_lines)
    current_file.close()
    print("modified successfully")


if __name__ == '__main__':
    file_name = "/home/nutanix/ncc/config/nusights/cfs/backup_cfs.config"
    get_search_elem(file_name)