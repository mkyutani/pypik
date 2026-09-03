# pypik

A Python project that converts [pikchr](https://pikchr.org/) (`.pik`)
diagram source into a tree structure, then into PowerPoint objects, SVG,
and other formats.

The pipeline has three stages:

1. **Parse** — `.pik` source is tokenized and parsed into an AST
   (`pypik.pik.ast.Document`), mirroring pikchr's own grammar.
2. **Layout** — the AST is resolved into concrete 2-D geometry (box
   positions, arrow paths, text placement) by a pragmatic subset of
   pikchr's own layout engine.
3. **Render** — the resolved geometry is written out in a target format.
   PowerPoint (`.pptx`) is implemented today; SVG is planned.

pypik doesn't define its own diagram language — `.pik` source is
pikchr's language. For the language spec itself (objects, attributes,
positions, expressions), see pikchr's own documentation:

- [Grammar](https://pikchr.org/home/doc/trunk/doc/grammar.md)
- [Examples](https://pikchr.org/home/doc/tip/doc/examples.md)
- [pikchr.y source](https://pikchr.org/home/doc/tip/pikchr.y) (the
  authoritative reference this project's parser and layout engine were
  ported from)

## Requirements

- Python 3.14+
- [uv](https://docs.astral.sh/uv/)

## Usage

Dump the parsed tree for a `.pik` file (useful for inspecting how a
script was understood, or for debugging):

```sh
uv run pypik diagram.pik
```

Render a `.pik` file straight to PowerPoint:

```sh
uv run pypik diagram.pik diagram.pptx
```

`.pik` or `.pikchr` fenced code blocks inside a Markdown file are also
accepted directly — every block in the file is processed in order:

```sh
uv run pypik doc.md doc.pptx
```

With no arguments, `pypik` just prints a hello-world message.

### Example

`examples/pipeline.pik`:

```pik
arrow right 200% "Markdown" "Source"
box rad 10px "Markdown" "Formatter" "(markdown.c)" fit
arrow right 200% "HTML+SVG" "Output"
arrow <-> down 70% from last box.s
box same "Pikchr" "Formatter" "(pikchr.c)" fit
```

```sh
uv run pypik examples/pipeline.pik examples/pipeline.pptx
```

## Scope

The parser and tokenizer aim to accept exactly the pikchr language. The
layout engine is a deliberately pragmatic *subset* of pikchr's own —
default object sizes, sequential chaining, `at`/`with`/`from`/`to`/
`then`/`go`/`same`/`chop`, and box/ellipse/diamond edge geometry are
ported faithfully, but a few things are simplified:

- spline/arc curves are drawn as straight polylines,
- `fit` text sizing uses real font metrics when rendering to PowerPoint,
  but falls back to a flat per-character estimate otherwise,
- chopping against diamond/cylinder/file shapes uses a rectangle-like
  approximation rather than each shape's true outline,
- `behind` is parsed but doesn't yet affect rendering order.

See the module docstrings in `src/pypik/pik/layout.py` for details.

## Development

```sh
uv run pytest
```

Test fixtures under `tests/fixtures/examples/` are pikchr's own official
example scripts, used as a real-world regression check.

## Acknowledgments

The `.pik` tokenizer, grammar, macro expansion, and layout engine in this
project are substantially ported from [pikchr](https://pikchr.org/) by
D. Richard Hipp, whose [source](https://pikchr.org/home/doc/tip/pikchr.y)
states it is released under the Zero-Clause BSD license. See
[NOTICE](NOTICE) for details.

## License

[0BSD](LICENSE)
