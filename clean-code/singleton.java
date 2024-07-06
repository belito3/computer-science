// Threadsafe singleton

class Singleton {
    private static Sington singleInstance = null;
    private Singleton() {
        // constructor
    }
    
    public static synchronized Singleton getInstance() {
        if (singleInstance == null) {
            singleInstance = new Singleton();
            return singleInstance;
        }
    }
}