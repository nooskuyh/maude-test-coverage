import re
import json

# Matches “rl … [label X]” or “ceq … [label Y]” at the start of a line
_LABEL_RE = re.compile(
    r'^(?P<kind>eq|crl|rl|ceq)\b.*?\[label\s+(?P<label>[^\]]+)\]',
    re.MULTILINE
)