import Foundation

func solution(_ d:[Int], _ budget:Int) -> Int {
    var budgets = budget
    let departs = d.sorted()
    var count = 0
    for i in departs{
        if budgets - i < 0{
            return count
        }else{
            count += 1
            budgets -= i
        }
    }
    return count
}
