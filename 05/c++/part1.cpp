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

bool stringContains(const std::string& string,
                    const std::string& searchFor) {
    return string.find(searchFor) != std::string::npos;
}

uint64_t numVowels(const std::string& string) {
    uint64_t returnVal = 0;

    for (const auto& character : string) {
        if ((character == 'a') ||
            (character == 'e') ||
            (character == 'i') ||
            (character == 'o') ||
            (character == 'u')) {
            ++returnVal;
        }
    }

    return returnVal;
}

bool containsDoubleLetter(const std::string& string) {
    for (decltype(string.size()) index = 0; index < string.size() - 1; ++index) {
        if (string[index] == string[index + 1]) {
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
        // Check for bad combinations
        if ((stringContains(line, "ab")) ||
            (stringContains(line, "cd")) ||
            (stringContains(line, "pq")) ||
            (stringContains(line, "xy"))) {
            continue;
        }

        // Check ofr number of vowels
        if (numVowels(line) < 3) {
            continue;
        }

        // Check for double letter sequences
        if (!containsDoubleLetter(line)) {
            continue;
        }

        ++numNice;
    }

    std::cout << "Number of nice strings : " << numNice << std::endl;

    return 0;
}
