import sys

import numpy
import pytest

import termtables as tt


@pytest.mark.skipif(
    sys.stdout.encoding not in ["UTF-8", "UTF8"],
    reason="Need UTF-8 terminal (not {})".format(sys.stdout.encoding),
)
def test_table():
    numpy.random.seed(0)
    data = numpy.random.rand(5, 2)

    string = tt.to_string(data)

    assert (
        string
        == """┌────────────────────┬────────────────────┐
│ 0.5488135039273248 │ 0.7151893663724195 │
├────────────────────┼────────────────────┤
│ 0.6027633760716439 │ 0.5448831829968969 │
├────────────────────┼────────────────────┤
│ 0.4236547993389047 │ 0.6458941130666561 │
├────────────────────┼────────────────────┤
│ 0.4375872112626925 │ 0.8917730007820798 │
├────────────────────┼────────────────────┤
│ 0.9636627605010293 │ 0.3834415188257777 │
└────────────────────┴────────────────────┘"""
    )
    return


@pytest.mark.skipif(
    sys.stdout.encoding not in ["UTF-8", "UTF8"],
    reason="Need UTF-8 terminal (not {})".format(sys.stdout.encoding),
)
def test_separate_header():
    numpy.random.seed(0)
    data = numpy.random.rand(3, 2)

    string = tt.to_string(data, header=["alpha", "beta"])

    assert (
        string
        == """┌────────────────────┬────────────────────┐
│ alpha              │ beta               │
╞════════════════════╪════════════════════╡
│ 0.5488135039273248 │ 0.7151893663724195 │
├────────────────────┼────────────────────┤
│ 0.6027633760716439 │ 0.5448831829968969 │
├────────────────────┼────────────────────┤
│ 0.4236547993389047 │ 0.6458941130666561 │
└────────────────────┴────────────────────┘"""
    )
    return


@pytest.mark.skipif(
    sys.stdout.encoding not in ["UTF-8", "UTF8"],
    reason="Need UTF-8 terminal (not {})".format(sys.stdout.encoding),
)
def test_table_double():
    numpy.random.seed(0)
    data = numpy.random.rand(5, 2)

    string = tt.to_string(data, style=tt.styles.double)

    assert (
        string
        == """╔════════════════════╦════════════════════╗
║ 0.5488135039273248 ║ 0.7151893663724195 ║
╠════════════════════╬════════════════════╣
║ 0.6027633760716439 ║ 0.5448831829968969 ║
╠════════════════════╬════════════════════╣
║ 0.4236547993389047 ║ 0.6458941130666561 ║
╠════════════════════╬════════════════════╣
║ 0.4375872112626925 ║ 0.8917730007820798 ║
╠════════════════════╬════════════════════╣
║ 0.9636627605010293 ║ 0.3834415188257777 ║
╚════════════════════╩════════════════════╝"""
    )
    return


def test_table_ascii():
    numpy.random.seed(0)
    data = numpy.random.rand(5, 2)

    string = tt.to_string(data, style=tt.styles.ascii_thin)

    assert (
        string
        == """+--------------------+--------------------+
| 0.5488135039273248 | 0.7151893663724195 |
+--------------------+--------------------+
| 0.6027633760716439 | 0.5448831829968969 |
+--------------------+--------------------+
| 0.4236547993389047 | 0.6458941130666561 |
+--------------------+--------------------+
| 0.4375872112626925 | 0.8917730007820798 |
+--------------------+--------------------+
| 0.9636627605010293 | 0.3834415188257777 |
+--------------------+--------------------+"""
    )
    return


def test_table_mixed():
    numpy.random.seed(0)
    data = [[0, 0.123], [1, 2.13], [2, 613.2323]]

    string = tt.to_string(data, style=tt.styles.ascii_thin)

    assert (
        string
        == """+---+----------+
| 0 | 0.123    |
+---+----------+
| 1 | 2.13     |
+---+----------+
| 2 | 613.2323 |
+---+----------+"""
    )
    return


