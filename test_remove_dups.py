import pytest


def remove_dups(sample):
    no_dups = []
    if type(sample) is list and len(sample) != 0:
        for x in sample:
            if x not in no_dups:
              no_dups.append(x)
        return no_dups
    else:
        return None

   
test1 = [1,2,3,4,4,3,2,1]
test2 = ["a", "b", "c", "d", "d", "a"]
test3 = [1,2,3,4,4,3,2,1,"h", "l", "m", "t","m","h","t"]
test4 = []
test5 = "astr"

def test_list_num():
    assert remove_dups(test1) == [1,2,3,4]

def test_list_str():
    assert remove_dups(test2) == ["a", "b", "c", "d"]

def test_list_str_num():
    assert remove_dups(test3) == [1, 2, 3, 4, "h", "l", "m", "t"]

def test_empty_list():
    assert remove_dups(test4) == None

def test_str():
    assert remove_dups(test5) == None

# @pytest.mark.parametrize("sample, list_no_dups", [
#     (test1, [1,2,3,4]),
#     (test2, ["h", "l", "m", "t"])
# ])

# def test_remove_dups(sample, list_no_dups):
#     assert remove_dups(sample) == list_no_dups