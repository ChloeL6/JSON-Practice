import pytest

from collections import Counter

def remove_dups(sample):
    no_dups = []
    check_dups = Counter(sample)
    print(check_dups,"\n",f"Total items before removal: {len(sample)}" )

    if type(sample) is list and len(sample) != 0:
        for x in sample:
            if x not in no_dups:
                no_dups.append(x)
        print(f"Total items after removal: {len(no_dups)}")
        return (no_dups)
    return "Please enter a string with at least 1 item"

   
test1 = [1,2,3,4,4,3,2,1]
test2 = ["a", "b", "c", "d", "d", "a"]
test3 = [1,2,3,4,4,3,2,1,"h", "l", "m", "t","m","h","t"]
test4 = []
test5 = "astr"

@pytest.mark.parametrize("sample, list_no_dups", [
    (test1, [1,2,3,4]),
    (test2, ["a", "b", "c", "d"]),
    (test3, [1, 2, 3, 4, "h", "l", "m", "t"]),
    (test4, "Please enter a string with at least 1 item"),
    (test5, "Please enter a string with at least 1 item"),
])

def test_remove_dups(sample, list_no_dups):
    assert remove_dups(sample) == list_no_dups

def test_pass_more_args():
    with pytest.raises(Exception) as e:
        remove_dups([1,2], {"h","i"})