@pytest.mark.skipif(
    sys.stdout.encoding not in ["UTF-8", "UTF8"],
    reason="Need UTF-8 terminal (not {})".format(sys.stdout.encoding),
)
def test_table_padding_top():
    numpy.random.seed(0)
    data = [[0, 0.123], [1, 2.13], [2, 613.2323]]

    string = tt.to_string(data, padding=(1, 0))

    assert (
        string
        == """┌─┬────────┐
│ │        │
│0│0.123   │
│ │        │
├─┼────────┤
│ │        │
│1│2.13    │
│ │        │
├─┼────────┤
│ │        │
│2│613.2323│
│ │        │
└─┴────────┘"""
    )
    return


@pytest.mark.skipif(
    sys.stdout.encoding not in ["UTF-8", "UTF8"],
    reason="Need UTF-8 terminal (not {})".format(sys.stdout.encoding),
)
def test_table_padding_both():
    numpy.random.seed(0)
    data = [[0, 0.123], [1, 2.13], [2, 613.2323]]

    string = tt.to_string(data, padding=(1, 1))

    assert (
        string
        == """┌───┬──────────┐
│   │          │
│ 0 │ 0.123    │
│   │          │
├───┼──────────┤
│   │          │
│ 1 │ 2.13     │
│   │          │
├───┼──────────┤
│   │          │
│ 2 │ 613.2323 │
│   │          │
└───┴──────────┘"""
    )
    return


def test_table_alignment():
    numpy.random.seed(0)
    data = [[1, 2, 3], [613.23236243236, 613.23236243236, 613.23236243236]]

    string = tt.to_string(data, style=tt.styles.ascii_thin, alignment="lcr")

    assert (
        string
        == """+-----------------+-----------------+-----------------+
| 1               |        2        |               3 |
+-----------------+-----------------+-----------------+
| 613.23236243236 | 613.23236243236 | 613.23236243236 |
+-----------------+-----------------+-----------------+"""
    )
    return


def test_noborder():
    numpy.random.seed(0)
    data = [
        [["a", "bb", "ccc"]],
        [[1, 2, 3], [613.23236243236, 613.23236243236, 613.23236243236]],
    ]

    string = tt.to_string(data, style=None, padding=0)

    assert (
        string
        == """a              bb             ccc
1              2              3
613.23236243236613.23236243236613.23236243236"""
    )
    return


@pytest.mark.skipif(
    sys.stdout.encoding not in ["UTF-8", "UTF8"],
    reason="Need UTF-8 terminal (not {})".format(sys.stdout.encoding),
)
def test_header():
    header = ["a", "bb", "ccc"]
    data = [[1, 2, 3], [613.23236243236, 613.23236243236, 613.23236243236]]

    string = tt.to_string(data, header, alignment="lcr")

    assert (
        string
        == """┌─────────────────┬─────────────────┬─────────────────┐
│ a               │       bb        │             ccc │
╞═════════════════╪═════════════════╪═════════════════╡
│ 1               │        2        │               3 │
├─────────────────┼─────────────────┼─────────────────┤
│ 613.23236243236 │ 613.23236243236 │ 613.23236243236 │
└─────────────────┴─────────────────┴─────────────────┘"""
    )
    return


def test_header_ascii():
    numpy.random.seed(0)
    header = ["a", "bb", "ccc"]
    data = [[1, 2, 3], [613.23236243236, 613.23236243236, 613.23236243236]]

    string = tt.to_string(
        data, header=header, style=tt.styles.ascii_thin_double, alignment="lcr"
    )

    assert (
        string
        == """+-----------------+-----------------+-----------------+
| a               |       bb        |             ccc |
+=================+=================+=================+
| 1               |        2        |               3 |
+-----------------+-----------------+-----------------+
| 613.23236243236 | 613.23236243236 | 613.23236243236 |
+-----------------+-----------------+-----------------+"""
    )
    return


@pytest.mark.skipif(
    sys.stdout.encoding not in ["UTF-8", "UTF8"],
    reason="Need UTF-8 terminal (not {})".format(sys.stdout.encoding),
)
def test_header_thick():
    numpy.random.seed(0)
    header = ["a", "bb", "ccc"]
    data = [[1, 2, 3], [613.23236243236, 613.23236243236, 613.23236243236]]

    string = tt.to_string(
        data, header=header, style=tt.styles.thin_thick, alignment="lcr"
    )

    assert (
        string
        == """┌─────────────────┬─────────────────┬─────────────────┐
│ a               │       bb        │             ccc │
┝━━━━━━━━━━━━━━━━━┿━━━━━━━━━━━━━━━━━┿━━━━━━━━━━━━━━━━━┥
│ 1               │        2        │               3 │
├─────────────────┼─────────────────┼─────────────────┤
│ 613.23236243236 │ 613.23236243236 │ 613.23236243236 │
└─────────────────┴─────────────────┴─────────────────┘"""
    )
    return


