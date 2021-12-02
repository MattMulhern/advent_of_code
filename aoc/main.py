import logging

logger = logging.getLogger(__name__)


def hello_world():
    print("Helo world!")


def chunk_list(my_list, size):
    chunked = []
    for i in range(0, len(my_list), size):
        chunked.append(my_list[i:i+size])
    return chunked


def file_to_list_of_ints(filename):
    logger.debug(f"parsing {filename}")
    with open(filename, "r") as fp:
        lines = fp.readlines()
        return [int(x) for x in lines]


def file_to_list_of_str_tuples(filename):
    logger.debug(f"parsing {filename}")
    with open(filename, "r") as fp:
        lines = fp.readlines()
        return [tuple(x.split()) for x in lines]
