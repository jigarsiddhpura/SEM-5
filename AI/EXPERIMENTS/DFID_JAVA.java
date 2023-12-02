import java.util.*;

public class DFID_JAVA{

    LinkedList<Integer> adj[];

    public void graph(int v){
        adj = new LinkedList[v];
        for(int i=0; i<v; i++){
            adj[i] = new LinkedList();
        }
    }

    void addEdge(int v, int w){
        adj[v].add(w);
    }

    boolean DLS(int v,int target,int limit){
        if(v == target)
            return true;

        if(limit <= 0)
            return false;

        for(int i : adj[v]){
            System.out.print(i+" -> ");
            if(DLS(i,target,limit-1))
                return true;
        }

        return false;
    }

    boolean DFID(int src,int target,int max_depth){
        for(int i=0;i<max_depth;i++){
            System.out.println("\nDepth = "+i);
            if(DLS(src,target,i))
                return true;
            }
        return false;
    }

    public static void main(String[] args){
        DFID_JAVA g = new DFID_JAVA();
        g.graph(7);
        g.addEdge(0,1);
        g.addEdge(0,2);
        g.addEdge(1,3);
        g.addEdge(1,4);
        g.addEdge(2,4);
        g.addEdge(2,5);
        g.addEdge(2,6);
        g.addEdge(3,7);
        g.addEdge(3,8);
        g.addEdge(4,5);

        int src=0,target=5,max_depth=4;
        if(g.DFID(src,target,max_depth)){
            System.out.println("Target found");
        } else {
            System.out.println("Target not found");
        }
    }
}