#include <string>

class Vigenere{
    private:
        std::string text;
        std::string key;

    public:
        Vigenere(std::string);
        Vigenere(std::string, std::string);
        void set_key(std::string);
        void set_text(std::string);
        std::string get_text();
        void encrypt();
        void decrypt();

};