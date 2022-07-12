#include <iostream>
#include <string>
#include <sstream>
#include <fstream>
#include <map>
#include <utility>

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
    std::map<std::pair<int64_t, int64_t>, bool> visitedHouses;
    char direction;
    int64_t x = 0;
    int64_t y = 0;

    // Flag house at position x, y as receiving a present
    visitedHouses[std::make_pair(0, 0)] = true;

    // For each direction
    while (contents.get(direction)) {
        // Calculate new position
        switch (direction) {
            case '>': {
                ++x;

                break;
            }

            case '<': {
                --x;

                break;
            }

            case '^': {
                ++y;

                break;
            }

            case 'v': {
                --y;

                break;
            }
        }

        // Flag house at position x, y as receiving a present
        visitedHouses[std::make_pair(x, y)] = true;
    }

    std::cout << "Number of houses which receive at least one present : " << visitedHouses.size() << std::endl;

    return 0;
}
