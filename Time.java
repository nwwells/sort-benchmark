import java.util.Random;
import java.util.Arrays;
public class Time {
  static Random rand = new Random();
  public static void main(String [ ] args) throws Exception {
    Thread.sleep(1000);
    for (int j = 0; j < 100; j++) {
      int arraySize = 10000;
      int[] array = new int[arraySize];
      for (int i = 0; i < arraySize; i++) 
        array[i] = Math.abs(rand.nextInt(100000)) + 1;
      long startTime = System.nanoTime() / 1000;
      Arrays.sort(array);
      long endTime = System.nanoTime() / 1000;
      long interval = endTime - startTime;
      System.out.println(String.format("Elapsed time: %1$d microseconds", interval));
    }
  }
}
