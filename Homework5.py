import datetime


class Publication:
    """
    Class of a publication that could be printed to txt file

    :parameter
    Self
    Name: The publication name
    Text: A text of the publication


    """
    def __init__(self, name, text):
        self.name = name
        self.text = text
        self.date = self.calculate_date()

    def calculate_date(self):
        """
        Date formatting

        :parameter
        Self
        :returns
        Today's date in specific format
        """
        return 'Date: ' + str(self.today().strftime('%b %d %Y %I:%M%p'))

    def publish(self):
        """
        Generate a string to print

        :parameter
        Self
        :returns
        String to print
        """
        return 'Publication' + '-' * 10 + '\n' + self.name + '\n' + self.text + '\n' + str(self.date)

    @staticmethod
    def today():
        """
        Calculates today's date

        :parameter
        Self
        :returns
        Today's date
        """
        return datetime.datetime.today()


class New(Publication):
    """
    Class of a new that could be printed to txt file

    :parameter
    Self
    Name: The new name
    Text: A text of the new
    City: A city of the new

    """
    def __init__(self, name, text, city):
        self.city = city
        super().__init__(name, text)

    def publish(self):
        """
        Generate a string to print

        :parameter
         Self
        :returns
        String to print
        """
        return 'New ' + '-' * 21 + '\n' + self.name + '\n' + self.text + '\n' + self.city + '\n' + str(self.date)


class Ad(Publication):
    """
    Class of a private ad that could be printed to txt file

    :parameter
    Self
    Name: The ad name
    Text: A text of the ad
    Expiration date: a date of the ad end


    """
    def __init__(self, name, text, exp_date):
        self.exp_date = datetime.datetime.strptime(exp_date, "%b %d %Y")
        super().__init__(name, text)

    def calculate_date(self):
        """
        Calculates ad dates

        :parameter
        Self
        :returns
        exp_date and date diff
        """
        today = self.today()
        date_diff = today - self.exp_date
        return 'Actual until: ' + str(self.exp_date.strftime('%b %d %Y')) + ', ' + str(abs(date_diff.days)) + ' Days left'

    def publish(self):
        """
        Generate a string to print

        :parameter
        Self
        :returns
        String to print
        """
        return 'Private Ad ' + '-' * 14 + '\n' + self.name + '\n' + self.text + '\n' + str(self.date)


class Stream(Publication):
    """
    Class of a stream that could be printed to txt file

    :parameter
    Self
    Name: A stream name
    Text: A desc text of the stream
    Start date: a date of the stream start
    Duration: the stream's duration


    """
    def __init__(self, name, text, link, start_date, duration):
        self.start_date = datetime.datetime.strptime(start_date, '%b %d %Y %I:%M%p')
        self.link = link
        self.duration = duration
        super().__init__(name, text)

    def calculate_date(self):
        """
        Calculates ad dates

        :parameter
        Self
        :returns
        start_date and end_date
        """
        today = self.today()
        date_diff = today - self.start_date
        end_time = self.start_date + datetime.timedelta(minutes=int(self.duration))
        return 'Stream start: ' + str(self.start_date.strftime('%b %d %Y %I:%M%p')) +\
               ', ' + str(abs(date_diff.days)) + ' Days to the stream' \
               + f'\nStream end: {end_time.strftime("%b %d %Y %I:%M%p")}'

    def publish(self):
        """
        Generate a string to print

        :parameter
         Self
        :returns
        String to print
        """
        return 'Stream ' + '-' * 18 + '\n' + self.name + '\n' + self.text + '\n' + self.link + '\n' + str(self.date)


class Menu:
    """
    Class to create and print a menu with options
    """
    def __init__(self):
        self.menu_options = {
            1: 'Add new',
            2: 'Add private ad',
            3: 'Add stream',
            4: 'Exit',
        }
        self.menu_exec()

    @staticmethod
    def add_to_file(pub):
        """
        Open newsfeed.txt file in utf-8
        Add the new/ad/stream to the end of a file

        :parameter
        Self
        :returns
        None
        """
        with open("newsfeed.txt", 'a', encoding='utf-8') as f:
            f.write(pub.publish() + f'\n{"-" * 25}\n')

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

    def option1(self):
        """
        Add a new option. Create 'a new' by console inputs

        :parameter
        Self
        :returns
        None
        """
        print('Handle option \'Add a new\'')
        name = input('Name of a new: ')
        text = input('Text of a new: ')
        city = input('City of a new: ')
        self.add_to_file(New(name, text, city))

    def option2(self):
        """
        Add an ad option. Create 'a private ad' by console inputs

        :parameter
        Self
        :returns
        None
        """
        print('Handle option \'Add a private ad\'')
        name = input('Name of an ad: ')
        text = input('Text of an ad: ')
        date = input('Expire date (ex. Jun 19 2022): ')
        self.add_to_file(Ad(name, text, date))

    def option3(self):
        """
        Add a stream option. Create 'a stream' by console inputs

        :parameter
        Self
        :returns
        None
        """
        print('Handle option \'Add a stream\'')
        name = input('Name of a stream: ')
        text = input('Text of a stream: ')
        link = input('Link of a stream: ')
        date = input('Stream date (ex. Jun 19 2022 1:33PM): ')
        duration = input('Stream duration in minutes (ex. 30): ')
        self.add_to_file(Stream(name, text, link, date, duration))

    def menu_exec(self):
        """
        Execute menu

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
    menu = Menu()