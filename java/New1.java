public class New1 {
  public static void main(String[] args) {
    
  
    int[][] Array = { { 1, 2, 3 }, { 2, 5, 6 }, { 2, 7, 7 } };

    for (int i = 0; i < 3; i++) {
      for (int j = 0; j < 3; j++) {
        System.out.print(Array[i][j] + " ");
      }
      System.out.println();
    }
    int Array2[] = { 1, 5, 4 };
    int arr[] = Array2.clone();
    for (int i : arr)
      System.out.println(i);

  }
}
