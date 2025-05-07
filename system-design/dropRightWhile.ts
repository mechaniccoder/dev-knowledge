/**
 * 오른쪽 element부터 시작해서 predicate에 맞지 않는 element가 나올때까지 제거한다.
 * @example
 * Example 1: Basic usage
 * dropRightWhile([1, 2, 3, 4, 5], (value, _index, _array) => value > 3);
 * => [1, 2, 3]
 *
 * Example 2: Predicate always true
 * dropRightWhile([1, 2, 3], (value, _index, _array) => value < 6);
 * => []
 *
 * Example 3: Predicate always false
 * dropRightWhile([1, 2, 3, 4, 5], (value, _index, _array) => value > 6);
 * => [1, 3, 2, 4, 5]
 *
 * Example 4: Using the `index` argument
 * dropRightWhile([1, 2, 3, 4, 5], (_value, index, _array) => index > 2);
 * => [1, 2, 3]
 *
 * Example 5: Using the `array` argument
 * dropRightWhile([10, 11, 12, 4, 5], (value, _index, array) => value < array[1]);
 * => [10, 11, 12]
 */
export default function dropRightWhile<T>(
  array: Array<T>,
  predicate: (value: T, index: number, array: Array<T>) => boolean
): Array<T> {
  let index = array.length - 1;

  while (predicate(array[index], index, array)) {
    index--;
  }

  return array.slice(0, index + 1);
}
