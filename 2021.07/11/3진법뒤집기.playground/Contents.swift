import Foundation

func solution(_ n:Int) -> Int {
    let result = String(String(n,radix: 3).reversed())
    return Int(result,radix: 3)!
}
solution(45)
