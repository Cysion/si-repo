#include "character.hpp"
#include "Fireball.hpp"
#include <iostream>


int main (){
    Fireball hero_fireball(400);
    Fireball villain_fireball;
    Character<Fireball> hero(100, "Hero", 1.5, hero_fireball);
    Character<Fireball> villain(600, "The hydra kraken lord", 10, villain_fireball);
    std::cout << "The villain says: You can only defeat me with a standard fireball taking into account your 1.5 spell proficiency!" << "\n"
              << "However i am safe, because the fireball ISN'T IMPLEMENTED YET!" << "\n"
              << "I will give you a free shot then i will STRIKE YOU DOWN!" << "\n\n"
              << "The hero considers this for a moment and then responds confidently: ";
    hero.taunt();
    bool villain_dead = hero.cast_spell(villain);
    if(villain_dead){
        std::cout << "The villain gasps and says: This is impossible! some dastardly c++ programmer must have saved you!" << std::endl;
    }
    else{
        hero.take_damage(500);
        std::cout << "The villain, standing over the heros corpse says: You are weak, just like your code!" << std::endl;
    }
}