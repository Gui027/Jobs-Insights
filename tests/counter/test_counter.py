from src.counter import count_ocurrences


def test_counter():
    path = "src/jobs.csv"
    word1 = "Python"
    word2 = "Javascript"

    assert count_ocurrences(path, word1)
    assert count_ocurrences(path, word2)
