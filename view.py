from model import Person


def show_all_view(list):
    print('In our db we have %i users. Here they are:' % len(list))
    for item in list:
        print(item.name())


def start_view():
    print('MVC - the simplest example')
    print('Do you want to see everyone in my db?[y/n]: ')


def end_view():
    print('Goodbye!')