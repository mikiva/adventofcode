defmodule Day02Test do
  use ExUnit.Case
  doctest Day02


  test "part 1 example" do
    assert Day02.part1(example()) == 15
  end
  test "part 1 input" do
    assert Day02.part1(input()) == 12855
  end

  test "part 2 example" do
    assert Day02.part2(example()) == 12
  end
  test "part 2 input" do
    assert Day02.part2(input()) == 13726
  end



  defp input() do
    File.read!("input.txt")
    |> String.split("\n", trim: true)
  end
  defp example() do
    File.read!("example.txt")
    |> String.split("\n", trim: true)
  end
end
