import json
import Homework5 as Hm5
import os


def parse_json(file_path):
    """
    Json parser
    :param file_path:
    :return parsed text as list of classes' objects:
    """
    objects = []
    inc_rows = []
    try:
        f = json.load(open(file_path, 'r'))
        for i in f:
            try:
                if i["Type"] == "New":
                    objects.append(Hm5.New(i["Name"], i["Text"], i["City"]))
                elif i["Type"] == "Ad":
                    objects.append(Hm5.Ad(i["Name"], i["Text"], i["Date"]))
                elif i["Type"] == "Stream":
                    objects.append(Hm5.Stream(i["Name"], i["Text"], i["Link"], i["Date"], i["Duration"]))
                elif i["Type"] is None:
                    inc_rows.append('Blank row')
                    continue
                else:
                    inc_rows.append(i)
                    continue
            except IndexError:
                inc_rows.append(i)
                continue
            except ValueError:
                inc_rows.append(i)
                continue
        print(f'Content parsed! Number of skipped rows: {len(inc_rows)}')
        if os.path.exists(file_path):
            os.remove(file_path)
        else:
            print("The file does not exist")
    except FileNotFoundError:
        print('File does not exist')
    return objects
