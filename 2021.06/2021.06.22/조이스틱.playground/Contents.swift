import Foundation

func solution(_ name:String) -> Int {
    var nameArray:[Character] = Array(name)
    let max = 90
    let min = 65
    var count = 0
    var pointer = 0
    var isReversed = false
    while true {
        let target = nameArray[pointer]
        if !(target == "A"){
            let maxDistance = abs(Int(target.asciiValue!) - max) + 1
            let minDistance = abs(Int(target.asciiValue!) - min)
            if maxDistance < minDistance{
                count += maxDistance
                nameArray[pointer] = "A"
            }else{
                count += minDistance
                nameArray[pointer] = "A"
            }
        }
        let origin = nameArray[pointer..<nameArray.count] + nameArray[0..<pointer]
        let reverse = Array(origin.reversed())
        let reverseIndex = reverse.firstIndex{ $0 != "A" }
        let originIndex = Array(origin).firstIndex{ $0 != "A" }
        if reverseIndex == nil { break }
        if !isReversed{
            if originIndex! - 1 > reverseIndex!{
                isReversed = true
                pointer = nameArray.count - 1 + (pointer - reverseIndex!)
                count = reverseIndex! + count + 1
                continue
            }
        }
        if isReversed{
            pointer -= 1
            count += 1
        }else{
            pointer += 1
            count += 1
        }
    }
    return count
}
solution("ABABAAAAAAAAB")
//solution("BBAABAAAAB")
//solution("ABBA")

