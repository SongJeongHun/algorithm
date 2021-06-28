import Foundation

func solution(_ absolutes:[Int], _ signs:[Bool]) -> Int {
    var nums:[Int] = []
    var result = 0
    for i in 0..<absolutes.count{
        let num = absolutes[i]
        if signs[i]{
            nums.append(num)
        }else{
            nums.append(-num)
        }
    }
    for i in nums{
        result += i
    }
    return result
}
solution([4,7,12], [true,false,true])
