# pypik

A Python project that converts pik format files into PowerPoint objects, SVG, and other formats via an intermediate tree structure.

## Requirements

- Python 3.14+
- [uv](https://docs.astral.sh/uv/)

## Usage

```sh
uv run pypik
```

## Acknowledgments

The `.pik` tokenizer, grammar, and layout engine in this project are
ported from [pikchr](https://pikchr.org/) by D. Richard Hipp, whose
[source](https://pikchr.org/home/doc/tip/pikchr.y) states it is released
under the Zero-Clause BSD license.

## License

[0BSD](LICENSE)
