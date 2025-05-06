/**
 * Computes the difference between two arrays.
 * @param array The array to filter.
 * @param values The values to exclude from the array.
 * @returns A new array with the values from the first array that are not in the second array.
 */
export function difference<T>(array: Array<T>, values: Array<T>): Array<T> {
  // Set으로 변환하면 filter predicate에서 O(1)으로 element를 검색할 수 있는 장점이 있다.
  const valuesSet = new Set(values);
  return array.filter((element) => !valuesSet.has(element));
}
