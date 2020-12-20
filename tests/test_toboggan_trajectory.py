from toboggan_trajectory import count_trees, multiply_trees
from toboggan_trajectory.__main__ import main, main2


def test_count_trees():
    assert count_trees("""..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#""") == 7


def test_muliply_trees():
    assert multiply_trees("""..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#""") == 336


def test_count_trees_main(capsys, mocker):
    mocker.patch(
        'fileinput.input',
        return_value=[
            '..##.......\n',
            '#...#...#..\n',
            '.#....#..#.\n',
            '..#.#...#.#\n',
            '.#...##..#.\n',
            '..#.##.....\n',
            '.#.#.#....#\n',
            '.#........#\n',
            '#.##...#...\n',
            '#...##....#\n',
            '.#..#...#.#',
        ]
    )

    main()

    captured = capsys.readouterr()
    assert captured.out == '7\n'


def test_muliply_trees_main(capsys, mocker):
    mocker.patch(
        'fileinput.input',
        return_value=[
            '..##.......\n',
            '#...#...#..\n',
            '.#....#..#.\n',
            '..#.#...#.#\n',
            '.#...##..#.\n',
            '..#.##.....\n',
            '.#.#.#....#\n',
            '.#........#\n',
            '#.##...#...\n',
            '#...##....#\n',
            '.#..#...#.#',
        ]
    )

    main2()

    captured = capsys.readouterr()
    assert captured.out == '336\n'
