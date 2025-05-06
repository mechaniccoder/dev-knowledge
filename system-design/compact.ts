export function compact<T>(
  array: Array<T | null | undefined | false | 0 | "">
): Array<T> {
  return array.filter((item): item is T => Boolean(item));
}
