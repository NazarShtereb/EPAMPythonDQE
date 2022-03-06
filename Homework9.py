import xml.etree.ElementTree as et
import Homework5 as Hm5
import os


def parse_xml(file_path):
    """
    Xml parser
    :param file_path:
    :return parsed text as list of classes' objects:
    """
    objects = []
    inc_rows = []
    try:
        f = et.parse(file_path)
        root = f.getroot()
        for i in root.iter():
            try:
                if i.get('type') == "New":
                    objects.append(Hm5.New(i.find('name').text, i.find('text').text, i.find('city').text))
                elif i.get('type') == "Ad":
                    objects.append(Hm5.Ad(i.find('name').text, i.find('text').text, i.find('date').text))
                elif i.get('type') == "Stream":
                    objects.append(Hm5.Stream(i.find('name').text, i.find('text').text, i.find('link').text,
                                              i.find('date').text,
                                              i.find('duration').text))
                elif i.get('type') not in ('New', 'Stream', 'Ad') and not None:
                    inc_rows.append(i.get('type'))
                    continue
                else:
                    inc_rows.append(i.text)
                    continue
            except IndexError:
                inc_rows.append(i.text)
                continue
            except ValueError:
                inc_rows.append(i.text)
                continue
            except AttributeError:
                inc_rows.append(i.text)
                continue
        print(f'Content parsed! Number of skipped rows: {len(inc_rows)}')
        while "the answer is invalid":
            reply = str(input('Delete input file? (y/n): ')).lower().strip()
            if reply[0] == 'y':
                if os.path.exists(file_path):
                    os.remove(file_path)
                    print(f"{file_path} deleted")
                    break
                else:
                    print("The file does not exist")
                    break
            else:
                break
    except FileNotFoundError:
        print('File does not exist')
    except et.ParseError:
        print('Parse error')
    return objects
