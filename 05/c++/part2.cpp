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

bool rule1(const std::string& string) {
    for (decltype(string.size()) index = 0; index < string.size() - 3; ++index) {
        for (decltype(string.size()) index2 = index + 2; index2 < string.size() - 1; ++index2) {
            if ((string[index2] == string[index]) && 
                (string[index2 + 1] == string[index + 1])) {
                return true;
            }
        }
    }

    return false;
}

bool rule2(const std::string& string) {
    for (decltype(string.size()) index = 0; index < string.size() - 2; ++index) {
        if (string[index] == string[index + 2]) {
            return true;
        }
    }

    return false;
}

int main() {
    std::stringstream contents = readFile();
    std::string line;
    uint64_t numNice = 0;

    // For each line in file
    while (std::getline(contents, line, '\n')) {
        // Check for double pairs
        if (!rule1(line)) {
            continue;
        }

        // Check for xyx combinations
        if (!rule2(line)) {
            continue;
        }

        ++numNice;
    }

    std::cout << "Number of nice strings : " << numNice << std::endl;

    return 0;
}
