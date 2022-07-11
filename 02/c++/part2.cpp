#include <iostream>
#include <string>
#include <sstream>
#include <fstream>

#define INPUT "../data/input"

/**
 * Read a file entirely into a stringstream
 * 
 * @param The name of the file to read
 * @return The contents of the file
 **/
std::stringstream readFile(const std::string& filename = INPUT) {
    std::ifstream fileStream(filename);
    std::stringstream returnVal;
    
    returnVal << fileStream.rdbuf();

    return returnVal;
}

int main() {
    std::stringstream contents = readFile();
    std::string line;
    int width;
    int length;
    int height;
    int widestSide;
    int ribbonLength = 0;

    // for each line in file
    while (std::getline(contents, line, '\n')) {
        // Read in width, length and height
        sscanf(line.c_str(), "%ix%ix%i", &width, &height, &length);

        // Add on all sides
        ribbonLength += 2 * width;
        ribbonLength += 2 * length;
        ribbonLength += 2 * height;

        // Calculate smallest side area
        widestSide = std::max(length, width);
        widestSide = std::max(widestSide, height);

        // Take away widestSide
        ribbonLength -= 2 * widestSide;

        // Add on volume
        ribbonLength += width * height * length;
    }

    std::cout << "Total ribbon length is " << ribbonLength << " feet" << std::endl;

    return 0;
}
