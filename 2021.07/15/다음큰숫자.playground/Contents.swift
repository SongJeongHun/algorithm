import Foundation

func solution(_ n:Int) -> Int
{
    var start = n
    let count = counting(n: String(n,radix: 2))
    start += 1
    while true{
        let target = String(start,radix: 2)
        let targetCount = counting(n: target)
        if count == targetCount{
            return Int(target,radix: 2)!
        }
        start += 1
    }
}
func counting(n:String) -> Int{
    var count = 0
    for i in n{
        if i == "1"{ count += 1}
    }
    return count
}
solution(78)
