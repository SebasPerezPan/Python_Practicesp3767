#include<iostream>
#include<stdlib.h>

using namespace std; 

int main () {
    
    int user , pc ; 
    cout<<"Piedra, papel, tijera, reptil, Spock!";
    
    cout<<"Selecciona:"<<endl<<endl<<"1. Papel."<<endl<<"2. Piedra."<<endl<<"3. Tijera."<<endl<<"4. Reptil."<<endl<<"5. Spock.";
    cin>>user;
    pc = rand();
    
    pc = 1+rand()%(6-1);
    cout<<pc;
    
    if (user == 3 and pc == 1) {
        cout<<"Tijeras cortan papel"}
    else if (user == 1 and pc == 2) {
        cout<<"Papel cubre piedra"}
    else if (user == 2 and pc == 4){
        cout<<"Papel golpea reptil"}
    else if (user == 4 and pc == )
Rock crushes Lizard
Lizard poisons Spock
Spock smashes Scissors
Scissors decapitates Lizard
Lizard eats Paper
Paper disproves Spock
Spock vaporizes Rock

    
    return 0;
}
