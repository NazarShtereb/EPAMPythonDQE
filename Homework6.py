import csv
import Homework5 as Hw5
import Homework4_2_review as Hw4_2
import Homework8 as Hw8
import os


def parse_text(file_path):
    """
    Text parser
    :param file_path:
    :return parsed text as list of classes' objects:
    """
    objects = []
    inc_rows = []
    try:
        with open(file_path, 'r', ) as f:
            reader = csv.reader(f, delimiter='|')
            for row in reader:
                try:
                    if row[0] == 'news':
                        objects.append(Hw5.New(Hw4_2.normalize(row[1]), Hw4_2.normalize(row[2]),
                                               Hw4_2.normalize(row[3])))
                    elif row[0] == 'ad':
                        objects.append(Hw5.Ad(Hw4_2.normalize(row[1]), Hw4_2.normalize(row[2]), row[3]))
                    elif row[0] == 'stream':
                        objects.append(
                            Hw5.Stream(Hw4_2.normalize(row[1]), Hw4_2.normalize(row[2]), Hw4_2.normalize(row[3]),
                                       row[4], row[5]))
                    elif row[0] is None:
                        inc_rows.append('Blank row')
                        continue
                    else:
                        inc_rows.append(row)
                        continue
                except IndexError:
                    inc_rows.append(row)
                    continue
                except ValueError:
                    inc_rows.append(row)
                    continue
            print(f'Content parsed! Number of skipped rows: {len(inc_rows)}')
        if os.path.exists(file_path):
            os.remove(file_path)
        else:
            print("The file does not exist")
    except FileNotFoundError:
        print('File does not exist')
    return objects


class MainMenu:
    """
    Class to create and print a menu with options. Has 3 options:
    1. add new record from the user's input
    2. add new records from the file
    3. exit program
    """

    def __init__(self):
        self.menu_options = {
            1: 'Add from the console input',
            2: 'Add from the file',
            3: 'Add from the json',
            4: 'Exit',
        }
        self.menu_exec()

    def print_menu(self):
        """
        Print menu options

        :parameter
        Self
        :returns
        None
        """
        print('Publish Creator')
        for key in self.menu_options.keys():
            print(key, '--', self.menu_options[key])

    @staticmethod
    def option1():
        """
        Calls sub menu from Homework5.py module
        :return:
        """
        Hw5.Menu()

    @staticmethod
    def option2():
        """
        Calls file parsed method - parse_text
        Requires user's file path input or use default path
        :return:
        """
        try:
            file_path = input('Write file path. Leave it blank if you want to use a default: ')
            if file_path == '':
                file_path = 'homework6.txt'
            for i in parse_text(file_path):
                Hw5.add_to_file(i)

        except ValueError:
            pass

    @staticmethod
    def option3():
        """
        Calls file parsed method - parse_json
        Requires user's file path input or use default path
        :return:
        """
        try:
            file_path = input('Write file path. Leave it blank if you want to use a default: ')
            if file_path == '':
                file_path = 'homework8.json'
            for i in Hw8.parse_json(file_path):
                Hw5.add_to_file(i)

        except ValueError:
            pass

    def menu_exec(self):
        """
        Execute menu. Print all options and waiting for user's choice

        :parameter
        Self
        :returns
        None
        """
        while True:
            self.print_menu()
            option = ''
            try:
                option = int(input('Enter your choice: '))
            except ValueError:
                print('Wrong input. Please enter a number ...')
            # Check what choice was entered and act accordingly
            try:
                if option == 1:
                    self.option1()
                elif option == 2:
                    self.option2()
                elif option == 3:
                    self.option3()
                elif option == 4:
                    exit()
                else:
                    print('Invalid option. Please enter a number between 1 and 4.')
            except ValueError:
                print("Invalid inputs. Please try again")


if __name__ == '__main__':
    menu = MainMenu()
