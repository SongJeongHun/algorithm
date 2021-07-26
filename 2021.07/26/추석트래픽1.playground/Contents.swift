import Foundation
struct Data{
    let hour:Double
    let min:Double
    let second:Double
    var endT:Double{ return hour * 60 * 60 * 1000 + min * 60 * 1000 + second * 1000 }
    let processT:Double
    var startT:Double { return endT - processT }
}
func solution(_ lines:[String]) -> Int {
    var log:[Data] = []
    
    // 로그 데이터 초기화 ms 단위로 맞춰줌
    for i in lines{
        let cmd = i.split(separator: " ")
        let completed = cmd[1].split(separator: ":")
        let hour = Double(completed[0])!
        let min = Double(completed[1])!
        let second = Double(completed[2])!
        let processT = Double(cmd[2][cmd[2].startIndex ..< cmd[2].index(cmd[2].endIndex, offsetBy: -1)])!
        log.append(Data(hour: hour, min: min, second: second, processT: processT * 1000))
    }
    
    var maxCount = 0
    // 서칭 로직: 현재 인덱스의 종료시간 + 1초를 한 시간이 나머지 인덱스의 시작시간보다 작다면 count += 1
    for i in 0..<log.count {
        var count = 1
        // target = 현재 인덱스의 종료시간
        let target = log[i].endT
        // 나머지 인덱스의 시작시간 탐색
        for j in i + 1..<log.count {
            if log[j].startT < target + 999 { count += 1 }
        }
        if maxCount < count { maxCount = count }
    }
    return maxCount
}
solution(["2016-09-15 01:00:04.001 2.0s", "2016-09-15 01:00:07.000 2s"])
