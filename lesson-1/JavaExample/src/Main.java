/*
This is just a comment at the beginning of a file.
Note how generating module documentation requires other tools than a simple text-editor.
*/

// Exception sub-class
class ForbiddenDivisionException extends ArithmeticException {
    ForbiddenDivisionException(int n) {
        super("Cannot divide by " + n);
    }
}


// Main class for program entry-point
public class Main {
    // Function (static)
    private static int safeDivide(int x, int y, int forbidden) {
        // Condition
        if (y == forbidden) {
            // Exception
            throw new ForbiddenDivisionException(forbidden);
        }
        return x / y;
    }

    // Function (static) - with default value
    public static int safeDivide(int x, int y) {
        return safeDivide(x, y, 0);
    }

    // Program entry-point
    public static void main(String[] args) {
        // Print text to stdout
        System.out.println("Hello World!");

        // Arguments (complex)
        int forbidden = args.length != 0 ? Integer.parseInt(args[0]) : 0;
        // Call function
        System.out.println("1 / 2 = " + safeDivide(1, 2, forbidden));
    }
}
