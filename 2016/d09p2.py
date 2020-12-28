import fileinput
import re

input_lines = list(fileinput.input())

charsequence = input_lines[0].strip()
literal_regexp = r"[A-Z]"
marker_regexp = r"\(\d+x\d+\)"
assert re.match(
    r"^(" + marker_regexp + r"|" + literal_regexp + r")+$", charsequence
).span() == (0, len(charsequence))


def process_chars(charseq):
    assert re.search(literal_regexp + r"$", charseq)
    first_marker = re.search(marker_regexp, charseq)
    if first_marker is None:
        return len(charseq)
    else:
        span_start, span_end = first_marker.span()
        marker_length, marker_repeat = list(
            map(int, re.findall(r"\d+", first_marker.group()))
        )
        assert len(charseq) >= span_end + marker_length
        return (
            span_start
            + marker_repeat
            * process_chars(charseq[span_end : span_end + marker_length])
            + (
                process_chars(charseq[span_end + marker_length :])
                if len(charseq) > span_end + marker_length
                else 0
            )
        )


print(process_chars(charsequence))
