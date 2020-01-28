#include <string>
#include <iostream>

template <typename T>
class Character{
    private:
        int health;
        std::string name;
        T spell;
        double spell_proficiency;

    public:
        Character();
        Character(int, std::string, T);
        void taunt();
        int cast_spell();
};

template <typename T>
Character<T>::Character(){
    this->health = 100;
    this->name = "John";
    this->spell = T();
    this->spell_proficiency;
};

template <typename T>
Character<T>::Character(int health, std::string name, T spell){

};

template <typename T>
void Character<T>::taunt(){

};

template <typename T>
int Character<T>::cast_spell(){

};

