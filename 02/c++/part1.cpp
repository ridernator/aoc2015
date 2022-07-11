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
    int totalArea = 0;
    int smallestSideArea;

    // for each line in file
    while (std::getline(contents, line, '\n')) {
        // Read in width, length and height
        sscanf(line.c_str(), "%ix%ix%i", &width, &height, &length);

        // Calculate smallest side area
        smallestSideArea = std::min(length * width, width * height);
        smallestSideArea = std::min(smallestSideArea, height * length);

        // Add amount of paper to total
        totalArea += smallestSideArea + (2 * (length * width + width * height + height * length));
    }

    std::cout << "Total area is " << totalArea << " square feet" << std::endl;

    return 0;
}
