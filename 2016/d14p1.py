import fileinput
import hashlib
import re

input_lines = list(fileinput.input())

salt = input_lines[0].strip()

keys_to_produce = 64
interval = 1000
keys_produced = set()
index = 0
candidates = []
limit = None
while limit is None or index <= limit:
    hashresult = hashlib.md5((salt + str(index)).encode("utf-8")).hexdigest()
    match3 = re.search(r"(\w)\1{2}", hashresult)
    if match3 is not None:
        digit3 = match3.group()[0]
        while len(candidates) > 0 and candidates[0][0] < index - interval:
            candidates.pop(0)
        match5 = re.search(r"(\w)\1{4}", hashresult)
        if match5 is not None:
            digit5 = match5.group()[0]
            for earlier_candidate_index, earlier_candidate_digit in candidates:
                if earlier_candidate_digit == digit5:
                    keys_produced.add(earlier_candidate_index)
                    if len(keys_produced) >= keys_to_produce and limit is None:
                        limit = index + interval
        candidates.append((index, digit3))
    index += 1
print(sorted(list(keys_produced))[keys_to_produce - 1])
