/**
 * @param {Array} array - The array to fill.
 * @param {*} value - The value to fill array with.
 * @param {number} [start=0] - The start position.
 * @param {number} [end=array.length] - The end position.
 * @return {Array} Returns the filled array.
 */
export default function fill<T>(
  array: Array<T>,
  value: any,
  start: number = 0,
  end: number = array.length
): Array<T> {
  if (start < 0) {
    start = -start > array.length ? 0 : array.length + start;
  }

  if (end > array.length) {
    end = array.length;
  }

  if (end < 0) {
    end += array.length;
  }

  for (let index = start; index < end; index++) {
    array[index] = value;
  }

  return array;
}
