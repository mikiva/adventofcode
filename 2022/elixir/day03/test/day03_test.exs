defmodule Day03Test do
  use ExUnit.Case
  doctest Day03

  test "part 1 example" do
    assert Day03.p1(example()) == 157
  end
  test "part 1 input" do
    assert Day03.p1(input()) == 7990
  end

  test "part 2 example" do
    assert Day03.p2(example()) == 70
  end
  test "part 2 input" do
    assert Day03.p2(input()) == 2602
  end

  defp input() do
    File.read!("input.txt")
    |> String.replace("\r", "")
    |> String.split("\n", trim: true)
  end
  defp example() do
    File.read!("example.txt")
    |> String.replace("\r", "")
    |> String.split("\n", trim: true)
  end
end
