from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path, encoding="utf-8") as file:
        list_of_dic = list(csv.DictReader(file, delimiter=",", quotechar='"'))
        return list_of_dic
