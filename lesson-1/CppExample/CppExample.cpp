/*
This is just a comment at the beginning of a file.
Note how generating module documentation requires other tools than a simple text - editor.
*/

// Imports
#include <iostream>
#include <string>


// Exception sub-class
class ForbiddenDivisionException : public std::exception {
public:
	ForbiddenDivisionException(int n) :
		std::exception((std::string("Cannot divide by ") + std::to_string(n)).c_str())
	{	}
};


// Function (static)
static int safeDivide(int x, int y, int forbidden) 
{
	// Condition
	if (y == forbidden) {
		// Exception
		throw new ForbiddenDivisionException(forbidden);
	}
	return x / y;
}

// Function (static) - with default value
static int safeDivide(int x, int y) 
{
	return safeDivide(x, y, 0);
}


// Program entry-point
void main(int argc, const char** argv) {
	// Print text to stdout
	std::cout << "Hello World!\n";

	// Arguments (complex)
	int forbidden = argc > 1 ? std::atoi(argv[1]) : 0;
	// Call function
	std::cout << "1 / 2 = " << safeDivide(1, 2, forbidden) << "\n";
}