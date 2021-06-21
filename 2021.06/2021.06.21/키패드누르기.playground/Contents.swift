import Foundation

func solution(_ numbers:[Int], _ hand:String) -> String {
    let leftSide = [1,4,7,-1]
    let rightSide = [3,6,9,-2]
    let middleSide = [2,5,8,0]
    var result = ""
    var left = -1
    var right = -2
    for i in numbers{
        if leftSide.contains(i){
            result.append("L")
            left = i
        }else if rightSide.contains(i){
            result.append("R")
            right = i
        }else{
            var isLeftMiddle = false
            var isRightMiddle = false
            var rightIndex = rightSide.firstIndex(of: right)
            if rightIndex == nil{
                rightIndex = middleSide.firstIndex(of: right)
                isRightMiddle = true
            }
            var leftIndex = leftSide.firstIndex(of: left)
            if leftIndex == nil{
                leftIndex = middleSide.firstIndex(of: left)
                isLeftMiddle = true
            }
            let middleIndex = middleSide.firstIndex(of: i)!
            
            var rightDistance = abs(rightIndex! - middleIndex)
            var leftDistance = abs(leftIndex! - middleIndex)
            if isLeftMiddle{
                leftDistance -= 1
            }
            if isRightMiddle{
                rightDistance -= 1
            }
            print("target -> \(i) right -> \(right), left -> \(left)")
            if rightDistance > leftDistance{
                result.append("L")
                left = i
            }else if rightDistance < leftDistance{
                result.append("R")
                right = i
            }else if rightDistance == leftDistance{
                if hand == "right"{
                    result.append("R")
                    right = i
                }else{
                    result.append("L")
                    left = i
                }
            }
        }
    }
    return result
}
solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right")
solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left")
solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right")
