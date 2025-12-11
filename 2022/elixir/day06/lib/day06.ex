defmodule Day06 do
  def solve(i, x, w) do
    s = i |> Enum.slice(x, w) |> MapSet.new |> MapSet.size
    cond do
      s == 0 -> -1
      s == w -> x + w
      true -> solve(i,x+1,w)
    end
  end
end