def test_padding_0():
    numpy.random.seed(0)
    data = [[1, 2, 3], [613.23236243236, 613.23236243236, 613.23236243236]]

    string = tt.to_string(
        data, style=tt.styles.ascii_thin_double, padding=0, alignment="lcr"
    )

    ref = """+---------------+---------------+---------------+
|1              |       2       |              3|
+---------------+---------------+---------------+
|613.23236243236|613.23236243236|613.23236243236|
+---------------+---------------+---------------+"""

    assert string == ref

    string = tt.to_string(
        data, style=tt.styles.ascii_thin_double, padding=(0,), alignment="lcr"
    )
    assert string == ref
    return


def test_padding_10():
    numpy.random.seed(0)
    data = [[1, 2, 3], [613.23236243236, 613.23236243236, 613.23236243236]]

    string = tt.to_string(
        data, style=tt.styles.ascii_thin, padding=(1, 0), alignment="lcr"
    )

    assert (
        string
        == """+---------------+---------------+---------------+
|               |               |               |
|1              |       2       |              3|
|               |               |               |
+---------------+---------------+---------------+
|               |               |               |
|613.23236243236|613.23236243236|613.23236243236|
|               |               |               |
+---------------+---------------+---------------+"""
    )
    return


def test_padding_012():
    numpy.random.seed(0)
    data = [[1, 2, 3], [613.23236243236, 613.23236243236, 613.23236243236]]

    string = tt.to_string(
        data, style=tt.styles.ascii_thin, padding=(0, 1, 2), alignment="lcr"
    )

    assert (
        string
        == """+-----------------+-----------------+-----------------+
| 1               |        2        |               3 |
|                 |                 |                 |
|                 |                 |                 |
+-----------------+-----------------+-----------------+
| 613.23236243236 | 613.23236243236 | 613.23236243236 |
|                 |                 |                 |
|                 |                 |                 |
+-----------------+-----------------+-----------------+"""
    )
    return


def test_padding_0123():
    numpy.random.seed(0)
    data = [[1, 2, 3], [613.23236243236, 613.23236243236, 613.23236243236]]

    string = tt.to_string(
        data, style=tt.styles.ascii_thin, padding=(0, 1, 2, 3), alignment="lcr"
    )

    assert (
        string
        == """+-------------------+-------------------+-------------------+
|   1               |          2        |                 3 |
|                   |                   |                   |
|                   |                   |                   |
+-------------------+-------------------+-------------------+
|   613.23236243236 |   613.23236243236 |   613.23236243236 |
|                   |                   |                   |
|                   |                   |                   |
+-------------------+-------------------+-------------------+"""
    )
    return


def test_booktabs():
    numpy.random.seed(0)
    data = [
        [["a", "bb", "ccc"]],
        [[1, 2, 3], [613.23236243236, 613.23236243236, 613.23236243236]],
    ]

    string = tt.to_string(data, style=tt.styles.booktabs)

    assert string == "\n".join(
        [
            " ───────────────────────────────────────────────────── ",
            "  a                 bb                ccc",
            " ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ ",
            "  1                 2                 3",
            " ───────────────────────────────────────────────────── ",
            "  613.23236243236   613.23236243236   613.23236243236",
            " ───────────────────────────────────────────────────── ",
        ]
    )
    return


def test_booktabs_ascii():
    numpy.random.seed(0)
    header = ["a", "bb", "ccc"]
    data = [[1, 2, 3], [613.23236243236, 613.23236243236, 613.23236243236]]

    string = tt.to_string(data, header=header, style=tt.styles.ascii_booktabs)

    assert string == "\n".join(
        [
            " ----------------------------------------------------- ",
            "  a                 bb                ccc",
            " ===================================================== ",
            "  1                 2                 3",
            " ----------------------------------------------------- ",
            "  613.23236243236   613.23236243236   613.23236243236",
            " ----------------------------------------------------- ",
        ]
    )
    return
