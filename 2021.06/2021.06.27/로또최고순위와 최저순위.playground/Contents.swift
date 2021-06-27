import Foundation

func solution(_ lottos:[Int], _ win_nums:[Int]) -> [Int] {
    var winCount = 0
    var zeroCount = 0
    for i in lottos{
        if win_nums.contains(i){
            winCount += 1
        }else if i == 0 {
            zeroCount += 1
        }
    }
    let worst:Int
    if winCount < 2{
        worst = 6
    }else{
        worst = 6 - winCount + 1
    }
    var best = worst - zeroCount
    if best == 0{
        best = 1
    }else if best > 6{
        best = 6
    }
    return [best,worst]
}
solution([0, 0, 0, 0, 0, 0],[38, 19, 20, 40, 15, 25])
