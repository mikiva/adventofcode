defmodule Day01Test do
  use ExUnit.Case
  doctest Day01

  test "part 1 input" do
    assert Day01.solve(input(), 1) == 70764
  end

  test "part 1 example" do
    assert Day01.solve(example(), 1) == 24000
  end
  test "part 2 example" do
    assert Day01.solve(example(), 3) == 45000
  end
  test "part 2 input" do
    assert Day01.solve(input(), 3) == 203905
  end

  defp input() do
    File.read!("input.txt")
    |> String.split("\n\n", trim: true)
  end
  defp example() do
    File.read!("example.txt")
    |> String.split("\n\n", trim: true)
  end

end
