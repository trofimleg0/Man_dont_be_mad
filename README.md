# Man don't be mad

### A simulator of a simplified game "Man, don't be mad".



## Rules:
- The game is played on a field with size n
- The figure starts moving on the board at position 1
- A die is thrown (1-6)
  - If 6 is dropped, the die is thrown again
  - If 5 is dropped, all dropped values per turn are canceled, and the player does not move
  - The figure moves by the sum of the dropped values per turn
  - The game ends when the figure hits the last field

## Example:
- 6 6 1 => shift by 13 (if the figure does not exceed the target, otherwise it doesn't move)
- 6 6 6 5 => the figure doesn't move
- 4 =>  shift by 4 (if the figure does not exceed the target, otherwise it doesn't move)
- 5 => don't move



## Notes:
- If the value of the game plan is < 2, then the program stops and outputs: ***"Please write a value higher than or equal to 2."***
- The figure moves either by the total amount of rolls of the dice, or doesn't move at all
(in a situation where it would cross the target or dropped 5)
