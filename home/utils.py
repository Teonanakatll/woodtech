def get_list(lst):
    list_project = []
    if len(lst) >= 5:
        list_project.append(lst[:5])
    if len(lst) >= 9:
        list_project.append(lst[5:9])
    if len(lst) >= 14:
        list_project.append(lst[9:14])
    if len(lst) >= 18:
        list_project.append(lst[14:18])
    return list_project
