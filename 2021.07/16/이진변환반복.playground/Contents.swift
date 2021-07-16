import Foundation

func solution(_ s:String) -> [Int] {
    return recursive(s:s,count: 0,totalCount: 0)
}
func recursive(s:String,count:Int,totalCount:Int) -> [Int]{
    let oneCount = s.filter { $0 == "1" }.count
    let x = String(repeating: "1", count:oneCount )
    let cnt = s.count - oneCount
    let target = x.count
    let targetBin = String(target,radix: 2)
    if Int(targetBin) == 1{
        return [totalCount + 1,count + cnt]
    }else{
        return recursive(s: targetBin,count: count + cnt,totalCount: totalCount + 1)
    }
}
solution("110010101001")
