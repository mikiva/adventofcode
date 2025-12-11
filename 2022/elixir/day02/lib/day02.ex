defmodule Day02 do
  def part1(input) do
    input
    |> Enum.map(fn x -> play(String.split(x, " ", trim: true)) end)
    |> Enum.sum()
  end

  defp play(game) do
    played = get_index(Enum.at(game, 0), "ABC")
    me = get_index(Enum.at(game, 1), "XYZ")
    score = me + 1
    mod = Integer.mod(me - played, 3)
    case mod do
      0 -> score + 3
      1 -> score + 6
      _ -> score
    end
  end

  def part2(input) do
    input
    |> Enum.map(fn x -> play_mod(String.split(x, " ", trim: true)) end)
    |> Enum.sum()
  end

  defp play_mod(game) do
    [a, b] = game
    played = get_index(a, "ABC")

    case b do
      "X" -> Integer.mod(played - 1, 3) + 1
      "Y" -> 3 + played + 1
      _   -> 6 + Integer.mod(played + 1, 3) + 1
    end
  end

  defp get_index(played, to_match) do
    case String.split(to_match, played, parts: 2) do
      [left, _] -> String.length(left)
      [_] -> nil
    end
  end
end
