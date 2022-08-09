from src.counter import count_ocurrences


def test_counter():
    path = "src/jobs.csv"
    word = "Python"
    word2 = "Javascript"
    assert count_ocurrences(path, word) == 1639
    assert count_ocurrences(path, word2) == 122
