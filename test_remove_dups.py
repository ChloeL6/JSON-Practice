import pytest

no_dups = []
def remove_dups(sample):
    for x in sample:
        if x not in no_dups:
          no_dups.append(x)
    return no_dups
   


test1 = [1,2,3,4,4,3,2,1]
# test2 = ["h", "l", "m", "t","m","h","t"]
# test3 = [1,2,3,4,4,3,2,1,"h", "l", "m", "t","m","h","t"]


@pytest.mark.parametrize("sample, list_no_dups", [
    (test1, [1,2,3,4]),
    # (test2, ["h", "l", "m", "t"])
])

def test_remove_dups(sample, list_no_dups):
    assert remove_dups(sample) == list_no_dups