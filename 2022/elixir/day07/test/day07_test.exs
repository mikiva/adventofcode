defmodule Day07Test do

  use ExUnit.Case
  doctest Day07

  test "part 1 example" do
    assert Day07.part1(example()) == 95437
  end

    defp example() do
      File.read!("example.txt")
      |> String.split("\n")
      |> Enum.map(fn l -> String.split(l, " ") end)
    end

end
