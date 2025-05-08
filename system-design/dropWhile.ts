/**
 * Starting from the first element, remove elements until predicate returns false
 * @example
 * dropWhile([1, 2, 3, 4, 5], (value, index, array) => value < 3);
 * => [3, 4, 5]
 *
 * dropWhile([1, 2, 3, 4, 5], (value, index, array) => value < 6);
 * => []
 *
 * dropWhile([1, 2, 3, 4, 5], (value, index, array) => value > 6);
 * => [1, 2, 3, 4, 5]
 */
export default function dropWhile<T>(
  array: Array<T>,
  predicate: (value: T, index: number, array: Array<T>) => boolean
): Array<T> {
  let index = 0;

  while (predicate(array[index], index, array) && index < array.length) {
    index++;
  }

  return array.slice(index);
}
