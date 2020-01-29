#ifndef CHARACTER_HPP
#define CHARACTER_HPP

#include <string>
#include <iostream>

template <class T>
class Character{
    private:
        int health;
        std::string name;
        double spell_proficiency;
        T spell;

    public:
        Character();
        Character(int, std::string, double, T);
        void taunt();
        bool cast_spell(Character<T> target);
        bool take_damage(int);
};

template <typename T>
Character<T>::Character(){
    this->health = 100;
    this->name = "John";
    this->spell_proficiency = 1.0;
    this->spell = T();
}

template <typename T>
Character<T>::Character(int health, std::string name, double spell_proficiency, T spell){
    this->health = health;
    this->name = name;
    this->spell_proficiency = spell_proficiency;
    this->spell = spell;
}

template <typename T>
void Character<T>::taunt(){
    std::cout << "I don't wanna talk to you no more you empty headed animal foot! Trough water! I'll fart in your general direction! Your mother was a Hamster and you father smelt of elderberries!!!!" << std::endl;
}

template <typename T>
bool Character<T>::cast_spell(Character<T> target){
    bool dead = this->spell.cast(target, *this);
    return dead;
}

template <typename T>
bool Character<T>::take_damage(int amount){
    std::cout << this->name << " takes " << amount << " damage!" << std::endl;
    this->health -= amount;
    if(this->health <= 0){
        return 1;
    }
    return 0;
}
#endif