import java.util.*;

public class FIFOpageReplacement {
    public static void main(String[] args) {
        int[] allPageRequests =  {4,7,6,1,7,6,1,2,7,2};
        int numPageFrames = 3;

        Queue<Integer> pageFrames = new LinkedList<>();        // ⭐⭐⭐
        int pageFaults = 0;

        for (int i = 0; i < allPageRequests.length; i++) {
            int page = allPageRequests[i];

            if (!pageFrames.contains(page)) {
                if (pageFrames.size() < numPageFrames) {
                    // .offer similar to .add   ⭐⭐
                    pageFrames.offer(page);
                } else {
                    // .poll similar to .remove   ⭐⭐
                    pageFrames.poll();
                    pageFrames.offer(page);
                }

                pageFaults++;
            }
        }

        System.out.println("Page faults: " + pageFaults);
    }
}
