import functools
import re
from logging import exception


text_example = """homEwork:
tHis iz your homeWork, copy these Text to variable. 

	You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

	it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE. 

	last iz TO calculate nuMber OF Whitespace characteRS in this Text. caREFULL, not only Spaces, but ALL whitespaces. I got 87.

"""


# decorator that print func return value
def print_decorator(func):
    @functools.wraps(func)
    def wrapper(*func_args, **func_kwargs):
        print('function call --> ' + func.__name__ + '()')
        retval = func(*func_args, **func_kwargs)
        print('function ' + func.__name__ + '() returns:\n' + str(retval))
        return retval

    return wrapper


# normalizing case view
def normalize(text_to_normalize):
    try:
        text_to_normalize = re.split('([.!?\t\n] *)', text_to_normalize)
        text_normalized = ''.join([i.capitalize() for i in text_to_normalize])
        return text_normalized
    except TypeError:
        exception('normalize: Incorrect input')


# mistake solver
def solve_mistake(text_incorrect, correct='', incorrect=''):
    try:
        text_incorrect = re.sub(f'({incorrect.title()}) ', f'{correct.title()} ', text_incorrect)
        text_correct = re.sub(f' ({incorrect}) ', f' {correct} ', text_incorrect, flags=re.I)
        return text_correct
    except AttributeError:
        exception('solve_mistake. Incorrect type of parameters')
    except TypeError:
        exception('solve_mistake. Incorrect text input')


# take last word of each sentence
@print_decorator
def take_last_words(add_after, text_take):
    try:
        lastW = ''
        for i in re.split('[.?!]', text_take)[0:-1]:
            lastW += re.search(r'(\w+)$', i).group() + ' '
        text_result = re.sub(f'{add_after}', f'{add_after}\n\tLast words: {lastW}', text_take, flags=re.I)
        return text_result
    except TypeError:
        exception('take_last_words. Incorrect values')


# char counter
@print_decorator
def counter(to_count, where_count):
    try:
        return len(re.findall(f'[{to_count}]', where_count))
    except TypeError:
        exception('counter. Incorrect parameters type')


# function calls and results print
normalized_text = normalize(text_to_normalize=text_example)
correct_text = solve_mistake(text_incorrect=normalized_text, incorrect='iz', correct='is')
counter(r'\s', correct_text)
take_last_words('end of this paragraph.', correct_text)
