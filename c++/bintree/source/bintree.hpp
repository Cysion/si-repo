#include <vector>

struct Node{
    int value;
    Node* left_child;
    Node* right_child;
    Node();
    Node(int);

    //cool addons
    int count;
};

class Bintree{
    private:
        Node* root;
        void insert(int, Node*);
        void get_ordered_list(std::vector<int>&, Node*);
        //cool addons
        void remove(int, Node*);

    public:
        Bintree();
        void insert(int);
        void get_ordered_list(std::vector<int>&);

        //cool addons
        void remove(int);   
        void remove(int, int);   
        Bintree operator + (Bintree);

};