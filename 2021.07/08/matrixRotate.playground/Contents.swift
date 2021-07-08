import Foundation

func solution(_ rows:Int, _ columns:Int, _ queries:[[Int]]) -> [Int] {
    var answer:[Int] = []
    var board:[Int] = Array(repeating: 0, count: columns * rows)
    for i in 0..<rows{
        for j in 0..<columns{
            board[columns * i + j] = columns * i + j + 1
        }
    }
    var queue:[Int] = []
    var indexQueue:[Int] = []
    for i in queries{
        let topLeft = columns * (i[0] - 1) + (i[1] - 1)
        var topRight = columns * (i[0] - 1) + (i[3] - 1)
        var bottomLeft = columns * (i[2] - 1) + (i[1] - 1)
        let bottomRight = columns * (i[2] - 1) + (i[3] - 1)
        for j in topLeft..<topRight{
            queue.append(board[j])
            indexQueue.append(j)
        }
        for _ in 0..<i[2] - i[0]{
            queue.append(board[topRight])
            indexQueue.append(topRight)
            topRight += columns
        }
        for j in Array(bottomLeft + 1...bottomRight).reversed(){
            queue.append(board[j])
            indexQueue.append(j)
        }
        for _ in 0..<i[2] - i[0]{
            queue.append(board[bottomLeft])
            indexQueue.append(bottomLeft)
            bottomLeft -= columns
        }
        print(queue,indexQueue)
        answer.append(queue.min()!)
        queue = [queue[queue.count - 1]] + Array(queue[0..<queue.count - 1])
        for j in 0..<indexQueue.count{
            board[indexQueue[j]] = queue[j]
        }
        print(queue,indexQueue)
        queue = []
        indexQueue = []
        print()
    }
    return answer
}
solution(6, 6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]])
