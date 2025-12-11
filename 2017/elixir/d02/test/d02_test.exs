defmodule D02Test do
  use ExUnit.Case
  doctest D02

  test "part 1 example" do
    assert D02.part1(puzzle_input("example")) == 18
  end

  test "part 2 example" do
    assert D02.part2(puzzle_input("example2")) == 9
  end

  test "part 1 solve" do
    assert D02.part1(puzzle_input("input")) == 44670
  end

  test "part 2 solve" do
    assert D02.part2(puzzle_input("input")) == 285
  end

  defp puzzle_input(file) do
    File.read!(file <> ".txt")
    |> parse_input()
  end

  defp parse_input(input) do
    String.split(input, "\n")
    |> Enum.map(fn s -> String.split(s) end)
    |> Enum.map(fn s ->
      Enum.map(s, fn str -> String.to_integer(str) end)
    end)
  end
end
