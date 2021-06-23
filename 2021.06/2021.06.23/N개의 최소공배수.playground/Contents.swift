import Foundation

func solution(_ arr:[Int]) -> Int {
    var result = lcm(arr[0],arr[1])
    for i in 2..<arr.count{
        result = lcm(result, arr[i])
    }
    return result
}
func gcd(_ a: Int, _ b: Int) -> Int {
  let n = a % b
  if n != 0 {
    return gcd(b, n)
  } else {
    return b
  }
}
 
func lcm(_ m: Int, _ n: Int) -> Int {
  return m / gcd(m, n) * n
}
solution([2,6,8,14])
