

import kotlin.math.absoluteValue

fun main() {

    var input = "R2, L5, L4, L5, R4, R1, L4, R5, R3, R1, L1, L1, R4, L4, L1, R4, L4, R4, L3, R5, R4, R1, R3, L1, L1, R1, L2, R5, L4, L3, R1, L2, L2, R192, L3, R5, R48, R5, L2, R76, R4, R2, R1, L1, L5, L1, R185, L5, L1, R5, L4, R1, R3, L4, L3, R1, L5, R4, L4, R4, R5, L3, L1, L2, L4, L3, L4, R2, R2, L3, L5, R2, R5, L1, R1, L3, L5, L3, R4, L4, R3, L1, R5, L3, R2, R4, R2, L1, R3, L1, L3, L5, R4, R5, R2, R2, L5, L3, L1, L1, L5, L2, L3, R3, R3, L3, L4, L5, R2, L1, R1, R3, R4, L2, R1, L1, R3, R3, L4, L2, R5, R5, L1, R4, L5, L5, R1, L5, R4, R2, L1, L4, R1, L1, L1, L5, R3, R4, L2, R1, R2, R1, R1, R3, L5, R1, R4"
    //var input = "R5, L5, R5, R3"
    //var input = "R8, R4, R4, R8"


    var i = input.split(", ")

    var directions = listOf(Pair(0,-1),Pair(1,0),Pair(0,1),Pair(-1,0))

    var currentDirection = 0;

    var currentPosition = Pair(0,0)

    //for (d in directions) {
    //    println(d.first.toString() + "   " + d.second.toString())
    //}


    var visited = ArrayList<Pair<Int, Int>>()
    visited.add(Pair(0,0))
    var twice = false
    var hereBeTwice: Int? = null;

    for(dir: String in i) {
        var turn = dir.substring(0, 1)
        var dist = dir.substring(1).toInt()


        if (turn.equals("R")) {
            currentDirection = (currentDirection + 1) % 4
        }
        else {
            currentDirection = (currentDirection - 1 + 4) % 4
        }

        for(d in 0..dist-1) {

            var dx = directions[currentDirection].first
            var dy = directions[currentDirection].second
            currentPosition = Pair(currentPosition.first + dx, currentPosition.second + dy)
            
            
            if (!twice && visited.contains(currentPosition)) {
                hereBeTwice = currentPosition.first.absoluteValue + currentPosition.second.absoluteValue
                twice = true
            }
            
            visited.add(currentPosition)
            
        }
        
        
    }

    var traveled = currentPosition.first.absoluteValue + currentPosition.second.absoluteValue

    println(traveled)
    println(hereBeTwice)


}