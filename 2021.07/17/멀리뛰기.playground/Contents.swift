func solution(_ n:Int) -> Int {
    if n == 1{
        return 1 % 1234567
    }else if n == 2{
        return 2 % 1234567
    }
    var jump:[Int] = Array(repeating: 0, count: n)
    jump[0] = 1
    jump[1] = 2
    for i in 2..<n{
        jump[i] = (jump[i - 1] + jump[i - 2]) % 1234567
    }
    return jump[n - 1]
}
solution(4)
