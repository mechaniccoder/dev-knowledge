/**
 * This function returns the index of the first element in the array 
 * Otherwise, it returns -1, indicating that no element passed the test.
 *
 * @param {Array} array - The array to search.
 * @param {Function} predicate - The function invoked per iteration.
 * @param {number} [fromIndex=0] - The index to start searching from.
 * @returns The index of the found element, else -1.
 */
export default function findIndex<T>(
    array: Array<T>,
    predicate: (value: T, index: number, array: Array<T>) => boolean,
    fromIndex: number = 0,
  ): number {
    // Consider negative value of fromIndex
    fromIndex = fromIndex >= 0 ? fromIndex : Math.max(0, fromIndex + array.length)
  
    for (let index = fromIndex; index < array.length; index++) {
      if (predicate(array[index], index, array)) {
        return index
      }
    }
  
    return -1
  }