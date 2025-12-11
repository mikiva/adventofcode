defmodule Day06Test do
  use ExUnit.Case
  doctest Day06

  test "part 1 example" do
    assert Day06.solve(example(), 0, 4) == 7
  end
  test "part 1 input" do
    assert Day06.solve(input(), 0, 4) == 1210
  end

  test "part 2 example" do
    assert Day06.solve(example(), 0, 14) == 19
  end

  test "part 2 input" do
    assert Day06.solve(input(), 0, 14) == 3476
  end

  defp example() do
    File.read!("example.txt")
    |> String.replace("\r", "")
    |> String.graphemes()
  end
  defp input() do
    File.read!("input.txt")
    |> String.replace("\r", "")
    |> String.graphemes()
  end
end
