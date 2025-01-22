class SumOfEven {
    static int num = 1000; 

    static int sum = 0;    
    
    public static void main(String[] args) 
    { 
        int counter = 1; 

        while (counter <= num) { 
            if (counter %2 == 0) { 
                sum = sum + counter; 
            }
            counter++; 
        }

        System.out.println("The sum of even numbers up to " + num + " is: " + sum);
    }
}


