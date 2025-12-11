defmodule Day03 do
  @moduledoc """
  Documentation for `Day03`.
  """

  defp alpha() do
    "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
  end

  def p1(input) do
    input
    |> Enum.map(&split_line(&1))
    |> Enum.map(&get_intersection(&1))
    |> Enum.map(&char_to_prio(&1))
    |> Enum.sum
  end

  defp split_line(line) do
    len = String.length(line)
    every = (Integer.floor_div(len, 2))

    String.split_at(line, every)
  end

  defp get_intersection([l, c, r]) do
    left = MapSet.new(String.graphemes(l))
    center = MapSet.new(String.graphemes(c))
    right = MapSet.new(String.graphemes(r))

    MapSet.intersection(left, center)
    |> MapSet.intersection(right)
    |> MapSet.to_list
    |> Enum.at(0)
    end
  defp get_intersection({l, r}) do
    left = MapSet.new(String.graphemes(l))
    right = MapSet.new(String.graphemes(r))

    MapSet.intersection(left, right)
    |> MapSet.to_list
    |> Enum.at(0)
  end

  defp char_to_prio(ch) when is_binary(ch) do
    {i, _} = :binary.match(alpha(), ch)
    i + 1
  end

  def p2(input) do
    input
    |> Enum.chunk_every(3)
    |> Enum.map(&get_intersection(&1))
    |> Enum.map(&char_to_prio(&1))
    |> Enum.sum

  end



end
