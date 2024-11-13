

# Valid moves in the game.
SHIFT = 'S'
SWAP = 'W'
CHECK = 'C'


# We provide a full solution to this function as an example.
def is_valid_move(move: str) -> bool:
    """Return True if and only if move is a valid move. Valid moves are
    SHIFT, SWAP, and CHECK.

    >>> is_valid_move('C')
    True
    >>> is_valid_move('S')
    True
    >>> is_valid_move('W')
    True
    >>> is_valid_move('R')
    False
    >>> is_valid_move('')
    False
    >>> is_valid_move('NOT')
    False

    """

    return move == CHECK or move == SHIFT or move == SWAP

# Your turn! Provide full solutions to the rest of the required functions.

if __name__ == '__main__':
    import doctest
    doctest.testmod()

def get_section_start(section_num: int, section_len: int) -> int:
    """Return the index of the first character in the specified section.

    """
    return section_len*(section_num-1)


def get_section(state: str, section_num: int, section_len: int) -> str:
    """Return the section of the state that corresponds to the given section
    number.

    """
    return state[section_len*(section_num-1) : section_len*(section_num)]


def is_valid_section(state: str, section_num: int, section_len: int) -> bool:
    """The state is divisible by len, and the number of section should be less
    than or equal to the number of segments taken.

    """
    return len(state) % section_len == 0 and len(state) / section_len >= \
section_num


def swap(state: str, start: int, end: int) -> str:
    """The result of applying a Swap operation to the section of the
    given state string between the start index (inclusive) and the end
    index (exclusive).

    """

    first_char = state[start]
    last_char = state[end-1]
    middle = state[start+1 : end-1]
    return state[0:start] + last_char + middle + first_char + state[end:]


def shift(state: str, start: int, end: int) -> str:
    """The letter taken from start is moved to the end letter.

    """
    first_char = state[start]
    last_char = state[end-1]
    middle = state[start+1 : end-1]
    return state[0:start] + middle + last_char + first_char + state[end:]


def check(state: str, start: int, end: int, answer: str) -> bool:
    """Returns True if the letters between the start and end indexes in the
    initial state are the same as the correct answer.

    """
    return state[start:end] == answer[start:end]


def check_section(state: str, section_num: int, section_len: int, \
                   answer: str) -> bool:
    """The function should return True if and only if the section with the
    specified section number is correct.

    """

    true = answer[section_len*(section_num-1) : section_len*(section_num)]
    return get_section(state, section_num, section_len) == true


def change_section(state: str, movestr: str, section_num: int,\
                    section_len: int) -> str:
    """Execute swap or shift according to movestr.

    """

    start = get_section_start(section_num, section_len)
    end = get_section_start(section_num, section_len) + section_len

    if movestr == 'W':
        change = swap(state, start, end)
    elif movestr == 'S':
        change = shift(state, start, end)
    else:
        change = None
    return change


def get_move_hint(state: str, section_num: int, section_len: int,
                  answer: str) -> str:
    """If you can get the answer with one shift or two, suggest S, otherwise
    suggest W

    """

    start = get_section_start(section_num, section_len)
    end = get_section_start(section_num, section_len) + section_len
    true = answer[section_len*(section_num-1) : section_len*(section_num)]

    if get_section(shift(state, start, end), section_num, section_len) == true\
       or get_section(shift(shift(state, start, end), start, end), \
                      section_num, section_len) == true:
        suggest = 'S'
    else:
        suggest = 'W'
    return suggest
