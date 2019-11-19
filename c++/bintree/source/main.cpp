#include "bintree.hpp"
#include <fstream>
#include <string>
#include <iostream>

int main(){
    std::ifstream numberfile("numbers.txt");
    std::vector<int> numbers;
    std::vector<int> ordered_numbers;
    std::string read_data;
    Bintree test_tree;

    while(getline(numberfile, read_data).good()){
        numbers.push_back(std::stoi(read_data));
    }

    for(int number : numbers){
        test_tree.insert(number);
    }

    test_tree.get_ordered_list(ordered_numbers);
    for(int number : ordered_numbers){
        std::cout << number << std::endl;
    }

}