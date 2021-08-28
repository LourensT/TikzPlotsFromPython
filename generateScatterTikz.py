from typing import List, Dict

def generate_plot(series: List[Dict[float] : float], labels : List[int], 
                            style="style.txt", 
                            log=False,
                            line=False):

    assert len(series) == len(labels), "number of labels does comply with number of series"

    if line:
        assert len(series) <= 8, "too many series (maximum 8 for lines)"
    else:
        assert len(series) <= 5, "too many series (maximum 5 for lines)"
