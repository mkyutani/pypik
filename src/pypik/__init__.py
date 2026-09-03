import sys

from .markdown import extract_pik_blocks
from .pik import PikSyntaxError, dump, parse


def main() -> None:
    args = sys.argv[1:]
    if not args:
        print("Hello from pypik!")
        return

    path = args[0]
    with open(path, encoding="utf-8") as f:
        text = f.read()

    if path.endswith((".md", ".markdown")):
        blocks = extract_pik_blocks(text)
        if not blocks:
            print("no ```pik``` or ```pikchr``` code blocks found", file=sys.stderr)
            raise SystemExit(1)
        for i, block in enumerate(blocks, start=1):
            if len(blocks) > 1:
                print(f"--- block {i} of {len(blocks)} ---")
            _parse_and_dump(block)
        return

    _parse_and_dump(text)


def _parse_and_dump(text: str) -> None:
    try:
        doc = parse(text)
    except PikSyntaxError as e:
        print(f"error: {e}", file=sys.stderr)
        raise SystemExit(1)
    print(dump(doc))
