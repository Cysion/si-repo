#include <vector>
#include <algorithm>
#include <iostream>
#include <cmath>
#include <fstream>

unsigned long long gcd(unsigned long long a, unsigned long long b){
    if (b==0) return a;
    return gcd(b, a%b);
}

bool is_coprime(unsigned long long num1, unsigned long long num2){
    if (gcd(num1, num2) == 1) return 1;
    return 0;
}

bool is_prime(unsigned long long number){
    bool status = 1;
    for(int i = 2; i<number; i++){
        if(number % i == 0){
            status = 0;
        }
    }
    return status;
}

auto gen_primes(int amount){
    std::cout << "Is PRiNtIng SlOwIng DowN thIs ProcCeSs a Lot More ThAn ComPutAtioN?" << std::endl;
    std::vector<unsigned long long> returnable;
    returnable.push_back(1);
    returnable.push_back(2);
    unsigned long long counter= 2;
    for(int i = 3; counter<amount-2; i++){
        if(is_prime(i)){
            returnable.push_back(i);
            counter++;
        }
    }
    return returnable;
}



auto sum_all(std::vector<unsigned long long> iterable){
    std::cout << "HoW LOnG DoEs OnE CoUt TaKe?" << std::endl;
    unsigned long long sum;
    for(auto prime: iterable){
        sum+=prime;
    }
    return sum;
}

auto gen_randoms(unsigned long long seed, unsigned long long amount){
    std::cout << "Is It EVeN PrEdiCtiBle?" << std::endl;
    std::srand(seed);
    std::vector<unsigned long long> randoms;
    for(int i = 0; i < amount; i++){
        unsigned long long rando = rand();
        randoms.push_back(rando);
    }
    return randoms;
}

unsigned long long count_coprimes(std::vector<unsigned long long> iterable){
    unsigned long long amount_coprime;
    for(int i = 0; i<iterable.size(); i+=2){
        if(is_coprime(iterable[i], iterable[i+1])) amount_coprime++;
    }
    return amount_coprime;
}


double get_secret(double_t coprimes, double_t len){
    long double secret, prob1, prob2;
    prob1 = coprimes / (len / 2.0);
    prob2 = 6 / prob1;
    secret = std::sqrt(prob2);
    return secret;
}

void print_to_file(long double output){
    std::ofstream outfile;
    outfile.open("results.txt");
    outfile << output;
    outfile.close();
}


int main(){
    //generate list of first 1000 prime numbers using function gen-primes, its return type needs to be iterable.
    auto prime_list = gen_primes(1000);

    //sum all the elements of the prime list;
    auto prime_sum = sum_all(prime_list);

    //use sum as seed to generate a new list of random numbers
    auto randoms = gen_randoms(prime_sum, 10000000);

    //find the amount coprime/cofactor from the list of random numbers
    auto amount_coprime = count_coprimes(randoms);

    //use the amount of coprimes and cofactors to find the secret number
    auto secret_number = get_secret(amount_coprime, randoms.size());

    //send secret number to file
    print_to_file(secret_number);
}