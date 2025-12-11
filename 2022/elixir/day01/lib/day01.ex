defmodule Day01 do
  def solve(input, nbr) do
    parse_elves(input)
    |> Enum.sort(:desc)
    |> Enum.take(nbr) #1
    |> Enum.sum()
  end

  defp parse_elves(input) do
    input
    |> Enum.map(fn elf -> elf_carry(elf) end)
  end

  defp elf_carry(elf) do
    String.split(elf, "\n")
    |> Enum.map(fn x -> x |> String.to_integer() end)
    |> Enum.sum()
  end
end
