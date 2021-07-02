import Foundation
func solution(_ cacheSize:Int, _ cities:[String]) -> Int {
    if cacheSize == 0{
        return 5 * cities.count
    }
    var answer = 0
    var cache:[String] = []
    for i in cities{
        let city = i.lowercased()
        if cache.contains(city){
            answer += 1
            cache.remove(at: cache.firstIndex(of: city)!)
            cache.append(city)
        }else{
            answer += 5
            if cache.count >= cacheSize{
                cache.removeFirst()
            }
            cache.append(city)
        }
    
    }
    return answer
}
