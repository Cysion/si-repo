#ifndef FIREBALL_HPP
#define FIREBALL_HPP


#include "character.hpp"


class Fireball{
    private:
        int base_dmg;
    public:
        Fireball();
        Fireball(int);
        bool cast(Character<Fireball>, Character<Fireball>);

};

#endif