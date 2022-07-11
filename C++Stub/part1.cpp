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

    // For each line in file
    while (std::getline(contents, line, '\n')) {
        // Do stuff with line
    }

    std::cout << "Done" << std::endl;

    return 0;
}
