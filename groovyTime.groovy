import java.util.*
1000.times {
  def rand = new Random()
  def arraySize = args.size() > 0 ? args[0] : 1000000
  int[] array = new int[arraySize];
  arraySize.times { array[it] = Math.abs(rand.nextInt(100000))+1 }
  def startTime = System.nanoTime() / 1000
  Arrays.sort(array)
  def endTime = System.nanoTime() / 1000
  println "Elapsed time: ${endTime-startTime} mircoseconds"
}
