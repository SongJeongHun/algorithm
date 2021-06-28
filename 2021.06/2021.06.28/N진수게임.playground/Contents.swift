import Foundation
func solution(_ n:Int, _ t:Int, _ m:Int, _ p:Int) -> String {
    let radix = n
    var count = 0
    var context = ""
    var turn = 0
    loop:while true{
        let target = String(count,radix: radix)
        for i in target{
            if turn % m == p - 1{
                context += String(i.uppercased())
                if context.count == t{
                    break loop
                }
                turn += 1
            }else{
                turn += 1
            }
        }
        count += 1
    }
    print(context)
    return ""
}
solution(16, 16, 2, 1)
